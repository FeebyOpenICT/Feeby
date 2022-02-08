import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/{update_id}")
async def root(update_id: str):
    print("updateId:", update_id)
    update_id += "this has been updated"
    return {"message": update_id}


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True, workers=1)
