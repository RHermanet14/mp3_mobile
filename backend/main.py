from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UrlRequest(BaseModel):
    url:str

@app.get("/")
def root():
    return {"message":"The backend is functional"}
@app.post("/url")
def get_url(data: dict):
    url = data["url"]
    return {
        "url": url,
    }