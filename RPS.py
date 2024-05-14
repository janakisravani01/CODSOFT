from tkinter import*
import random

def play_game(user_input):
    computer_selection=random.choice(["rock", "paper", "scissors"]) 
    label_2.config(text=computer_selection)
    if user_input==computer_selection:
        result="It's a tie!"
    elif (user_input=="rock" and computer_selection=="scissors") or (user_input=="scissors" and computer_selection=="paper") or (user_input=="paper" and computer_selection=="rock"):
        result="You win!"
    else:
        result="You lose!"
    label_3.config(text=result)
    button_4.pack()

def play_again():
    label_2.config(text="")
    label_3.config(text="")
    button_4.pack_forget()
    
root=Tk()
root.title("Rock Paper Scissors Game")

label=Label(root,text="Choose:")
label.pack()

button_1=Button(root,text="rock",command=lambda:play_game("rock"))
button_1.pack()
button_2=Button(root,text="paper",command=lambda:play_game("paper"))
button_2.pack()
button_3=Button(root,text="scissors",command=lambda:play_game("scissors"))
button_3.pack()

label=Label(root,text="computer selected")
label.pack()

label_2=Label(root,text="")
label_2.pack()
label_3=Label(root,text="")
label_3.pack()

button_4=Button(root,text="play again",command=play_again)


root.mainloop()