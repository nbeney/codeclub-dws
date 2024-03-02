# This is essential. Without this line, things like 'run', 'size', 'background', 'text' would not be available and you would get errors (NameError).
from p5 import *

# This function is executed by 'run', only once (at startup).
def setup():
    size(300, 200)
    background("lightpink")
    text("setup", 10, 10)

# This function is executed by 'run', periodically (for each frame).
def draw():
    background("lightgreen")
    text(f"draw: {frame_count}", 10, 10)

# This is essential. Without this line, 'setup' and 'draw' would never be executed and the screen would stay blank.
# The optional 'frame_rate' argument specifies the number of frames per second.
run(frame_rate=1)
