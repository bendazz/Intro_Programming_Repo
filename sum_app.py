import gradio as gr   

# def f(sum):
#     if sum == 3:
#         return "Correct!"
#     else:
#         return "Wrong!"


# with gr.Blocks() as iface:
#     answer_box = gr.Number(label = "Add the numbers 1 and 2 and submit your answer")
#     submit_button = gr.Button("submit")
#     message_box = gr.Text(label = " ")

#     submit_button.click(fn = f, inputs = [answer_box], outputs = [message_box])

# iface.launch()

# def f(color):
#     if color == "blue" or color == "red" or color =="blue":
#         return "Correct!"
#     else:
#         return "Wrong!"

# with gr.Blocks() as iface:
#     answer_box = gr.Text(label = "Name one of the primary colors.")
#     submit_button = gr.Button("submit")
#     message_box = gr.Text(label = " ")
#     submit_button.click(fn = f, inputs = [answer_box], outputs = [message_box])

# iface.launch()

mlb_team_names = [
    "Diamondbacks",
    "Braves",
    "Orioles",
    "Red Sox",
    "Cubs",
    "White Sox",
    "Reds",
    "Guardians",
    "Rockies",
    "Tigers",
    "Astros",
    "Royals",
    "Angels",
    "Dodgers",
    "Marlins",
    "Brewers",
    "Twins",
    "Mets",
    "Yankees",
    "Athletics",
    "Phillies",
    "Pirates",
    "Padres",
    "Giants",
    "Mariners",
    "Cardinals",
    "Rays",
    "Rangers",
    "Blue Jays",
    "Nationals",
]


def f(answer):
    message = "Wrong!"
    for team in mlb_team_names:
        if answer == team:
            message = "Correct!"
    return message
        

with gr.Blocks() as iface:
    answer_box = gr.Text(label = "Name one of the MLB teams.")
    submit_button = gr.Button("submit")
    message_box = gr.Text(label = " ")
    submit_button.click(fn = f, inputs = [answer_box], outputs = [message_box])

iface.launch()