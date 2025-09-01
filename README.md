
8/31/2025 
All five agents have been set on individual docker containers.








Quick health check (60s)
docker compose -f infra/docker-compose.dev.yml ps
# hit UIs
start http://localhost:8001/__docs__/   # scoring (R)
start http://localhost:8002/__docs__/   # fairness (R)
start http://localhost:8003/docs        # selection (Py)
start http://localhost:8004/docs        # reporting (Py)
start http://localhost:8005/docs        # orchestrator (Py)



Run an end-to-end call
Invoke-RestMethod -Uri "http://localhost:8005/run" `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"value":21,"options":["A","B"],"group":"control"}'









Test:

Invoke-WebRequest -Uri "http://localhost:8005/run" `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"value":21,"options":["A","B"],"group":"control"}'



docker compose -f infra/docker-compose.prod.yml up -d --build


