from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Selection Agent")

class Payload(BaseModel):
    options: Optional[List[str]] = None

@app.get("/ping")
def ping():
    return {"status": "ok", "agent": "selection"}

@app.post("/select")
def select(payload: Payload):
    choice = payload.options[0] if payload.options else None
    return {"agent": "selection", "chosen": choice}
