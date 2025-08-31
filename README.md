mas-psychometrics/
│
├── agents/                        # All agents (R and Python)
│   ├── scoring/                   # R (Plumber)
│   │   ├── plumber.R              # Defines endpoints (/ping, /score)
│   │   └── run.R                  # Starts plumber service on port 8001
│   │
│   ├── fairness/                  # R (Plumber)
│   │   ├── plumber.R              # Defines endpoints (/ping, /audit)
│   │   └── run.R                  # Starts plumber service on port 8002
│   │
│   ├── selection/                 # Python (FastAPI)
│   │   └── app.py                 # Defines endpoints (/ping, /select) on port 8003
│   │
│   ├── reporting/                 # Python (FastAPI)
│   │   └── app.py                 # Defines endpoints (/ping, /report) on port 8004
│   │
│   └── orchestrator/              # Python (FastAPI) — central coordinator
│       └── app.py                 # Calls scoring, fairness, selection, reporting (port 8005)
│
├── infra/                         # Infrastructure configs
│   ├── Dockerfile.r               # Base image for R services (plumber, jsonlite, httr)
│   ├── Dockerfile.py              # Base image for Python services (fastapi, uvicorn, httpx)
│   └── docker-compose.dev.yml     # Multi-service dev environment (hot reload)
│
├── data/                          # (Optional) datasets, inputs/outputs
├── docs/                          # (Optional) documentation, design notes
├── .dockerignore                  # Ignore unnecessary files in Docker build
├── .gitignore                     # Ignore temp / local files in Git
└── README.md                      # Main project overview
