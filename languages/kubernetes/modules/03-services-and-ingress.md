# Services & Ingress

**Course:** Kubernetes Course (donor / allowlist access)  
**Module:** 3 of 10

## Learning goals

By the end of this lesson you will be able to:

- Use Services to provide stable discovery over changing pod endpoints
- Choose ClusterIP, NodePort, LoadBalancer, or headless service behavior
- Route HTTP with Ingress while distinguishing controller, resource, DNS, and TLS responsibilities

## Why this matters

Pods are replaceable and their IPs change. Services and ingress create stable traffic paths, but only when selectors, ports, controllers, and application readiness agree.

## Core ideas

1. **A Service selector produces EndpointSlices** containing ready matching pod addresses.
2. **ClusterIP is the default internal virtual IP**; LoadBalancer asks an integration to provision external or internal load balancing.
3. **Ingress is an HTTP routing API, not the data plane** — an installed ingress controller implements it.
4. **`port`, `targetPort`, and container port describe different hops** and mismatches cause silent-looking failures.

## Worked example

### Lab: expose and diagnose an internal Service

```yaml
apiVersion: v1
kind: Service
metadata: {name: api, namespace: course}
spec:
  selector: {app: api}
  ports:
    - name: http
      port: 80
      targetPort: 8080
  type: ClusterIP
```

```bash
kubectl apply -f service.yaml
kubectl get service,endpointslice -n course
kubectl run curl -n course --rm -it --restart=Never   --image=curlimages/curl -- http://api.course.svc.cluster.local/health
```

If EndpointSlices are empty, compare the Service selector with pod labels and readiness.

## Practice

1. Create a ClusterIP Service and resolve its DNS name from another pod.
2. Break and repair a selector while watching EndpointSlices.
3. Write an Ingress rule for `/api` with a TLS secret and named backend port.

## Common mistakes

- Creating an Ingress resource without an ingress controller
- Confusing Service `port` with `targetPort`
- Debugging DNS first when the Service has no ready endpoints

## Stretch goal

Compare Ingress with Gateway API roles and resources for a multi-team platform.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](kubernetes-course.html) for the full path.
