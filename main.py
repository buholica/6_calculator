import tkinter as tk
from button import GreenButton, GreyButton, NumButton

# --------------------------------- CONSTANTS ----------------------------- #
BG_COLOR = "#202020"
FONT_NAME = "Helvetica"

num = None


# ---------------------------------- Window ------------------------------- #
window = tk.Tk()
window.title("Calculator")
window.geometry("400x600")
window.config(bg=BG_COLOR)

# -------------------------------- Screen Division ---------------------- #
screen_frame = tk.Frame(window, bg=BG_COLOR, relief=tk.RAISED, bd=2)
screen_frame.grid(row=0, column=0, sticky="ns")

btn_frame = tk.Frame(window, bg=BG_COLOR, width=600, height=400)
btn_frame.grid(row=1, column=0)

# ----------------------------- LABEL --------------------------------- #

# ------------------------------ BUTTONS ------------------------------ #
ac_btn = GreyButton(btn_frame, text="AC")
ac_btn.grid(row=0, column=0, padx=10, pady=10)

plus_minus_btn = GreyButton(btn_frame, text="+/-")
plus_minus_btn.grid(row=0, column=1, padx=10, pady=5)

percent_btn = GreyButton(btn_frame, text="%")
percent_btn.grid(row=0, column=2, padx=10, pady=5)

division_btn = GreenButton(btn_frame, text="÷")
division_btn.grid(row=0, column=3, padx=10, pady=5)

multiply_btn = GreenButton(btn_frame, text="x")
multiply_btn.grid(row=1, column=3, padx=10, pady=5)

minus_btn = GreenButton(btn_frame, text="-")
minus_btn.grid(row=2, column=3, padx=10, pady=5)

plus_btn = GreenButton(btn_frame, text="+")
plus_btn.grid(row=3, column=3, padx=10, pady=5)

equals_btn = GreenButton(btn_frame, text="=")
equals_btn.grid(row=4, column=3, padx=10, pady=5)

row = 1
column = 2
for num in reversed(range(1, 10)):
    num_btn = NumButton(btn_frame, text=num)
    num_btn.grid(row=row, column=column, padx=10, pady=5)
    column -= 1
    if column < 0:
        column = 2
        row += 1

zero_btn = NumButton(btn_frame, text="0", width=125)
zero_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

dot_btn = NumButton(btn_frame, text=".")
dot_btn.grid(row=4, column=2, padx=10, pady=5)


window.mainloop()