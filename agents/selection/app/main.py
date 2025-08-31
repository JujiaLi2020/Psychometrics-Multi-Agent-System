from fastapi import FastAPI
app = FastAPI()

@app.get("/next_item")
def next_item():
    return {"item_id": "I001", "rationale": ["max-info placeholder"]}
