from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict

app = FastAPI(title="Reporting Agent")

class Payload(BaseModel):
    __root__: Dict[str, Any] | None = None

@app.get("/ping")
def ping():
    return {"status": "ok", "agent": "reporting"}

@app.post("/report")
def report(payload: Payload):
    n = len(payload.__root__) if payload.__root__ else 0
    return {"agent": "reporting", "summary": {"n_fields": n}}
