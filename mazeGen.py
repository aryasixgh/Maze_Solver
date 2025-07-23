# Example file showing a circle moving on screen
import pygame
import time
from debug import debug
from randomDFS import traversalOutput

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1500, 1000))
clock = pygame.time.Clock()
running = True
dt = 0

mazzeList = []
path = traversalOutput() # Result of RDFS

#maze
# cubeWallData = [1,1,1,1] # LEFT, BOTTOM , RIGTH, TOP
# mazzeList = [[list(cubeWallData) for _ in range(10)] for _ in range(10)] #init a 10x10 maze matrix 
n = 1
for i in range(10):
    row_data = []
    for j in range(10):
        cubeWallData=[1,1,1,1,n]
        row_data.append(list(cubeWallData))
        n+=1
    mazzeList.append(row_data)

def printer(arrayThreeD):
    result = ""
    for i in range(10):
        for j in range(10):
            result += str(arrayThreeD[i][j]) + " "
        result += "\n"
    return result



# Animation state
current_x = 0
current_y = 0
draw_delay = 0.1  # seconds between cubes
last_draw_time = time.time()
player_pos = pygame.Vector2(502 / 20, 502 / 20)

#line(surface, color, start_pos, end_pos, width=1) -> Syntax
# start_pos (tuple(int or float, int or float) or list(int or float, int or float) or Vector2(int or float, int or float)) -- start position of the line, (x, y)

# end_pos (tuple(int or float, int or float) or list(int or float, int or float) or Vector2(int or float, int or float)) -- end position of the line, (x, y)
star_pos = ()
def drawCustomCube(stepValX, stepValY):
    offSetValX = 50 * stepValX
    offSetValY = 50 * stepValY
    sizeCube = 50 
    width = 2
    if mazzeList[stepValX][stepValY][0] == 1: 
        pygame.draw.line(screen, "red", (offSetValX, offSetValY), (offSetValX, sizeCube + offSetValY), width=width) # left
    if mazzeList[stepValX][stepValY][1] == 1:
        pygame.draw.line(screen, "green", (offSetValX, sizeCube + offSetValY), (sizeCube + offSetValX, sizeCube + offSetValY), width=width) # bottom
    if mazzeList[stepValX][stepValY][2] == 1:
        pygame.draw.line(screen, "blue", (sizeCube + offSetValX, sizeCube + offSetValY), (sizeCube + offSetValX, offSetValY), width=width) # right
    if mazzeList[stepValX][stepValY][3] == 1:
        pygame.draw.line(screen, "black", (sizeCube + offSetValX, offSetValY), (offSetValX, offSetValY), width=width) # top

def removeLines(stepValX, stepValY):
    offSetValX = 50 * stepValX
    offSetValY = 50 * stepValY
    sizeCube = 50 
    width = 2
    colorRemove = "white"
    if mazzeList[stepValX][stepValY][0] == 0: 
        pygame.draw.line(screen, colorRemove, (offSetValX, offSetValY), (offSetValX, sizeCube + offSetValY), width=width) # left
    if mazzeList[stepValX][stepValY][1] == 0:
        pygame.draw.line(screen, colorRemove, (offSetValX, sizeCube + offSetValY), (sizeCube + offSetValX, sizeCube + offSetValY), width=width) # bottom
    if mazzeList[stepValX][stepValY][2] == 0:
        pygame.draw.line(screen, colorRemove, (sizeCube + offSetValX, sizeCube + offSetValY), (sizeCube + offSetValX, offSetValY), width=width) # right
    if mazzeList[stepValX][stepValY][3] == 0:
        pygame.draw.line(screen, colorRemove, (sizeCube + offSetValX, offSetValY), (offSetValX, offSetValY), width=width) # top

while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    player_pos_X = int(player_pos.x/50)-1
    player_pos_Y = int(player_pos.y/50)-1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and player_pos.y - 50 >= 0: 
                player_pos.y -= 50
                #cubeValues[3] = 0
                mazzeList[int(player_pos.x/50)][int(player_pos.y/50)+1][3] -=1  #TOP instead of hard coding apply increments and decerements to array vals to dyanmically update cube wall data
                mazzeList[int(player_pos.x/50)][int(player_pos.y/50)][1] -=1
            if event.key == pygame.K_s and player_pos.y + 50 < 500:
                player_pos.y += 50
                #cubeValues[1] = 0
                mazzeList[int(player_pos.x/50)][int(player_pos.y/50)-1][1] -= 1  #BOTTOM
                mazzeList[int(player_pos.x/50)][int(player_pos.y/50)][3] -=1 
            if event.key == pygame.K_a and player_pos.x - 50 >= 0:
                player_pos.x -= 50
                #cubeValues[0] = 0
                mazzeList[int(player_pos.x/50)+1][int(player_pos.y/50)][0] -= 1 #LEFT
                mazzeList[int(player_pos.x/50)][int(player_pos.y/50)][2] -= 1
            if event.key == pygame.K_d and player_pos.x + 50 < 500:
                player_pos.x += 50
                #cubeValues[2] = 0
                mazzeList[int(player_pos.x/50)-1][int(player_pos.y/50)][2] -= 1 #RIGHT    
                mazzeList[int(player_pos.x/50)][int(player_pos.y/50)][0] -= 1
            if event.key == pygame.K_f:
                
                for i in path:
                    player_pos_singular = ((int(((player_pos.y/50)+1)-1) * 10)) + int((player_pos.x/50)+1)
                    grid_index = mazzeList[int(player_pos.x/50)-1][int(player_pos.y/50)][4]
                    if  grid_index-i == 10: # TOP
                        player_pos.y -= 50
                        mazzeList[int(player_pos.x/50)][int(player_pos.y/50)+1][3] -=1 
                        mazzeList[int(player_pos.x/50)][int(player_pos.y/50)][1] -=1  
                    if grid_index-i == 1: # LEFT
                        player_pos.x -= 50
                        mazzeList[int(player_pos.x/50)+1][int(player_pos.y/50)][0] -= 1 
                        mazzeList[int(player_pos.x/50)][int(player_pos.y/50)][2] -= 1
                    if grid_index - i == -1: # RIGHT
                        player_pos.x += 50
                        mazzeList[int(player_pos.x/50)-1][int(player_pos.y/50)][2] -= 1     
                        mazzeList[int(player_pos.x/50)][int(player_pos.y/50)][0] -= 1
                    if grid_index - i == -10: # BOTTOM
                        player_pos.y += 50
                        mazzeList[int(player_pos.x/50)][int(player_pos.y/50)-1][1] -= 1  
                        mazzeList[int(player_pos.x/50)][int(player_pos.y/50)][3] -=1         



    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # Draw all previously completed cubes
    for x in range(10):
        for y in range(10):
            #if (x < current_x) or (x == current_x and y < current_y):
            drawCustomCube(x, y)
                #removeLines(x,y)

    debug(printer(mazzeList), 10, 600)
    player_posX_val = "Player X position = "+str(int(player_pos.x/50)+1)
    player_posY_val = "Player Y position = "+str(int(player_pos.y/50)+1)
    player_pos_singular = "Player pos individual = "+ str(((int(((player_pos.y/50)+1)-1) * 10)) + int((player_pos.x/50)+1))
    debug(player_posX_val, 10, 900)
    debug(player_posY_val, 10, 920)
    debug(player_pos_singular, 10, 940)
    debug(path, 10, 960)
    

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


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()