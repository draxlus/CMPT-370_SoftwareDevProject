import time
import datetime as dt
import tkinter as tk
from tkinter import messagebox
import threading as t

def startPomThread(root):
    pom_thread = t.Thread(target=startPomodoro, args=(root,))
    pom_thread.start()

def createAlert(root):
    timer_running_alert = tk.Toplevel(root, )
    timer_running_alert.title("Timer running")
    timer_running_text = tk.Label(timer_running_alert,
                                  text="The Timer is running!\nPlease wait for the timer to run before returning to the Board.")
    timer_running_text.pack()
    timer_running_alert.update()
    return timer_running_alert


def destroyAlert(alert):
    alert.destroy()

def startPomodoro(root):
    pom_minutes = 25
    break_minutes = 5
    seconds = 60

    now = dt.datetime.now()
    pomodoro = pom_minutes * seconds
    pomodoro_delta = dt.timedelta(0, pomodoro)
    future_time = now + pomodoro_delta
    break_time = break_minutes * seconds
    total_time = now + dt.timedelta(0, pomodoro + break_time)

    start_pom_question = messagebox.askyesno("Start Pomodoro", "Do you want to start the pomodoro timer?")

    if start_pom_question == True:

        messagebox.showinfo("Pomodoro starting", "Pomodoro started for 25 minutes")

        timer_alert = createAlert(root)

        while True:
            if now < future_time:
                print("Timer running")
            elif future_time <= now <= total_time:
                messagebox.showinfo("Break Time!", "It is break time for 5 minutes")
                print('Break time')
            else:
                print("Timer finished")
                ask_box = messagebox.askyesno("Pomodoro Finished!", "You have successfully finished 1 cycle!\n"
                                                                    "Would you like to start another timer?")
                destroyAlert(timer_alert)

                if ask_box:
                    now = dt.datetime.now()
                    future_time = now + dt.timedelta(0, pomodoro)
                    total_time = now + dt.timedelta(0, pomodoro + break_time)
                    timer_alert = createAlert(root)
                    continue
                else:
                    messagebox.showinfo("Pomodoro completed!", "You have finished the pomodoro timer!")
                    break
            time.sleep(20)
            now = dt.datetime.now()
    else:
        messagebox.showinfo("Pomodoro cancelled", "You have cancelled the Pomodoro timer.")
