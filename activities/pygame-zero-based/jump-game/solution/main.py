import pgzrun


WIDTH = 600
HEIGHT = 400

GRAVITY = 0.35


def reset():
    global hen, egg, score, game_over

    hen = Actor("bird", anchor=("center", "bottom"), pos=(90, HEIGHT))
    hen.speed_y = 0

    egg = Actor("egg1", anchor=("left", "bottom"), pos=(WIDTH, HEIGHT))
    egg.speed_x = -2

    score = 0
    game_over = False


def draw():
    if game_over:
        msg = "GAME OVER!\n\nPress R to restart."
        screen.draw.text(msg, center=(WIDTH / 2, HEIGHT / 2), color="white", fontsize=80)
    else:
        screen.fill("forestgreen")
        hen.draw()
        egg.draw()
        screen.draw.text(f"Score: {score}", (20, 20), color="white", fontsize=40)


def update():
    global score, game_over

    # Update the hen.
    hen.y += hen.speed_y
    hen.speed_y += GRAVITY
    if hen.y > HEIGHT:
        hen.y = HEIGHT
        hen.speed_y = 0

    # Update the egg.
    egg.x += egg.speed_x
    if egg.x < 0:
        egg.x = WIDTH + 20
        egg.speed_x -= 0.1

        score += 1

    # Check for collisions.
    if hen.colliderect(egg) and hen.distance_to(egg) < 30:
        game_over = True


def on_key_down(key, mod):
    if key == keys.SPACE and hen.y == HEIGHT:
        hen.speed_y = -12
    elif key == keys.R and game_over:
        reset()


reset()

pgzrun.go()
