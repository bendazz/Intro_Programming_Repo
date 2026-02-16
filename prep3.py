
import gradio as gr
import pandas as pd  

def f(first,second):
    sum = 0
    for i in range(first,second+1):
        sum = sum + i

    return sum



with gr.Blocks() as iface:
    first_box = gr.Number(label = "type in an integer")
    second_box = gr.Number(label = "type in a larger integer")
    sum_box = gr.Number(label = "this is the sum of the integers in that range")
    first_box.change(fn = f,inputs = [first_box,second_box],outputs = [sum_box])
    second_box.change(fn = f,inputs = [first_box,second_box],outputs = [sum_box])


iface.launch()



