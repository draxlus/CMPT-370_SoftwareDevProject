import tkinter as tk
import view.Board as b
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry


class Date():
    """ A Class for Selecting the Deadline Date of a Task using tkcalendar """

    def __init__(self):
        # Create a String class Variable for the selected date
        self.selected_date = "None"

    def setDate(self, date, root):
        """ Sets selected_date as the chosen date and terminates calendar window """

        self.selected_date = date
        # Displays a Message when a new date is set
        tk.messagebox.showinfo(title="Message", message="Date Successfully Added!")
        root.destroy()

    def getDate(self):
        """ Returns selected_date """

        return self.selected_date

    def drawCalendar(self):
        """ Draws the Calendar window for Selection """

        # Initialize tkinter window
        calendar_window = tk.Tk()

        # Set up how the calendar will look
        calendar_window.title("Select Deadline")
        calendar_window.minsize(width=300, height=300)
        calendar_window.resizable(0, 0)

        # Create a separate frame for the button inside of the window
        # This step is important, as it allows the button to work
        button_frame = tk.Frame(calendar_window, width=400, height=200)
        button_frame.grid(row=1, column=0)

        # Set up calendar specifications
        calendar = Calendar(calendar_window, setmode="day", date_pattern="d/m/yy")
        calendar.grid(row=0, column=0)

        # Select Button
        tk.Button(button_frame, text="Select Date",
                  command=lambda: self.setDate(calendar.get_date(), calendar_window)).grid(row=1, column=0)

        calendar_window.mainloop()

