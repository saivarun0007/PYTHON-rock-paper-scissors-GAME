from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from random import randint
import os
print("Current working directory:", os.getcwd())
window = Tk()
window.title("ROCK PAPER SCISSOR GAME")
window.configure(background="black")
window.geometry("800x600") 
try:
    image_rock_left = ImageTk.PhotoImage(Image.open("rock left side direction.png").resize((100, 100)))   
    image_rock_right = ImageTk.PhotoImage(Image.open("rock right side direction.png").resize((100, 100)))  
    image_paper_left = ImageTk.PhotoImage(Image.open("paper left side direction.jpg").resize((100, 100))) 
    image_paper_right = ImageTk.PhotoImage(Image.open("paper right side direction.jpg").resize((100, 100))) 
    image_scissor_left = ImageTk.PhotoImage(Image.open("scissors left side direction.png").resize((100, 100)))
    image_scissor_right = ImageTk.PhotoImage(Image.open("scissors right side direction.png").resize((100, 100))) 
except FileNotFoundError as e:
    print(f"Error: {e}. Please ensure the images are in the same directory as this script.")
    exit()
label_agent = Label(window, image=image_rock_left)  
label_digibot = Label(window, image=image_rock_right)  
label_digibot.grid(row=1, column=0, padx=10, pady=10)
label_agent.grid(row=1, column=4, padx=10, pady=10)
digibot_score = Label(window, text=0, font=('arial', 30, "bold"), fg="blue", bg="black")
agent_score = Label(window, text=0, font=('arial', 30, "bold"), fg="blue", bg="black")
digibot_score.grid(row=1, column=1, padx=10)
agent_score.grid(row=1, column=3, padx=10)
agent_indicator = Label(window, font=('arial', 20, "bold"), text="AGENT", bg="orange", fg="red")
digibot_indicator = Label(window, font=('arial', 20, "bold"), text="DIGIBOT", bg="orange", fg="red")
digibot_indicator.grid(row=0, column=1)
agent_indicator.grid(row=0, column=3)
def updateMessage(msg):
    final_message['text'] = msg
def Digibot_Update():
    final = int(digibot_score['text'])
    final += 1
    digibot_score['text'] = str(final)
    check_winner()
def Agent_Update():
    final = int(agent_score['text'])
    final += 1
    agent_score['text'] = str(final)
    check_winner()
def check_winner():
    if int(agent_score['text']) >= 20:
        updateMessage("AGENT WINS THE GAME!")
        disable_buttons()
        ask_restart()
    elif int(digibot_score['text']) >= 20:
        updateMessage("DIGIBOT WINS THE GAME!")
        disable_buttons()
        ask_restart()
def disable_buttons():
    button_rock.config(state=DISABLED)
    button_paper.config(state=DISABLED)
    button_scissor.config(state=DISABLED)
def ask_restart():
    response = messagebox.askyesno("Game Over", "Do you want to restart the game?")
    if response:
        restart_game()
    else:
        window.quit()
def restart_game():
    agent_score['text'] = "0"
    digibot_score['text'] = "0"
    updateMessage("")
    button_rock.config(state=NORMAL)
    button_paper.config(state=NORMAL)
    button_scissor.config(state=NORMAL)
    label_agent.config(image=image_rock_left)  
    label_digibot.config(image=image_rock_right)
def winner_check(agent_choice, digibot_choice):
    if agent_choice == digibot_choice:
        updateMessage("IT'S A TIE!")
    elif agent_choice == "rock":
        if digibot_choice == "paper":
            updateMessage("WINNER IS DIGIBOT")
            Digibot_Update()
        else:
            updateMessage("WINNER IS AGENT")
            Agent_Update()
    elif agent_choice == "paper":
        if digibot_choice == "scissor":
            updateMessage("WINNER IS DIGIBOT")
            Digibot_Update()
        else:
            updateMessage("WINNER IS AGENT")
            Agent_Update()
    elif agent_choice == "scissor":
        if digibot_choice == "rock":
            updateMessage("WINNER IS DIGIBOT")
            Digibot_Update()
        else:
            updateMessage("WINNER IS AGENT")
            Agent_Update()
to_select = ["rock", "paper", "scissor"]
def choice_update(agent_choice):
    digibot_choice = to_select[randint(0, 2)]
    if digibot_choice == "rock":
        label_digibot.configure(image=image_rock_right)
    elif digibot_choice == "paper":
        label_digibot.configure(image=image_paper_right)
    else:
        label_digibot.configure(image=image_scissor_right)
    if agent_choice == "rock":
        label_agent.configure(image=image_rock_left)
    elif agent_choice == "paper":
        label_agent.configure(image=image_paper_left)
    else:
        label_agent.configure(image=image_scissor_left)
    winner_check(agent_choice, digibot_choice)
final_message = Label(window, font=('arial', 20, "bold"), bg="blue", fg="white")
final_message.grid(row=3, column=2)
button_rock = Button(window, width=10, height=2, text="ROCK", font=("arial", 15, "bold"), bg="yellow", fg="red",
                     command=lambda: choice_update("rock"))
button_rock.grid(row=2, column=1, padx=5)

button_paper = Button(window, width=10, height=2, text="PAPER", font=("arial", 15, "bold"), bg="yellow", fg="red",
                      command=lambda: choice_update("paper"))
button_paper.grid(row=2, column=2, padx=5)

button_scissor = Button(window, width=10, height=2, text="SCISSOR", font=("arial", 15, "bold"), bg="yellow", fg="red",
                        command=lambda: choice_update("scissor"))
button_scissor.grid(row=2, column=3, padx=5)
window.mainloop()
