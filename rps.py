import random
import tkinter as tk
from tkinter import messagebox

def rps(user_choice):
    game = ['rock', 'paper', 'scissor']
    comp = random.choice(game)
    
    result = ""
    if user_choice == comp:
        result = "It is a tie!"
    elif (user_choice == 'rock' and comp == 'scissor') or \
         (user_choice == 'paper' and comp == 'rock') or \
         (user_choice == 'scissor' and comp == 'paper'):
        result = "You win!"
    else:
        result = 'Computer wins!'
    
    messagebox.showinfo("Result", f'Your choice: {user_choice}\nComputer choice: {comp}\n\n{result}')

root = tk.Tk()
root.geometry('400x400')
root.title('Rock Paper Scissor')

rock_btn = tk.Button(root, text='Rock', command=lambda: rps('rock'))
rock_btn.pack(pady=10)

paper_btn = tk.Button(root, text='Paper', command=lambda: rps('paper'))
paper_btn.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: rps('scissors'))
scissors_button.pack(pady=10)

root.mainloop()