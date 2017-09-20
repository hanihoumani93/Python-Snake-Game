import pygame
import time
import random

pygame.init()

display_width = 800  # game frame display width
display_height = 600  # game frame display height

gameDisplay = pygame.display.set_mode((display_width,
                                       display_height))  # All the stuff we will create will be at this surface(gameDisplay) its like the canvas
# pygame.display.update() #Its like the flip book each page have an image when you flip the book you will get a movie (its imp in games)

white = (255, 255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

pygame.display.set_caption('Snake')  # set_caption() func it put a tittle to our pygame windows(surface)
icon =  pygame.image.load('snakeHead.png') # change the icon of the game in the top left of the windows
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
AppleThickness = 20

block_size = 20  # its the width and height of one block of the snake
FPS = 10
img = pygame.image.load('snakeHead.png')
apple = pygame.image.load('newApple1.png')
direction = 'right' # when the game starts we want the direction of the head to be to the right not to up like its by default

smallfont = pygame.font.Font(None, 25)  # creating a font object
medfont = pygame.font.Font(None, 50)
largefont = pygame.font.Font(None, 80)

def paused():

    paused = True
    message_to_screen("Paused", black, -100, size='large')
    message_to_screen("Press C to continue or Q to quit", black, 25, size= 'small')
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #gameDisplay.fill(white)
        
        clock.tick(5)
        

def score (score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])

def game_intro():
    intro = True
    
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()



            
        gameDisplay.fill(white)
        message_to_screen("Welcome to Snake Game", green, -100, size='large')
        message_to_screen("The objective of the game is to eat red apples", black, -30)
        message_to_screen("The more apples you eat the longer you get", black, 10)
        message_to_screen("If you run into yourself, or the edges, you die!", black, 50)
        message_to_screen("Press C to play, P to pause or Q to quit", black, 180)

        pygame.display.update()
        clock.tick(15)
        
def randAppleGen ():
    randAppleX = round(random.randrange(0, display_width - AppleThickness))  # / 10.0) * 10.0 generate random X and Y position to creat the apple
    randAppleY = round(random.randrange(0, display_height - AppleThickness))
    return randAppleX, randAppleY


def snake(block_size, snakeLinst):
    if direction == 'right':
        head = pygame.transform.rotate(img, 270)
    if direction == 'left':
        head = pygame.transform.rotate(img, 90)
    if direction == 'up':
        head = img
    if direction == 'down':
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snakeLinst[-1][0], snakeLinst[-1][1]))
    for XnY in snakeLinst[:-1]: #for every element in list except the head
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])


def message_to_screen(msg, color, y_displace=0, size='small'):
    if size == 'small':
        text_surf = smallfont.render(msg, True, color)
    elif size == 'medium':
        text_surf = medfont.render(msg, True, color)
    elif size == 'large':
        text_surf = largefont.render(msg, True, color)
    
    text_rect = text_surf.get_rect()
    text_rect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(text_surf, text_rect)


