import pgzrun
import random

from pgzero.actor import Actor
from pgzero.game import screen

# --- CONFIGURATION ---
TITLE = "Flappy Bird - Modular Lesson"
WIDTH = 288
HEIGHT = 512
SPEED = 2
GRAVITY = 0.25
FLAP_FORCE = -5.5

# --- ACTORS ---
bg = Actor('background-day', center=(WIDTH/2, HEIGHT/2))
bird = Actor('yellowbird-midflap', (50, HEIGHT/2))
bird.vy = 0

# PART 1: The Ground Actors
ground1 = Actor('base', anchor=('left', 'bottom'))
ground1.pos = (0, HEIGHT)
ground2 = Actor('base', anchor=('left', 'bottom'))
ground2.pos = (ground1.width, HEIGHT)

# PART 2 & 3: The Pipe Actor
pipe_top = Actor('pipe-green', anchor=('center', 'bottom'))
pipe_top.pos = (WIDTH + 100, 200)
pipe_top.angle = 180
pipe_bottom = Actor('pipe-green', anchor=('center', 'top'))
pipe_bottom.pos = (WIDTH + 100, 300)

# PART 4: Game State
game_active = True

def draw():
    screen.clear()
    bg.draw()

    # Draw pipes (under ground)
    pipe_top.draw()
    pipe_bottom.draw()

    ground1.draw()
    ground2.draw()
    bird.draw()

    #if not game_active:
    #    screen.draw.text("GAME OVER", center=(WIDTH/2, HEIGHT/2), fontsize=50, color="orange", shadow=(1,1))

def update():
    global game_active

    if not game_active:
        return

    # RECAP: Movement/Gravity
    bird.vy += GRAVITY
    bird.y += bird.vy

    # PART 1: Infinite Ground Scroll
    ground1.x -= SPEED
    ground2.x -= SPEED

    if ground1.right < 0:
        ground1.left = ground2.right
    if ground2.right < 0:
        ground2.left = ground1.right

    # PART 2: Simple Pipe Loop
    pipe_top.x -= SPEED
    pipe_bottom.x -= SPEED

    if pipe_top.right < 0:
        pipe_top.left = WIDTH
        pipe_bottom.left = WIDTH

        # PART 3: Adding Randomness
        #gap_y = random.randint(150, 350)
        #pipe_top.y = gap_y - 60
        #pipe_bottom.y = gap_y + 60

    # PART 4: Collision Logic
    #if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
    #    game_active = False
    #
    #if bird.top < 0 or bird.bottom > HEIGHT - 50: # -50 is ground level
    #    game_active = False

def on_key_down(key):
    if key == keys.SPACE and game_active:
        bird.vy = FLAP_FORCE

pgzrun.go()
