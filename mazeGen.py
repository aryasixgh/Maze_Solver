# Example file showing a circle moving on screen
import pygame
import time

# pygame setup
pygame.init()
screen = pygame.display.set_mode((502, 502))
clock = pygame.time.Clock()
running = True
dt = 0

#maze
cubeWallData = [1,1,1,1]
mazzeList = [[cubeWallData for _ in range(10)] for _ in range(10)] #init a 10x10 maze matrix 

# Animation state
current_x = 0
current_y = 0
draw_delay = 0.1  # seconds between cubes
last_draw_time = time.time()

player_pos = pygame.Vector2(screen.get_width() / 20, screen.get_height() / 20)

#line(surface, color, start_pos, end_pos, width=1) -> Syntax
# start_pos (tuple(int or float, int or float) or list(int or float, int or float) or Vector2(int or float, int or float)) -- start position of the line, (x, y)

# end_pos (tuple(int or float, int or float) or list(int or float, int or float) or Vector2(int or float, int or float)) -- end position of the line, (x, y)
star_pos = ()
def drawCustomCube(stepValX, stepValY):
    offSetValX = 50 * stepValX
    offSetValY = 50 * stepValY
    sizeCube = 50 
    width = 2
    if mazzeList[stepValX][stepValY] == [1,1,1,1]: 
        pygame.draw.line(screen, "black", (offSetValX, offSetValY), (offSetValX, sizeCube + offSetValY), width=width) # left
    if mazzeList[stepValX][stepValY] == [1,1,1,1]:
        pygame.draw.line(screen, "black", (offSetValX, sizeCube + offSetValY), (sizeCube + offSetValX, sizeCube + offSetValY), width=width) # bottom
    if mazzeList[stepValX][stepValY] == [1,1,1,1]:
        pygame.draw.line(screen, "black", (sizeCube + offSetValX, sizeCube + offSetValY), (sizeCube + offSetValX, offSetValY), width=width) # right
    if mazzeList[stepValX][stepValY] == [1,1,1,1]:
        pygame.draw.line(screen, "black", (sizeCube + offSetValX, offSetValY), (offSetValX, offSetValY), width=width) # top

def removeLines(stepValX, stepValY):
    offSetValX = 50 * stepValX
    offSetValY = 50 * stepValY
    sizeCube = 50 
    width = 2
    colorRemove = "white"
    if mazzeList[stepValX][stepValY][0] == 0: 
        pygame.draw.line(screen, colorRemove, (offSetValX, offSetValY), (offSetValX, sizeCube + offSetValY), width=width) # left
        # pygame.draw.line(screen, "black", (offSetValX, sizeCube + offSetValY), (sizeCube + offSetValX, sizeCube + offSetValY), width=width) # bottom
        # pygame.draw.line(screen, "black", (sizeCube + offSetValX, sizeCube + offSetValY), (sizeCube + offSetValX, offSetValY), width=width) # right
        # pygame.draw.line(screen, "black", (sizeCube + offSetValX, offSetValY), (offSetValX, offSetValY), width=width) # top
    if mazzeList[stepValX][stepValY][1] == 0:
        # pygame.draw.line(screen, "black", (offSetValX, offSetValY), (offSetValX, sizeCube + offSetValY), width=width) # left
        pygame.draw.line(screen, colorRemove, (offSetValX, sizeCube + offSetValY), (sizeCube + offSetValX, sizeCube + offSetValY), width=width) # bottom
        # pygame.draw.line(screen, "black", (sizeCube + offSetValX, sizeCube + offSetValY), (sizeCube + offSetValX, offSetValY), width=width) # right
        # pygame.draw.line(screen, "black", (sizeCube + offSetValX, offSetValY), (offSetValX, offSetValY), width=width) # top
    if mazzeList[stepValX][stepValY][2] == 0:
        # pygame.draw.line(screen, "black", (offSetValX, offSetValY), (offSetValX, sizeCube + offSetValY), width=width) # left
        # pygame.draw.line(screen, "black", (offSetValX, sizeCube + offSetValY), (sizeCube + offSetValX, sizeCube + offSetValY), width=width) # bottoms
        pygame.draw.line(screen, colorRemove, (sizeCube + offSetValX, sizeCube + offSetValY), (sizeCube + offSetValX, offSetValY), width=width) # right
        # pygame.draw.line(screen, "black", (sizeCube + offSetValX, offSetValY), (offSetValX, offSetValY), width=width) # top
    if mazzeList[stepValX][stepValY][3] == 0:
        # pygame.draw.line(screen, "black", (offSetValX, offSetValY), (offSetValX, sizeCube + offSetValY), width=width) # left
        # pygame.draw.line(screen, "black", (offSetValX, sizeCube + offSetValY), (sizeCube + offSetValX, sizeCube + offSetValY), width=width) # bottoms
        # pygame.draw.line(screen, "black", (sizeCube + offSetValX, sizeCube + offSetValY), (sizeCube + offSetValX, offSetValY), width=width) # right
        pygame.draw.line(screen, colorRemove, (sizeCube + offSetValX, offSetValY), (offSetValX, offSetValY), width=width) # top

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and player_pos.y - 50 >= 0: 
                player_pos.y -= 50
                #cubeValues[3] = 0
                mazzeList[int(player_pos.x/50)][int(player_pos.y/50)][3] -=1  #TOP instead of hard coding apply increments and decerements to array vals to dyanmically update cube wall data
            if event.key == pygame.K_s and player_pos.y + 50 < 500:
                player_pos.y += 50
                #cubeValues[1] = 0
                mazzeList[int(player_pos.x/50)][int(player_pos.y/50)][1] -= 1  #BOTTOM
            if event.key == pygame.K_a and player_pos.x - 50 >= 0:
                player_pos.x -= 50
                #cubeValues[0] = 0
                mazzeList[int(player_pos.x/50)][int(player_pos.y/50)][0] -= 1 #LEFT
            if event.key == pygame.K_d and player_pos.x + 50 < 500:
                player_pos.x += 50
                #cubeValues[2] = 0
                mazzeList[int(player_pos.x/50)][int(player_pos.y/50)][2] -= 1 #RIGHT    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # Draw all previously completed cubes
    for x in range(10):
        for y in range(10):
            #if (x < current_x) or (x == current_x and y < current_y):
                if(mazzeList[y][x] == [1,1,1,1]):
                    drawCustomCube(x, y)
                removeLines(x,y)

   # Draw the next cube after a delay
    # if current_x < 10:
    #     if current_y < 10:
    #         if time.time() - last_draw_time > draw_delay:
    #             drawCustomCube(current_x, current_y)
    #             last_draw_time = time.time()
    #             current_y += 1
    #     else:
    #         current_y = 0
    #         current_x += 1

    pygame.draw.circle(screen, "red", player_pos, 10)        
    #key strokes
    #keys = pygame.key.get_pressed()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()