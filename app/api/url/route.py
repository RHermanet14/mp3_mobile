from fastapi import FastAPI
app = FastAPI()
@app.post("/url")
def get_url(data: dict):
    url = data["url"]
    return {
        "url": url,
        "message": "backend linked"
    }