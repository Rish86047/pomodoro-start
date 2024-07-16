from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer_reset = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer_reset)
    title.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer, text="00:00")
    check.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global rep
    rep += 1
    if rep % 8 == 0:
        count_down(WORK_MIN * 60)
        title.config(text="BREAK", fg=GREEN)
    elif rep % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title.config(text="BREAK", fg=PINK)
    else:
        count_down(LONG_BREAK_MIN * 60)
        title.config(text="BREAK", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    if len(str(sec)) == 1:
        sec = f"0{sec}"
    canvas.itemconfig(timer, text=f"{min}:{sec}")
    if count > 0:
        global timer_reset
        timer_reset = window.after(1000, count_down, count - 1)
    else:
        start_count()
        mark = ""
        for i in range(rep // 2):
            mark += "✔"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=500)
window.config(padx=130, pady=50, bg=YELLOW)

title = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
title.grid(column=1, row=0)

canvas = Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=photo)
timer = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", highlightthickness=0, command=start_count)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

check = Label(fg=GREEN, font=(FONT_NAME, 20))
check.grid(column=1, row=3)

window.mainloop()
