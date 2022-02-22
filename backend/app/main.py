import uvicorn
from fastapi import FastAPI, Form, Request

from authentication import redir_to_oauth

app = FastAPI(
    title="Feeby",
    version=1,
    # root_path="/api/v1" # Docker
)

# temp db
users = {}

@app.post("/launch")
async def launch(user_id: str = Form(...)):
    # Ceck if user already exists in db
    print(user_id, "does hot reload even work anymore ")
    if user_id in users:
        # if True get refresh token from db and get token that way to avoid having to re log in
        return 'already logged in'
    else:
        # if False send user to auth flow 
        return redir_to_oauth()


@app.get("/{update_id}")
async def root(update_id: str):
    update_id += "this has been updated"
    return {"message": update_id}


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True, workers=1)
