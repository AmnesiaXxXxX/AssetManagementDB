import uvicorn
from main import app  # Adjust import if main.py is in root

def start():
    uvicorn.run(app, host="0.0.0.0", port=8000)