from fastapi import FastAPI
from db.db import SQLiteDB
from classes.users import User
from fastapi.middleware.cors import CORSMiddleware
import bcrypt

# Create an instance of the FastAPI application
app = FastAPI()
# Allow requests from the React frontend (http://localhost:3000)
origins = ["http://localhost:3000"]

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can restrict to specific HTTP methods if needed
    allow_headers=["*"],  # You can restrict to specific headers if needed
)

db_conn = SQLiteDB('db.db')
db_conn.connect()
# Define your FastAPI routes


# Salt for password hash
SALT = bcrypt.gensalt()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/signup")
async def signup(data: dict):
    if data:
        # Map 'password' to 'password_hash'
        if 'password' in data:
            data['password_hash'] = bcrypt.hashpw(data['password'].encode('utf-8'), SALT)
            del data['password']  # Remove the 'password' key from the data

        user = User(
            name=data['name'],
            surname=data['surname'],
            email=data['email'],
            phone=data['phone'],
            password=data['password_hash']
        )

        if db_conn.insert_data('users', **user.__dict__):
            print('User registered successfully!')
        else:
            print('Something went wrong!')


    return {'none': 'none'}
