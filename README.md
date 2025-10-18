# Minimal Ollama + Gradio Demo

A minimal demo showing how to connect Gradio with Ollama for image analysis.

## Requirements

- Python 3.7+
- Ollama running locally
- Qwen model downloaded

## Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Make sure Ollama is running
ollama serve

# Download Qwen model
ollama pull qwen2.5vl:7b
```

## Usage

```bash
python app.py
```

Then open http://localhost:7860 in your browser.

## Features

- Upload any image (JPG, PNG)
- Enter custom prompt
- Select Ollama model
- Get AI analysis of the image

## How it works

1. User uploads image to Gradio interface
2. Image is encoded to base64
3. Sent to Ollama with selected prompt
4. Response displayed in text box

## Models supported

- qwen2.5vl:7b (recommended)
- llava:7b
- bakllava:7b

## Simple and clean

Just one file: `app.py` with minimal code.