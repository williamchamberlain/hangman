import pygame
#eqution for buttons      width-(gap+radius*2)*button-on-row/2

WHITE = (255,255,255)
BLACK = (0,0,0)





pygame.init() #initialise it
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT)) #capitals because of constant and its a variable because we ass things to the screen win for window
pygame.display.set_caption("Hangman by Will C")



LETTER_FONT = pygame.font.SysFont('comicsans', 40) #font for letters 




images = []
for i in range(7): #load in 6 images (use 7 because it's up to 7)
  image = pygame.image.load("hangman" +str(i) + ".png") #loads in image (1-6)
  images.append(image)


RADIUS = 20 #for button
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 +GAP) * 13) / 2)
starty = 400

A=65

for i in range(26): #x and y postion for each button
  x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))  #the percentage sign returns remainder until 13 (the second row)
  y = starty + ((i // 13) * (GAP + RADIUS * 2)) #// is whole number division
  letters.append([x,y, chr(A+i)]) #chr is character









def draw(): #for the circle
  win.fill((WHITE)) #fills white

  for letter in letters:
    x , y, ltr = letter #splitting up variable
    pygame.draw.circle(win,BLACK, (x, y), RADIUS, 3)
    text = LETTER_FONT.render(ltr, 1, BLACK)
    win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    
  
  win.blit(images[hangman_status], (150,100) ) #blit is draw
  pygame.display.update() 

hangman_status = 6 #what image is needed










FPS = 60

clock = pygame.time.Clock() #set a clock at fps variable speed
run = True #for while loop

while run: #while run is true (playing)
  clock.tick(FPS) 

  draw()
 
  for event in pygame.event.get(): #any event stored in here 
      if event.type == pygame.QUIT: 
          run = False
      if event.type ==pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos() #pos is postion of where it is clicked
        print(pos) #note for future self cooridnates are from top left 
        
        



        

pygame.quit() 


