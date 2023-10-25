import os
import zlib
import json
import requests
from loguru import logger
import redis
import httpx

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from typing import Dict

app = FastAPI(title="Web Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "")
MODEL_SERVER_URL = os.environ.get("MODEL_SERVER_URL", "http://localhost:8000")

@app.on_event("startup")
async def initialize() -> None:
    global redis_pool
    logger.info(f"creating redis connection with {REDIS_HOST=} {REDIS_PORT=}")
    redis_pool = redis.ConnectionPool(
        host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=0, decode_responses=True
    )
    logger.info(f"initialization complete...")

def get_redis() -> redis.Redis:
    return redis.Redis(connection_pool=redis_pool)

async def check_cached(text: str) -> Dict[str, str] or None:
    hash = zlib.adler32(bytes(text, 'utf-8'))
    cache = get_redis()

    data = cache.get(hash)

    logger.info(f"cache data {data=}")

    return json.loads(data) if data else None

@app.post("/generate")
async def generate(text: str) -> Dict[str, str]:
    infer_cache = await check_cached(text)
    logger.info(f"{infer_cache=}")
    if infer_cache == None:
        async with httpx.AsyncClient() as client:
            try:
                # print("this")
                # response = await client.post(
                #     f"{MODEL_SERVER_URL}/infer", files={"image": image}
                # )

                # print(f"response", response)

                # return response.json()
                url = f"{MODEL_SERVER_URL}/infer?text={text}"
                
                response = requests.post(url)

                logger.info(f"response generated successfully")

                response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)

                return response.json()
            except Exception as e:
                logger.error(f"error from model server {e}")
                raise HTTPException(status_code=500, detail="Error from Model Endpoint")

    return infer_cache

# uvicorn server:app --host 0.0.0.0 --port 9000 --reload