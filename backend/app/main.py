import uvicorn
from fastapi import FastAPI, Request

app = FastAPI(
    title="Feeby",
    version=1,
    root_path="/api/v1"
)

@app.post("/launch")
async def launch(request: Request):
    return "launched"   

@app.get("/{update_id}")
async def root(update_id: str):
    update_id += "this has been updated"
    return {"message": update_id}


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True, workers=1)
