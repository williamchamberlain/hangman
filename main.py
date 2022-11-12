import pygame
import math
import random
#eqution for buttons      width-(gap+radius*2)*button-on-row/2


WHITE = (255,255,255)
BLACK = (0,0,0)





pygame.init() #initialise it
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT)) #capitals because of constant and its a variable because we ass things to the screen win for window
pygame.display.set_caption("Hangman by Will C")



LETTER_FONT = pygame.font.SysFont('comicsans', 40) #font for letters 
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT= pygame.font.SysFont('comicsans', 70)

#BUTTON VARIABLES

RADIUS = 20 #for button
GAP = 15
letters = [] 
startx = round((WIDTH - (RADIUS * 2 +GAP) * 13) / 2)
starty = 400

A=65

for i in range(26): #x and y postion for each button
  x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))  #the percentage sign returns remainder until 13 (the second row)
  y = starty + ((i // 13) * (GAP + RADIUS * 2)) #// is whole number division
  letters.append([x,y, chr(A + i), True]) #chr is character




#LOAD IMAGES
images = []
for i in range(7): #load in 6 images (use 7 because it's up to 7)
  image = pygame.image.load("hangman" +str(i) + ".png") #loads in image (1-6)
  images.append(image)


  
#GAME VARIABLES 
hangman_status = 0 #what image is needed
words=["COLLEGE","PYTHON","CODING","IDLE","PYGAME"]
word = random.choice(words)
guessed = [] #what letters the player has guessed 







def draw(): #for the circle
  win.fill((WHITE)) #fills white
  text = TITLE_FONT.render("PYGAME HANGMAN!",1,BLACK)
  win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

  #DRAW LETTERS 
  display_word = ""
  for letter in word:
    if letter in guessed:
      display_word += letter + " " #word being displayed with space if its in the word
    else:
      display_word += "_ "

  text = WORD_FONT.render(display_word, 1 ,BLACK)
  win.blit(text,(400,200))

    


  
  #DRAW BUTTONS
  for letter in letters:
    x , y, ltr, visible = letter #splitting up variable
    if visible:
      
      pygame.draw.circle(win,BLACK, (x, y), RADIUS, 3)
      text = LETTER_FONT.render(ltr, 1, BLACK)
      win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    
  
  win.blit(images[hangman_status], (150,100) ) #blit is draw
  pygame.display.update() 







def display_message(message): #brakcets pass through
  pygame.time.delay(1000)
  win.fill(WHITE)
  text = WORD_FONT.render(message, 1, BLACK)
  win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 -text.get_height()/2)) #centre equation
  pygame.display.update()
  pygame.time.delay(3000)
  





FPS = 60

clock = pygame.time.Clock() #set a clock at fps variable speed
run = True #for while loop

while run: #while run is true (playing)
  clock.tick(FPS) 
 
  for event in pygame.event.get(): #any event stored in here 
      if event.type == pygame.QUIT: 
          run = False
      if event.type ==pygame.MOUSEBUTTONDOWN:
        m_x , m_y = pygame.mouse.get_pos() #gets x and y where it is clicked
        for letter in letters:
          x, y , ltr, visible = letter
          if visible:
              
            dis = math.sqrt((x - m_x)**2 + (y-m_y)**2) #pythagoruous
            if dis < RADIUS:
              letter[3]= False
              guessed.append(ltr)
              if ltr not in word:
                hangman_status += 1
  draw()

  
  won = True

    
  for letter in word:
    if letter not in guessed:
      won= False
      break
        
  if won:
    display_message("You win!")
    break
    

  if hangman_status == 6:
    display_message("You lost")
    break
      
        #if the mouse is less than the radius away from centre there is no collision
        



        

pygame.quit() 


