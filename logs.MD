# GPT2 deployment on minikube logs

## Logs:

1. `kubectl describe deployment model-serve -n dev`
```bash
Name:                   model-serve
Namespace:              dev
CreationTimestamp:      Thu, 26 Oct 2023 04:15:29 +0530
Labels:                 app.kubernetes.io/managed-by=Helm
Annotations:            deployment.kubernetes.io/revision: 1
                        meta.helm.sh/release-name: fastapi-release-dev
                        meta.helm.sh/release-namespace: default
Selector:               app=model-serve
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=model-serve
  Containers:
   model-serve:
    Image:      gpt-model-server:latest
    Port:       80/TCP
    Host Port:  0/TCP
    Environment:
      REDIS_HOST:      <set to the key 'hostname' of config map 'redis-config-v1.0'>  Optional: false
      REDIS_PORT:      <set to the key 'port' of config map 'redis-config-v1.0'>      Optional: false
      REDIS_PASSWORD:  <set to the key 'db_password' in secret 'redis-secret-v1.0'>   Optional: false
      HF_MODEL:        <set to the key 'hf_model' of config map 'model-config-v1.0'>  Optional: false
    Mounts:            <none>
  Volumes:             <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   model-serve-7549bc9b6 (1/1 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  21m   deployment-controller  Scaled up replica set model-serve-7549bc9b6 to 1
```

2. `kubectl describe deployment web-serve -n dev`
```bash
Name:                   web-serve
Namespace:              dev
CreationTimestamp:      Thu, 26 Oct 2023 04:15:29 +0530
Labels:                 app=web-serve
                        app.kubernetes.io/managed-by=Helm
Annotations:            deployment.kubernetes.io/revision: 1
                        meta.helm.sh/release-name: fastapi-release-dev
                        meta.helm.sh/release-namespace: default
Selector:               app=web-serve
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=web-serve
  Containers:
   web-serve:
    Image:      gpt-web-server:latest
    Port:       80/TCP
    Host Port:  0/TCP
    Environment:
      REDIS_HOST:        <set to the key 'hostname' of config map 'redis-config-v1.0'>          Optional: false
      REDIS_PORT:        <set to the key 'port' of config map 'redis-config-v1.0'>              Optional: false
      REDIS_PASSWORD:    <set to the key 'db_password' in secret 'redis-secret-v1.0'>           Optional: false
      MODEL_SERVER_URL:  <set to the key 'model_server_url' of config map 'model-config-v1.0'>  Optional: false
    Mounts:              <none>
  Volumes:               <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   web-serve-566fb45bb9 (1/1 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  21m   deployment-controller  Scaled up replica set web-serve-566fb45bb9 to 1
```

3. `kubectl describe deployment redis-db -n dev`
```bash
Name:                   redis-db
Namespace:              dev
CreationTimestamp:      Thu, 26 Oct 2023 04:15:29 +0530
Labels:                 app.kubernetes.io/managed-by=Helm
Annotations:            deployment.kubernetes.io/revision: 1
                        meta.helm.sh/release-name: fastapi-release-dev
                        meta.helm.sh/release-namespace: default
Selector:               app=redis-db,role=master
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=redis-db
           role=master
  Containers:
   redis-master:
    Image:      redis:7.2.1
    Port:       6379/TCP
    Host Port:  0/TCP
    Command:
      redis-server
    Args:
      --requirepass
      $(REDIS_PASSWORD)
    Limits:
      cpu:     200m
      memory:  200Mi
    Environment:
      REDIS_PASSWORD:  <set to the key 'db_password' in secret 'redis-secret-v1.0'>  Optional: false
    Mounts:            <none>
  Volumes:
   redis-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  redis-pvc
    ReadOnly:   false
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   redis-db-686b7bfff8 (1/1 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  22m   deployment-controller  Scaled up replica set redis-db-686b7bfff8 to 1
```

4. `kubectl describe pod model-serve-7549bc9b6-8xrn5 -n dev`
```bash
Name:             model-serve-7549bc9b6-8xrn5
Namespace:        dev
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Thu, 26 Oct 2023 04:15:29 +0530
Labels:           app=model-serve
                  pod-template-hash=7549bc9b6
Annotations:      <none>
Status:           Running
IP:               10.244.0.57
IPs:
  IP:           10.244.0.57
Controlled By:  ReplicaSet/model-serve-7549bc9b6
Containers:
  model-serve:
    Container ID:   docker://0e7b19fbdb6fe17cfb4c8c01b04932e425b0dbb8a9a16f385aacc429fa40ad74
    Image:          gpt-model-server:latest
    Image ID:       docker://sha256:e45057dcdb5e14954f0878cdd383d891be6688d0d64759ebf9530facaf1006c5
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Thu, 26 Oct 2023 04:15:29 +0530
    Ready:          True
    Restart Count:  0
    Environment:
      REDIS_HOST:      <set to the key 'hostname' of config map 'redis-config-v1.0'>  Optional: false
      REDIS_PORT:      <set to the key 'port' of config map 'redis-config-v1.0'>      Optional: false
      REDIS_PASSWORD:  <set to the key 'db_password' in secret 'redis-secret-v1.0'>   Optional: false
      HF_MODEL:        <set to the key 'hf_model' of config map 'model-config-v1.0'>  Optional: false
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-ft8nd (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-ft8nd:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  23m   default-scheduler  Successfully assigned dev/model-serve-7549bc9b6-8xrn5 to minikube
  Normal  Pulled     23m   kubelet            Container image "gpt-model-server:latest" already present on machine
  Normal  Created    23m   kubelet            Created container model-serve
  Normal  Started    23m   kubelet            Started container model-serve
```

5. `kubectl describe pod web-serve-566fb45bb9-9h95c -n dev`
```bash
Name:             web-serve-566fb45bb9-9h95c
Namespace:        dev
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Thu, 26 Oct 2023 04:15:29 +0530
Labels:           app=web-serve
                  pod-template-hash=566fb45bb9
Annotations:      <none>
Status:           Running
IP:               10.244.0.58
IPs:
  IP:           10.244.0.58
Controlled By:  ReplicaSet/web-serve-566fb45bb9
Containers:
  web-serve:
    Container ID:   docker://0a14414663ae40166baab3ad93de6447fd42cd1f87be2cfb2d208113051de961
    Image:          gpt-web-server:latest
    Image ID:       docker://sha256:af4ba6d3a3f179e8d46034ffbebbd4e8021f9b27b626fb8b74f4c8a24cd97682
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Thu, 26 Oct 2023 04:15:29 +0530
    Ready:          True
    Restart Count:  0
    Environment:
      REDIS_HOST:        <set to the key 'hostname' of config map 'redis-config-v1.0'>          Optional: false
      REDIS_PORT:        <set to the key 'port' of config map 'redis-config-v1.0'>              Optional: false
      REDIS_PASSWORD:    <set to the key 'db_password' in secret 'redis-secret-v1.0'>           Optional: false
      MODEL_SERVER_URL:  <set to the key 'model_server_url' of config map 'model-config-v1.0'>  Optional: false
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-smcw9 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-smcw9:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  24m   default-scheduler  Successfully assigned dev/web-serve-566fb45bb9-9h95c to minikube
  Normal  Pulled     24m   kubelet            Container image "gpt-web-server:latest" already present on machine
  Normal  Created    24m   kubelet            Created container web-serve
  Normal  Started    24m   kubelet            Started container web-serve
```

6. `kubectl describe pod redis-db-686b7bfff8-ms8kx -n dev`
```bash
Name:             redis-db-686b7bfff8-ms8kx
Namespace:        dev
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Thu, 26 Oct 2023 04:15:41 +0530
Labels:           app=redis-db
                  pod-template-hash=686b7bfff8
                  role=master
Annotations:      <none>
Status:           Running
IP:               10.244.0.59
IPs:
  IP:           10.244.0.59
Controlled By:  ReplicaSet/redis-db-686b7bfff8
Containers:
  redis-master:
    Container ID:  docker://3d8898aaeb9b3afb972a799d93348ecd0a33d0dd8019c1fef6148f79199c5f92
    Image:         redis:7.2.1
    Image ID:      docker-pullable://redis@sha256:4ca2a277f1dc3ddd0da33a258096de9a1cf5b9d9bd96b27ee78763ee2248c28c
    Port:          6379/TCP
    Host Port:     0/TCP
    Command:
      redis-server
    Args:
      --requirepass
      $(REDIS_PASSWORD)
    State:          Running
      Started:      Thu, 26 Oct 2023 04:15:42 +0530
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     200m
      memory:  200Mi
    Requests:
      cpu:     200m
      memory:  200Mi
    Environment:
      REDIS_PASSWORD:  <set to the key 'db_password' in secret 'redis-secret-v1.0'>  Optional: false
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-vc5mb (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  redis-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  redis-pvc
    ReadOnly:   false
  kube-api-access-vc5mb:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Guaranteed
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason            Age   From               Message
  ----     ------            ----  ----               -------
  Warning  FailedScheduling  25m   default-scheduler  0/1 nodes are available: pod has unbound immediate PersistentVolumeClaims. preemption: 0/1 nodes are available: 1 No preemption victims found for incoming pod..
  Warning  FailedScheduling  24m   default-scheduler  0/1 nodes are available: pod has unbound immediate PersistentVolumeClaims. preemption: 0/1 nodes are available: 1 No preemption victims found for incoming pod..
  Normal   Scheduled         24m   default-scheduler  Successfully assigned dev/redis-db-686b7bfff8-ms8kx to minikube
  Normal   Pulled            24m   kubelet            Container image "redis:7.2.1" already present on machine
  Normal   Created           24m   kubelet            Created container redis-master
  Normal   Started           24m   kubelet            Started container redis-master
```

7. `kubectl describe ingress web-serve -n dev`
```bash
Name:             web-serve
Labels:           app.kubernetes.io/managed-by=Helm
Namespace:        dev
Address:          192.168.49.2
Ingress Class:    nginx
Default backend:  <default>
Rules:
  Host         Path  Backends
  ----         ----  --------
  fastapi.gpt  
               /   web-serve:8000 (10.244.0.58:80)
Annotations:   meta.helm.sh/release-name: fastapi-release-dev
               meta.helm.sh/release-namespace: default
Events:
  Type    Reason  Age                From                      Message
  ----    ------  ----               ----                      -------
  Normal  Sync    25m (x2 over 25m)  nginx-ingress-controller  Scheduled for sync
```

8. `kubectl describe pvc redis-pvc -n dev`
```bash
Name:          redis-pvc
Namespace:     dev
StorageClass:  local-storage
Status:        Bound
Volume:        redis-pv
Labels:        app.kubernetes.io/managed-by=Helm
Annotations:   meta.helm.sh/release-name: fastapi-release-dev
               meta.helm.sh/release-namespace: default
               pv.kubernetes.io/bind-completed: yes
Finalizers:    [kubernetes.io/pvc-protection]
Capacity:      10Gi
Access Modes:  RWO
VolumeMode:    Filesystem
Used By:       redis-db-686b7bfff8-ms8kx
Events:        <none>
```

9. `kubectl describe pv redis-pv -n dev`
```bash
Name:            redis-pv
Labels:          app.kubernetes.io/managed-by=Helm
Annotations:     meta.helm.sh/release-name: fastapi-release-dev
                 meta.helm.sh/release-namespace: default
                 pv.kubernetes.io/bound-by-controller: yes
Finalizers:      [kubernetes.io/pv-protection]
StorageClass:    local-storage
Status:          Bound
Claim:           dev/redis-pvc
Reclaim Policy:  Retain
Access Modes:    RWO
VolumeMode:      Filesystem
Capacity:        10Gi
Node Affinity:   <none>
Message:         
Source:
    Type:          HostPath (bare host directory volume)
    Path:          /data/redis-pv/
    HostPathType:  
Events:            <none>
```

10. `kubectl top pod -n dev`
```bash
NAME                          CPU(cores)   MEMORY(bytes)   
model-serve-7549bc9b6-8xrn5   3m           1237Mi          
redis-db-686b7bfff8-ms8kx     3m           2Mi             
web-serve-566fb45bb9-9h95c    3m           44Mi
```

11. `kubectl top node -n dev`
```bash
NAME       CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
minikube   203m         1%     3583Mi          11% 
```

