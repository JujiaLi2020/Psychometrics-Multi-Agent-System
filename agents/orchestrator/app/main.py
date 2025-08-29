from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/score")
async def score(payload: dict):
    async with httpx.AsyncClient() as client:
        r = await client.post("http://scoring:8001/score", json=payload)
    return r.json()
