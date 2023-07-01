import codeclub_dws

from adventurelib import *

Item.is_edible = False
Item.is_drinkable = False

toothbrush = Item('toothbrush')
toothpaste = Item('toothpaste')
chocolate = Item('chocolate')
chocolate.is_edible = True
candy = Item('candy')
candy.is_edible = True
water = Item('water')
water.is_drinkable = True


items_around = Bag([toothbrush, toothpaste, chocolate, candy, water])

items_in_hands = Bag()


@when("look")
@when("look around")
def look_around():
    say(f"""Around you:    {", ".join(_.name for _ in items_around)}""")
    say(f"""In your hands: {", ".join(_.name for _ in items_in_hands) or "-"}""")


@when("pick THING")
@when("take THING")
def pick(thing):
    if thing not in items_around:
        say(f"""There is no '{thing}' around you!""")
    elif len(items_in_hands) == 2:
        say("""Your hands are full!. Drop something first.""")
    else:
        item = items_around.take(thing)
        items_in_hands.add(item)


@when("drop THING")
def drop(thing):
    if thing not in items_in_hands:
        say(f"""You are not holding '{thing}'!""")
    else:
        item = items_in_hands.take(thing)
        items_around.add(item)


@when("eat THING")
def eat(thing):
    if thing not in items_in_hands:
        say(f"""You are not holding '{thing}'!""")
    else:
        item = items_in_hands.find(thing)
        if item.is_edible:
            items_in_hands.take(thing)
            say(f"""Mmmhhh, that was delicious!""")
        else:
            say(f"""Don't be silly! You cannot eat '{thing}'.""")


@when("drink THING")
def drink(thing):
    if thing not in items_in_hands:
        say(f"""You are not holding '{thing}'!""")
    else:
        item = items_in_hands.find(thing)
        if item.is_drinkable:
            items_in_hands.take(thing)
            say(f"""Mmmhhh, that was delicious!""")
        else:
            say(f"""Don't be silly! You cannot drink '{thing}'.""")


@when("brush teeth")
def brush_teeth():
    if toothbrush.name in items_in_hands and toothpaste.name in items_in_hands:
        say("""
            You squirt a bit too much toothpaste onto your
            brush and dozily jiggle it round your mouth.

            Your teeth feel clean and shiny now, as you
            run your tongue over them.

            Well done! Your teeth and gums thank you from 
            the bottom of their heart!
        """)
        drop(toothbrush.name)
        drop(toothpaste.name)
    else:
        say("""
            Sorry, you cannot brush your teeth unless you 
            are holding the toothbrush and the toothpaste!
        """)


start()
