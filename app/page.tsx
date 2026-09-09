"use client";
import {useState} from "react"
export default function Home() {
  const [url, setURL] = useState("");
  const downloadURL = () => {
    if(url === "") return;
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
