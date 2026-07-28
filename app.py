import os
os.system("pip install gradio groq")
import gradio as gr
from groq import daal

client = Groq(api_key=os.environ.get("GROQ_API_KEY", "your_groq_api_key_here"))

def generate_script(prompt):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert viral video script writer and AI prompt generator."
                },
                {
                    "role": "user",
                    "content": f"Create a detailed viral script and image prompts for: {prompt}"
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio Interface Setup
with gr.Blocks(title="Jaanu AI Studio") as demo:
    gr.Markdown("# 🚀 Jaanu AI Studio")
    gr.Markdown("Apna topic dalo aur viral script & image prompts pao!")
    
    with gr.Row():
        topic_input = gr.Textbox(label="Video Topic / Idea", placeholder="e.g. Daily Vlog in village...")
        submit_btn = gr.Button("Generate Script", variant="primary")
        
    output_text = gr.Textbox(label="Generated Content", lines=12)
    
    submit_btn.click(fn=generate_script, inputs=topic_input, outputs=output_text)

if __name__ == "__main__":
    demo.launch()
