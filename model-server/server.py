import os
import zlib
import json
import redis

from transformers import AutoModelForCausalLM, AutoTokenizer
from loguru import logger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from typing import Dict


app = FastAPI(title="Model Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HF_MODEL = os.environ.get("HF_MODEL", "gpt2")
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "")

@app.on_event("startup")
async def initialize():
    # initializes model, categories, redis connection
    global tokenizer, model
    logger.info(f"loading model {HF_MODEL=}...")
    tokenizer = AutoTokenizer.from_pretrained('gpt2')
    model = AutoModelForCausalLM.from_pretrained('gpt2')
    logger.info(f"loaded model {HF_MODEL=}")

    global redis_pool
    logger.info(f"creating redis connection with {REDIS_HOST=} {REDIS_PORT=}")
    redis_pool = redis.ConnectionPool(
        host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=0, decode_responses=True
    )
    logger.info(f"created redis connection pool with {REDIS_HOST=} {REDIS_PORT=}")

def get_redis():
    # Here, we re-use our connection pool
    # not creating a new one
    return redis.Redis(connection_pool=redis_pool)

def predict(inp_text: str) -> Dict[str, str]:
    
    encoded_input = tokenizer(inp_text, return_tensors='pt')
    output = model.generate(**encoded_input, max_new_tokens=50)

    return {
            "generated_text": tokenizer.decode(output[0], skip_special_tokens=True)
        }

async def write_to_cache(text: str, output: Dict[str, str]) -> None:
    cache = get_redis()

    hash = zlib.adler32(bytes(text, 'utf-8'))
    cache.set(hash, json.dumps(output))
    logger.info(f"written to cache for {hash=}")

@app.post("/infer")
async def infer(text: str) -> Dict[str, str]:
    generated_text = predict(text)

    await write_to_cache(text, generated_text)

    logger.info(f"generated text successfully...")

    return generated_text

# uvicorn server:app --host 0.0.0.0 --port 8000 --reload