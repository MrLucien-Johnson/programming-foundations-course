# Quiz — Kubernetes security basics

1. What does Kubernetes RBAC govern?
   - A. API actions on resources
   - B. Container network packets
   - C. Image vulnerabilities
   - D. Disk encryption

2. Which namespace label can enforce a Pod Security profile?
   - A. pod-security.kubernetes.io/enforce
   - B. app.kubernetes.io/name
   - C. service.beta/name
   - D. storage.kubernetes.io/class

3. What does a default-deny NetworkPolicy require next?
   - A. Explicit allow policies for necessary flows
   - B. Cluster-admin
   - C. Public NodePorts
   - D. Deleting DNS

4. Why pin an image digest?
   - A. To identify immutable image content
   - B. To grant registry access
   - C. To add replicas
   - D. To create a Secret

5. Should a pod normally use the default service account token?
   - A. Only when API access is required and scoped
   - B. Always
   - C. It grants no access ever
   - D. Only for public ingress
