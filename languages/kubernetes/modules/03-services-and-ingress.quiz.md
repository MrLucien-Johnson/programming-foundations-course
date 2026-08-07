# Quiz — Services & Ingress

1. What gives clients a stable address for changing pods?
   - A. Service
   - B. ReplicaSet only
   - C. ConfigMap
   - D. Namespace

2. What lists Service backend addresses?
   - A. EndpointSlices
   - B. Secrets
   - C. ResourceQuotas
   - D. StorageClasses

3. What implements an Ingress resource?
   - A. An ingress controller
   - B. The YAML file itself
   - C. kubelet alone
   - D. etcd clients

4. What does `targetPort` name?
   - A. The backend pod port
   - B. The public DNS zone
   - C. The node count
   - D. The TLS issuer

5. Why might a matching pod be absent from ready endpoints?
   - A. Its readiness probe fails
   - B. Its image has a tag
   - C. It has a namespace
   - D. It uses TCP
