import gradio as gr   

weeks = [1,2,3,4,5,6,7,8]
opponents = ["Cowboys","Chiefs","Rams","Buccaneers","Broncos","Giants","Vikings","Giants"]

def f(week):
    return opponents[week-1]


with gr.Blocks() as iface:
    week_dd = gr.Dropdown(choices = weeks,label = "Select a Week",interactive = True)
    opponent_box = gr.Text(label = "The Eagles played this team in the chosen week.")
    week_dd.change(fn = f,   inputs = [week_dd],   outputs = [opponent_box])



iface.launch()