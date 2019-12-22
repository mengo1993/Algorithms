import pygame
from pygame.locals import QUIT

# -- VARIABLES --

# COLORS
BLACK = (0,0,0)

# COLORS

WIDTH, HEIGHT = 640, 480
FPS = 10
# -- VARIABLES --

pygame.init()

fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game loop
while True:
  screen.fill(BLACK)

  # Events
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  # Update

  # Draw

  pygame.display.flip()
  fpsClock.tick(FPS)
