

Test:

Invoke-WebRequest -Uri "http://localhost:8005/run" `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"value":21,"options":["A","B"],"group":"control"}'



docker compose -f infra/docker-compose.prod.yml up -d --build

