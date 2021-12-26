import os.path
import PySimpleGUI as sg

VERSION = "1.0.1"
title = str("IE CLUB EDITION " + VERSION)

#sg.ChangeLookAndFeel("black")

layout_names = [
    [sg.Text("Name1", size=(30, 1)), sg.Text("Name2", size=(30, 1))],
    [sg.Input("3", size=(30, 1)), sg.Input("4", size=(30, 1))],
]
layout_name1 = [
    [sg.Input("3", size=(30, 1))],
]
layout_name2 = [
    [sg.Input("3", size=(30, 1))],
]
layout_names = [
    [
        sg.Frame("Name 1", layout_name1, element_justification="left", border_width=0),
        sg.Frame("Name 2", layout_name2, element_justification="left", border_width=0),
    ],
    [sg.Button("Update")],
]
layout = [
    [sg.Frame("Names", layout_names,title_location='n',font=('',15))],
    [],
    # [sg.Button("Close")],
    [sg.B("Start A Thread"), sg.B("Dummy"), sg.Button("Exit2")],
    [sg.Exit()],
]
size = (150, 300)
window = sg.Window(
    title=title, layout=layout, margins=size, icon=r"icon/ie logo only ( dark ).ico"
)
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event is "Update":
        # TODO change names
        print("Updated")
    if event in ("Exit", sg.WIN_CLOSED):
        break

window.close()
exit()


def split(word):
    return [char for char in word]


userInput = ""
print(
    "Program Started!\nIE CLUB EDITION 1.0.1\ns -->  Set Scores\nc --> Set Contestants\nf --> Flip Names and Scores\nb --> Set Current Bracket\ne --> Exit\nh --> help"
)
while userInput.lower() != "e":
    print("__________________________")
    userInput = input()
    if userInput.lower() == "s":
        # ------------Scores-----------------
        scoreInput = input("Enter Score:\n")
        score = open("Score.txt", "w")
        score.write(scoreInput)
        score.close()
    # elif userInput.lower() == "ss":
    #     s1Input = input("Enter Score 1:\n")
    #     score = open("Score1.txt", "w")
    #     score.write(s1Input)
    #     score.close()
    #     s2Input = input("Enter Score 2:\n")
    #     score = open("Score2.txt", "w")
    #     score.write(s2Input)
    #     score.close()
    elif userInput.lower() == "c":
        # ------------Name 1-----------------
        nameInput = input("Enter Contestant 1's Name:\n")
        a = nameInput.find(" ")
        if nameInput[a] == " ":
            nameInput = nameInput[0:a] + "   " + nameInput[a : (len(nameInput))]
        name1 = open("Name1.txt", "w")
        name1.write(nameInput)
        name1.close()
        # ------------Name 2-----------------
        nameInput = input("Enter Contestant 2's Name:\n")
        a = nameInput.find(" ")
        if nameInput[a] == " ":
            nameInput = nameInput[0:a] + "   " + nameInput[a : (len(nameInput))]
        name2 = open("Name2.txt", "w")
        name2.write(nameInput)
        name2.close()
    elif userInput.lower() == "h":
        # ------------Help-----------------
        print(
            "s -->  Set Scores\nc --> Set Contestants\nf --> Flip Names and Scores\nb --> Set Current Bracket\ne --> Exit"
        )
    elif userInput.lower() == "b":
        # -----------Bracket---------------
        bracket = open("bracket.txt", "w")
        bracketInput = input("Enter current bracket: \n")
        a = bracketInput.find(" ")
        if bracketInput[a] == " ":
            bracketInput = (
                bracketInput[0:a] + "   " + bracketInput[a : (len(bracketInput))]
            )
        bracket.write(bracketInput)
        bracket.close()
    elif userInput.lower() == "f":
        # --------------flip---------------
        if (
            (os.path.isfile("Name1.txt"))
            and (os.path.isfile("Name2.txt"))
            and (os.path.isfile("Score.txt"))
        ):
            name1 = open("Name1.txt", "r")
            temp1 = name1.readline()
            name1.close()
            name2 = open("Name2.txt", "r")
            temp2 = name2.readline()
            name2.close()
            name1 = open("Name1.txt", "w")
            name1.write(temp2)
            name1.close()
            name2 = open("Name2.txt", "w")
            name2.write(temp1)
            name2.close()
            score = open("Score.txt", "r")
            temp3 = score.readline()
            score.close()
            temp4 = split(temp3)
            temp5 = temp4[2] + "-" + temp4[0]
            score1 = open("Score.txt", "w")
            score1.write(temp5)
            score1.close()
        else:
            print("files missing")
    else:
        print("Invalid choice")