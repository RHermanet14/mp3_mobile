"use client";
import {useState} from "react"
export default function Home() {
  const [url, setURL] = useState("");
  const downloadURL = async() => {
    if(url === "") return;
    const res = await fetch('http://localhost:8000/download', {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        url: url
      }),
    });
    if (!res.ok) {
      throw new Error("Download failed");
    }

    const blob = await res.blob();
    const downloadURL = URL.createObjectURL(blob);

    const link = document.createElement("a");
    link.href = downloadURL;
    link.download = "audio.mp3";
    link.click();
    URL.revokeObjectURL(downloadURL);
  }
  return (
    <div className="flex items-center justify-center flex-col h-screen gap-10">
      <p className="">
        MP3 Downloader
      </p>
      <input
        value={url}
        onChange={(e) => setURL(e.target.value)}
        placeholder="Enter valid mp3 URL."
        className="w-fit"
      />
      <button onClick={downloadURL}
        className="bg-gray-800 rounded p-5"
      >
        Download
      </button>
    </div>
  );
}
