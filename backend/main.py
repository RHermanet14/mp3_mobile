from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yt_dlp
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
@app.post("/download")
def download_mp3(request: UrlRequest):
    ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "downloads/%(title)s%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([request.url])
    return {"message": "Download complete"}

@app.post("/url")
def get_url(request: UrlRequest):
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(request.url, download=False)

    return {
        "title": info.get("title"),
        "thumbnail": info.get("thumbnail"),
        "duration":info.get("duration"),
    }