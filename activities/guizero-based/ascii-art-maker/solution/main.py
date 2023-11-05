from guizero import *
from resources import path_for
import pyfiglet as pf
import random


IMAGE_LOGO = path_for("logo.png")
IMAGE_COLORS = path_for("color-wheel.png")
IMAGE_SURPRISE = path_for("surprise-box.png")

# Get the list of fonts and sort it.
FONT_NAMES = sorted(pf.FigletFont.getFonts())


# Callback function for when the text or font changes.
def on_change():
    text = input_text.value
    font = font_combo.value
    output_text.value = pf.figlet_format(text, font)


# Callback function for when the color button is clicked.
def on_color():
    color = app.select_color(color=output_text.text_color)
    if color:
        output_text.text_color = color


# Callback function for when the surprise button is clicked.
def on_surprise():
    font = random.choice(font_combo.options)
    font_combo.value = font
    on_change()


if __name__ == "__main__":
    app = App(title="ASCII Art Maker", width=800, height=600)

    Text(app)  # spacer

    Picture(app, image=IMAGE_LOGO)

    Text(app)  # spacer

    box = Box(app)
    input_text = TextBox(
        box, align="left", text="Hello World!", width="60", command=on_change)

    font_combo = Combo(box, align="left",
                       options=FONT_NAMES, command=on_change)
    Text(box, align="left", text="  ")  # spacer
    font_combo.value = "speed"

    Text(box, align="left", text="  ")  # spacer
    PushButton(
        box, align="left", text="", image=IMAGE_COLORS,
        width=32, height=32, command=on_color)
    PushButton(
        box, align="left", text="", image=IMAGE_SURPRISE, width=32, height=32, command=on_surprise)

    Text(app)  # spacer

    output_text = TextBox(
        app, text="", width="fill", height="fill",
        multiline=True, scrollbar=True, enabled=False)
    output_text.text_color = "red"

    on_change()

    app.display()
