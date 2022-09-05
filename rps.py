#!/usr/local/bin/python
import PySimpleGUI as sg
import random as rnd
import os , sys
userChoice = ""
options = ["rock","paper","scissors"]
def rockPressed():
    global userChoice
    userChoice="rock"
    global choice
    choice = f"{rnd.choice(options)}"
    logic()
    os.execv(sys.executable, ['python'] + sys.argv)
def paperPressed():
    global userChoice
    userChoice="paper"
    global choice
    choice = f"{rnd.choice(options)}"
    logic()
    os.execv(sys.executable, ['python'] + sys.argv)
def scissorsPressed():
    global userChoice
    userChoice="scissors"
    global choice
    choice = f"{rnd.choice(options)}"
    logic()
    os.execv(sys.executable, ['python'] + sys.argv)
sg.theme('SystemDefaultForReal ')
layout = [
    [sg.Text("Play Rock Paper Scissors!")],
    [sg.Button("Rock"), sg.Button("Paper"), sg.Button("Scissors")]
]
window = sg.Window('Rock Paper Scissors', layout)
#rps logic
def logic():
    if userChoice == "rock" and choice == "rock":
        sg.popup("It's a tie")
    elif userChoice == "rock" and choice == "paper":
        sg.popup("You lose!")
    elif userChoice == "rock" and choice == "scissors":
        sg.popup("You win!")
    elif userChoice == "paper" and choice == "rock":
        sg.popup("You win!")
    elif userChoice == "paper" and choice == "paper":
        sg.popup("It's a tie!")
    elif userChoice == "paper" and choice == "scissors":
        sg.popup("You lose!")
    elif userChoice == "scissors" and choice == "rock":
        sg.popup("You lose!")
    elif userChoice == "scissors" and choice == "paper":
        sg.popup("You win!")
    elif userChoice == "scissors" and choice == "scissors":
        sg.popup("It's a tie!")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    if event == "Rock":
        rockPressed()
    if event == "Paper":
        paperPressed()
    if event == "Scissors":
        scissorsPressed()
    window.close()
