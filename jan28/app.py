import gradio as gr

def f():
    return 5

iface = gr.Interface(fn = f,inputs=[],outputs=["number"])

iface.launch()