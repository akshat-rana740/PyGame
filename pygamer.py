#this is a game using pygame
import pygame
#this is your code for creating window and adding title to it
GameScreen = pygame.display.set_mode((1200,900))
pygame.display.set_caption("Game")
#this is the code for continous losding of screen
exit_game = False
while not exit_game:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit_game=True
pygame.quit()
quit()

      
