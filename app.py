from fastapi import FastAPI, Header, HTTPException
import requests
from fastapi.responses import Response, HTMLResponse
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API details
API_URL = "https://ece140-wi25-api.frosty-sky-f43d.workers.dev/api/v1/ai/image"

@app.get("/")
def read_root():
    return HTMLResponse(open("index.html").read())

@app.get("/generate-image")
def generate_image(
    prompt: str,
):
    email = "YOUR UCSD EMAIL HERE"
    pid = "YOUR UCSD PID HERE"
    width = 512
    height = 512

    headers = {
        "email": email,
        "pid": pid
    }
    payload = {
        "prompt": prompt,
        "width": width,
        "height": height
    }

    # Sending the request
    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching image")

    # Return the image as a response
    return Response(content=response.content, media_type="image/png")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)