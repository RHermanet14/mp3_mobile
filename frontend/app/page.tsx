"use client";
import {useState} from "react"
export default function Home() {
  const [url, setURL] = useState("");
  const downloadURL = async() => {
    if(url === "") return;
    const res = await fetch('http://localhost:8000/url', {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        url: url
      }),
    });
    const data = await res.json();
    alert(data.url);
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
