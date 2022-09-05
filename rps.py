<one line to give the program's name and a brief idea of what it does.>
Copyright (C) <year>  <name of author>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
