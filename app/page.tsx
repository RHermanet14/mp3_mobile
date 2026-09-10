"use client";
import {useState} from "react"
export default function Home() {
  const [url, setURL] = useState("");
  const downloadURL = async() => {
    if(url === "") return;
    await fetch("/api/url", {
      method: "POST",
      body: JSON.stringify({url: url})
    });
  }
  return (
    <div>
      <input
        value={url}
        onChange={(e) => setURL(e.target.value)}
        placeholder="Enter valid mp3 URL."
        className=""
      />
      <button onClick={downloadURL}
        className=""
      >
        Download
      </button>
    </div>
  );
}
