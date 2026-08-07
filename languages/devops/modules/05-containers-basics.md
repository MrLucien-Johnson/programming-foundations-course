# Containers basics

**Course:** DevOps Foundations Course (donor / allowlist access)  
**Module:** 5 of 10

## Learning goals

By the end of this lesson you will be able to:

- Explain image vs container
- Write a simple Dockerfile for a web app
- Tag images and avoid `latest` in production notes

## Why this matters

Containers package runtime + app so CI and prod share the same shape. Mis-tagged images cause “it worked yesterday” incidents.

## Core ideas

1. **Image = recipe snapshot; container = running instance.**
2. **One process focus** — keep containers simple; compose for multi-service.
3. **Pin base images** — digest or specific tags for reproducibility.
4. **Non-root when you can** — smaller privilege surface.

## Worked example

### Lab: Dockerfile for a tiny Node API

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
USER node
EXPOSE 3000
CMD ["node", "server.js"]
```

```bash
docker build -t myapi:0.1.0 .
docker run --rm -p 3000:3000 myapi:0.1.0
curl -s localhost:3000/health
```


## Practice

1. Containerise your sample app and hit a health endpoint.
2. Record the image tag you used (not only `latest`).
3. List what must stay *out* of the image (secrets, local `.env`).

## Common mistakes

- Baking secrets into layers
- Huge images with unused toolchains
- Running everything as root “just because”

## Stretch goal

Multi-stage build to keep the final image slim.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](devops-course.html) for the full path.
