# Example file showing a circle moving on screen
import pygame
import time

# pygame setup
pygame.init()
screen = pygame.display.set_mode((502, 502))
clock = pygame.time.Clock()
running = True
dt = 0

# Animation state
current_x = 0
current_y = 0
draw_delay = 0.1  # seconds between cubes
last_draw_time = time.time()

def drawCustomCube(stepValX, stepValY):
    offSetValX = 50 * stepValX
    offSetValY = 50 * stepValY
    sizeCube = 50 
    width = 2
    pygame.draw.line(screen, "black", (offSetValX, offSetValY), (offSetValX, sizeCube + offSetValY), width=width) # left
    pygame.draw.line(screen, "black", (offSetValX, sizeCube + offSetValY), (sizeCube + offSetValX, sizeCube + offSetValY), width=width) # bottom
    pygame.draw.line(screen, "black", (sizeCube + offSetValX, sizeCube + offSetValY), (sizeCube + offSetValX, offSetValY), width=width) # right
    pygame.draw.line(screen, "black", (sizeCube + offSetValX, offSetValY), (offSetValX, offSetValY), width=width) # top

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # Draw all previously completed cubes
    for x in range(10):
        for y in range(10):
            if (x < current_x) or (x == current_x and y < current_y):
                drawCustomCube(x, y)

    # Draw the next cube after a delay
    if current_x < 10:
        if current_y < 10:
            if time.time() - last_draw_time > draw_delay:
                drawCustomCube(current_x, current_y)
                last_draw_time = time.time()
                current_y += 1
        else:
            current_y = 0
            current_x += 1

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()