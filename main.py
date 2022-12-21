# Import the pygame library and initialise the game engine
import pygame
import random
import math

leftPlatformSegmentImg=pygame.image.load('Images/platformLeft.png')
middlePlatformSegmentImg=pygame.image.load('Images/platformMiddle.png')
rightPlatformSegmentImg=pygame.image.load('Images/platformRight.png')

leftWallImg = pygame.image.load('Images/leftWall.png')
rightWallImg = pygame.image.load('Images/rightWall.png')
backgroundSlice = pygame.image.load('Images/backgroundSlice.png')
kuzniaLogoImg = pygame.image.load('Images/kuzniaLogo.png')
playerStandingAnim=[pygame.image.load("./PlayerStanding/1.png"),pygame.image.load("./PlayerStanding/2.png")]
pygame.init()

travelledDistance=0
playerPosX=60
playerPosY=540
playerSpeed=3
offset=0
playerMoveVector=[0,0]

def generatePlatform(leftBounds,rightBounds,heightOfGameWindow):
    numberOfPlatformSegments = random.randint(2, 7)  # I made it so platform has maximum 7 segments
    posX=random.randint(leftBounds+80,rightBounds-numberOfPlatformSegments*40)#40 is player width, so -40 makes minimal gap from wall 2x player width
    posX=posX-posX%40
    posY=-20#heightOfGameWindow is bottom, platform height is 20

    return [posX,posY,numberOfPlatformSegments]
def displayPlatform(screen,platform):
    screen.blit(leftPlatformSegmentImg,(platform[0],platform[1]))
    for i in range(1,platform[2]-1):
        screen.blit(middlePlatformSegmentImg, (platform[0] + i * 40, platform[1]))
    screen.blit(rightPlatformSegmentImg,(platform[0]+platform[2]*40-40,platform[1]))
platforms=[]#[[posX,posY,numberOfPlatformSegments],[posX,posY,numberOfPlatformSegments],[posX,posY,numberOfPlatformSegments], ... ]
doesPlayerCollideWithPlatforms=False

# Open a new window
sizeOfWindow = (800, 600)
screen = pygame.display.set_mode(sizeOfWindow)
pygame.display.set_caption("KuzniaTower")

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

platforms.append(generatePlatform(80,sizeOfWindow[0],sizeOfWindow[1]))
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we can exit the while loop
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerMoveVector[0]=-playerSpeed
        if keys[pygame.K_RIGHT]:
            playerMoveVector[0]=playerSpeed
        if keys[pygame.K_UP]:
            playerMoveVector[1]=-playerSpeed
        if keys[pygame.K_DOWN]:
            playerMoveVector[1]=playerSpeed
        if keys[pygame.K_RIGHT]==False and keys[pygame.K_LEFT]==False:
            playerMoveVector[0] = 0
        if keys[pygame.K_DOWN]==False and keys[pygame.K_UP]==False:
            playerMoveVector[1] = 0



        # --- Game logic should go here

        # --- Drawing code should go here
        # First, clear the screen to white.
    # The you can draw different shapes and lines or add text to your background stage.
    travelledDistance = travelledDistance - playerMoveVector[1]
    print("travelledDistance: " + str(travelledDistance))
    if (playerMoveVector[1]!=0):
        offset = offset + playerSpeed
        offset = offset % 40
        #print(offset)
    if(playerPosY<=40):#need to move camera smoothly, need to make a boolean flag here and transition all platforms nicely with player
        if(playerMoveVector[1]<0):
            playerPosY = playerPosY - 2 * playerMoveVector[1]
        #for i in platforms:
        #    i[1]=i[1]-playerMoveVector[1]
        
    #render left walls and background and right walls
    for i in range(0,45):
        if(playerMoveVector[1]<0):
            screen.blit(backgroundSlice, (0, -600 + i * 40+offset))
            screen.blit(leftWallImg, (0, -600 + i * 40+offset))
            screen.blit(rightWallImg, (sizeOfWindow[0]-40, -600 + i * 40 + offset))
        else:
            screen.blit(backgroundSlice, (0, -600 + i * 40-offset))
            screen.blit(leftWallImg, (0, -600 + i * 40-offset))
            screen.blit(rightWallImg, (sizeOfWindow[0]-40, -600 + i * 40-offset))
    # display platforms and check for collision with player
    doesPlayerCollideWithPlatforms=False
    for i in platforms:
        print(playerPosX,playerPosY)
        print(i[0],i[1])
        #y collision
        if((abs(playerPosY+playerMoveVector[1]-i[1])<=20 or abs(playerPosY+playerMoveVector[1]+40-i[1])<=20) and
         playerPosX+playerMoveVector[0]<=i[0]+i[2]*40 and playerPosX+playerMoveVector[0]>=i[0]-30):
            playerPosX=playerPosX-playerMoveVector[0]
            playerPosY=playerPosY-2*playerMoveVector[1]
            doesPlayerCollideWithPlatforms=True
        #x collision
        i[1] = i[1] - playerMoveVector[1]
        displayPlatform(screen, i)
        #if (playerPosX + playerMoveVector[0] - i[0] <= i[2]*40):
        #    playerMoveVector[0] = 0
        #    doesPlayerCollideWithPlatforms = True
        # print(playerMoveVector)

    #check player collision with bounds and move player
    LEFT_BOUNDS=40
    RIGHT_BOUNDS=730
    if(playerPosX+playerMoveVector[0]>LEFT_BOUNDS and playerPosX+playerMoveVector[0]<RIGHT_BOUNDS):
        playerPosY+=playerMoveVector[1]
        playerPosX+=playerMoveVector[0]

    #display player on his coordinated with his image
    screen.blit(playerStandingAnim[0],(playerPosX,playerPosY))





    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()