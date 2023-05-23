from tkinter import *
import customtkinter
import sys
import chime
import time

root = Tk()

root.geometry("300x400")

root.resizable(False, False)

root.title("Pomodoro")

timer = customtkinter.CTkEntry(root, justify="center" , width=150, height=150, font=('Times New Roman', 40, 'bold'))
timer.insert(0, 25)
timer.place(x=75, y=20)

def adding():
    current_minute = int(timer.get())
    current_minute += 5
    timer.delete(0, END)
    timer.insert(0, current_minute)

def decreasing():
    current_minute = int(timer.get())
    if (current_minute-5) == 0:
        timer.delete(0, END)
        timer.insert(0, 5)
    else:
        current_minute -= 5
        timer.delete(0, END)
        timer.insert(0, current_minute)

addition_button = customtkinter.CTkButton(root, text="+5", command=adding, width=30)
addition_button.place(x=250, y=80)

decrease_button = customtkinter.CTkButton(root, text="-5", command=decreasing, width=30)
decrease_button.place(x=22, y=80)

def counting_down():
    starting_message = Label(root, text="Your Pomodoro Timer Started")
    starting_message.place(x=55, y=300)
    time_left = int(timer.get())
    time_left -= 1
    timer.delete(0, END)
    timer.insert(0, time_left)
    if time_left < 0:
        chime.success()
        time.sleep(1)
        sys.exit()
    root.after(60000, counting_down)

play_button = customtkinter.CTkButton(root, text="PLAY", width=70, command=counting_down)
play_button.place(x=115, y=200)

root.mainloop()