import pandas as pd
import gradio as gr     

df = pd.DataFrame()
df["x"] = []
df["y"] = []

def f(x,y):
    df["x"] = [x]
    df["y"] = [y]
    return df



with gr.Blocks() as iface:
    x_box = gr.Number(label="x")
    y_box = gr.Number(label = "y")
    plot = gr.ScatterPlot(df,x = "x", y="y",x_lim = [0,10],y_lim = [0,10])
    x_box.change(fn = f,inputs = [x_box,y_box],outputs = [plot])
    y_box.change(fn = f,inputs = [x_box,y_box],outputs = [plot])

iface.launch()