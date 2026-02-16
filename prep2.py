import pandas as pd
import gradio as gr     

df = pd.DataFrame()
df["x"] = []
df["y"] = []


def f(x1,y1,x2,y2):
    df["x"] = [x1,x2]
    df["y"] = [y1,y2]
    slope = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else None
    return (df,slope)



with gr.Blocks() as iface:
    x1_box = gr.Number(label="x1")
    y1_box = gr.Number(label = "y1")
    x2_box = gr.Number(label="x2")
    y2_box = gr.Number(label = "y2")
    slope_box = gr.Number(label="slope")
    plot = gr.LinePlot(df,x = "x", y="y",x_lim = [0,10],y_lim = [0,10])
    x1_box.change(fn = f,inputs = [x1_box,y1_box,x2_box,y2_box],outputs = [plot,slope_box])
    y1_box.change(fn = f,inputs = [x1_box,y1_box,x2_box,y2_box],outputs = [plot,slope_box])
    x2_box.change(fn = f,inputs = [x1_box,y1_box,x2_box,y2_box],outputs = [plot,slope_box])
    y2_box.change(fn = f,inputs = [x1_box,y1_box,x2_box,y2_box],outputs = [plot,slope_box])

iface.launch()