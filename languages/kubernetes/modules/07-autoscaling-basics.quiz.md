# Quiz — Autoscaling basics

1. What does HPA change?
   - A. Workload replica count
   - B. Node kernel
   - C. Container image
   - D. PVC reclaim policy

2. CPU utilization for HPA is relative to what?
   - A. CPU requests
   - B. CPU limits only
   - C. Node count
   - D. Image size

3. What can add nodes for unschedulable pods?
   - A. A node autoscaler
   - B. HPA alone
   - C. A Service
   - D. A ConfigMap

4. Why set a maximum replica count?
   - A. To bound cost and downstream load
   - B. To disable metrics
   - C. To encrypt Secrets
   - D. To assign nodes manually

5. What reduces rapid scale-down oscillation?
   - A. A stabilization window
   - B. Deleting requests
   - C. Using `latest`
   - D. A NodePort
