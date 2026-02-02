import gradio as gr
import pandas as pd   


def f(x1,y1,x2,y2):
    x = [x1,x2]
    y = [y1,y2]
    df = pd.DataFrame()
    df["x"] = x  
    df["y"] = y
    return (df,f"The slope is {(y1-y2)/(x1-x2)}.")  

with gr.Blocks() as iface:
    with gr.Row():
        x1 = gr.Number(label = "x1")
        y1 = gr.Number(label = "y1")
    with gr.Row():
        x2 = gr.Number(label = "x2")
        y2 = gr.Number(label = "y2")
    with gr.Row():
        plot = gr.LinePlot(x = "x",y="y",x_lim = [0,10],y_lim = [0,10])
        output = gr.Text()
    x1.change(fn = f,inputs = [x1,y1,x2,y2],outputs = [plot,output])
    y1.change(fn = f,inputs = [x1,y1,x2,y2],outputs = [plot,output])
    x2.change(fn = f,inputs = [x1,y1,x2,y2],outputs = [plot,output])
    y2.change(fn = f,inputs = [x1,y1,x2,y2],outputs = [plot,output])


iface.launch()    








