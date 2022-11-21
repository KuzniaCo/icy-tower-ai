# Import the pygame library and initialise the game engine
import pygame
import random


leftPlatformSegmentImg=pygame.image.load('platformLeft.png')
middlePlatformSegmentImg=pygame.image.load('platformMiddle.png')
rightPlatformSegmentImg=pygame.image.load('platformRight.png')

leftWallImg = pygame.image.load('leftWall.png')
rightWallImg = pygame.image.load('rightWall.png')
backgroundSlice = pygame.image.load('backgroundSlice.png')
kuzniaLogoImg = pygame.image.load('kuzniaLogo.png')
playerStandingAnim=[pygame.image.load("./PlayerStanding/1.png"),pygame.image.load("./PlayerStanding/2.png")]
pygame.init()


playerPosX=400
playerPosY=150
playerSpeed=3
offset=0
playerMoveVector=[0,0]

def generatePlatform(leftBounds,rightBounds,heightOfGameWindow):
    posX=random.randint(leftBounds-40,rightBounds+40)#40 is player width, so -40 makes minimal gap from wall 2x player width
    posX=posX%40
    posY=-20#heightOfGameWindow is bottom, platform height is 20
    numberOfPlatformSegments=random.randint(2,7)#I made it so platform has maximum 7 segments
    return [posX,posY,numberOfPlatformSegments]
platforms=[]#[[posX,posY,numberOfPlatformSegments],[posX,posY,numberOfPlatformSegments],[posX,posY,numberOfPlatformSegments], ... ]
def displayPlatform(screen,platform):
    screen.blit(leftPlatformSegmentImg,(platform[0],platform[1]))
    for i in range(1,platform[2]-1):
        screen.blit(middlePlatformSegmentImg, (platform[0] + i * 40, platform[1]))
    screen.blit(rightPlatformSegmentImg,(platform[0]+platform[2]*40-40,platform[1]))

# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("KuzniaTower")

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

platforms.append(generatePlatform(40,size[0]-40,size[1]))
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
    if (playerPosY < 120):
        offset = offset + playerSpeed
        offset = offset % 40
        playerPosY=playerPosY+playerSpeed/2
        #print(offset)
        
    #render left walls and background and right walls
    for i in range(0,45):
        if(playerPosY<120):
            screen.blit(backgroundSlice, (0, -600 + i * 40+offset))
            screen.blit(leftWallImg, (0, -600 + i * 40+offset))
            screen.blit(rightWallImg, (size[0]-40, -600 + i * 40 + offset))
        else:
            screen.blit(backgroundSlice, (0, -600 + i * 40))
            screen.blit(leftWallImg, (0, -600 + i * 40))
            screen.blit(rightWallImg, (size[0]-40, -600 + i * 40))
    playerPosY+=playerMoveVector[1]
    playerPosX+=playerMoveVector[0]
    screen.blit(playerStandingAnim[0],(playerPosX,playerPosY))
    for i in platforms:
        i[1] = i[1] - playerMoveVector[1]
        displayPlatform(screen,i)
        print(playerMoveVector)



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()