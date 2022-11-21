# Import the pygame library and initialise the game engine
import pygame
wallImg = pygame.image.load('leftWall.png')
backgroundSlice = pygame.image.load('backgroundSlice.png')
playerStandingAnim=[pygame.image.load("./PlayerStanding/1.png"),pygame.image.load("./PlayerStanding/2.png")]
pygame.init()


playerPosX=400
playerPosY=150
playerSpeed=3
offset=0
playerMoveVector=[0,0]

platformColliders=[]

# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("KuzniaTower")

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

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
        print(offset)
    for i in range(0,45):
        if(playerPosY<120):
            screen.blit(backgroundSlice, (0, -600 + i * 40+offset))
            screen.blit(wallImg, (0, -600 + i * 40+offset))
        else:
            screen.blit(backgroundSlice, (0, -600 + i * 40))
            screen.blit(wallImg, (0, -600 + i * 40))
    playerPosY+=playerMoveVector[1]
    playerPosX+=playerMoveVector[0]
    screen.blit(playerStandingAnim[0],(playerPosX,playerPosY))



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()