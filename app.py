"""FastAPI application for interacting with the ECE 140 image generation API."""

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, Response
import requests

app = FastAPI(title="AI Image Generator")

# Allow the example front-end to access the API when served from a file
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint provided by the course
API_URL = "https://ece140-wi25-api.frosty-sky-f43d.workers.dev/api/v1/ai/image"

# Read user credentials from environment variables. This keeps secrets out of
# the source code.
USER_EMAIL = os.getenv("ECE140_EMAIL", "YOUR UCSD EMAIL HERE")
USER_PID = os.getenv("ECE140_PID", "YOUR UCSD PID HERE")


@app.get("/", response_class=FileResponse)
def read_root() -> FileResponse:
    """Serve the front-end HTML page."""
    return FileResponse("index.html")


@app.get("/generate-image")
def generate_image(prompt: str) -> Response:
    """Generate an image for the given prompt using the course API."""

    payload = {
        "prompt": prompt,
        "width": 512,
        "height": 512,
    }

    headers = {"email": USER_EMAIL, "pid": USER_PID}

    response = requests.post(API_URL, json=payload, headers=headers)
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail="Error fetching image",
        )

    return Response(content=response.content, media_type="image/png")


if __name__ == "__main__":    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