12. `kubectl get all -A -o yaml -n dev`
```bash
apiVersion: v1
items:
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-25T22:45:29Z"
    generateName: model-serve-7549bc9b6-
    labels:
      app: model-serve
      pod-template-hash: 7549bc9b6
    name: model-serve-7549bc9b6-8xrn5
    namespace: dev
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: model-serve-7549bc9b6
      uid: b6c26587-1a61-45f8-a9d3-958053ef17a2
    resourceVersion: "64555"
    uid: 900d0fb1-9842-48be-b4aa-285962df801c
  spec:
    containers:
    - env:
      - name: REDIS_HOST
        valueFrom:
          configMapKeyRef:
            key: hostname
            name: redis-config-v1.0
      - name: REDIS_PORT
        valueFrom:
          configMapKeyRef:
            key: port
            name: redis-config-v1.0
      - name: REDIS_PASSWORD
        valueFrom:
          secretKeyRef:
            key: db_password
            name: redis-secret-v1.0
      - name: HF_MODEL
        valueFrom:
          configMapKeyRef:
            key: hf_model
            name: model-config-v1.0
      image: gpt-model-server:latest
      imagePullPolicy: Never
      name: model-serve
      ports:
      - containerPort: 80
        protocol: TCP
      resources: {}
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-ft8nd
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: default
    serviceAccountName: default
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - name: kube-api-access-ft8nd
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T22:45:29Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T22:45:30Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T22:45:30Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T22:45:29Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://0e7b19fbdb6fe17cfb4c8c01b04932e425b0dbb8a9a16f385aacc429fa40ad74
      image: gpt-model-server:latest
      imageID: docker://sha256:e45057dcdb5e14954f0878cdd383d891be6688d0d64759ebf9530facaf1006c5
      lastState: {}
      name: model-serve
      ready: true
      restartCount: 0
      started: true
      state:
        running:
          startedAt: "2023-10-25T22:45:29Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 10.244.0.57
    podIPs:
    - ip: 10.244.0.57
    qosClass: BestEffort
    startTime: "2023-10-25T22:45:29Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-25T22:45:29Z"
    generateName: redis-db-686b7bfff8-
    labels:
      app: redis-db
      pod-template-hash: 686b7bfff8
      role: master
    name: redis-db-686b7bfff8-ms8kx
    namespace: dev
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: redis-db-686b7bfff8
      uid: dab7978c-9694-4e8f-8c89-9f2d77c6a564
    resourceVersion: "64584"
    uid: 4e656826-9cf7-4af3-aa3e-5ee9492731cf
  spec:
    containers:
    - args:
      - --requirepass
      - $(REDIS_PASSWORD)
      command:
      - redis-server
      env:
      - name: REDIS_PASSWORD
        valueFrom:
          secretKeyRef:
            key: db_password
            name: redis-secret-v1.0
      image: redis:7.2.1
      imagePullPolicy: IfNotPresent
      name: redis-master
      ports:
      - containerPort: 6379
        protocol: TCP
      resources:
        limits:
          cpu: 200m
          memory: 200Mi
        requests:
          cpu: 200m
          memory: 200Mi
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-vc5mb
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: default
    serviceAccountName: default
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - name: redis-storage
      persistentVolumeClaim:
        claimName: redis-pvc
    - name: kube-api-access-vc5mb
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T22:45:41Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T22:45:43Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T22:45:43Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T22:45:41Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://3d8898aaeb9b3afb972a799d93348ecd0a33d0dd8019c1fef6148f79199c5f92
      image: redis:7.2.1
      imageID: docker-pullable://redis@sha256:4ca2a277f1dc3ddd0da33a258096de9a1cf5b9d9bd96b27ee78763ee2248c28c
      lastState: {}
      name: redis-master
      ready: true
      restartCount: 0
      started: true
      state:
        running:
          startedAt: "2023-10-25T22:45:42Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 10.244.0.59
    podIPs:
    - ip: 10.244.0.59
    qosClass: Guaranteed
    startTime: "2023-10-25T22:45:41Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-25T22:45:29Z"
    generateName: web-serve-566fb45bb9-
    labels:
      app: web-serve
      pod-template-hash: 566fb45bb9
    name: web-serve-566fb45bb9-9h95c
    namespace: dev
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: web-serve-566fb45bb9
      uid: f3341d18-770d-4e4f-93a7-aa1993c63bcf
    resourceVersion: "64550"
    uid: 7681075e-d326-4be0-9dc6-3cc98cbaa7f7
  spec:
    containers:
    - env:
      - name: REDIS_HOST
        valueFrom:
          configMapKeyRef:
            key: hostname
            name: redis-config-v1.0
      - name: REDIS_PORT
        valueFrom:
          configMapKeyRef:
            key: port
            name: redis-config-v1.0
      - name: REDIS_PASSWORD
        valueFrom:
          secretKeyRef:
            key: db_password
            name: redis-secret-v1.0
      - name: MODEL_SERVER_URL
        valueFrom:
          configMapKeyRef:
            key: model_server_url
            name: model-config-v1.0
      image: gpt-web-server:latest
      imagePullPolicy: Never
      name: web-serve
      ports:
      - containerPort: 80
        protocol: TCP
      resources: {}
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-smcw9
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: default
    serviceAccountName: default
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - name: kube-api-access-smcw9
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T22:45:29Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T22:45:30Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T22:45:30Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T22:45:29Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://0a14414663ae40166baab3ad93de6447fd42cd1f87be2cfb2d208113051de961
      image: gpt-web-server:latest
      imageID: docker://sha256:af4ba6d3a3f179e8d46034ffbebbd4e8021f9b27b626fb8b74f4c8a24cd97682
      lastState: {}
      name: web-serve
      ready: true
      restartCount: 0
      started: true
      state:
        running:
          startedAt: "2023-10-25T22:45:29Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 10.244.0.58
    podIPs:
    - ip: 10.244.0.58
    qosClass: BestEffort
    startTime: "2023-10-25T22:45:29Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-24T07:46:33Z"
    generateName: ingress-nginx-admission-create-
    labels:
      app.kubernetes.io/component: admission-webhook
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
      batch.kubernetes.io/controller-uid: 545a479b-89f6-497c-858e-fe287310d0e5
      batch.kubernetes.io/job-name: ingress-nginx-admission-create
      controller-uid: 545a479b-89f6-497c-858e-fe287310d0e5
      job-name: ingress-nginx-admission-create
    name: ingress-nginx-admission-create-spl2z
    namespace: ingress-nginx
    ownerReferences:
    - apiVersion: batch/v1
      blockOwnerDeletion: true
      controller: true
      kind: Job
      name: ingress-nginx-admission-create
      uid: 545a479b-89f6-497c-858e-fe287310d0e5
    resourceVersion: "37098"
    uid: 8a0ed954-8faa-42c4-8b1e-2399ab25559b
  spec:
    containers:
    - args:
      - create
      - --host=ingress-nginx-controller-admission,ingress-nginx-controller-admission.$(POD_NAMESPACE).svc
      - --namespace=$(POD_NAMESPACE)
      - --secret-name=ingress-nginx-admission
      env:
      - name: POD_NAMESPACE
        valueFrom:
          fieldRef:
            apiVersion: v1
            fieldPath: metadata.namespace
      image: registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
      imagePullPolicy: IfNotPresent
      name: create
      resources: {}
      securityContext:
        allowPrivilegeEscalation: false
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-cgqdq
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    nodeSelector:
      kubernetes.io/os: linux
      minikube.k8s.io/primary: "true"
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: OnFailure
    schedulerName: default-scheduler
    securityContext:
      runAsNonRoot: true
      runAsUser: 2000
    serviceAccount: ingress-nginx-admission
    serviceAccountName: ingress-nginx-admission
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - name: kube-api-access-cgqdq
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:46:33Z"
      reason: PodCompleted
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:46:33Z"
      reason: PodCompleted
      status: "False"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:46:33Z"
      reason: PodCompleted
      status: "False"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:46:33Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://7daebec123d7065508f8e4d9125640a5f9aa6cf5cad52d070982607f1dff2b19
      image: registry.k8s.io/ingress-nginx/kube-webhook-certgen@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
      imageID: docker-pullable://registry.k8s.io/ingress-nginx/kube-webhook-certgen@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
      lastState: {}
      name: create
      ready: false
      restartCount: 0
      started: false
      state:
        terminated:
          containerID: docker://7daebec123d7065508f8e4d9125640a5f9aa6cf5cad52d070982607f1dff2b19
          exitCode: 0
          finishedAt: "2023-10-24T07:46:42Z"
          reason: Completed
          startedAt: "2023-10-24T07:46:42Z"
    hostIP: 192.168.49.2
    phase: Succeeded
    qosClass: BestEffort
    startTime: "2023-10-24T07:46:33Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-24T07:46:33Z"
    generateName: ingress-nginx-admission-patch-
    labels:
      app.kubernetes.io/component: admission-webhook
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
      batch.kubernetes.io/controller-uid: 323613ba-5375-4acd-aaf0-d93c33152ebb
      batch.kubernetes.io/job-name: ingress-nginx-admission-patch
      controller-uid: 323613ba-5375-4acd-aaf0-d93c33152ebb
      job-name: ingress-nginx-admission-patch
    name: ingress-nginx-admission-patch-9qk8j
    namespace: ingress-nginx
    ownerReferences:
    - apiVersion: batch/v1
      blockOwnerDeletion: true
      controller: true
      kind: Job
      name: ingress-nginx-admission-patch
      uid: 323613ba-5375-4acd-aaf0-d93c33152ebb
    resourceVersion: "37097"
    uid: fae1202d-07a0-4885-8687-a0afe708a2c8
  spec:
    containers:
    - args:
      - patch
      - --webhook-name=ingress-nginx-admission
      - --namespace=$(POD_NAMESPACE)
      - --patch-mutating=false
      - --secret-name=ingress-nginx-admission
      - --patch-failure-policy=Fail
      env:
      - name: POD_NAMESPACE
        valueFrom:
          fieldRef:
            apiVersion: v1
            fieldPath: metadata.namespace
      image: registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
      imagePullPolicy: IfNotPresent
      name: patch
      resources: {}
      securityContext:
        allowPrivilegeEscalation: false
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-kn48q
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    nodeSelector:
      kubernetes.io/os: linux
      minikube.k8s.io/primary: "true"
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: OnFailure
    schedulerName: default-scheduler
    securityContext:
      runAsNonRoot: true
      runAsUser: 2000
    serviceAccount: ingress-nginx-admission
    serviceAccountName: ingress-nginx-admission
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - name: kube-api-access-kn48q
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:46:33Z"
      reason: PodCompleted
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:46:33Z"
      reason: PodCompleted
      status: "False"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:46:33Z"
      reason: PodCompleted
      status: "False"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:46:33Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://9f86115ee01ddf66f041c057bff7edab6330e0170800ba079cd6f96ac9e1abff
      image: sha256:7e7451bb70423d31bdadcf0a71a3107b64858eccd7827d066234650b5e7b36b0
      imageID: docker-pullable://registry.k8s.io/ingress-nginx/kube-webhook-certgen@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
      lastState: {}
      name: patch
      ready: false
      restartCount: 1
      started: false
      state:
        terminated:
          containerID: docker://9f86115ee01ddf66f041c057bff7edab6330e0170800ba079cd6f96ac9e1abff
          exitCode: 0
          finishedAt: "2023-10-24T07:46:42Z"
          reason: Completed
          startedAt: "2023-10-24T07:46:42Z"
    hostIP: 192.168.49.2
    phase: Succeeded
    qosClass: BestEffort
    startTime: "2023-10-24T07:46:33Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-24T07:46:33Z"
    generateName: ingress-nginx-controller-7799c6795f-
    labels:
      app.kubernetes.io/component: controller
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
      gcp-auth-skip-secret: "true"
      pod-template-hash: 7799c6795f
    name: ingress-nginx-controller-7799c6795f-cq9h9
    namespace: ingress-nginx
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: ingress-nginx-controller-7799c6795f
      uid: 703ba820-1234-405e-8939-205eb16235ff
    resourceVersion: "50903"
    uid: 2cc46e2e-92bb-4853-b8ed-24239faa47a7
  spec:
    containers:
    - args:
      - /nginx-ingress-controller
      - --election-id=ingress-nginx-leader
      - --controller-class=k8s.io/ingress-nginx
      - --watch-ingress-without-class=true
      - --configmap=$(POD_NAMESPACE)/ingress-nginx-controller
      - --tcp-services-configmap=$(POD_NAMESPACE)/tcp-services
      - --udp-services-configmap=$(POD_NAMESPACE)/udp-services
      - --validating-webhook=:8443
      - --validating-webhook-certificate=/usr/local/certificates/cert
      - --validating-webhook-key=/usr/local/certificates/key
      env:
      - name: POD_NAME
        valueFrom:
          fieldRef:
            apiVersion: v1
            fieldPath: metadata.name
      - name: POD_NAMESPACE
        valueFrom:
          fieldRef:
            apiVersion: v1
            fieldPath: metadata.namespace
      - name: LD_PRELOAD
        value: /usr/local/lib/libmimalloc.so
      image: registry.k8s.io/ingress-nginx/controller:v1.8.1@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd
      imagePullPolicy: IfNotPresent
      lifecycle:
        preStop:
          exec:
            command:
            - /wait-shutdown
      livenessProbe:
        failureThreshold: 5
        httpGet:
          path: /healthz
          port: 10254
          scheme: HTTP
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 1
      name: controller
      ports:
      - containerPort: 80
        hostPort: 80
        name: http
        protocol: TCP
      - containerPort: 443
        hostPort: 443
        name: https
        protocol: TCP
      - containerPort: 8443
        name: webhook
        protocol: TCP
      readinessProbe:
        failureThreshold: 3
        httpGet:
          path: /healthz
          port: 10254
          scheme: HTTP
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 1
      resources:
        requests:
          cpu: 100m
          memory: 90Mi
      securityContext:
        allowPrivilegeEscalation: true
        capabilities:
          add:
          - NET_BIND_SERVICE
          drop:
          - ALL
        runAsUser: 101
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /usr/local/certificates/
        name: webhook-cert
        readOnly: true
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-l6s2k
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    nodeSelector:
      kubernetes.io/os: linux
      minikube.k8s.io/primary: "true"
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: ingress-nginx
    serviceAccountName: ingress-nginx
    terminationGracePeriodSeconds: 0
    tolerations:
    - effect: NoSchedule
      key: node-role.kubernetes.io/master
      operator: Equal
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - name: webhook-cert
      secret:
        defaultMode: 420
        secretName: ingress-nginx-admission
    - name: kube-api-access-l6s2k
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:46:33Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:53Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:53Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:46:33Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://a6eed6572005dd53344ff46a3d6daced8e0802b5e9c395c6569cc8e0fcae0c1c
      image: sha256:825aff16c20cc2c6039fce49bafaa0f510de0f9238da475f3de949adadb9be7f
      imageID: docker-pullable://registry.k8s.io/ingress-nginx/controller@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd
      lastState:
        terminated:
          containerID: docker://6b3d2c1ba333de346efa5c767fd3b7cda0f186bf08032c40ac4a80e159a5b66b
          exitCode: 255
          finishedAt: "2023-10-25T19:00:48Z"
          reason: Error
          startedAt: "2023-10-25T10:19:58Z"
      name: controller
      ready: true
      restartCount: 3
      started: true
      state:
        running:
          startedAt: "2023-10-25T19:01:11Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 10.244.0.36
    podIPs:
    - ip: 10.244.0.36
    qosClass: Burstable
    startTime: "2023-10-24T07:46:33Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-24T07:41:19Z"
    generateName: coredns-5d78c9869d-
    labels:
      k8s-app: kube-dns
      pod-template-hash: 5d78c9869d
    name: coredns-5d78c9869d-k8wcd
    namespace: kube-system
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: coredns-5d78c9869d
      uid: 5e54de92-26a5-483f-8482-c80a7e495792
    resourceVersion: "50894"
    uid: 2e775aa9-9ad6-460e-8ca8-ab24e5b579c6
  spec:
    affinity:
      podAntiAffinity:
        preferredDuringSchedulingIgnoredDuringExecution:
        - podAffinityTerm:
            labelSelector:
              matchExpressions:
              - key: k8s-app
                operator: In
                values:
                - kube-dns
            topologyKey: kubernetes.io/hostname
          weight: 100
    containers:
    - args:
      - -conf
      - /etc/coredns/Corefile
      image: registry.k8s.io/coredns/coredns:v1.10.1
      imagePullPolicy: IfNotPresent
      livenessProbe:
        failureThreshold: 5
        httpGet:
          path: /health
          port: 8080
          scheme: HTTP
        initialDelaySeconds: 60
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 5
      name: coredns
      ports:
      - containerPort: 53
        name: dns
        protocol: UDP
      - containerPort: 53
        name: dns-tcp
        protocol: TCP
      - containerPort: 9153
        name: metrics
        protocol: TCP
      readinessProbe:
        failureThreshold: 3
        httpGet:
          path: /ready
          port: 8181
          scheme: HTTP
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 1
      resources:
        limits:
          memory: 170Mi
        requests:
          cpu: 100m
          memory: 70Mi
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          add:
          - NET_BIND_SERVICE
          drop:
          - all
        readOnlyRootFilesystem: true
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /etc/coredns
        name: config-volume
        readOnly: true
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-vz4sz
        readOnly: true
    dnsPolicy: Default
    enableServiceLinks: true
    nodeName: minikube
    nodeSelector:
      kubernetes.io/os: linux
    preemptionPolicy: PreemptLowerPriority
    priority: 2000000000
    priorityClassName: system-cluster-critical
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: coredns
    serviceAccountName: coredns
    terminationGracePeriodSeconds: 30
    tolerations:
    - key: CriticalAddonsOnly
      operator: Exists
    - effect: NoSchedule
      key: node-role.kubernetes.io/control-plane
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - configMap:
        defaultMode: 420
        items:
        - key: Corefile
          path: Corefile
        name: coredns
      name: config-volume
    - name: kube-api-access-vz4sz
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:41:19Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:49Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:49Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:41:19Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://34b90e38190ece5e09636e3f1fe622aeb9f1edeb506b3c9edfb2e8117dae67c6
      image: registry.k8s.io/coredns/coredns:v1.10.1
      imageID: docker-pullable://registry.k8s.io/coredns/coredns@sha256:a0ead06651cf580044aeb0a0feba63591858fb2e43ade8c9dea45a6a89ae7e5e
      lastState:
        terminated:
          containerID: docker://f153799eec864f30d780548176b10c6f574b6e342a8147e2c984675451a2caa5
          exitCode: 0
          finishedAt: "2023-10-25T13:48:25Z"
          reason: Completed
          startedAt: "2023-10-25T10:19:58Z"
      name: coredns
      ready: true
      restartCount: 3
      started: true
      state:
        running:
          startedAt: "2023-10-25T19:01:12Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 10.244.0.35
    podIPs:
    - ip: 10.244.0.35
    qosClass: Burstable
    startTime: "2023-10-24T07:41:19Z"
- apiVersion: v1
  kind: Pod
  metadata:
    annotations:
      kubeadm.kubernetes.io/etcd.advertise-client-urls: https://192.168.49.2:2379
      kubernetes.io/config.hash: 8af0e85a28544808d52bb7c47ad824ed
      kubernetes.io/config.mirror: 8af0e85a28544808d52bb7c47ad824ed
      kubernetes.io/config.seen: "2023-10-24T07:41:01.249673429Z"
      kubernetes.io/config.source: file
    creationTimestamp: "2023-10-24T07:41:05Z"
    labels:
      component: etcd
      tier: control-plane
    name: etcd-minikube
    namespace: kube-system
    ownerReferences:
    - apiVersion: v1
      controller: true
      kind: Node
      name: minikube
      uid: 9604bb8c-f280-45e5-9e0a-81766980684a
    resourceVersion: "50871"
    uid: 4229d6f0-b903-4df9-aef9-06f260d5b7ae
  spec:
    containers:
    - command:
      - etcd
      - --advertise-client-urls=https://192.168.49.2:2379
      - --cert-file=/var/lib/minikube/certs/etcd/server.crt
      - --client-cert-auth=true
      - --data-dir=/var/lib/minikube/etcd
      - --experimental-initial-corrupt-check=true
      - --experimental-watch-progress-notify-interval=5s
      - --initial-advertise-peer-urls=https://192.168.49.2:2380
      - --initial-cluster=minikube=https://192.168.49.2:2380
      - --key-file=/var/lib/minikube/certs/etcd/server.key
      - --listen-client-urls=https://127.0.0.1:2379,https://192.168.49.2:2379
      - --listen-metrics-urls=http://127.0.0.1:2381
      - --listen-peer-urls=https://192.168.49.2:2380
      - --name=minikube
      - --peer-cert-file=/var/lib/minikube/certs/etcd/peer.crt
      - --peer-client-cert-auth=true
      - --peer-key-file=/var/lib/minikube/certs/etcd/peer.key
      - --peer-trusted-ca-file=/var/lib/minikube/certs/etcd/ca.crt
      - --proxy-refresh-interval=70000
      - --snapshot-count=10000
      - --trusted-ca-file=/var/lib/minikube/certs/etcd/ca.crt
      image: registry.k8s.io/etcd:3.5.7-0
      imagePullPolicy: IfNotPresent
      livenessProbe:
        failureThreshold: 8
        httpGet:
          host: 127.0.0.1
          path: /health?exclude=NOSPACE&serializable=true
          port: 2381
          scheme: HTTP
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 15
      name: etcd
      resources:
        requests:
          cpu: 100m
          memory: 100Mi
      startupProbe:
        failureThreshold: 24
        httpGet:
          host: 127.0.0.1
          path: /health?serializable=false
          port: 2381
          scheme: HTTP
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 15
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /var/lib/minikube/etcd
        name: etcd-data
      - mountPath: /var/lib/minikube/certs/etcd
        name: etcd-certs
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    hostNetwork: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 2000001000
    priorityClassName: system-node-critical
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext:
      seccompProfile:
        type: RuntimeDefault
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      operator: Exists
    volumes:
    - hostPath:
        path: /var/lib/minikube/certs/etcd
        type: DirectoryOrCreate
      name: etcd-certs
    - hostPath:
        path: /var/lib/minikube/etcd
        type: DirectoryOrCreate
      name: etcd-data
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:08Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:27Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:27Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:08Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://4ba265af61674fe2043fe59d9db8204880e5aaf3610f136ab48b68c2ee585242
      image: registry.k8s.io/etcd:3.5.7-0
      imageID: docker-pullable://registry.k8s.io/etcd@sha256:51eae8381dcb1078289fa7b4f3df2630cdc18d09fb56f8e56b41c40e191d6c83
      lastState:
        terminated:
          containerID: docker://2a1b88a3538e687467b265971f5e3ff02c76c618cfff7f75d11209de90fa7ed0
          exitCode: 0
          finishedAt: "2023-10-25T13:48:20Z"
          reason: Completed
          startedAt: "2023-10-25T10:19:54Z"
      name: etcd
      ready: true
      restartCount: 3
      started: true
      state:
        running:
          startedAt: "2023-10-25T19:01:09Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 192.168.49.2
    podIPs:
    - ip: 192.168.49.2
    qosClass: Burstable
    startTime: "2023-10-25T19:01:08Z"
- apiVersion: v1
  kind: Pod
  metadata:
    annotations:
      kubeadm.kubernetes.io/kube-apiserver.advertise-address.endpoint: 192.168.49.2:8443
      kubernetes.io/config.hash: f241819aff4d77a34fc71bea1fac9af8
      kubernetes.io/config.mirror: f241819aff4d77a34fc71bea1fac9af8
      kubernetes.io/config.seen: "2023-10-24T07:41:01.249674080Z"
      kubernetes.io/config.source: file
    creationTimestamp: "2023-10-24T07:41:05Z"
    labels:
      component: kube-apiserver
      tier: control-plane
    name: kube-apiserver-minikube
    namespace: kube-system
    ownerReferences:
    - apiVersion: v1
      controller: true
      kind: Node
      name: minikube
      uid: 9604bb8c-f280-45e5-9e0a-81766980684a
    resourceVersion: "50869"
    uid: 2ba31537-de81-4584-8fd9-c47f601e87d0
  spec:
    containers:
    - command:
      - kube-apiserver
      - --advertise-address=192.168.49.2
      - --allow-privileged=true
      - --authorization-mode=Node,RBAC
      - --client-ca-file=/var/lib/minikube/certs/ca.crt
      - --enable-admission-plugins=NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,DefaultTolerationSeconds,NodeRestriction,MutatingAdmissionWebhook,ValidatingAdmissionWebhook,ResourceQuota
      - --enable-bootstrap-token-auth=true
      - --etcd-cafile=/var/lib/minikube/certs/etcd/ca.crt
      - --etcd-certfile=/var/lib/minikube/certs/apiserver-etcd-client.crt
      - --etcd-keyfile=/var/lib/minikube/certs/apiserver-etcd-client.key
      - --etcd-servers=https://127.0.0.1:2379
      - --kubelet-client-certificate=/var/lib/minikube/certs/apiserver-kubelet-client.crt
      - --kubelet-client-key=/var/lib/minikube/certs/apiserver-kubelet-client.key
      - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
      - --proxy-client-cert-file=/var/lib/minikube/certs/front-proxy-client.crt
      - --proxy-client-key-file=/var/lib/minikube/certs/front-proxy-client.key
      - --requestheader-allowed-names=front-proxy-client
      - --requestheader-client-ca-file=/var/lib/minikube/certs/front-proxy-ca.crt
      - --requestheader-extra-headers-prefix=X-Remote-Extra-
      - --requestheader-group-headers=X-Remote-Group
      - --requestheader-username-headers=X-Remote-User
      - --secure-port=8443
      - --service-account-issuer=https://kubernetes.default.svc.cluster.local
      - --service-account-key-file=/var/lib/minikube/certs/sa.pub
      - --service-account-signing-key-file=/var/lib/minikube/certs/sa.key
      - --service-cluster-ip-range=10.96.0.0/12
      - --tls-cert-file=/var/lib/minikube/certs/apiserver.crt
      - --tls-private-key-file=/var/lib/minikube/certs/apiserver.key
      image: registry.k8s.io/kube-apiserver:v1.27.4
      imagePullPolicy: IfNotPresent
      livenessProbe:
        failureThreshold: 8
        httpGet:
          host: 192.168.49.2
          path: /livez
          port: 8443
          scheme: HTTPS
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 15
      name: kube-apiserver
      readinessProbe:
        failureThreshold: 3
        httpGet:
          host: 192.168.49.2
          path: /readyz
          port: 8443
          scheme: HTTPS
        periodSeconds: 1
        successThreshold: 1
        timeoutSeconds: 15
      resources:
        requests:
          cpu: 250m
      startupProbe:
        failureThreshold: 24
        httpGet:
          host: 192.168.49.2
          path: /livez
          port: 8443
          scheme: HTTPS
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 15
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /etc/ssl/certs
        name: ca-certs
        readOnly: true
      - mountPath: /etc/ca-certificates
        name: etc-ca-certificates
        readOnly: true
      - mountPath: /var/lib/minikube/certs
        name: k8s-certs
        readOnly: true
      - mountPath: /usr/local/share/ca-certificates
        name: usr-local-share-ca-certificates
        readOnly: true
      - mountPath: /usr/share/ca-certificates
        name: usr-share-ca-certificates
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    hostNetwork: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 2000001000
    priorityClassName: system-node-critical
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext:
      seccompProfile:
        type: RuntimeDefault
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      operator: Exists
    volumes:
    - hostPath:
        path: /etc/ssl/certs
        type: DirectoryOrCreate
      name: ca-certs
    - hostPath:
        path: /etc/ca-certificates
        type: DirectoryOrCreate
      name: etc-ca-certificates
    - hostPath:
        path: /var/lib/minikube/certs
        type: DirectoryOrCreate
      name: k8s-certs
    - hostPath:
        path: /usr/local/share/ca-certificates
        type: DirectoryOrCreate
      name: usr-local-share-ca-certificates
    - hostPath:
        path: /usr/share/ca-certificates
        type: DirectoryOrCreate
      name: usr-share-ca-certificates
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:08Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:27Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:27Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:08Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://bf9c26f266984dcf34b25e56e23d9a258f479f87ccf9cf50d0dbbf56a4bbb734
      image: registry.k8s.io/kube-apiserver:v1.27.4
      imageID: docker-pullable://registry.k8s.io/kube-apiserver@sha256:697cd88d94f7f2ef42144cb3072b016dcb2e9251f0e7d41a7fede557e555452d
      lastState:
        terminated:
          containerID: docker://2fc72a48d53ada5377adf35dd70c84aede07e6634677afcbcb098708a89ebca5
          exitCode: 1
          finishedAt: "2023-10-25T13:48:20Z"
          reason: Error
          startedAt: "2023-10-25T10:19:54Z"
      name: kube-apiserver
      ready: true
      restartCount: 3
      started: true
      state:
        running:
          startedAt: "2023-10-25T19:01:09Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 192.168.49.2
    podIPs:
    - ip: 192.168.49.2
    qosClass: Burstable
    startTime: "2023-10-25T19:01:08Z"
- apiVersion: v1
  kind: Pod
  metadata:
    annotations:
      kubernetes.io/config.hash: b3702ceb912504d37098b922ccdcfa41
      kubernetes.io/config.mirror: b3702ceb912504d37098b922ccdcfa41
      kubernetes.io/config.seen: "2023-10-24T07:41:01.249669577Z"
      kubernetes.io/config.source: file
    creationTimestamp: "2023-10-24T07:41:06Z"
    labels:
      component: kube-controller-manager
      tier: control-plane
    name: kube-controller-manager-minikube
    namespace: kube-system
    ownerReferences:
    - apiVersion: v1
      controller: true
      kind: Node
      name: minikube
      uid: 9604bb8c-f280-45e5-9e0a-81766980684a
    resourceVersion: "50864"
    uid: 89737aae-3bed-4c8a-9357-fcf81c010b8a
  spec:
    containers:
    - command:
      - kube-controller-manager
      - --allocate-node-cidrs=true
      - --authentication-kubeconfig=/etc/kubernetes/controller-manager.conf
      - --authorization-kubeconfig=/etc/kubernetes/controller-manager.conf
      - --bind-address=127.0.0.1
      - --client-ca-file=/var/lib/minikube/certs/ca.crt
      - --cluster-cidr=10.244.0.0/16
      - --cluster-name=mk
      - --cluster-signing-cert-file=/var/lib/minikube/certs/ca.crt
      - --cluster-signing-key-file=/var/lib/minikube/certs/ca.key
      - --controllers=*,bootstrapsigner,tokencleaner
      - --kubeconfig=/etc/kubernetes/controller-manager.conf
      - --leader-elect=false
      - --requestheader-client-ca-file=/var/lib/minikube/certs/front-proxy-ca.crt
      - --root-ca-file=/var/lib/minikube/certs/ca.crt
      - --service-account-private-key-file=/var/lib/minikube/certs/sa.key
      - --service-cluster-ip-range=10.96.0.0/12
      - --use-service-account-credentials=true
      image: registry.k8s.io/kube-controller-manager:v1.27.4
      imagePullPolicy: IfNotPresent
      livenessProbe:
        failureThreshold: 8
        httpGet:
          host: 127.0.0.1
          path: /healthz
          port: 10257
          scheme: HTTPS
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 15
      name: kube-controller-manager
      resources:
        requests:
          cpu: 200m
      startupProbe:
        failureThreshold: 24
        httpGet:
          host: 127.0.0.1
          path: /healthz
          port: 10257
          scheme: HTTPS
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 15
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /etc/ssl/certs
        name: ca-certs
        readOnly: true
      - mountPath: /etc/ca-certificates
        name: etc-ca-certificates
        readOnly: true
      - mountPath: /usr/libexec/kubernetes/kubelet-plugins/volume/exec
        name: flexvolume-dir
      - mountPath: /var/lib/minikube/certs
        name: k8s-certs
        readOnly: true
      - mountPath: /etc/kubernetes/controller-manager.conf
        name: kubeconfig
        readOnly: true
      - mountPath: /usr/local/share/ca-certificates
        name: usr-local-share-ca-certificates
        readOnly: true
      - mountPath: /usr/share/ca-certificates
        name: usr-share-ca-certificates
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    hostNetwork: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 2000001000
    priorityClassName: system-node-critical
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext:
      seccompProfile:
        type: RuntimeDefault
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      operator: Exists
    volumes:
    - hostPath:
        path: /etc/ssl/certs
        type: DirectoryOrCreate
      name: ca-certs
    - hostPath:
        path: /etc/ca-certificates
        type: DirectoryOrCreate
      name: etc-ca-certificates
    - hostPath:
        path: /usr/libexec/kubernetes/kubelet-plugins/volume/exec
        type: DirectoryOrCreate
      name: flexvolume-dir
    - hostPath:
        path: /var/lib/minikube/certs
        type: DirectoryOrCreate
      name: k8s-certs
    - hostPath:
        path: /etc/kubernetes/controller-manager.conf
        type: FileOrCreate
      name: kubeconfig
    - hostPath:
        path: /usr/local/share/ca-certificates
        type: DirectoryOrCreate
      name: usr-local-share-ca-certificates
    - hostPath:
        path: /usr/share/ca-certificates
        type: DirectoryOrCreate
      name: usr-share-ca-certificates
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:08Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:24Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:24Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:08Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://add15ba855d52327b3fd487894908b5d924d7c24760a05609b5ad432a95bfb98
      image: registry.k8s.io/kube-controller-manager:v1.27.4
      imageID: docker-pullable://registry.k8s.io/kube-controller-manager@sha256:6286e500782ad6d0b37a1b8be57fc73f597dc931dfc73ff18ce534059803b265
      lastState:
        terminated:
          containerID: docker://5d0a0588c759a5c5c98d206122f19244b075c4ecf3075cc8724d019158e4012c
          exitCode: 2
          finishedAt: "2023-10-25T13:48:20Z"
          reason: Error
          startedAt: "2023-10-25T10:19:54Z"
      name: kube-controller-manager
      ready: true
      restartCount: 3
      started: true
      state:
        running:
          startedAt: "2023-10-25T19:01:09Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 192.168.49.2
    podIPs:
    - ip: 192.168.49.2
    qosClass: Burstable
    startTime: "2023-10-25T19:01:08Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-24T07:41:19Z"
    generateName: kube-proxy-
    labels:
      controller-revision-hash: 86cc8bcbf7
      k8s-app: kube-proxy
      pod-template-generation: "1"
    name: kube-proxy-2zrjv
    namespace: kube-system
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: DaemonSet
      name: kube-proxy
      uid: 3eb2857b-792a-4dd0-beff-fb537a5fbd09
    resourceVersion: "50764"
    uid: 44436f7a-25a6-4cc5-a8a8-39d3bbbe3dfd
  spec:
    affinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchFields:
            - key: metadata.name
              operator: In
              values:
              - minikube
    containers:
    - command:
      - /usr/local/bin/kube-proxy
      - --config=/var/lib/kube-proxy/config.conf
      - --hostname-override=$(NODE_NAME)
      env:
      - name: NODE_NAME
        valueFrom:
          fieldRef:
            apiVersion: v1
            fieldPath: spec.nodeName
      image: registry.k8s.io/kube-proxy:v1.27.4
      imagePullPolicy: IfNotPresent
      name: kube-proxy
      resources: {}
      securityContext:
        privileged: true
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /var/lib/kube-proxy
        name: kube-proxy
      - mountPath: /run/xtables.lock
        name: xtables-lock
      - mountPath: /lib/modules
        name: lib-modules
        readOnly: true
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-8vl52
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    hostNetwork: true
    nodeName: minikube
    nodeSelector:
      kubernetes.io/os: linux
    preemptionPolicy: PreemptLowerPriority
    priority: 2000001000
    priorityClassName: system-node-critical
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: kube-proxy
    serviceAccountName: kube-proxy
    terminationGracePeriodSeconds: 30
    tolerations:
    - operator: Exists
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
    - effect: NoSchedule
      key: node.kubernetes.io/disk-pressure
      operator: Exists
    - effect: NoSchedule
      key: node.kubernetes.io/memory-pressure
      operator: Exists
    - effect: NoSchedule
      key: node.kubernetes.io/pid-pressure
      operator: Exists
    - effect: NoSchedule
      key: node.kubernetes.io/unschedulable
      operator: Exists
    - effect: NoSchedule
      key: node.kubernetes.io/network-unavailable
      operator: Exists
    volumes:
    - configMap:
        defaultMode: 420
        name: kube-proxy
      name: kube-proxy
    - hostPath:
        path: /run/xtables.lock
        type: FileOrCreate
      name: xtables-lock
    - hostPath:
        path: /lib/modules
        type: ""
      name: lib-modules
    - name: kube-api-access-8vl52
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:41:19Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:13Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:13Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:41:19Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://0535d4cd053fe61966ac8fca15b4ea9bdbcf75ec2d55dc5f76447d2b4d708f9a
      image: registry.k8s.io/kube-proxy:v1.27.4
      imageID: docker-pullable://registry.k8s.io/kube-proxy@sha256:4bcb707da9898d2625f5d4edc6d0c96519a24f16db914fc673aa8f97e41dbabf
      lastState:
        terminated:
          containerID: docker://26b1d3b419a8fe3ad5b798bf31ffc0f0b3896a5577dc27834276baa3a58c3f32
          exitCode: 2
          finishedAt: "2023-10-25T13:48:20Z"
          reason: Error
          startedAt: "2023-10-25T10:19:58Z"
      name: kube-proxy
      ready: true
      restartCount: 3
      started: true
      state:
        running:
          startedAt: "2023-10-25T19:01:12Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 192.168.49.2
    podIPs:
    - ip: 192.168.49.2
    qosClass: BestEffort
    startTime: "2023-10-24T07:41:19Z"
- apiVersion: v1
  kind: Pod
  metadata:
    annotations:
      kubernetes.io/config.hash: eb675835e10503c79265cf0e2983f93c
      kubernetes.io/config.mirror: eb675835e10503c79265cf0e2983f93c
      kubernetes.io/config.seen: "2023-10-24T07:41:06.769885761Z"
      kubernetes.io/config.source: file
    creationTimestamp: "2023-10-24T07:41:06Z"
    labels:
      component: kube-scheduler
      tier: control-plane
    name: kube-scheduler-minikube
    namespace: kube-system
    ownerReferences:
    - apiVersion: v1
      controller: true
      kind: Node
      name: minikube
      uid: 9604bb8c-f280-45e5-9e0a-81766980684a
    resourceVersion: "50867"
    uid: b9ea36f4-4cba-4017-9e23-4a652bcc8a29
  spec:
    containers:
    - command:
      - kube-scheduler
      - --authentication-kubeconfig=/etc/kubernetes/scheduler.conf
      - --authorization-kubeconfig=/etc/kubernetes/scheduler.conf
      - --bind-address=127.0.0.1
      - --kubeconfig=/etc/kubernetes/scheduler.conf
      - --leader-elect=false
      image: registry.k8s.io/kube-scheduler:v1.27.4
      imagePullPolicy: IfNotPresent
      livenessProbe:
        failureThreshold: 8
        httpGet:
          host: 127.0.0.1
          path: /healthz
          port: 10259
          scheme: HTTPS
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 15
      name: kube-scheduler
      resources:
        requests:
          cpu: 100m
      startupProbe:
        failureThreshold: 24
        httpGet:
          host: 127.0.0.1
          path: /healthz
          port: 10259
          scheme: HTTPS
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 15
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /etc/kubernetes/scheduler.conf
        name: kubeconfig
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    hostNetwork: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 2000001000
    priorityClassName: system-node-critical
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext:
      seccompProfile:
        type: RuntimeDefault
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      operator: Exists
    volumes:
    - hostPath:
        path: /etc/kubernetes/scheduler.conf
        type: FileOrCreate
      name: kubeconfig
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:08Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:25Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:25Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:01:08Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://c5567ef5d1a02d20b901f3115a9515ed93eea19f7090733f8af830720ce43cde
      image: registry.k8s.io/kube-scheduler:v1.27.4
      imageID: docker-pullable://registry.k8s.io/kube-scheduler@sha256:5897d7a97d23dce25cbf36fcd6e919180a8ef904bf5156583ffdb6a733ab04af
      lastState:
        terminated:
          containerID: docker://f38f9797f30f5550ec7f881af02998186544ae5f60e95b3b16b26e6c8fe6e098
          exitCode: 1
          finishedAt: "2023-10-25T13:48:20Z"
          reason: Error
          startedAt: "2023-10-25T10:19:54Z"
      name: kube-scheduler
      ready: true
      restartCount: 3
      started: true
      state:
        running:
          startedAt: "2023-10-25T19:01:09Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 192.168.49.2
    podIPs:
    - ip: 192.168.49.2
    qosClass: Burstable
    startTime: "2023-10-25T19:01:08Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-24T07:46:28Z"
    generateName: metrics-server-7746886d4f-
    labels:
      k8s-app: metrics-server
      pod-template-hash: 7746886d4f
    name: metrics-server-7746886d4f-8klxd
    namespace: kube-system
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: metrics-server-7746886d4f
      uid: aa735f0f-911a-457b-a096-dad3f1c6d22d
    resourceVersion: "50927"
    uid: ee9f5df6-88e0-4e52-aa5a-06babe955b09
  spec:
    containers:
    - args:
      - --cert-dir=/tmp
      - --secure-port=4443
      - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
      - --kubelet-use-node-status-port
      - --metric-resolution=60s
      - --kubelet-insecure-tls
      image: registry.k8s.io/metrics-server/metrics-server:v0.6.4@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e
      imagePullPolicy: IfNotPresent
      livenessProbe:
        failureThreshold: 3
        httpGet:
          path: /livez
          port: https
          scheme: HTTPS
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 1
      name: metrics-server
      ports:
      - containerPort: 4443
        name: https
        protocol: TCP
      readinessProbe:
        failureThreshold: 3
        httpGet:
          path: /readyz
          port: https
          scheme: HTTPS
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 1
      resources:
        requests:
          cpu: 100m
          memory: 200Mi
      securityContext:
        readOnlyRootFilesystem: true
        runAsNonRoot: true
        runAsUser: 1000
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /tmp
        name: tmp-dir
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-2lpcj
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 2000000000
    priorityClassName: system-cluster-critical
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: metrics-server
    serviceAccountName: metrics-server
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - emptyDir: {}
      name: tmp-dir
    - name: kube-api-access-2lpcj
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:46:28Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:02:14Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:02:14Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:46:28Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://7bee9e6dd24d8cea449fb2ca32694c69bf77c741c265df4755d251d85a389335
      image: sha256:a608c686bac931a5955f10a01b606f289af2b6fd9250e7c4eadc4a8117002c57
      imageID: docker-pullable://registry.k8s.io/metrics-server/metrics-server@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e
      lastState:
        terminated:
          containerID: docker://4a5b577678e61114c3cfd2f810e148779798feb64c8504e0d5a289beea828b7f
          exitCode: 1
          finishedAt: "2023-10-25T13:48:20Z"
          reason: Error
          startedAt: "2023-10-25T10:19:58Z"
      name: metrics-server
      ready: true
      restartCount: 4
      started: true
      state:
        running:
          startedAt: "2023-10-25T19:01:12Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 10.244.0.34
    podIPs:
    - ip: 10.244.0.34
    qosClass: Burstable
    startTime: "2023-10-24T07:46:28Z"
- apiVersion: v1
  kind: Pod
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"v1","kind":"Pod","metadata":{"annotations":{},"labels":{"addonmanager.kubernetes.io/mode":"Reconcile","integration-test":"storage-provisioner"},"name":"storage-provisioner","namespace":"kube-system"},"spec":{"containers":[{"command":["/storage-provisioner"],"image":"gcr.io/k8s-minikube/storage-provisioner:v5","imagePullPolicy":"IfNotPresent","name":"storage-provisioner","volumeMounts":[{"mountPath":"/tmp","name":"tmp"}]}],"hostNetwork":true,"serviceAccountName":"storage-provisioner","volumes":[{"hostPath":{"path":"/tmp","type":"Directory"},"name":"tmp"}]}}
    creationTimestamp: "2023-10-24T07:41:07Z"
    labels:
      addonmanager.kubernetes.io/mode: Reconcile
      integration-test: storage-provisioner
    name: storage-provisioner
    namespace: kube-system
    resourceVersion: "50922"
    uid: e4881303-9b6d-4524-9953-de2cf4d04b7f
  spec:
    containers:
    - command:
      - /storage-provisioner
      image: gcr.io/k8s-minikube/storage-provisioner:v5
      imagePullPolicy: IfNotPresent
      name: storage-provisioner
      resources: {}
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /tmp
        name: tmp
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-g6vtt
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    hostNetwork: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: storage-provisioner
    serviceAccountName: storage-provisioner
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - hostPath:
        path: /tmp
        type: Directory
      name: tmp
    - name: kube-api-access-g6vtt
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:41:19Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:02:09Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-25T19:02:09Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-24T07:41:19Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://aeedf5f69b62a72ed4ef990ad565f7c3df417b22d06c0914aa78596b6edb72a3
      image: gcr.io/k8s-minikube/storage-provisioner:v5
      imageID: docker-pullable://gcr.io/k8s-minikube/storage-provisioner@sha256:18eb69d1418e854ad5a19e399310e52808a8321e4c441c1dddad8977a0d7a944
      lastState:
        terminated:
          containerID: docker://6b03e730e5b81052d9518eb9642ddfac3748f1e2c2b842e875eebdb31d8073d0
          exitCode: 1
          finishedAt: "2023-10-25T19:01:42Z"
          reason: Error
          startedAt: "2023-10-25T19:01:12Z"
      name: storage-provisioner
      ready: true
      restartCount: 7
      started: true
      state:
        running:
          startedAt: "2023-10-25T19:02:09Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 192.168.49.2
    podIPs:
    - ip: 192.168.49.2
    qosClass: BestEffort
    startTime: "2023-10-24T07:41:19Z"
- apiVersion: v1
  kind: Service
  metadata:
    creationTimestamp: "2023-10-24T07:41:05Z"
    labels:
      component: apiserver
      provider: kubernetes
    name: kubernetes
    namespace: default
    resourceVersion: "193"
    uid: b76b8ab0-fa64-4b84-b386-ea9c202a902a
  spec:
    clusterIP: 10.96.0.1
    clusterIPs:
    - 10.96.0.1
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - name: https
      port: 443
      protocol: TCP
      targetPort: 8443
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      meta.helm.sh/release-name: fastapi-release-dev
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-25T22:45:29Z"
    labels:
      app.kubernetes.io/managed-by: Helm
    name: model-serve
    namespace: dev
    resourceVersion: "64495"
    uid: 0577217c-fc14-47da-9085-3269a8deb5af
  spec:
    clusterIP: 10.109.83.181
    clusterIPs:
    - 10.109.83.181
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - port: 9000
      protocol: TCP
      targetPort: 80
    selector:
      app: model-serve
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      meta.helm.sh/release-name: fastapi-release-dev
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-25T22:45:29Z"
    labels:
      app: redis-db
      app.kubernetes.io/managed-by: Helm
      role: master
    name: redis-db
    namespace: dev
    resourceVersion: "64491"
    uid: c08f93d9-f02d-400e-8044-d9c23a3ae74e
  spec:
    clusterIP: 10.99.246.243
    clusterIPs:
    - 10.99.246.243
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - port: 6379
      protocol: TCP
      targetPort: 6379
    selector:
      app: redis-db
      role: master
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      meta.helm.sh/release-name: fastapi-release-dev
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-25T22:45:29Z"
    labels:
      app.kubernetes.io/managed-by: Helm
    name: web-serve
    namespace: dev
    resourceVersion: "64493"
    uid: 2fd77ca2-2e44-4038-9d58-b357d07a49d2
  spec:
    clusterIP: 10.104.119.7
    clusterIPs:
    - 10.104.119.7
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - port: 8000
      protocol: TCP
      targetPort: 80
    selector:
      app: web-serve
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-controller","namespace":"ingress-nginx"},"spec":{"ipFamilies":["IPv4"],"ipFamilyPolicy":"SingleStack","ports":[{"appProtocol":"http","name":"http","port":80,"protocol":"TCP","targetPort":"http"},{"appProtocol":"https","name":"https","port":443,"protocol":"TCP","targetPort":"https"}],"selector":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"type":"NodePort"}}
    creationTimestamp: "2023-10-24T07:46:33Z"
    labels:
      app.kubernetes.io/component: controller
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
    name: ingress-nginx-controller
    namespace: ingress-nginx
    resourceVersion: "663"
    uid: d1e307d1-8da1-4b67-bfb6-f794674b9519
  spec:
    clusterIP: 10.104.80.237
    clusterIPs:
    - 10.104.80.237
    externalTrafficPolicy: Cluster
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - appProtocol: http
      name: http
      nodePort: 32017
      port: 80
      protocol: TCP
      targetPort: http
    - appProtocol: https
      name: https
      nodePort: 30711
      port: 443
      protocol: TCP
      targetPort: https
    selector:
      app.kubernetes.io/component: controller
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
    sessionAffinity: None
    type: NodePort
  status:
    loadBalancer: {}
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-controller-admission","namespace":"ingress-nginx"},"spec":{"ports":[{"appProtocol":"https","name":"https-webhook","port":443,"targetPort":"webhook"}],"selector":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"type":"ClusterIP"}}
    creationTimestamp: "2023-10-24T07:46:33Z"
    labels:
      app.kubernetes.io/component: controller
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
    name: ingress-nginx-controller-admission
    namespace: ingress-nginx
    resourceVersion: "667"
    uid: b29b3f52-edd8-41d3-9968-372a595b4265
  spec:
    clusterIP: 10.109.19.236
    clusterIPs:
    - 10.109.19.236
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - appProtocol: https
      name: https-webhook
      port: 443
      protocol: TCP
      targetPort: webhook
    selector:
      app.kubernetes.io/component: controller
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      prometheus.io/port: "9153"
      prometheus.io/scrape: "true"
    creationTimestamp: "2023-10-24T07:41:06Z"
    labels:
      k8s-app: kube-dns
      kubernetes.io/cluster-service: "true"
      kubernetes.io/name: CoreDNS
    name: kube-dns
    namespace: kube-system
    resourceVersion: "239"
    uid: a014481a-8097-484d-beef-614a5b93aed9
  spec:
    clusterIP: 10.96.0.10
    clusterIPs:
    - 10.96.0.10
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - name: dns
      port: 53
      protocol: UDP
      targetPort: 53
    - name: dns-tcp
      port: 53
      protocol: TCP
      targetPort: 53
    - name: metrics
      port: 9153
      protocol: TCP
      targetPort: 9153
    selector:
      k8s-app: kube-dns
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"labels":{"addonmanager.kubernetes.io/mode":"Reconcile","k8s-app":"metrics-server","kubernetes.io/minikube-addons":"metrics-server","kubernetes.io/minikube-addons-endpoint":"metrics-server","kubernetes.io/name":"Metrics-server"},"name":"metrics-server","namespace":"kube-system"},"spec":{"ports":[{"name":"https","port":443,"protocol":"TCP","targetPort":"https"}],"selector":{"k8s-app":"metrics-server"}}}
    creationTimestamp: "2023-10-24T07:46:28Z"
    labels:
      addonmanager.kubernetes.io/mode: Reconcile
      k8s-app: metrics-server
      kubernetes.io/minikube-addons: metrics-server
      kubernetes.io/minikube-addons-endpoint: metrics-server
      kubernetes.io/name: Metrics-server
    name: metrics-server
    namespace: kube-system
    resourceVersion: "630"
    uid: c4a40432-29dc-472f-8d65-37143d381dbd
  spec:
    clusterIP: 10.109.70.19
    clusterIPs:
    - 10.109.70.19
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - name: https
      port: 443
      protocol: TCP
      targetPort: https
    selector:
      k8s-app: metrics-server
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
- apiVersion: apps/v1
  kind: DaemonSet
  metadata:
    annotations:
      deprecated.daemonset.template.generation: "1"
    creationTimestamp: "2023-10-24T07:41:06Z"
    generation: 1
    labels:
      k8s-app: kube-proxy
    name: kube-proxy
    namespace: kube-system
    resourceVersion: "50756"
    uid: 3eb2857b-792a-4dd0-beff-fb537a5fbd09
  spec:
    revisionHistoryLimit: 10
    selector:
      matchLabels:
        k8s-app: kube-proxy
    template:
      metadata:
        creationTimestamp: null
        labels:
          k8s-app: kube-proxy
      spec:
        containers:
        - command:
          - /usr/local/bin/kube-proxy
          - --config=/var/lib/kube-proxy/config.conf
          - --hostname-override=$(NODE_NAME)
          env:
          - name: NODE_NAME
            valueFrom:
              fieldRef:
                apiVersion: v1
                fieldPath: spec.nodeName
          image: registry.k8s.io/kube-proxy:v1.27.4
          imagePullPolicy: IfNotPresent
          name: kube-proxy
          resources: {}
          securityContext:
            privileged: true
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
          - mountPath: /var/lib/kube-proxy
            name: kube-proxy
          - mountPath: /run/xtables.lock
            name: xtables-lock
          - mountPath: /lib/modules
            name: lib-modules
            readOnly: true
        dnsPolicy: ClusterFirst
        hostNetwork: true
        nodeSelector:
          kubernetes.io/os: linux
        priorityClassName: system-node-critical
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        serviceAccount: kube-proxy
        serviceAccountName: kube-proxy
        terminationGracePeriodSeconds: 30
        tolerations:
        - operator: Exists
        volumes:
        - configMap:
            defaultMode: 420
            name: kube-proxy
          name: kube-proxy
        - hostPath:
            path: /run/xtables.lock
            type: FileOrCreate
          name: xtables-lock
        - hostPath:
            path: /lib/modules
            type: ""
          name: lib-modules
    updateStrategy:
      rollingUpdate:
        maxSurge: 0
        maxUnavailable: 1
      type: RollingUpdate
  status:
    currentNumberScheduled: 1
    desiredNumberScheduled: 1
    numberAvailable: 1
    numberMisscheduled: 0
    numberReady: 1
    observedGeneration: 1
    updatedNumberScheduled: 1
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    annotations:
      deployment.kubernetes.io/revision: "1"
      meta.helm.sh/release-name: fastapi-release-dev
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-25T22:45:29Z"
    generation: 1
    labels:
      app.kubernetes.io/managed-by: Helm
    name: model-serve
    namespace: dev
    resourceVersion: "64559"
    uid: dea8ce01-d8fe-4e35-8499-24da6b0a92e2
  spec:
    progressDeadlineSeconds: 600
    replicas: 1
    revisionHistoryLimit: 10
    selector:
      matchLabels:
        app: model-serve
    strategy:
      rollingUpdate:
        maxSurge: 25%
        maxUnavailable: 25%
      type: RollingUpdate
    template:
      metadata:
        creationTimestamp: null
        labels:
          app: model-serve
      spec:
        containers:
        - env:
          - name: REDIS_HOST
            valueFrom:
              configMapKeyRef:
                key: hostname
                name: redis-config-v1.0
          - name: REDIS_PORT
            valueFrom:
              configMapKeyRef:
                key: port
                name: redis-config-v1.0
          - name: REDIS_PASSWORD
            valueFrom:
              secretKeyRef:
                key: db_password
                name: redis-secret-v1.0
          - name: HF_MODEL
            valueFrom:
              configMapKeyRef:
                key: hf_model
                name: model-config-v1.0
          image: gpt-model-server:latest
          imagePullPolicy: Never
          name: model-serve
          ports:
          - containerPort: 80
            protocol: TCP
          resources: {}
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        terminationGracePeriodSeconds: 30
  status:
    availableReplicas: 1
    conditions:
    - lastTransitionTime: "2023-10-25T22:45:30Z"
      lastUpdateTime: "2023-10-25T22:45:30Z"
      message: Deployment has minimum availability.
      reason: MinimumReplicasAvailable
      status: "True"
      type: Available
    - lastTransitionTime: "2023-10-25T22:45:29Z"
      lastUpdateTime: "2023-10-25T22:45:30Z"
      message: ReplicaSet "model-serve-7549bc9b6" has successfully progressed.
      reason: NewReplicaSetAvailable
      status: "True"
      type: Progressing
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
    updatedReplicas: 1
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    annotations:
      deployment.kubernetes.io/revision: "1"
      meta.helm.sh/release-name: fastapi-release-dev
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-25T22:45:29Z"
    generation: 1
    labels:
      app.kubernetes.io/managed-by: Helm
    name: redis-db
    namespace: dev
    resourceVersion: "64588"
    uid: 3c617f61-95ae-48d8-afc6-5209ae3fb195
  spec:
    progressDeadlineSeconds: 600
    replicas: 1
    revisionHistoryLimit: 10
    selector:
      matchLabels:
        app: redis-db
        role: master
    strategy:
      rollingUpdate:
        maxSurge: 25%
        maxUnavailable: 25%
      type: RollingUpdate
    template:
      metadata:
        creationTimestamp: null
        labels:
          app: redis-db
          role: master
      spec:
        containers:
        - args:
          - --requirepass
          - $(REDIS_PASSWORD)
          command:
          - redis-server
          env:
          - name: REDIS_PASSWORD
            valueFrom:
              secretKeyRef:
                key: db_password
                name: redis-secret-v1.0
          image: redis:7.2.1
          imagePullPolicy: IfNotPresent
          name: redis-master
          ports:
          - containerPort: 6379
            protocol: TCP
          resources:
            limits:
              cpu: 200m
              memory: 200Mi
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        terminationGracePeriodSeconds: 30
        volumes:
        - name: redis-storage
          persistentVolumeClaim:
            claimName: redis-pvc
  status:
    availableReplicas: 1
    conditions:
    - lastTransitionTime: "2023-10-25T22:45:43Z"
      lastUpdateTime: "2023-10-25T22:45:43Z"
      message: Deployment has minimum availability.
      reason: MinimumReplicasAvailable
      status: "True"
      type: Available
    - lastTransitionTime: "2023-10-25T22:45:29Z"
      lastUpdateTime: "2023-10-25T22:45:43Z"
      message: ReplicaSet "redis-db-686b7bfff8" has successfully progressed.
      reason: NewReplicaSetAvailable
      status: "True"
      type: Progressing
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
    updatedReplicas: 1
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    annotations:
      deployment.kubernetes.io/revision: "1"
      meta.helm.sh/release-name: fastapi-release-dev
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-25T22:45:29Z"
    generation: 1
    labels:
      app: web-serve
      app.kubernetes.io/managed-by: Helm
    name: web-serve
    namespace: dev
    resourceVersion: "64554"
    uid: e4098ee1-7b50-4d3b-92e4-1b04b2bd727d
  spec:
    progressDeadlineSeconds: 600
    replicas: 1
    revisionHistoryLimit: 10
    selector:
      matchLabels:
        app: web-serve
    strategy:
      rollingUpdate:
        maxSurge: 25%
        maxUnavailable: 25%
      type: RollingUpdate
    template:
      metadata:
        creationTimestamp: null
        labels:
          app: web-serve
      spec:
        containers:
        - env:
          - name: REDIS_HOST
            valueFrom:
              configMapKeyRef:
                key: hostname
                name: redis-config-v1.0
          - name: REDIS_PORT
            valueFrom:
              configMapKeyRef:
                key: port
                name: redis-config-v1.0
          - name: REDIS_PASSWORD
            valueFrom:
              secretKeyRef:
                key: db_password
                name: redis-secret-v1.0
          - name: MODEL_SERVER_URL
            valueFrom:
              configMapKeyRef:
                key: model_server_url
                name: model-config-v1.0
          image: gpt-web-server:latest
          imagePullPolicy: Never
          name: web-serve
          ports:
          - containerPort: 80
            protocol: TCP
          resources: {}
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        terminationGracePeriodSeconds: 30
  status:
    availableReplicas: 1
    conditions:
    - lastTransitionTime: "2023-10-25T22:45:30Z"
      lastUpdateTime: "2023-10-25T22:45:30Z"
      message: Deployment has minimum availability.
      reason: MinimumReplicasAvailable
      status: "True"
      type: Available
    - lastTransitionTime: "2023-10-25T22:45:29Z"
      lastUpdateTime: "2023-10-25T22:45:30Z"
      message: ReplicaSet "web-serve-566fb45bb9" has successfully progressed.
      reason: NewReplicaSetAvailable
      status: "True"
      type: Progressing
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
    updatedReplicas: 1
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    annotations:
      deployment.kubernetes.io/revision: "1"
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-controller","namespace":"ingress-nginx"},"spec":{"minReadySeconds":0,"revisionHistoryLimit":10,"selector":{"matchLabels":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"}},"strategy":{"rollingUpdate":{"maxUnavailable":1},"type":"RollingUpdate"},"template":{"metadata":{"labels":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx","gcp-auth-skip-secret":"true"}},"spec":{"containers":[{"args":["/nginx-ingress-controller","--election-id=ingress-nginx-leader","--controller-class=k8s.io/ingress-nginx","--watch-ingress-without-class=true","--configmap=$(POD_NAMESPACE)/ingress-nginx-controller","--tcp-services-configmap=$(POD_NAMESPACE)/tcp-services","--udp-services-configmap=$(POD_NAMESPACE)/udp-services","--validating-webhook=:8443","--validating-webhook-certificate=/usr/local/certificates/cert","--validating-webhook-key=/usr/local/certificates/key"],"env":[{"name":"POD_NAME","valueFrom":{"fieldRef":{"fieldPath":"metadata.name"}}},{"name":"POD_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}},{"name":"LD_PRELOAD","value":"/usr/local/lib/libmimalloc.so"}],"image":"registry.k8s.io/ingress-nginx/controller:v1.8.1@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd","imagePullPolicy":"IfNotPresent","lifecycle":{"preStop":{"exec":{"command":["/wait-shutdown"]}}},"livenessProbe":{"failureThreshold":5,"httpGet":{"path":"/healthz","port":10254,"scheme":"HTTP"},"initialDelaySeconds":10,"periodSeconds":10,"successThreshold":1,"timeoutSeconds":1},"name":"controller","ports":[{"containerPort":80,"hostPort":80,"name":"http","protocol":"TCP"},{"containerPort":443,"hostPort":443,"name":"https","protocol":"TCP"},{"containerPort":8443,"name":"webhook","protocol":"TCP"}],"readinessProbe":{"failureThreshold":3,"httpGet":{"path":"/healthz","port":10254,"scheme":"HTTP"},"initialDelaySeconds":10,"periodSeconds":10,"successThreshold":1,"timeoutSeconds":1},"resources":{"requests":{"cpu":"100m","memory":"90Mi"}},"securityContext":{"allowPrivilegeEscalation":true,"capabilities":{"add":["NET_BIND_SERVICE"],"drop":["ALL"]},"runAsUser":101},"volumeMounts":[{"mountPath":"/usr/local/certificates/","name":"webhook-cert","readOnly":true}]}],"dnsPolicy":"ClusterFirst","nodeSelector":{"kubernetes.io/os":"linux","minikube.k8s.io/primary":"true"},"serviceAccountName":"ingress-nginx","terminationGracePeriodSeconds":0,"tolerations":[{"effect":"NoSchedule","key":"node-role.kubernetes.io/master","operator":"Equal"}],"volumes":[{"name":"webhook-cert","secret":{"secretName":"ingress-nginx-admission"}}]}}}}
    creationTimestamp: "2023-10-24T07:46:33Z"
    generation: 1
    labels:
      app.kubernetes.io/component: controller
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
    name: ingress-nginx-controller
    namespace: ingress-nginx
    resourceVersion: "50909"
    uid: 7e49ef92-6ed3-4bfc-819b-642021317e72
  spec:
    progressDeadlineSeconds: 600
    replicas: 1
    revisionHistoryLimit: 10
    selector:
      matchLabels:
        app.kubernetes.io/component: controller
        app.kubernetes.io/instance: ingress-nginx
        app.kubernetes.io/name: ingress-nginx
    strategy:
      rollingUpdate:
        maxSurge: 25%
        maxUnavailable: 1
      type: RollingUpdate
    template:
      metadata:
        creationTimestamp: null
        labels:
          app.kubernetes.io/component: controller
          app.kubernetes.io/instance: ingress-nginx
          app.kubernetes.io/name: ingress-nginx
          gcp-auth-skip-secret: "true"
      spec:
        containers:
        - args:
          - /nginx-ingress-controller
          - --election-id=ingress-nginx-leader
          - --controller-class=k8s.io/ingress-nginx
          - --watch-ingress-without-class=true
          - --configmap=$(POD_NAMESPACE)/ingress-nginx-controller
          - --tcp-services-configmap=$(POD_NAMESPACE)/tcp-services
          - --udp-services-configmap=$(POD_NAMESPACE)/udp-services
          - --validating-webhook=:8443
          - --validating-webhook-certificate=/usr/local/certificates/cert
          - --validating-webhook-key=/usr/local/certificates/key
          env:
          - name: POD_NAME
            valueFrom:
              fieldRef:
                apiVersion: v1
                fieldPath: metadata.name
          - name: POD_NAMESPACE
            valueFrom:
              fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
          - name: LD_PRELOAD
            value: /usr/local/lib/libmimalloc.so
          image: registry.k8s.io/ingress-nginx/controller:v1.8.1@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd
          imagePullPolicy: IfNotPresent
          lifecycle:
            preStop:
              exec:
                command:
                - /wait-shutdown
          livenessProbe:
            failureThreshold: 5
            httpGet:
              path: /healthz
              port: 10254
              scheme: HTTP
            initialDelaySeconds: 10
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          name: controller
          ports:
          - containerPort: 80
            hostPort: 80
            name: http
            protocol: TCP
          - containerPort: 443
            hostPort: 443
            name: https
            protocol: TCP
          - containerPort: 8443
            name: webhook
            protocol: TCP
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: /healthz
              port: 10254
              scheme: HTTP
            initialDelaySeconds: 10
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          resources:
            requests:
              cpu: 100m
              memory: 90Mi
          securityContext:
            allowPrivilegeEscalation: true
            capabilities:
              add:
              - NET_BIND_SERVICE
              drop:
              - ALL
            runAsUser: 101
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
          - mountPath: /usr/local/certificates/
            name: webhook-cert
            readOnly: true
        dnsPolicy: ClusterFirst
        nodeSelector:
          kubernetes.io/os: linux
          minikube.k8s.io/primary: "true"
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        serviceAccount: ingress-nginx
        serviceAccountName: ingress-nginx
        terminationGracePeriodSeconds: 0
        tolerations:
        - effect: NoSchedule
          key: node-role.kubernetes.io/master
          operator: Equal
        volumes:
        - name: webhook-cert
          secret:
            defaultMode: 420
            secretName: ingress-nginx-admission
  status:
    availableReplicas: 1
    conditions:
    - lastTransitionTime: "2023-10-24T07:46:33Z"
      lastUpdateTime: "2023-10-24T07:46:33Z"
      message: Deployment has minimum availability.
      reason: MinimumReplicasAvailable
      status: "True"
      type: Available
    - lastTransitionTime: "2023-10-24T07:46:33Z"
      lastUpdateTime: "2023-10-24T07:47:19Z"
      message: ReplicaSet "ingress-nginx-controller-7799c6795f" has successfully progressed.
      reason: NewReplicaSetAvailable
      status: "True"
      type: Progressing
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
    updatedReplicas: 1
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    annotations:
      deployment.kubernetes.io/revision: "1"
    creationTimestamp: "2023-10-24T07:41:06Z"
    generation: 5
    labels:
      k8s-app: kube-dns
    name: coredns
    namespace: kube-system
    resourceVersion: "50898"
    uid: 3cd8abbf-7656-4088-953d-87b517bebd86
  spec:
    progressDeadlineSeconds: 600
    replicas: 1
    revisionHistoryLimit: 10
    selector:
      matchLabels:
        k8s-app: kube-dns
    strategy:
      rollingUpdate:
        maxSurge: 25%
        maxUnavailable: 1
      type: RollingUpdate
    template:
      metadata:
        creationTimestamp: null
        labels:
          k8s-app: kube-dns
      spec:
        affinity:
          podAntiAffinity:
            preferredDuringSchedulingIgnoredDuringExecution:
            - podAffinityTerm:
                labelSelector:
                  matchExpressions:
                  - key: k8s-app
                    operator: In
                    values:
                    - kube-dns
                topologyKey: kubernetes.io/hostname
              weight: 100
        containers:
        - args:
          - -conf
          - /etc/coredns/Corefile
          image: registry.k8s.io/coredns/coredns:v1.10.1
          imagePullPolicy: IfNotPresent
          livenessProbe:
            failureThreshold: 5
            httpGet:
              path: /health
              port: 8080
              scheme: HTTP
            initialDelaySeconds: 60
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 5
          name: coredns
          ports:
          - containerPort: 53
            name: dns
            protocol: UDP
          - containerPort: 53
            name: dns-tcp
            protocol: TCP
          - containerPort: 9153
            name: metrics
            protocol: TCP
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: /ready
              port: 8181
              scheme: HTTP
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          resources:
            limits:
              memory: 170Mi
            requests:
              cpu: 100m
              memory: 70Mi
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              add:
              - NET_BIND_SERVICE
              drop:
              - all
            readOnlyRootFilesystem: true
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
          - mountPath: /etc/coredns
            name: config-volume
            readOnly: true
        dnsPolicy: Default
        nodeSelector:
          kubernetes.io/os: linux
        priorityClassName: system-cluster-critical
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        serviceAccount: coredns
        serviceAccountName: coredns
        terminationGracePeriodSeconds: 30
        tolerations:
        - key: CriticalAddonsOnly
          operator: Exists
        - effect: NoSchedule
          key: node-role.kubernetes.io/control-plane
        volumes:
        - configMap:
            defaultMode: 420
            items:
            - key: Corefile
              path: Corefile
            name: coredns
          name: config-volume
  status:
    availableReplicas: 1
    conditions:
    - lastTransitionTime: "2023-10-24T07:41:19Z"
      lastUpdateTime: "2023-10-24T07:41:19Z"
      message: Deployment has minimum availability.
      reason: MinimumReplicasAvailable
      status: "True"
      type: Available
    - lastTransitionTime: "2023-10-24T07:41:19Z"
      lastUpdateTime: "2023-10-24T07:41:21Z"
      message: ReplicaSet "coredns-5d78c9869d" has successfully progressed.
      reason: NewReplicaSetAvailable
      status: "True"
      type: Progressing
    observedGeneration: 5
    readyReplicas: 1
    replicas: 1
    updatedReplicas: 1
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    annotations:
      deployment.kubernetes.io/revision: "1"
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{},"labels":{"addonmanager.kubernetes.io/mode":"Reconcile","k8s-app":"metrics-server","kubernetes.io/minikube-addons":"metrics-server"},"name":"metrics-server","namespace":"kube-system"},"spec":{"selector":{"matchLabels":{"k8s-app":"metrics-server"}},"strategy":{"rollingUpdate":{"maxUnavailable":0}},"template":{"metadata":{"labels":{"k8s-app":"metrics-server"},"name":"metrics-server"},"spec":{"containers":[{"args":["--cert-dir=/tmp","--secure-port=4443","--kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname","--kubelet-use-node-status-port","--metric-resolution=60s","--kubelet-insecure-tls"],"image":"registry.k8s.io/metrics-server/metrics-server:v0.6.4@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e","imagePullPolicy":"IfNotPresent","livenessProbe":{"failureThreshold":3,"httpGet":{"path":"/livez","port":"https","scheme":"HTTPS"},"periodSeconds":10},"name":"metrics-server","ports":[{"containerPort":4443,"name":"https","protocol":"TCP"}],"readinessProbe":{"failureThreshold":3,"httpGet":{"path":"/readyz","port":"https","scheme":"HTTPS"},"periodSeconds":10},"resources":{"requests":{"cpu":"100m","memory":"200Mi"}},"securityContext":{"readOnlyRootFilesystem":true,"runAsNonRoot":true,"runAsUser":1000},"volumeMounts":[{"mountPath":"/tmp","name":"tmp-dir"}]}],"priorityClassName":"system-cluster-critical","serviceAccountName":"metrics-server","volumes":[{"emptyDir":{},"name":"tmp-dir"}]}}}}
    creationTimestamp: "2023-10-24T07:46:28Z"
    generation: 1
    labels:
      addonmanager.kubernetes.io/mode: Reconcile
      k8s-app: metrics-server
      kubernetes.io/minikube-addons: metrics-server
    name: metrics-server
    namespace: kube-system
    resourceVersion: "50932"
    uid: 8a8a30ca-2e6c-47cb-b3a7-ec24306ef542
  spec:
    progressDeadlineSeconds: 600
    replicas: 1
    revisionHistoryLimit: 10
    selector:
      matchLabels:
        k8s-app: metrics-server
    strategy:
      rollingUpdate:
        maxSurge: 25%
        maxUnavailable: 0
      type: RollingUpdate
    template:
      metadata:
        creationTimestamp: null
        labels:
          k8s-app: metrics-server
        name: metrics-server
      spec:
        containers:
        - args:
          - --cert-dir=/tmp
          - --secure-port=4443
          - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
          - --kubelet-use-node-status-port
          - --metric-resolution=60s
          - --kubelet-insecure-tls
          image: registry.k8s.io/metrics-server/metrics-server:v0.6.4@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e
          imagePullPolicy: IfNotPresent
          livenessProbe:
            failureThreshold: 3
            httpGet:
              path: /livez
              port: https
              scheme: HTTPS
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          name: metrics-server
          ports:
          - containerPort: 4443
            name: https
            protocol: TCP
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: /readyz
              port: https
              scheme: HTTPS
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          resources:
            requests:
              cpu: 100m
              memory: 200Mi
          securityContext:
            readOnlyRootFilesystem: true
            runAsNonRoot: true
            runAsUser: 1000
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
          - mountPath: /tmp
            name: tmp-dir
        dnsPolicy: ClusterFirst
        priorityClassName: system-cluster-critical
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        serviceAccount: metrics-server
        serviceAccountName: metrics-server
        terminationGracePeriodSeconds: 30
        volumes:
        - emptyDir: {}
          name: tmp-dir
  status:
    availableReplicas: 1
    conditions:
    - lastTransitionTime: "2023-10-24T07:46:28Z"
      lastUpdateTime: "2023-10-24T07:47:39Z"
      message: ReplicaSet "metrics-server-7746886d4f" has successfully progressed.
      reason: NewReplicaSetAvailable
      status: "True"
      type: Progressing
    - lastTransitionTime: "2023-10-25T19:02:14Z"
      lastUpdateTime: "2023-10-25T19:02:14Z"
      message: Deployment has minimum availability.
      reason: MinimumReplicasAvailable
      status: "True"
      type: Available
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
    updatedReplicas: 1
- apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    annotations:
      deployment.kubernetes.io/desired-replicas: "1"
      deployment.kubernetes.io/max-replicas: "2"
      deployment.kubernetes.io/revision: "1"
      meta.helm.sh/release-name: fastapi-release-dev
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-25T22:45:29Z"
    generation: 1
    labels:
      app: model-serve
      pod-template-hash: 7549bc9b6
    name: model-serve-7549bc9b6
    namespace: dev
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: Deployment
      name: model-serve
      uid: dea8ce01-d8fe-4e35-8499-24da6b0a92e2
    resourceVersion: "64558"
    uid: b6c26587-1a61-45f8-a9d3-958053ef17a2
  spec:
    replicas: 1
    selector:
      matchLabels:
        app: model-serve
        pod-template-hash: 7549bc9b6
    template:
      metadata:
        creationTimestamp: null
        labels:
          app: model-serve
          pod-template-hash: 7549bc9b6
      spec:
        containers:
        - env:
          - name: REDIS_HOST
            valueFrom:
              configMapKeyRef:
                key: hostname
                name: redis-config-v1.0
          - name: REDIS_PORT
            valueFrom:
              configMapKeyRef:
                key: port
                name: redis-config-v1.0
          - name: REDIS_PASSWORD
            valueFrom:
              secretKeyRef:
                key: db_password
                name: redis-secret-v1.0
          - name: HF_MODEL
            valueFrom:
              configMapKeyRef:
                key: hf_model
                name: model-config-v1.0
          image: gpt-model-server:latest
          imagePullPolicy: Never
          name: model-serve
          ports:
          - containerPort: 80
            protocol: TCP
          resources: {}
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        terminationGracePeriodSeconds: 30
  status:
    availableReplicas: 1
    fullyLabeledReplicas: 1
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
- apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    annotations:
      deployment.kubernetes.io/desired-replicas: "1"
      deployment.kubernetes.io/max-replicas: "2"
      deployment.kubernetes.io/revision: "1"
      meta.helm.sh/release-name: fastapi-release-dev
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-25T22:45:29Z"
    generation: 1
    labels:
      app: redis-db
      pod-template-hash: 686b7bfff8
      role: master
    name: redis-db-686b7bfff8
    namespace: dev
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: Deployment
      name: redis-db
      uid: 3c617f61-95ae-48d8-afc6-5209ae3fb195
    resourceVersion: "64587"
    uid: dab7978c-9694-4e8f-8c89-9f2d77c6a564
  spec:
    replicas: 1
    selector:
      matchLabels:
        app: redis-db
        pod-template-hash: 686b7bfff8
        role: master
    template:
      metadata:
        creationTimestamp: null
        labels:
          app: redis-db
          pod-template-hash: 686b7bfff8
          role: master
      spec:
        containers:
        - args:
          - --requirepass
          - $(REDIS_PASSWORD)
          command:
          - redis-server
          env:
          - name: REDIS_PASSWORD
            valueFrom:
              secretKeyRef:
                key: db_password
                name: redis-secret-v1.0
          image: redis:7.2.1
          imagePullPolicy: IfNotPresent
          name: redis-master
          ports:
          - containerPort: 6379
            protocol: TCP
          resources:
            limits:
              cpu: 200m
              memory: 200Mi
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        terminationGracePeriodSeconds: 30
        volumes:
        - name: redis-storage
          persistentVolumeClaim:
            claimName: redis-pvc
  status:
    availableReplicas: 1
    fullyLabeledReplicas: 1
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
- apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    annotations:
      deployment.kubernetes.io/desired-replicas: "1"
      deployment.kubernetes.io/max-replicas: "2"
      deployment.kubernetes.io/revision: "1"
      meta.helm.sh/release-name: fastapi-release-dev
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-25T22:45:29Z"
    generation: 1
    labels:
      app: web-serve
      pod-template-hash: 566fb45bb9
    name: web-serve-566fb45bb9
    namespace: dev
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: Deployment
      name: web-serve
      uid: e4098ee1-7b50-4d3b-92e4-1b04b2bd727d
    resourceVersion: "64553"
    uid: f3341d18-770d-4e4f-93a7-aa1993c63bcf
  spec:
    replicas: 1
    selector:
      matchLabels:
        app: web-serve
        pod-template-hash: 566fb45bb9
    template:
      metadata:
        creationTimestamp: null
        labels:
          app: web-serve
          pod-template-hash: 566fb45bb9
      spec:
        containers:
        - env:
          - name: REDIS_HOST
            valueFrom:
              configMapKeyRef:
                key: hostname
                name: redis-config-v1.0
          - name: REDIS_PORT
            valueFrom:
              configMapKeyRef:
                key: port
                name: redis-config-v1.0
          - name: REDIS_PASSWORD
            valueFrom:
              secretKeyRef:
                key: db_password
                name: redis-secret-v1.0
          - name: MODEL_SERVER_URL
            valueFrom:
              configMapKeyRef:
                key: model_server_url
                name: model-config-v1.0
          image: gpt-web-server:latest
          imagePullPolicy: Never
          name: web-serve
          ports:
          - containerPort: 80
            protocol: TCP
          resources: {}
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        terminationGracePeriodSeconds: 30
  status:
    availableReplicas: 1
    fullyLabeledReplicas: 1
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
- apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    annotations:
      deployment.kubernetes.io/desired-replicas: "1"
      deployment.kubernetes.io/max-replicas: "2"
      deployment.kubernetes.io/revision: "1"
    creationTimestamp: "2023-10-24T07:46:33Z"
    generation: 1
    labels:
      app.kubernetes.io/component: controller
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
      gcp-auth-skip-secret: "true"
      pod-template-hash: 7799c6795f
    name: ingress-nginx-controller-7799c6795f
    namespace: ingress-nginx
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: Deployment
      name: ingress-nginx-controller
      uid: 7e49ef92-6ed3-4bfc-819b-642021317e72
    resourceVersion: "50908"
    uid: 703ba820-1234-405e-8939-205eb16235ff
  spec:
    replicas: 1
    selector:
      matchLabels:
        app.kubernetes.io/component: controller
        app.kubernetes.io/instance: ingress-nginx
        app.kubernetes.io/name: ingress-nginx
        pod-template-hash: 7799c6795f
    template:
      metadata:
        creationTimestamp: null
        labels:
          app.kubernetes.io/component: controller
          app.kubernetes.io/instance: ingress-nginx
          app.kubernetes.io/name: ingress-nginx
          gcp-auth-skip-secret: "true"
          pod-template-hash: 7799c6795f
      spec:
        containers:
        - args:
          - /nginx-ingress-controller
          - --election-id=ingress-nginx-leader
          - --controller-class=k8s.io/ingress-nginx
          - --watch-ingress-without-class=true
          - --configmap=$(POD_NAMESPACE)/ingress-nginx-controller
          - --tcp-services-configmap=$(POD_NAMESPACE)/tcp-services
          - --udp-services-configmap=$(POD_NAMESPACE)/udp-services
          - --validating-webhook=:8443
          - --validating-webhook-certificate=/usr/local/certificates/cert
          - --validating-webhook-key=/usr/local/certificates/key
          env:
          - name: POD_NAME
            valueFrom:
              fieldRef:
                apiVersion: v1
                fieldPath: metadata.name
          - name: POD_NAMESPACE
            valueFrom:
              fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
          - name: LD_PRELOAD
            value: /usr/local/lib/libmimalloc.so
          image: registry.k8s.io/ingress-nginx/controller:v1.8.1@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd
          imagePullPolicy: IfNotPresent
          lifecycle:
            preStop:
              exec:
                command:
                - /wait-shutdown
          livenessProbe:
            failureThreshold: 5
            httpGet:
              path: /healthz
              port: 10254
              scheme: HTTP
            initialDelaySeconds: 10
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          name: controller
          ports:
          - containerPort: 80
            hostPort: 80
            name: http
            protocol: TCP
          - containerPort: 443
            hostPort: 443
            name: https
            protocol: TCP
          - containerPort: 8443
            name: webhook
            protocol: TCP
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: /healthz
              port: 10254
              scheme: HTTP
            initialDelaySeconds: 10
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          resources:
            requests:
              cpu: 100m
              memory: 90Mi
          securityContext:
            allowPrivilegeEscalation: true
            capabilities:
              add:
              - NET_BIND_SERVICE
              drop:
              - ALL
            runAsUser: 101
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
          - mountPath: /usr/local/certificates/
            name: webhook-cert
            readOnly: true
        dnsPolicy: ClusterFirst
        nodeSelector:
          kubernetes.io/os: linux
          minikube.k8s.io/primary: "true"
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        serviceAccount: ingress-nginx
        serviceAccountName: ingress-nginx
        terminationGracePeriodSeconds: 0
        tolerations:
        - effect: NoSchedule
          key: node-role.kubernetes.io/master
          operator: Equal
        volumes:
        - name: webhook-cert
          secret:
            defaultMode: 420
            secretName: ingress-nginx-admission
  status:
    availableReplicas: 1
    fullyLabeledReplicas: 1
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
- apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    annotations:
      deployment.kubernetes.io/desired-replicas: "1"
      deployment.kubernetes.io/max-replicas: "2"
      deployment.kubernetes.io/revision: "1"
    creationTimestamp: "2023-10-24T07:41:19Z"
    generation: 1
    labels:
      k8s-app: kube-dns
      pod-template-hash: 5d78c9869d
    name: coredns-5d78c9869d
    namespace: kube-system
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: Deployment
      name: coredns
      uid: 3cd8abbf-7656-4088-953d-87b517bebd86
    resourceVersion: "50897"
    uid: 5e54de92-26a5-483f-8482-c80a7e495792
  spec:
    replicas: 1
    selector:
      matchLabels:
        k8s-app: kube-dns
        pod-template-hash: 5d78c9869d
    template:
      metadata:
        creationTimestamp: null
        labels:
          k8s-app: kube-dns
          pod-template-hash: 5d78c9869d
      spec:
        affinity:
          podAntiAffinity:
            preferredDuringSchedulingIgnoredDuringExecution:
            - podAffinityTerm:
                labelSelector:
                  matchExpressions:
                  - key: k8s-app
                    operator: In
                    values:
                    - kube-dns
                topologyKey: kubernetes.io/hostname
              weight: 100
        containers:
        - args:
          - -conf
          - /etc/coredns/Corefile
          image: registry.k8s.io/coredns/coredns:v1.10.1
          imagePullPolicy: IfNotPresent
          livenessProbe:
            failureThreshold: 5
            httpGet:
              path: /health
              port: 8080
              scheme: HTTP
            initialDelaySeconds: 60
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 5
          name: coredns
          ports:
          - containerPort: 53
            name: dns
            protocol: UDP
          - containerPort: 53
            name: dns-tcp
            protocol: TCP
          - containerPort: 9153
            name: metrics
            protocol: TCP
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: /ready
              port: 8181
              scheme: HTTP
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          resources:
            limits:
              memory: 170Mi
            requests:
              cpu: 100m
              memory: 70Mi
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              add:
              - NET_BIND_SERVICE
              drop:
              - all
            readOnlyRootFilesystem: true
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
          - mountPath: /etc/coredns
            name: config-volume
            readOnly: true
        dnsPolicy: Default
        nodeSelector:
          kubernetes.io/os: linux
        priorityClassName: system-cluster-critical
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        serviceAccount: coredns
        serviceAccountName: coredns
        terminationGracePeriodSeconds: 30
        tolerations:
        - key: CriticalAddonsOnly
          operator: Exists
        - effect: NoSchedule
          key: node-role.kubernetes.io/control-plane
        volumes:
        - configMap:
            defaultMode: 420
            items:
            - key: Corefile
              path: Corefile
            name: coredns
          name: config-volume
  status:
    availableReplicas: 1
    fullyLabeledReplicas: 1
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
- apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    annotations:
      deployment.kubernetes.io/desired-replicas: "1"
      deployment.kubernetes.io/max-replicas: "2"
      deployment.kubernetes.io/revision: "1"
    creationTimestamp: "2023-10-24T07:46:28Z"
    generation: 1
    labels:
      k8s-app: metrics-server
      pod-template-hash: 7746886d4f
    name: metrics-server-7746886d4f
    namespace: kube-system
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: Deployment
      name: metrics-server
      uid: 8a8a30ca-2e6c-47cb-b3a7-ec24306ef542
    resourceVersion: "50930"
    uid: aa735f0f-911a-457b-a096-dad3f1c6d22d
  spec:
    replicas: 1
    selector:
      matchLabels:
        k8s-app: metrics-server
        pod-template-hash: 7746886d4f
    template:
      metadata:
        creationTimestamp: null
        labels:
          k8s-app: metrics-server
          pod-template-hash: 7746886d4f
        name: metrics-server
      spec:
        containers:
        - args:
          - --cert-dir=/tmp
          - --secure-port=4443
          - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
          - --kubelet-use-node-status-port
          - --metric-resolution=60s
          - --kubelet-insecure-tls
          image: registry.k8s.io/metrics-server/metrics-server:v0.6.4@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e
          imagePullPolicy: IfNotPresent
          livenessProbe:
            failureThreshold: 3
            httpGet:
              path: /livez
              port: https
              scheme: HTTPS
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          name: metrics-server
          ports:
          - containerPort: 4443
            name: https
            protocol: TCP
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: /readyz
              port: https
              scheme: HTTPS
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          resources:
            requests:
              cpu: 100m
              memory: 200Mi
          securityContext:
            readOnlyRootFilesystem: true
            runAsNonRoot: true
            runAsUser: 1000
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
          - mountPath: /tmp
            name: tmp-dir
        dnsPolicy: ClusterFirst
        priorityClassName: system-cluster-critical
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        serviceAccount: metrics-server
        serviceAccountName: metrics-server
        terminationGracePeriodSeconds: 30
        volumes:
        - emptyDir: {}
          name: tmp-dir
  status:
    availableReplicas: 1
    fullyLabeledReplicas: 1
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
- apiVersion: batch/v1
  kind: Job
  metadata:
    annotations:
      batch.kubernetes.io/job-tracking: ""
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"batch/v1","kind":"Job","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"admission-webhook","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-admission-create","namespace":"ingress-nginx"},"spec":{"template":{"metadata":{"labels":{"app.kubernetes.io/component":"admission-webhook","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-admission-create"},"spec":{"containers":[{"args":["create","--host=ingress-nginx-controller-admission,ingress-nginx-controller-admission.$(POD_NAMESPACE).svc","--namespace=$(POD_NAMESPACE)","--secret-name=ingress-nginx-admission"],"env":[{"name":"POD_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}}],"image":"registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b","imagePullPolicy":"IfNotPresent","name":"create","securityContext":{"allowPrivilegeEscalation":false}}],"nodeSelector":{"kubernetes.io/os":"linux","minikube.k8s.io/primary":"true"},"restartPolicy":"OnFailure","securityContext":{"runAsNonRoot":true,"runAsUser":2000},"serviceAccountName":"ingress-nginx-admission"}}}}
    creationTimestamp: "2023-10-24T07:46:33Z"
    generation: 1
    labels:
      app.kubernetes.io/component: admission-webhook
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
    name: ingress-nginx-admission-create
    namespace: ingress-nginx
    resourceVersion: "740"
    uid: 545a479b-89f6-497c-858e-fe287310d0e5
  spec:
    backoffLimit: 6
    completionMode: NonIndexed
    completions: 1
    parallelism: 1
    selector:
      matchLabels:
        batch.kubernetes.io/controller-uid: 545a479b-89f6-497c-858e-fe287310d0e5
    suspend: false
    template:
      metadata:
        creationTimestamp: null
        labels:
          app.kubernetes.io/component: admission-webhook
          app.kubernetes.io/instance: ingress-nginx
          app.kubernetes.io/name: ingress-nginx
          batch.kubernetes.io/controller-uid: 545a479b-89f6-497c-858e-fe287310d0e5
          batch.kubernetes.io/job-name: ingress-nginx-admission-create
          controller-uid: 545a479b-89f6-497c-858e-fe287310d0e5
          job-name: ingress-nginx-admission-create
        name: ingress-nginx-admission-create
      spec:
        containers:
        - args:
          - create
          - --host=ingress-nginx-controller-admission,ingress-nginx-controller-admission.$(POD_NAMESPACE).svc
          - --namespace=$(POD_NAMESPACE)
          - --secret-name=ingress-nginx-admission
          env:
          - name: POD_NAMESPACE
            valueFrom:
              fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
          image: registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
          imagePullPolicy: IfNotPresent
          name: create
          resources: {}
          securityContext:
            allowPrivilegeEscalation: false
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        nodeSelector:
          kubernetes.io/os: linux
          minikube.k8s.io/primary: "true"
        restartPolicy: OnFailure
        schedulerName: default-scheduler
        securityContext:
          runAsNonRoot: true
          runAsUser: 2000
        serviceAccount: ingress-nginx-admission
        serviceAccountName: ingress-nginx-admission
        terminationGracePeriodSeconds: 30
  status:
    completionTime: "2023-10-24T07:46:44Z"
    conditions:
    - lastProbeTime: "2023-10-24T07:46:44Z"
      lastTransitionTime: "2023-10-24T07:46:44Z"
      status: "True"
      type: Complete
    ready: 0
    startTime: "2023-10-24T07:46:33Z"
    succeeded: 1
    uncountedTerminatedPods: {}
- apiVersion: batch/v1
  kind: Job
  metadata:
    annotations:
      batch.kubernetes.io/job-tracking: ""
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"batch/v1","kind":"Job","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"admission-webhook","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-admission-patch","namespace":"ingress-nginx"},"spec":{"template":{"metadata":{"labels":{"app.kubernetes.io/component":"admission-webhook","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-admission-patch"},"spec":{"containers":[{"args":["patch","--webhook-name=ingress-nginx-admission","--namespace=$(POD_NAMESPACE)","--patch-mutating=false","--secret-name=ingress-nginx-admission","--patch-failure-policy=Fail"],"env":[{"name":"POD_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}}],"image":"registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b","imagePullPolicy":"IfNotPresent","name":"patch","securityContext":{"allowPrivilegeEscalation":false}}],"nodeSelector":{"kubernetes.io/os":"linux","minikube.k8s.io/primary":"true"},"restartPolicy":"OnFailure","securityContext":{"runAsNonRoot":true,"runAsUser":2000},"serviceAccountName":"ingress-nginx-admission"}}}}
    creationTimestamp: "2023-10-24T07:46:33Z"
    generation: 1
    labels:
      app.kubernetes.io/component: admission-webhook
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
    name: ingress-nginx-admission-patch
    namespace: ingress-nginx
    resourceVersion: "748"
    uid: 323613ba-5375-4acd-aaf0-d93c33152ebb
  spec:
    backoffLimit: 6
    completionMode: NonIndexed
    completions: 1
    parallelism: 1
    selector:
      matchLabels:
        batch.kubernetes.io/controller-uid: 323613ba-5375-4acd-aaf0-d93c33152ebb
    suspend: false
    template:
      metadata:
        creationTimestamp: null
        labels:
          app.kubernetes.io/component: admission-webhook
          app.kubernetes.io/instance: ingress-nginx
          app.kubernetes.io/name: ingress-nginx
          batch.kubernetes.io/controller-uid: 323613ba-5375-4acd-aaf0-d93c33152ebb
          batch.kubernetes.io/job-name: ingress-nginx-admission-patch
          controller-uid: 323613ba-5375-4acd-aaf0-d93c33152ebb
          job-name: ingress-nginx-admission-patch
        name: ingress-nginx-admission-patch
      spec:
        containers:
        - args:
          - patch
          - --webhook-name=ingress-nginx-admission
          - --namespace=$(POD_NAMESPACE)
          - --patch-mutating=false
          - --secret-name=ingress-nginx-admission
          - --patch-failure-policy=Fail
          env:
          - name: POD_NAMESPACE
            valueFrom:
              fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
          image: registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
          imagePullPolicy: IfNotPresent
          name: patch
          resources: {}
          securityContext:
            allowPrivilegeEscalation: false
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        nodeSelector:
          kubernetes.io/os: linux
          minikube.k8s.io/primary: "true"
        restartPolicy: OnFailure
        schedulerName: default-scheduler
        securityContext:
          runAsNonRoot: true
          runAsUser: 2000
        serviceAccount: ingress-nginx-admission
        serviceAccountName: ingress-nginx-admission
        terminationGracePeriodSeconds: 30
  status:
    completionTime: "2023-10-24T07:46:45Z"
    conditions:
    - lastProbeTime: "2023-10-24T07:46:45Z"
      lastTransitionTime: "2023-10-24T07:46:45Z"
      status: "True"
      type: Complete
    ready: 0
    startTime: "2023-10-24T07:46:33Z"
    succeeded: 1
    uncountedTerminatedPods: {}
kind: List
metadata:
  resourceVersion: ""
```

