# AI Image Generation Demo

This repository demonstrates how to call the ECE 140 course image generation API from a FastAPI backend and display the resulting image in a simple web page.

## Requirements

- Python 3.8+
- `pip` for installing dependencies

## Setup

1. **Install dependencies**
   ```bash
   pip install fastapi uvicorn requests
   ```
2. **Set your credentials**
   The API requires your UCSD email and PID. Export them as environment variables so they are not stored in the code:
   ```bash
   export ECE140_EMAIL="<YOUR UCSD EMAIL>"
   export ECE140_PID="<YOUR UCSD PID>"
   ```

## Running the app

Start the FastAPI server using Uvicorn:

```bash
uvicorn app:app --reload
```

Then open `index.html` in your browser or navigate to `http://127.0.0.1:8000/` if the HTML file is served by FastAPI.

Type a prompt into the text box and click **Generate**. The backend forwards your prompt to the ECE 140 API and the generated image will appear below the button.

## Project Structure

- `app.py` – FastAPI backend that calls the image generation API.
- `index.html` – Frontend with JavaScript to call the backend and display the image.
- `.gitignore` – Standard Python ignores.

Feel free to modify the HTML and CSS to customize the look of your application or extend the backend for your own experiments.

