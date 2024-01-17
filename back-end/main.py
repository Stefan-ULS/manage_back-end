from fastapi import FastAPI
from db.db import SQLiteDB
# Create an instance of the FastAPI application
app = FastAPI()

db_conn = SQLiteDB('db.db')
db_conn.connect()
# Define your FastAPI routes
@app.get("/")
async def root():
    return {"message": "Hello World"}


