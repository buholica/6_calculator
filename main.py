import tkinter as tk
from button import GreenButton, GreyButton, NumButton

# --------------------------------- CONSTANTS ----------------------------- #
BG_COLOR = "#202020"
FONT_NAME = "Helvetica"
user_entry = ""


# -------------------------------- Functions ----------------------------- #
def create_btn(cls, frame, text, b_row, b_column, width=50, b_colspan=1, command=None):
    btn = cls(frame, text=text, width=width, command=command)
    btn.grid(row=b_row, column=b_column, columnspan=b_colspan, padx=12, pady=5)


def update_display(value):
    display.delete(0, tk.END)
    display.insert(0, value)


def clean_display():
    global user_entry
    user_entry = ""
    update_display("")


def press_btn(value):
    global user_entry
    str_value = str(value)
    user_entry += str(value)

    if isinstance(value, int) or str_value == ".":
        current_value = display.get()
        display.delete(0, tk.END)
        display.insert(0, current_value + str_value)
    else:
        update_display("")


def press_percent_btn():
    global user_entry
    try:
        total = str(eval(user_entry) / 100)
        user_entry = total
        display.delete(0, tk.END)
        display.insert(0, total)
    except Exception as e:
        user_entry = "Error"
        update_display("Error")


def calculate():
    global user_entry
    print(user_entry)
    try:
        total = str(round(eval(user_entry), 3))
        user_entry = total
        update_display(total)
    except Exception as e:
        user_entry = "Error"
        update_display("Error")


# ---------------------------------- Window ------------------------------- #
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")
window.config(bg=BG_COLOR)

# -------------------------------- Screen Division ---------------------- #
screen_frame = tk.Frame(window, bg=BG_COLOR, relief=tk.RAISED, bd=0, width=250, height=90)
screen_frame.grid(row=0, column=0, sticky="ns")

screen_frame.grid_propagate(False)

btn_frame = tk.Frame(window, bg=BG_COLOR)
btn_frame.grid(row=1, column=0)

# ----------------------------- LABEL --------------------------------- #
display = tk.Entry(screen_frame, bg=BG_COLOR, fg="white", font=(FONT_NAME, 34, "normal"), bd=0)
display.grid(row=0, column=0, padx=20, pady=15, sticky="se")

screen_frame.grid_rowconfigure(0, weight=1)
screen_frame.grid_columnconfigure(0, weight=1)

# ------------------------------ BUTTONS ------------------------------ #
# AC, % buttons
create_btn(GreyButton, btn_frame, "AC", 0, 0, width=125, b_colspan=2, command=clean_display)
create_btn(GreyButton, btn_frame, "%", 0, 2, command=press_percent_btn)

# /, *, -, +, = buttons
create_btn(GreenButton, btn_frame, "÷", 0, 3, command=lambda: press_btn("/"))
create_btn(GreenButton, btn_frame, "x", 1, 3, command=lambda: press_btn("*"))
create_btn(GreenButton, btn_frame, "-", 2, 3, command=lambda: press_btn("-"))
create_btn(GreenButton, btn_frame, "+", 3, 3, command=lambda: press_btn("+"))
create_btn(GreenButton, btn_frame, "=", 4, 3, command=calculate)

# Dot button
create_btn(NumButton, btn_frame, ".", 4, 2, command=lambda: press_btn("."))

# Number buttons
row = 1
column = 2
for num in reversed(range(10)):
    if num == 0:
        create_btn(NumButton, btn_frame, num, 4, 0, width=125, b_colspan=2,
                   command=lambda n=num: press_btn(n))
    else:
        create_btn(NumButton, btn_frame, num, row, column, command=lambda n=num: press_btn(n))
        column -= 1
        if column < 0:
            column = 2
            row += 1


window.mainloop()