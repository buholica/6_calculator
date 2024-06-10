import tkinter as tk
from button import GreenButton, GreyButton, NumButton
from customtkinter import CTkEntry

# --------------------------------- CONSTANTS ----------------------------- #
BG_COLOR = "#202020"
FONT_NAME = "Helvetica"


# -------------------------------- Functions ----------------------------- #
def clean_display():
    display.delete(0, tk.END)


def num_btn_click(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + str(value))


# ---------------------------------- Window ------------------------------- #
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")
window.config(bg=BG_COLOR)

# -------------------------------- Screen Division ---------------------- #

screen_frame = tk.Frame(window, bg=BG_COLOR, relief=tk.RAISED, bd=2, width=250, height=90)
screen_frame.grid(row=0, column=0, sticky="nsew")

screen_frame.grid_propagate(False)

btn_frame = tk.Frame(window, bg=BG_COLOR)
btn_frame.grid(row=1, column=0)

# ----------------------------- LABEL --------------------------------- #
display = tk.Entry(screen_frame, bg=BG_COLOR, fg="white",
                   font=(FONT_NAME, 34, "normal"), bd=0)
display.grid(row=0, column=0, padx=20, pady=15, sticky="se")

screen_frame.grid_rowconfigure(0, weight=1)
screen_frame.grid_columnconfigure(0, weight=1)


# ------------------------------ BUTTONS ------------------------------ #
ac_btn = GreyButton(btn_frame, text="AC", command=clean_display)
ac_btn.grid(row=0, column=0, padx=12, pady=5)

plus_minus_btn = GreyButton(btn_frame, text="+/-")
plus_minus_btn.grid(row=0, column=1, padx=12, pady=5)

percent_btn = GreyButton(btn_frame, text="%")
percent_btn.grid(row=0, column=2, padx=12, pady=5)

division_btn = GreenButton(btn_frame, text="÷")
division_btn.grid(row=0, column=3, padx=12, pady=5)

multiply_btn = GreenButton(btn_frame, text="x")
multiply_btn.grid(row=1, column=3, padx=12, pady=5)

minus_btn = GreenButton(btn_frame, text="-")
minus_btn.grid(row=2, column=3, padx=12, pady=5)

plus_btn = GreenButton(btn_frame, text="+")
plus_btn.grid(row=3, column=3, padx=12, pady=5)

equals_btn = GreenButton(btn_frame, text="=")
equals_btn.grid(row=4, column=3, padx=12, pady=5)

num_list = []
row = 1
column = 2
for num in reversed(range(10)):
    if num == 0:
        num_btn = NumButton(btn_frame, text=num, width=125, command=lambda n=num: num_btn_click(n))
        num_btn.grid(row=4, column=0, columnspan=2, padx=12, pady=5)
        num_list.append(num)
    else:
        num_btn = NumButton(btn_frame, text=num, command=lambda n=num: num_btn_click(n))
        num_btn.grid(row=row, column=column, padx=12, pady=5)
        num_list.append(num)
        column -= 1
        if column < 0:
            column = 2
            row += 1

print(num_list)

dot_btn = NumButton(btn_frame, text=".")
dot_btn.grid(row=4, column=2, padx=12, pady=5)


window.mainloop()