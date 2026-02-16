import gradio as gr  
import pandas as pd 

df = pd.DataFrame(columns = ['x','y'])
df['x'] = [0]
df['y'] = [0]

def f(x,y):
    df['x'] = [x]
    df['y'] = [y]
    return df


with gr.Blocks() as iface:
    x_box = gr.Number(label = 'Type in an x-value')
    y_box = gr.Number(label = 'Type in a y-value')
    plot = gr.ScatterPlot(df,x = 'x',y = 'y',x_lim = [-10,10],y_lim = [-10,10])
    x_box.change(fn = f, inputs = [x_box,y_box], outputs = [plot])
    y_box.change(fn = f, inputs = [x_box,y_box], outputs = [plot])

iface.launch()