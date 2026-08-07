# Quiz — Deployments & rollouts

## Instructions

Answer from memory first, then check explanations after you submit.

## Questions

### Question 1: What object stores a Deployment revision's pod template?

A) ReplicaSet  
B) Service  
C) ConfigMap  
D) Node  

**Your answer:** _______________

---

### Question 2: What does `maxUnavailable: 0` require during rollout?

A) No desired replica may be unavailable  
B) No surge is allowed  
C) No image pull occurs  
D) No probes run  

**Your answer:** _______________

---

### Question 3: What command restores a prior Deployment revision?

A) kubectl rollout undo  
B) kubectl delete node  
C) kubectl expose  
D) kubectl auth reconcile  

**Your answer:** _______________

---

### Question 4: Does rollback reverse a database migration?

A) Always  
B) No; it needs a compatible data strategy  
C) Only for StatefulSets  
D) Only if DNS is enabled  

**Your answer:** _______________

---

### Question 5: Why use an image digest?

A) It identifies immutable content  
B) It increases replicas  
C) It grants RBAC  
D) It creates TLS  

**Your answer:** _______________

---
