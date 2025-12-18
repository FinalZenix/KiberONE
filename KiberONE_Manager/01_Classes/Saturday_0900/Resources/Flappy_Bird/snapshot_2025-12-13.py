import pgzrun

# --- Configuration ---
TITLE = "Simple Bird"
WIDTH = 288
HEIGHT = 512

# --- Constants ---
GRAVITY = 0.25
FLAP_FORCE = -5.5

# --- Setup Actors ---
bg = Actor('background-day', center=(WIDTH/2, HEIGHT/2))
ground = Actor('base', anchor=('left', 'bottom'))
ground.pos = (0, HEIGHT)

bird = Actor('yellowbird-midflap', (50, HEIGHT/2))
bird.vy = 0  # Vertical velocity

def draw():
    screen.clear()
    bg.draw()
    ground.draw()
    bird.draw()

def update():
    # Apply Gravity
    bird.vy += GRAVITY
    bird.y += bird.vy

def on_key_down(key):
    # Jump
    if key == keys.SPACE:
        bird.vy = FLAP_FORCE

pgzrun.go()
