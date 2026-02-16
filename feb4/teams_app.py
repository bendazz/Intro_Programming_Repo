import gradio as gr  

teams = ['Cowboys','Eagles','Commanders','Giants']

def f(name):
    return len(name)


with gr.Blocks() as iface:
    team_dd = gr.Dropdown(teams,interactive = True,label = 'Pick a Team')
    numLetters = gr.Number(label='Number of Letters in Team Name')
    team_dd.change(fn = f, inputs=[team_dd],outputs=[numLetters])


iface.launch()