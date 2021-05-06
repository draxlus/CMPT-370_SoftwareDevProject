import tkinter as tk

import view.Comparable as Comparable

class Card():

    def __init__(self, title, desc, date, index):
        self.title = title
        self.desc = desc
        self.date = date
        self.index = index

    #Initialize a card, with the essential fields.
    def drawCard(self, frame):
        frame.insert(tk.INSERT, "\nTask: " + self.title + "\n" + "Desc: " + self.desc + "\nDue Date: " + self.date +"\n-------------------------------\n")
        return frame
