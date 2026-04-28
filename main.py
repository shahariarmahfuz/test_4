from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # পরে চাইলে নির্দিষ্ট frontend domain দিবেন
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "Backend is running"
    }

@app.get("/api/hello")
def hello():
    return {
        "message": "Hello from FastAPI"
    }
