# Saman Sandhu
# January 26, 2016
# SharkTank_Saman.py
# my summative project (game)

# import
import pygame
import random
import time
import textwrap

# --- Create the window

# initialize pygame
pygame.init()

# music
crash_sound = pygame.mixer.Sound("sadTrombone.wav")
Game_sound = pygame.mixer.music.load("GameSoundTrack.wav")
 
# Set the height and width of the screen
display_width = 900
display_height = 700

# define colours
black = (0,0,0)
white = (255,255,255)

green = (0,200,0)
yellow = (255,215,0)
red = (200,0,0)

bright_green = (0,255,0)
bright_yellow = (255,255,0)
bright_red = (255,0,0)

gameDisplay = pygame.display.set_mode([display_width,display_height])
pygame.display.set_caption("Summative Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# --- Sprite lists
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each Shark / Whale in the game
Shark_list = pygame.sprite.Group()
Whale_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()

# pause function
pause = True

# seconds between lost of live and continue
sec = 3

# --- Classes --- #

class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.image.load("submarineSmall.png")
        self.rect = self.image.get_rect()
        self.width = 170
        self.height = 170
        self.distance = 0

# This represents the player
Player = Player()
# Add the player to the all_sprites_list
all_sprites_list.add(Player)

# Shark Class
class Shark(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.width = 228
        self.height = 126
        self.speed = 7
        self.dodged = 0
        self.image = pygame.image.load("Shark.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = random.randrange(0,display_height-self.height)

    def Draw(self):
        # --- Create the sprites
        if self.rect.x == 1000: 
            # Add the block to the list of objects
            Shark_list.add(self)
            all_sprites_list.add(self)
            print(self)
        # --- Create new sprite when one leaves the screen
        if self.rect.x <= -300:
            self.rect.x = 1000
            self.rect.y = random.randrange(0,display_height-self.height)
            self.dodged +=1

    def bulletHit(self):
        # See if it hit a block
        Shark_hit_list = pygame.sprite.spritecollide(Bullet, Shark_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in Shark_hit_list:
            bullet_list.remove(Bullet)
            all_sprites_list.remove(Bullet)
            self.dodged += 1
            self.rect.x = 1000
            self.rect.y = random.randrange(0,display_height-self.height)

    def update(self):
        """ Move the shark. """
        self.rect.x -= self.speed

# This represents a block
Shark = Shark()

# Whale Class
class Whale(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.width = 350
        self.height = 177
        self.speed = 5
        self.dodged = 0
        self.image = pygame.image.load("Whale.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = random.randrange(0,display_height-self.height)

    def Draw(self):
        # --- Create the sprites
        if self.rect.x == 1200: 
            # Add the block to the list of objects
            Whale_list.add(self)
            all_sprites_list.add(self)
            print("YES")
        # --- Create new sprite when one leaves the screen
        if self.rect.x <= -500:
            self.rect.x = 1200
            self.rect.y = random.randrange(0,display_height-self.height)
            self.dodged += 1
            print("YES")

    def bulletHit(self):
        # See if it hit a block
        Whale_hit_list = pygame.sprite.spritecollide(Bullet, Whale_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in Whale_hit_list:
            bullet_list.remove(Bullet)
            all_sprites_list.remove(Bullet)
            self.dodged += 1
            self.rect.x = 1200
            self.rect.y = random.randrange(0,display_height-self.height)

    def update(self):
        """ Move the whale. """
        self.rect.x -= self.speed

# This represents a block
Whale = Whale()

# Missile Class
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.image.load("rocket.png")
        self.rect = self.image.get_rect()
        self.numbBullet = 5

    def bulletGone(self):
        # Remove the bullet if it flies up off the screen
        if self.rect.y < -10:
            bullet_list.remove(Bullet)
            all_sprites_list.remove(Bullet)
 
    def update(self):
        """ Move the bullet. """
        self.rect.x += 10

# This represents a bullet
Bullet = Bullet()

# Setting Class 
class Setting: 
      # x,y,width,height values
    def __init__(self,x,y,width,height): 
        self.x=0 
        self.y=0 
        self.width = display_width 
        self.height = display_height
        self.image = pygame.image.load("Underwater.png")

    def render(self):
        gameDisplay.blit(self.image, (self.x, self.y))

# variable sprite
Setting=Setting(0,0,900,700)

# # # # # # ------ GAME FUNCTIONS ------ # # # # # #

#text
def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

#Game Intro
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        Setting.render()
        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("Shark Tank", largeText, black)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("PLAY",175,450,175,50,green,bright_green,game_loop)
        button("INSTRUCTIONS",375,450,175,50,yellow,bright_yellow,Instructions)
        button("QUIT",575,450,175,50,red,bright_red,quitGame)

        pygame.display.update()
        clock.tick(15)

# instruction part 1
instruction_text1 = (
    "Due to pressure differences in the sub polar waters, the captain cannot exceed the parameters of the screen.In order to avoid death, the player must use the up and down keys on the keyboard, to increase or decrease in depth:"
    )
# instruction part 2
instruction_text2 = (
    "Since the captain of the submarine knew that the sub polar waters are full of Sharks and Whales, the captain equipped himself with multiple missiles, however there is a time interval between bursts of  5 missiles when no missiles can be fired. In order to fire missiles, the player must press the spacebar:"
    )
# display instructions function
def Instructions():
    Setting.render()
    y = 0
    x = 0
    # text part 1
    string1 = textwrap.wrap(instruction_text1)
    for line1 in string1:
        if y <= 75:
            y += 25
        else:
            y = 0
            time.sleep(3)

        font = pygame.font.SysFont(None, 37)
        text1 = font.render(line1, True, white)
        gameDisplay.blit(text1, (15,y))
        pygame.display.update()
    # picture 1
    arrows = pygame.image.load("InstructionMovement.png")
    arrows = pygame.transform.scale(arrows,(350,193))
    gameDisplay.blit(arrows,(300,150))
    pygame.display.update()
    # text part 2
    string2 = textwrap.wrap(instruction_text2)
    for line2 in string2:
        y += 25
        font = pygame.font.SysFont(None, 37)
        text2 = font.render(line2, True, white)
        gameDisplay.blit(text2, (15,250+y))
        pygame.display.update()
    # picture 2
    missile = pygame.image.load("InstructionRocket.png")
    missile = pygame.transform.scale(missile,(450,144))
    gameDisplay.blit(missile,(237.5,525))
    pygame.display.update()

    time.sleep(10)

# Lives Control Function
def Lives():

    if Player.lives <= 0:
            crash()

    pygame.mixer.music.pause()
    pygame.mixer.Sound.play(crash_sound)
    Shark.rect.x = 1000
    Whale.rect.x = 1200
    moveY = 0
    
    while not pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects(("Lives Left: ")+str(Player.lives), largeText, black)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        moveY = 0

        button("CONTINUE",225,450,150,50,green,bright_green,unpause)
        button("QUIT",525,450,150,50,red,bright_red,quitGame)

        pygame.display.update()
        clock.tick(15)

# Crash Function
def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # diaplay "Game Over"
        gameDisplay.blit(pygame.image.load("GameOverScreen.jpg"),(0,0))
        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("Game Over", largeText, white)
        TextRect.center = ((display_width/2),(display_height/2)-100)
        gameDisplay.blit(TextSurf, TextRect)
        #### Define font
        font = pygame.font.SysFont(None, 50)
        #### number of sharks dodged
        text1 = font.render("Sharks Dodged: "+str(Shark.dodged), True, white)
        gameDisplay.blit(text1, (300,385))
        #### number of whales dodged
        text2 = font.render("Whales Dodged: "+str(Whale.dodged), True, white)
        gameDisplay.blit(text2, (297.5,415))
        #### distance travelled
        text3 = font.render("Distance Travelled: "+str(Player.distance)+" m", True, white)
        gameDisplay.blit(text3, (230,355))
        # stage conditionals
        if -1 < Player.distance < 1000:
            font = pygame.font.SysFont(None, 75)
            text = font.render("Stage: 1", True, white)
        if 999 < Player.distance < 2000:
            font = pygame.font.SysFont(None, 75)
            text = font.render("Stage: 2", True, white)
        if 1999 < Player.distance < 3000:
            font = pygame.font.SysFont(None, 75)
            text = font.render("Stage: 3", True, white)
        if 2999 < Player.distance < 4000:
            font = pygame.font.SysFont(None, 75)
            text = font.render("Stage: 4", True, white)
        if 3999 < Player.distance < 5000:
            font = pygame.font.SysFont(None, 75)
            text = font.render("Stage: 5", True, white)
        if 4999 < Player.distance:
            font = pygame.font.SysFont(None, 75)
            text = font.render("Stage: FINAL", True, white)
        #### display stage
        gameDisplay.blit(text, (350,300))
        #### buttons
        button("PLAY AGAIN",225,475,150,50,green,bright_green,game_loop)
        button("QUIT",525,475,150,50,red,bright_red,quitGame)

        pygame.display.update()
        clock.tick(15)

# Function for button
def button(msg,x,y,width,height,iC,aC,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # detect if "button" was pressed
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, aC, (x,y,width,height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, iC, (x,y,width,height))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ( (x+(width/2)),(y+(height/2)) )
    gameDisplay.blit(textSurf, textRect)

# Function to quit game
def quitGame():
    pygame.quit()
    quit()

# Pause Function
def paused():

    pygame.mixer.music.pause()

    while not pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("Paused", largeText, black)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("CONTINUE",225,450,150,50,green,bright_green,unpause)
        button("QUIT",525,450,150,50,red,bright_red,quitGame)

        pygame.display.update()
        clock.tick(15)

# Unpause Function
def unpause():
    global pause
    moveY = 0
    sec = 3
    x = 0
    pygame.mixer.music.unpause()
    pause = True
    while 0 < sec < 4:
        font = pygame.font.SysFont(None, 150)
        text = font.render(str(sec), True, black)
        gameDisplay.blit(text, (350+x,150))
        time.sleep(1)
        sec -= 1
        x += 75
        pygame.display.update()

# Shark -- Score Function
def Shark_dodge(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Sharks Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0,0))

# Whale -- Score Function
def Whale_dodge(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Whales Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0,20))

# Whale -- Score Function
def NumberOfRockets(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Number of Rockets: "+str(count), True, black)
    gameDisplay.blit(text, (0,40))

# distance travelled
def distance():
    Player.distance += 1
    font = pygame.font.SysFont(None, 25)
    text = font.render("Distance Travelled: "+str(Player.distance)+" m", True, black)
    gameDisplay.blit(text, (331,35))

# "You Win" function
def Winner():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(pygame.image.load("GameOverScreen.jpg"),(0,0))
        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("You Win", largeText, black)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("PLAY AGAIN",225,450,150,50,green,bright_green,game_loop)
        button("QUIT",525,450,150,50,red,bright_red,quitGame)

        pygame.display.update()
        clock.tick(15)

# stages function
def stages():
    if -1 < Player.distance < 1000:
        font = pygame.font.SysFont(None, 50)
        text = font.render("Stage: 1", True, black)
        gameDisplay.blit(text, (375,0))
        Shark.speed = 7
        Shark.Draw()

    if 999 < Player.distance < 2000:
        font = pygame.font.SysFont(None, 50)
        text = font.render("Stage: 2", True, black)
        gameDisplay.blit(text, (375,0))
        Shark.speed = 7
        Shark.Draw()

    if 1999 < Player.distance < 3000:
        font = pygame.font.SysFont(None, 50)
        text = font.render("Stage: 3", True, black)
        gameDisplay.blit(text, (375,0))
        Shark.speed = 9
        Whale.speed = 5
        if Player.distance == 2000:
            Bullet.numbBullet = 5
        Shark.Draw()
        Whale.Draw()

    if 2999 < Player.distance < 4000:
        font = pygame.font.SysFont(None, 50)
        text = font.render("Stage: 4", True, black)
        gameDisplay.blit(text, (375,0))
        Shark.speed = 11
        Whale.speed = 7
        Shark.Draw()
        Whale.Draw()

    if 3999 < Player.distance < 5000:
        font = pygame.font.SysFont(None, 50)
        text = font.render("Stage: 5", True, black)
        gameDisplay.blit(text, (375,0))
        Shark.speed = 13
        Whale.speed = 9
        if Player.distance == 4000:
            Bullet.numbBullet = 5
        Shark.Draw()
        Whale.Draw()

    if 4999 < Player.distance:
        font = pygame.font.SysFont(None, 50)
        text = font.render("Stage: FINAL", True, black)
        gameDisplay.blit(text, (375,0))
        Shark.speed = 15
        Whale.speed = 11
        if Player.distance == 5000:
            Bullet.numbBullet = 5
        Shark.Draw()
        Whale.Draw()
    if Player.distance == 6000:
        Winner()

# -------- Main Program Loop -----------
def game_loop():

    # music
    pygame.mixer.music.play(-1)

    # Loop until the user clicks the close button.
    running = True

    #reset variables
    Player.rect.x=50 
    Player.rect.y=250
    Player.distance = 0
    Player.lives = 3
    
    Shark.rect.x = 1000
    Shark.rect.y = random.randrange(0,display_height-Shark.height)
    Shark.speed = 7
    Shark.dodged = 0

    Whale.rect.x = 1200
    Whale.rect.y = random.randrange(0,display_height-Whale.height)
    Whale.speed = 5
    Whale.dodged = 0
    all_sprites_list.remove(Whale)
    
    Bullet.numbBullet = 5
    bullet_list.remove(Bullet)
    all_sprites_list.remove(Bullet)

    moveY = 0
    global pause
    ################
    

    while running:
        # --- Event Processing ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    moveY = -5
                if event.key == pygame.K_DOWN:
                    moveY = 5
                if event.key == pygame.K_p:
                    pause = False
                    paused()
                if event.key == pygame.K_SPACE:
                    if 0 < Bullet.numbBullet:
                        # Set the bullet so it is where the player is
                        Bullet.rect.x = Player.rect.x + Player.width * 0.9
                        Bullet.rect.y = Player.rect.y + Player.height * 0.5
                        # Add the bullet to the lists
                        all_sprites_list.add(Bullet)
                        bullet_list.add(Bullet)
                        Bullet.numbBullet -= 1
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    moveY = 0
                if event.key == pygame.K_DOWN:
                    moveY = 0
     
    # --- Game logic
        # Clear the screen
        Setting.render()

        stages()

        # move player
        Player.rect.y += moveY
        
        all_sprites_list.update()
     
        # Calculate mechanics for each bullet
        for bullet in bullet_list:
            Shark.bulletHit()
            Whale.bulletHit()
            Bullet.bulletGone()
     
        # Player and Shark Collision detection
        if Player.rect.x + Player.width > Shark.rect.x:

            if Player.rect.y > Shark.rect.y and Player.rect.y < Shark.rect.y + Shark.height:
                moveY = 0
                pause = False
                Player.lives -= 1
                Lives()
            if Player.rect.y + Player.height > Shark.rect.y and Player.rect.y + Player.height < Shark.rect.y + Shark.height:
                moveY = 0
                pause = False
                Player.lives -= 1
                Lives()
            if Player.rect.y < Shark.rect.y and Player.rect.y + Player.height > Shark.rect.y + Shark.height:
                moveY = 0
                pause = False
                Player.lives -= 1
                Lives()
                
        # Player and Whale Collision detection
        if Player.rect.x + Player.width > Whale.rect.x:

            if Player.rect.y > Whale.rect.y and Player.rect.y < Whale.rect.y + Whale.height:
                moveY = 0
                pause = False
                Player.lives -= 2
                Lives()
            if Player.rect.y + Player.height > Whale.rect.y and Player.rect.y + Player.height < Whale.rect.y + Whale.height:
                moveY = 0
                pause = False
                Player.lives -= 2                
                Lives()
            if Player.rect.y < Whale.rect.y and Player.rect.y + Player.height > Whale.rect.y + Whale.height:
                moveY = 0
                pause = False
                Player.lives -= 2
                Lives()

        # Player and Wall Collision detection
        if Player.rect.y > display_height-Player.width or Player.rect.y < 0:
            moveY = 0
            pause = False
            Player.rect.y = 250
            Player.lives -= 1
            Lives()

        # call display functions
        Shark_dodge(Shark.dodged)
        Whale_dodge(Whale.dodged)
        NumberOfRockets(Bullet.numbBullet)
        distance()

        # draw all the sprites to the screen
        all_sprites_list.draw(gameDisplay)
     
        # Update the screen with what's drawn
        pygame.display.update()
     
        # --- Limit to 20 frames per second
        clock.tick(60)
        
game_intro()        
pygame.quit()
quit()
