import gradio as gr  

def f(name,course):
    return f"Welcome to {course}, {name}!"


iface = gr.Interface(fn = f,inputs = ["text","text"],outputs=["text"])

iface.launch()