import pgzrun
import random

# --- Configuration ---
TITLE = "Flappy Bird"
WIDTH = 288
HEIGHT = 512

# --- Constants ---
GRAVITY = 0.25
FLAP_FORCE = -5.5
SPEED = 2
GAP = 100

# --- Setup Actors ---
bg = Actor('background-day', center=(WIDTH/2, HEIGHT/2))

bird_images = ['yellowbird-downflap', 'yellowbird-midflap', 'yellowbird-upflap']
bird = Actor(bird_images[0], (50, HEIGHT/2))
bird.vy = 0
bird.frame = 0

ground1 = Actor('base', anchor=('left', 'bottom'))
ground1.pos = (0, HEIGHT)
ground2 = Actor('base', anchor=('left', 'bottom'))
ground2.pos = (ground1.width, HEIGHT)

pipes = []
score = 0
game_active = False
dead = False

def draw():
    screen.clear()
    bg.draw()
    for pipe in pipes:
        pipe.draw()
    ground1.draw()
    ground2.draw()
    bird.draw()
    
    if game_active:
        screen.draw.text(str(score), center=(WIDTH/2, 50), fontsize=40, owidth=1.5, ocolor="black")
    elif not dead:
        screen.draw.text("PRESS SPACE", center=(WIDTH/2, HEIGHT/2 - 50), fontsize=30, owidth=1, ocolor="black")
    else:
        Actor('gameover', center=(WIDTH/2, HEIGHT/2)).draw()

def update():
    global game_active, score, dead
    animate_bird()
    update_ground()

    if not game_active:
        return

    bird.vy += GRAVITY
    bird.y += bird.vy
    update_pipes()
    check_collisions()

def on_key_down(key):
    global game_active, dead, score, pipes
    if key == keys.SPACE:
        if not game_active and not dead:
            game_active = True
            bird.vy = FLAP_FORCE
            sounds.wing.play()
        elif game_active:
            bird.vy = FLAP_FORCE
            sounds.wing.play()
        elif dead:
            reset_game()

def animate_bird():
    if game_active:
        bird.frame += 0.2
        if bird.frame >= 3:
            bird.frame = 0
        bird.image = bird_images[int(bird.frame)]
        bird.angle = min(20, max(-90, -bird.vy * 3))
    else:
        bird.image = 'yellowbird-midflap'
        bird.angle = 0

def update_ground():
    ground1.x -= SPEED
    ground2.x -= SPEED
    if ground1.right < 0:
        ground1.left = ground2.right
    if ground2.right < 0:
        ground2.left = ground1.right

def update_pipes():
    global score
    for pipe in pipes:
        pipe.x -= SPEED
    if pipes and pipes[0].right < 0:
        pipes.pop(0)
        pipes.pop(0)
        score += 1
        sounds.point.play()
    if not pipes or pipes[-1].x < WIDTH - 150:
        create_pipe_pair()

def create_pipe_pair():
    ground_y = HEIGHT - 112
    gap_y = random.randint(150, ground_y - 150)
    bottom = Actor('pipe-green', anchor=('center', 'top'))
    bottom.pos = (WIDTH, gap_y + GAP/2)
    pipes.append(bottom)
    top = Actor('pipe-green', anchor=('center', 'top'))
    top.pos = (WIDTH, gap_y - GAP/2)
    top.angle = 180
    pipes.append(top)

def check_collisions():
    if bird.bottom >= HEIGHT - 112:
        game_over()
    if bird.top < 0:
        game_over()
    bird_box = Rect(bird.left, bird.top, bird.width, bird.height)
    hitbox = bird_box.inflate(-10, -10)
    for pipe in pipes:
        pipe_box = Rect(pipe.left, pipe.top, pipe.width, pipe.height)
        if hitbox.colliderect(pipe_box):
            game_over()

def game_over():
    global game_active, dead
    game_active = False
    dead = True
    sounds.hit.play()
    sounds.die.play()

def reset_game():
    global game_active, dead, score
    bird.pos = (50, HEIGHT/2)
    bird.vy = 0
    pipes.clear()
    score = 0
    dead = False
    game_active = False

pgzrun.go()
