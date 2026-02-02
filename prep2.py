import gradio as gr
import pandas as pd

x = [1,5,9]
y = [4,0,7]

df = pd.DataFrame(columns = ["x","y"])
df["x"] = x  
df["y"] = y






with gr.Blocks() as iface:
    output = gr.ScatterPlot(df,x = "x",y="y",x_lim = [-2,15],y_lim = [-2,15])
    

iface.launch()


