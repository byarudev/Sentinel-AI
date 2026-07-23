from fastapi import FastAPI

app = FastAPI(title="Sentinel AI Security", version="0.1.0")


@app.get("/")
async def root():
    return {"service": "Sentinel AI Security"}
