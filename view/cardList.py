import tkinter as tk
import model.Pomodoro as pom
import threading as t

from view.color import getColumnColors


class cardList:

    def __init__(self, name):
        self.name = name
        self.cards = []
    # Creating a basic framework with three columns of cards
    def drawList(self, root):
        text_col1, text_col2, text_col3 = getColumnColors()

        frame = tk.Text(root, width=50, height=40, bg=text_col1, highlightbackground="black", highlightthickness=1,
                        pady=2)
        frame1 = tk.Text(root, width=50, height=40, bg=text_col2, highlightbackground="black", highlightthickness=1,
                         pady=2)
        frame2 = tk.Text(root, width=50, height=40, bg=text_col3, highlightbackground="black", highlightthickness=1,
                         pady=2)

        frame3 = None

        self.cards = [frame, frame1, frame2, frame3]

        return self.cards

    # Moving a card between the three categories.
    # Since the cards are only moved to the right.
    def moveCard(self, root, card_number, fromframe, toframe):
        if card_number == '':
            card_start = 0
            card_end = 6
        else:
            card_number = int(card_number) - 1
            card_start = card_number * 5 + 1
            card_end = (card_number * 5) + 6

        if toframe == None:
            fromframe.delete('%d.0'%card_start,'%d.end'%card_end)
            pass
        elif toframe == self.cards[1]:
            toframe.insert(tk.INSERT, fromframe.get('%d.0'%card_start,'%d.end'%card_end))
            fromframe.delete('%d.0'%card_start,'%d.end'%card_end)
            pom.startPomThread(root)
        else:
            toframe.insert(tk.INSERT, fromframe.get('%d.0'%card_start,'%d.end'%card_end))
            fromframe.delete('%d.0'%card_start,'%d.end'%card_end)