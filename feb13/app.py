import gradio as gr  
import pandas as pd  

x = [1,5,9]
y = [7,2,8]
points = pd.DataFrame()
points["x"] = x
points["y"] = y

with gr.Blocks() as iface:
    gr.LinePlot(points,x = "x",y = "y",x_lim = [0,10],y_lim = [0,10])

iface.launch()
