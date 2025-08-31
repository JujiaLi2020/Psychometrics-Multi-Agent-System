services:
  scoring:
    build:
      context: ..
      dockerfile: infra/Dockerfile.r
    working_dir: /app/agents/scoring
    volumes:
      - ../:/app
    command: ["Rscript", "run.R"]
    ports:
      - "8001:8001"

  fairness:
    build:
      context: ..
      dockerfile: infra/Dockerfile.r
    working_dir: /app/agents/fairness
    volumes:
      - ../:/app
    command: ["Rscript", "run.R"]
    ports:
      - "8002:8002"

  selection:
    build:
      context: ..
      dockerfile: infra/Dockerfile.py
    working_dir: /app/agents/selection
    volumes:
      - ../:/app
    command: ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8003", "--reload"]
    ports:
      - "8003:8003"

  reporting:
    build:
      context: ..
      dockerfile: infra/Dockerfile.py
    working_dir: /app/agents/reporting
    volumes:
      - ../:/app
    command: ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8004", "--reload"]
    ports:
      - "8004:8004"

  orchestrator:
    build:
      context: ..
      dockerfile: infra/Dockerfile.py     # ← moved under build
    working_dir: /app/agents/orchestrator
    volumes:
      - ../:/app
    environment:
      SCORING_URL:    http://scoring:8001
      FAIRNESS_URL:   http://fairness:8002
      SELECTION_URL:  http://selection:8003
      REPORTING_URL:  http://reporting:8004
    command: ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8005", "--reload"]
    ports:
      - "8005:8005"
