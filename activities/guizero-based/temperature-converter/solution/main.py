from guizero import *
from resources import path_for

IMAGE_LOGO = path_for("thermometer.png")


def on_change_celsius():
    try:
        celsius = float(textbox_celsius.value)
        textbox_farenheit.value = celsius_to_farenheit(celsius)
        textbox_celsius.bg = "white"
        textbox_farenheit.bg = "white"
    except ValueError:
        textbox_farenheit.value = ""
        textbox_celsius.bg = "pink"
        textbox_farenheit.bg = "pink"


def on_change_farenheit():
    try:
        farenheit = float(textbox_farenheit.value)
        textbox_celsius.value = farenheit_to_celsius(farenheit)
        textbox_celsius.bg = "white"
        textbox_farenheit.bg = "white"
    except ValueError:
        textbox_celsius.value = ""
        textbox_celsius.bg = "pink"
        textbox_farenheit.bg = "pink"


def celsius_to_farenheit(celsius):
    return (celsius * 9 / 5) + 32


def farenheit_to_celsius(farenheit):
    return (farenheit - 32) * 5 / 9


if __name__ == "__main__":
    app = App(title="Temperature Converter", width=400, height=300)

    Text(app, align="right", width=3)  # spacer

    Picture(app, align="right", image=IMAGE_LOGO, width=83, height=240)

    box_temperatures = Box(app, align="right", width="fill")

    Text(box_temperatures, text="Celsius", size=18)
    textbox_celsius = TextBox(
        box_temperatures, width=10, command=on_change_celsius)
    textbox_celsius.text_size = 18

    Text(box_temperatures)  # spacer

    Text(box_temperatures, text="Farenheit", size=18)
    textbox_farenheit = TextBox(
        box_temperatures, width=10, command=on_change_farenheit)
    textbox_farenheit.text_size = 18

    app.display()
