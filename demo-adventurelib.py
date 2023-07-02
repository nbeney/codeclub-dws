# Add the folder with the downloaded Python packages to the Python path. 
import codeclub_dws

import sys

from adventurelib import *
from printy import inputy
from pyfiglet import print_figlet


def initialize_health():
    global health

    health = 50


def format_health():
    n = health // 10
    stars = "*" * n
    return f"|{stars:10}| {health}%"


def change_health_by(value):
    global health

    if value == 0:
        return

    health = max(0, health + value)

    comment = "GOOD" if value > 0 else "BAD"
    print(f"{comment}: {format_health()}")

    match health:
        case 0:
            game_over("You died!")
        case 100:
            game_over("Top health!")


def initialize_items():
    global toothbrush, toothpaste
    global free_items, held_items

    Item.is_edible = False
    Item.is_drinkable = False
    Item.nutritious_value = 0

    object_items = make_object_items()
    food_items = make_food_items()
    drink_items = make_drink_items()

    free_items = Bag(object_items + food_items + drink_items)

    held_items = Bag()


def make_object_items():
    global toothbrush, toothpaste

    toothbrush = Item("toothbrush")

    toothpaste = Item("toothpaste")

    return [toothbrush, toothpaste]


def make_food_items():
    return [
        # good
        make_food_item("apple", +10),
        make_food_item("orange", +10),
        make_food_item("banana", +10),
        make_food_item("bread", +10),
        make_food_item("salad", +10),
        make_food_item("fish oil", +20),
        # bad
        make_food_item("chocolate", -10),
        make_food_item("candy", -10),
        make_food_item("poison", -100),
    ]


def make_food_item(name, nutritious_value):
    item = Item(name)
    item.is_edible = True
    item.nutritious_value = nutritious_value
    return item


def make_drink_items():
    return [
        # good
        make_drink_item("water", +10),
        make_drink_item("fruit juice", +10),
        # bad
        make_drink_item("beer", -5),
        make_drink_item("wine", -10),
        make_drink_item("whisky", -20),
        make_drink_item("fizzy drink", -5),
    ]


def make_drink_item(name, nutritious_value):
    item = Item(name)
    item.is_drinkable = True
    item.nutritious_value = nutritious_value
    return item


def welcome():
    print_figlet("Game of Life", font="slant")
    say("""
        Welcome to the Game of Life!

        There are various items around you that you can <pick> or <drop>.

        There are various actions like <eat> or <drink> that can increase or decrease your health.

        Use <help> at any time to see the list of the available commands.
    """)


def game_over(message):
    print_figlet(message, font="slant")
    sys.exit(0)


@when("look")
@when("look around")
@when("status")
def status():
    def format_bag(bag):
        names = sorted(_.name for _ in bag)
        return ", ".join(names) or "-"

    print()
    print(f"Free items: {format_bag(free_items)}")
    print(f"Held items: {format_bag(held_items)}")
    print(f"    Health: {format_health()}")
    print()


@when("pick")
@when("take")
def pick_from_list():
    if len(free_items) == 0:
        say(f"There is nothing around you!")
    elif len(held_items) == 2:
        say("Your hands are full! Drop something first.")
    else:
        free_names = sorted([_.name for _ in free_items])
        name = inputy(options=free_names)
        do_pick(name)


@when("pick THING")
@when("take THING")
def pick_thing(thing):
    if thing not in free_items:
        say(f"There is no '{thing}' around you!")
    elif len(held_items) == 2:
        say("Your hands are full! Drop something first.")
    else:
        do_pick(thing)


def do_pick(name):
    item = free_items.take(name)
    held_items.add(item)

    value = item.nutritious_value
    if value != 0:
        say(f"{item.name} is {'good' if value > 0 else 'bad'} for your health.")


@when("drop")
def drop_from_list():
    if len(held_items) == 0:
        say(f"You are not holding anything!")
    else:
        held_names = sorted([_.name for _ in held_items])
        name = inputy(options=held_names)
        do_drop(name)


@when("drop THING")
def drop_thing(thing):
    if thing not in held_items:
        say(f"You are not holding '{thing}'!")
    else:
        do_drop(thing)


def do_drop(name):
    item = held_items.take(name)
    free_items.add(item)


@when("eat")
def eat_from_list():
    match len(held_items):
        case 0:
            say(f"You are not holding anything!")
        case 1:
            name = list(held_items)[0].name
            do_eat(name)
        case _:
            held_names = sorted([_.name for _ in held_items])
            name = inputy(options=held_names)
            do_eat(name)


@when("eat THING")
def eat_thing(thing):
    if thing not in held_items:
        say(f"You are not holding '{thing}'!")
    else:
        do_eat(thing)


def do_eat(name):
    item = held_items.find(name)
    if item.is_edible:
        held_items.take(name)
        say(f"Mmmhhh, that was delicious!")
        change_health_by(item.nutritious_value)
    else:
        say(f"Don't be silly! You cannot eat '{name}'.")


@when("drink")
def drink_from_list():
    match len(held_items):
        case 0:
            say(f"You are not holding anything!")
        case 1:
            name = list(held_items)[0].name
            do_drink(name)
        case _:
            held_names = sorted([_.name for _ in held_items])
            name = inputy(options=held_names)
            do_drink(name)


@when("drink THING")
def drink_thing(thing):
    if thing not in held_items:
        say(f"You are not holding '{thing}'!")
    else:
        do_drink(thing)


def do_drink(name):
    item = held_items.find(name)
    if item.is_drinkable:
        held_items.take(name)
        say(f"Mmmhhh, that was delicious!")
        change_health_by(item.nutritious_value)
    else:
        say(f"Don't be silly! You cannot drink '{name}'.")


@when("brush")
@when("brush teeth")
def brush_teeth():
    if toothbrush.name in held_items and toothpaste.name in held_items:
        say("""
            You squirt a bit too much toothpaste onto your
            brush and dozily jiggle it round your mouth.

            Your teeth feel clean and shiny now, as you
            run your tongue over them.

            Well done! Your teeth and gums thank you from 
            the bottom of their heart!
        """)
        do_drop(toothbrush.name)
        do_drop(toothpaste.name)
        change_health_by(+5)
    else:
        say("""
            Sorry, you cannot brush your teeth unless you 
            are holding the toothbrush and the toothpaste!
        """)


@when("walk", action="walking", points=5)
@when("cycle", action="cycling", points=10)
@when("run", action="running", points=10)
@when("swim", action="swimming", points=10)
@when("sleep", action="sleeping", points=10)
def do_action(action, points):
    say(f"Yes, {action} is good for your health!")
    change_health_by(points)


#
# Main
#


initialize_health()
initialize_items()
welcome()
status()
start()
