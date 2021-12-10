import time
from tkinter import *
from tkinter import messagebox
import random
import threading

TEXT_TO_TEST = ["it sportsman earnestly ye preserved an on moment led family sooner cannot her window pulled any Or",
                "raillery if improved landlord to speaking hastened differed he furniture discourse elsewhere",
                "yet her sir extensive defective unwilling get why resolution one motionless you him thoroughly",
                "noise is round to in it quick timed doors written address greatly get attacks inhabit pursuit our",
                "lasted hunted enough an up seeing in lively letter had judgment out opinions property the supplied"]

TEXT_FONT = ("Ariel", 20, "normal")
BAR_FONT = ("Ariel", 10, "normal")

WINDOW_BORDER = "#CEE5D0"
BAR_BG = "#FED2AA"
CANVAS_BG = "#F3F0D7"
BUTTON_BG = "#F6D7A7"

DURATION = 61

COUNTING_CHAR = 0
COUNTING_WORD = 0
CPM = 0

RESTART_CLICKED = False

# --- Restart The Testing --- #


def restart():
    global RESTART_CLICKED, COUNTING_WORD, COUNTING_CHAR, CPM
    RESTART_CLICKED = True
    user_type.delete(0, END)
    bar_canvas.itemconfig(word_per_min, text="?")
    bar_canvas.itemconfig(character_per_min, text="?")
    COUNTING_WORD = 0
    COUNTING_CHAR = 0
    CPM = 0


# --- Character Per Min --- #


def char_count(event):
    global COUNTING_WORD, COUNTING_CHAR, CPM
    word = input_text.split()[COUNTING_WORD]
    try:
        letter = list(word)[COUNTING_CHAR]
    except IndexError:
        if event.char == " ":
            user_type.delete(0, END)
            COUNTING_WORD += 1
            COUNTING_CHAR = 0
            bar_canvas.itemconfig(word_per_min, text=COUNTING_WORD)
    else:
        if letter == event.char:
            body_canvas.itemconfig(text, activefill="red")
            COUNTING_CHAR += 1
            CPM += 1
            bar_canvas.itemconfig(character_per_min, text=CPM)


# --- Time Countdown --- #


def countdown():
    global RESTART_CLICKED
    user_type.delete(0, END)
    checker = DURATION
    start_countdown = time.time() + DURATION
    printed_countdown = int(start_countdown - time.time())
    while printed_countdown > 0:
        if RESTART_CLICKED:
            start_countdown = time.time() + DURATION
            checker = DURATION
            RESTART_CLICKED = False
        printed_countdown = int(start_countdown - time.time())
        if printed_countdown < checker:
            checker = printed_countdown
            bar_canvas.itemconfig(running_time, text=printed_countdown)
        if printed_countdown == 1:
            messagebox.showinfo(title="Score", message=f"Your WPM score is: {COUNTING_WORD}\nYour CPM score is: {CPM}")
            restart()


# --- UI --- #

window = Tk()
window.title("Typing Speed Test")
window.config(padx=20, pady=20, bg=WINDOW_BORDER)

bar_canvas = Canvas(width=500, height=50, bg=BAR_BG)
cpm_label = bar_canvas.create_text(50, 25, text="CPM:", font=BAR_FONT, justify="center")
character_per_min = bar_canvas.create_text(90, 25, text="?", font=BAR_FONT, justify="center")
wpm_label = bar_canvas.create_text(130, 25, text="WPM:", font=BAR_FONT, justify="center")
word_per_min = bar_canvas.create_text(170, 25, text="?", font=BAR_FONT, justify="center")
time_label = bar_canvas.create_text(380, 25, text="Time Left:", font=BAR_FONT, justify="center")
running_time = bar_canvas.create_text(420, 25, text="60", font=BAR_FONT, justify="center")
bar_canvas.grid(row=0, column=0)

restart_button = Button(text="Restart", command=restart, bg=BAR_BG)
restart_button.grid(row=0, column=0)

input_text = random.choice(TEXT_TO_TEST)

body_canvas = Canvas(width=500, height=150, bg=CANVAS_BG)
text = body_canvas.create_text(250, 75, text=input_text, font=TEXT_FONT, width=480, justify="center")
body_canvas.grid(row=1, column=0)

user_type = Entry(width=33, justify="center", relief="sunken", font=TEXT_FONT)
user_type.insert(END, "type the words here")
user_type.grid(row=2, column=0)

user_type.bind("<Button-1>", lambda x=None: threading.Thread(target=countdown).start())
user_type.bind("<Key>", char_count)


window.mainloop()