def gameLoop():
    global direction # this global direction variable is used to change the direction of the img
    direction = 'right' # every time the game loop begin the snake should be in the right direction
    gameExit = False
    gameOver = False

    lead_x = display_width / 2  # the X position of the rectangle
    lead_y = display_height / 2  # the Y position of the rectangle
    lead_x_change = 10  # lead_X and Y_ change it role to keep our rect moving, without the lead_x_change it will not move automatically
    lead_y_change = 0

    randAppleX, randAppleY = randAppleGen()
    # We round redAppleX and Y since the location of apple not the same for snake it should face to face to snake so we round it
    # The equation is such as x = 7 in this case the x = random.randrange(0, display_width - block_size)
    # So formula is random(x / 10.0) * 10.0 the value then is rounded if x = 7 then it will be 10 or if x = 14 it will be 10
    snakeList = []  # empty List
    snakeLength = 1

    while not gameExit:  # If you want 'while false' functionality, you need 'not'
        
        if gameOver == True:
            message_to_screen('Game Over', red, -50, size = 'large')
            message_to_screen(' Press C to play again or Q to quit', black, 50, size = 'medium')
            message_to_screen(' Your Score: ' +str(snakeLength-1), black, 100, size = 'medium')
            pygame.display.update()  # every time you make a message you should then update the display
            
        while gameOver == True:
            #gameDisplay.fill(white)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():  # pygame.event.get() this func gets every event don by the user (Mouse, key press...)
            if event.type == pygame.QUIT:  # when the user close the window the type of event will be QUIT so if its QUIT then close the windows
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left' # change the drection of the img to the left since by default it towers UP
                    lead_x_change = -block_size
                    lead_y_change = 0  # we make it = 0 since without this it will move as parabola waves (each time x change y should change and vis versa)
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p: # if we press P key while game is running then the game will be 
                    paused()
                    
            if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:  # this is for the boundaries of the game when the snake reach the walls the game will exit
                gameOver = True


                # ******************************** These lines of codes will make the rect stop when we keyup our key  ********************************

                #   if event.type == pygame.KEYUP:
                #      if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                #         lead_x_change = 0

                # ************************************************************************************************************************************

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)  # change the color of our windows display from black to white

        
        #pygame.draw.rect(gameDisplay, red,[randAppleX, randAppleY, AppleThickness, AppleThickness])  # draw the random apple
        gameDisplay.blit(apple,(randAppleX,randAppleY))
        pygame.display.flip()

        snakeHead = []
        snakeHead.append(lead_x)  # append the X position to the snakeHead List
        snakeHead.append(lead_y)  # append the X position to the snakeHead List
        snakeList.append(snakeHead)  # append list to a list in this case snake_list = [(1,2), (2,3), ...]
        if len(snakeList) > snakeLength:  # without this 'if' our snake will become bigger whenever it is running
            del snakeList[0]

        for eachSegment in snakeList[:-1]:  # [:-1] analise every thing in list up to last element
            if eachSegment == snakeHead:  # if we have collision of the snake (move in opposite direction or move around it self then Game Over)
                gameOver = True
        snake(block_size, snakeList)  # calling the snake() to create the snake
        # gameDisplay.fill(red, rect=[200, 200, 50, 50]) #another way to draw a rect on the surface

        ##        if lead_x == randAppleX and lead_y == randAppleY: #eating the apple, generate a new one, and then remove the eaten apple
        ##            randAppleX = round(random.randrange(0,display_width - block_size) / 10.0) * 10.0
        ##            randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
        ##            snakeLength += 1 #increase the size of the snake
        ##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness: #in this case the size of the apple is bigger than the snake
        ##            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
        ##                randAppleX = round(random.randrange(0,display_width - AppleThickness))# / 10.0) * 10.0
        ##                randAppleY = round(random.randrange(0, display_height - AppleThickness))# / 10.0) * 10.0
        ##                snakeLength += 1 #increase the size of the snake

        
        score(snakeLength-1) # increase the score by 1 depending on the size of the Snakelist, -1 since list began at 1 since of snakehead so -1 to be 0 Score
        pygame.display.update()
        
        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen() #call randAppleGen() func to creat random position of the apple
                snakeLength += 1  # increase the size of the snake
                

            elif lead_y + block_size >= randAppleY and lead_y + block_size <= randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1  # increase the size of the snake
                

        
        clock.tick(FPS)  # its the amount of frames per second (10 frames per second) # it forces the while loop to run each 15 second (FSP frame per second)

    # message_to_screen('You Lose!', red) #calling this functions before user lose or quit
    # pygame.display.update() # we should update again to let our msg to be shown
    # time.sleep(2) # keep msg for 5 second before quiting the game to let the user see the msg without this line the user will not see the msg it goes quickly


    pygame.quit()  # this will quit the pygame windows display
    quit()  # it quits the python code

game_intro()
gameLoop()

