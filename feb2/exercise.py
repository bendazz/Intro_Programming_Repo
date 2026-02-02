import gradio as gr

def f(name):
    return f"How is programming going, {name}?"



with gr.Blocks() as iface:
    name = gr.Text(label = "Type in a name")
    message = gr.Text(label = "Here is your message")
    name.change(fn=f,  inputs=[name],  outputs=[message])



iface.launch()