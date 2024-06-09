from customtkinter import *

GREEN = "#254336"
HOVER_COLOR = "#365E32"
FONT_NAME = "Helvetica"
FONT_STYLE = (FONT_NAME, 20, "normal")


class GreenButton(CTkButton):
    def __init__(self, master, **kwargs):
        default_options = {
            "width": 50,
            "height": 50,
            "corner_radius": 6,
            "fg_color": GREEN,
            "hover_color": HOVER_COLOR,
            "text_color": "white",
            "font": FONT_STYLE,
        }
        default_options.update(kwargs)
        super().__init__(master, **default_options)


class GreyButton(CTkButton):
    def __init__(self, master, **kwargs):
        default_options = {
            "width": 50,
            "height": 50,
            "corner_radius": 6,
            "fg_color": "#B4B4B8",
            "hover_color": "#C7C8CC",
            "text_color": "black",
            "font": FONT_STYLE,
        }
        default_options.update(kwargs)
        super().__init__(master, **default_options)


class NumButton(CTkButton):
    def __init__(self, master, **kwargs):
        default_options = {
            "width": 50,
            "height": 50,
            "corner_radius": 6,
            "fg_color": "#404258",
            "hover_color": "#474E68",
            "text_color": "white",
            "font": FONT_STYLE,
        }
        default_options.update(kwargs)
        super().__init__(master, **default_options)
