from fastapi import FastAPI
from models import User

app = FastAPI()
users = []

@app.post("/create_user")
async def create_user():
    return {"message": "Hello World"}

@app.delete("/delete_user")
async def delete_user():
    return {"message": "Hello World"}

@app.get("/get_users")
async def get_users():
    return {"message": "Hello World"}

@app.get("/get_user/{id}")
async def get_users():
    return {"message": "Hello World"}