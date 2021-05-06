import view.cardList as c
from view.Card import *
import view.Date as d
from view.CardEncoder import *
import tkinter as tk
import model.Pomodoro as p
from view.color import getHeaderColors, getBottomColors

class Board:

    def __init__(self, name):
        self.name = name
        self.cardLists = []
        self.task = ""
        self.date = d.Date()

    def getTask(self):
        return self.task

    def setTask(self, new_task, new_desc):
        self.task = new_task

        if new_task.strip() == "":  # Check for an empty task
            tk.messagebox.showwarning(title="Warning", message="The given task is Empty.")
        else:
            card = Card(new_task, new_desc, self.date.getDate(), 1)
            cardfr = card.drawCard(fr[0])

            #save the card
            self.save(card)

    # Save the entire board's current state
    def save(self, card):
        import json
        with open('file.json', 'a+') as f:
            json.dump(CardEncoder().encode(card), f, sort_keys=True)
            f.write(",")

    #Purpose: Use a saved file to re-create the board
    def deserializeBoard(self):
        #Read the file
        f = open("file.json", "r")
        jsonObjects = f.readlines()
        #update the board
        for object in jsonObjects:
            print(json.loads(object))

    def drawBoard(self, board):

        frame_width = 400
        frame_height = 100
        board_width = frame_width * 3
        board_height = 600

        headercol1, headercol2, headercol3 = getHeaderColors()
        basecol, buttoncol = getBottomColors()
        basecol, buttoncol = getBottomColors()

        # Create a board GUI
        board.title("Kanban")
        board.minsize(width=board_width, height=board_height)
        board.resizable(0, 0)

        #Add a menu
        menubar = tk.Menu(board)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=board.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        board.config(menu=menubar, bg =basecol)

        # Create three columns for the board
        topfr = tk.Frame(board, width=frame_width, height=frame_height, highlightbackground="black",
                         highlightthickness=1, bg=headercol1)
        topfr1 = tk.Frame(board, width=frame_width, height=frame_height, highlightbackground="black",
                          highlightthickness=1, bg=headercol2)
        topfr2 = tk.Frame(board, width=frame_width, height=frame_height, highlightbackground="black",
                          highlightthickness=1, bg=headercol3)
        topfr.grid(row=0, column=0)
        topfr1.grid(row=0, column=1)
        topfr2.grid(row=0, column=2)

        cl = c.cardList("All")
        global fr
        fr = cl.drawList(board)

        # Draw the columns
        fr[0].grid(row=1, column=0)
        fr[1].grid(row=1, column=1)
        fr[2].grid(row=1, column=2)



        # Labels for the columns
        fr_label = tk.Label(topfr, text=" To-Do ", bg=headercol1).grid(row=0, column=0, padx=179)
        fr2_label = tk.Label(topfr1, text=" Doing ", bg=headercol2).grid(row=0, column=0, padx=179)
        fr3_label = tk.Label(topfr2, text=" Done ", bg=headercol3).grid(row=0, column=0, padx=183)

        botfr = tk.Frame(board, width=board_width, height=200, bg = basecol)
        botfr1 = tk.Frame(board, width=board_width, height=200, bg = basecol)
        botfr2 = tk.Frame(board, width=board_width, height=200, bg = basecol)

        botfr.grid(row=2, column=0)
        botfr1.grid(row=2, column=1)
        botfr2.grid(row=2, column=2)

        # User entry form
        new_task = tk.Entry(botfr)
        new_task.grid(row=2, column=1)

        task_label = tk.Label(botfr, text=" Enter Task ", bg = basecol).grid(row=2, column=0)

        new_desc = tk.Entry(botfr)
        new_desc.grid(row=3, column=1)

        desc_label = tk.Label(botfr, text=" Enter Description ", bg = basecol).grid(row=3, column=0, pady=10)

        submit_button = tk.Button(botfr, text="Submit",bg = buttoncol, command=lambda: self.setTask(new_task.get(), new_desc.get()))\
            .grid(row=2, column=2, padx=10)
        deadline_button = tk.Button(botfr, text="Select Deadline",bg = buttoncol, command=lambda: self.date.drawCalendar())\
            .grid(row=4, column=1, pady=10)
        move_select_label1 = tk.Label(botfr, text = "Enter Task to Move:", bg = basecol).grid(row=0, column=0)
        move_select1 = tk.Entry(botfr, width= 5)
        move_select1.grid(row=0, column= 1)

        move_select_label2 = tk.Label(botfr1, text = "Enter Task to Move:",bg = basecol).grid(row=0, column=0)
        move_select2 = tk.Entry(botfr1, width= 5)
        move_select2.grid(row=0, column= 1)

        move_select_label3 = tk.Label(botfr2, text = "Enter Task to Move:", bg = basecol).grid(row=0, column=0)
        move_select3 = tk.Entry(botfr2, width= 5)
        move_select3.grid(row=0, column= 1, padx = 10)


        move1_2 = tk.Button(botfr, text=" Move -> ",bg = buttoncol, command=lambda: cl.moveCard(board, move_select1.get(), fr[0], fr[1]))\
            .grid(row=0, column=2,pady=10)
        move2_3 = tk.Button(botfr1, text=" Move -> ",bg = buttoncol, command=lambda: cl.moveCard(board, move_select2.get(), fr[1], fr[2]))\
            .grid(row=0, column=2, pady=10)
        move3_fin = tk.Button(botfr2, text=" Move -> ",bg = buttoncol, command=lambda: cl.moveCard(board, move_select3.get(), fr[2], fr[3]))\
            .grid(row=0, column=2, pady=10)

        start_pomodoro = tk.Button(botfr1, text=" Start Pomodoro Timer ",bg = buttoncol, command=lambda: p.startPomThread(board))\
            .grid(row=1, column=1, pady=10)
