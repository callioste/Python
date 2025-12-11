import tkinter as tk
import random

result = [0, 0] # [player, computer]

def set_player_choice(symbol):
    player_text.set("Player's choice: " + symbol)
    return symbol

def set_computer_choice():
    computer_choice = random.choice(['R', 'P', 'S'])
    computer_text.set("Computer's choice: " + computer_choice)
    return computer_choice

def calc_winner(player_choice, computer_choice):
    # Returned value: tie = 0, player = 1, computer = 2

    # Tie
    if player_choice == computer_choice:
        return 0

    # Player wins
    if ((player_choice == 'R' and computer_choice == 'S') or
        (player_choice == 'S' and computer_choice == 'P') or
        (player_choice == "P" and computer_choice == 'R')):
        return 1

    # Computer wins
    else: return 2

def prepare_labels():
    player_text.set("Player's choice:")
    computer_text.set("Computer's choice:")
    result_text.set("Result:")

def update_result_label(winner):
    global result

    if winner == 1:
        result[0] += 1

    if winner == 2:
        result[1] += 1

    result_text.set(f"Result \n(Player: {result[0]} | Computer: {result[1]})")

def play(symbol):

    player_choice = set_player_choice(symbol)
    computer_choice = set_computer_choice()
    winner = calc_winner(player_choice, computer_choice)
    update_result_label(winner)


root = tk.Tk()

root.title("Rock-Paper-Scissors")
root.configure(width=600, height=500)

button_r = tk.Button(root, text="R", width=10, height=2, font=("Arial", 16, "bold"), command=lambda: play('R'))
button_p = tk.Button(root, text="P", width=10, height=2, font=("Arial", 16, "bold"), command=lambda: play('P'))
button_s = tk.Button(root, text="S", width=10, height=2, font=("Arial", 16, "bold"), command=lambda: play('S'))

player_text = tk.StringVar()
computer_text = tk.StringVar()
result_text = tk.StringVar()

label_player = tk.Label(root, textvariable = player_text, font=("Arial", 14), anchor="center")
label_computer = tk.Label(root, textvariable = computer_text, font=("Arial", 14), anchor="center")
label_result = tk.Label(root, textvariable = result_text, font=("Arial", 14), anchor="center")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

label_result.grid(row=0, column=0, columnspan=3, pady=20)
label_player.grid(row=1, column=0, padx=10, pady=10)
label_computer.grid(row=1, column=2, padx=10, pady=10)

button_r.grid(row=2, column=0, padx=10, pady=10)
button_p.grid(row=2, column=1, padx=10, pady=10)
button_s.grid(row=2, column=2, padx=10, pady=10)

prepare_labels()

root.mainloop()
