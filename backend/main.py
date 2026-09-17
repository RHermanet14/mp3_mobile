from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
from fastapi.responses import FileResponse
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
        info = ydl.extract_info(request.url,download = True)
    original_file = Path(ydl.prepare_filename(info))
    mp3_file = original_file.with_suffix(".mp3")

    return FileResponse(
        path = mp3_file,
        media_type = "audio/mpeg",
        filename = mp3_file.name
    )

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