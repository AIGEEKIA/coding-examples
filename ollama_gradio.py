"""
Minimal Ollama + Gradio Demo
Just upload an image and analyze it with Ollama
"""

import gradio as gr
import ollama
from PIL import Image
import io
import base64

def encode_image(image):
    """Encode PIL image to base64"""
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def analyze_image(image, prompt, model):
    """Analyze image with Ollama"""
    if image is None:
        return "Please upload an image."
    
    try:
        # Encode image
        image_base64 = encode_image(image)
        
        # Prepare message
        messages = [
            {
                "role": "user",
                "content": prompt,
                "images": [image_base64]
            }
        ]
        
        # Call Ollama
        response = ollama.chat(
            model=model,
            messages=messages
        )
        
        return response['message']['content']
        
    except Exception as e:
        return f"Error: {str(e)}"

# Simple Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# 📷 Simple Image Analyzer with Ollama")
    
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil", label="Upload Image")
            prompt_input = gr.Textbox(
                label="Prompt",
                value="Describe this image in detail.",
                lines=3
            )
            model_input = gr.Dropdown(
                choices=["qwen2.5vl:7b", "llava:7b", "bakllava:7b"],
                value="qwen2.5vl:7b",
                label="Model"
            )
            analyze_btn = gr.Button("Analyze Image")
        
        with gr.Column():
            output_text = gr.Textbox(
                label="Analysis Result",
                lines=15,
                interactive=False
            )
    
    analyze_btn.click(
        analyze_image,
        inputs=[image_input, prompt_input, model_input],
        outputs=output_text
    )

if __name__ == "__main__":
    print("Starting minimal Ollama + Gradio demo...")
    print("Make sure Ollama is running!")
    demo.launch()