import pygame
from pygame.locals import QUIT
from Graph_Class import Graph, Node
import graphAlgorithms as alg
from itertools import cycle



BLACK = (0,0,0)
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 650
FPS = 40


pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

nodes_names1 = ["A", "B", "C", "D"]
nodes_xy1 = [(50,300), (350, 150), (200, 300), (200,150)]
edges1 = [[0,0,1,0], [0, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]

# apply the function you want to see, edges as argoument -> in the example we call Dfs()
selected_algorithm_path = alg.Dfs(edges1)

# create a graph to visually represent it
gr = Graph(nodes_xy1, edges1, nodes_names1)

      # RAPRESENTATION OF GR

# A -- C -- D -- B -- C ('--' means connected in the 2 directions)

#      D--B
#      |  |
#   A--C--

click = False
path_index = 0

# Game loop
while True:

  fpsClock.tick(FPS)
  mouse_xy = pygame.mouse.get_pos()

  # Events
  for event in pygame.event.get():

    if event.type == pygame.MOUSEBUTTONDOWN: click = True
    elif event.type == pygame.MOUSEBUTTONUP: click = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE: path_index += 1

    elif event.type == QUIT:
      pygame.quit()
      sys.exit()

  # Update
  try: algorithm_curr_node = selected_algorithm_path[path_index]
  except IndexError: print "You reached the end of the path"
  Node.updateNodes(mouse_xy, click, algorithm_curr_node) # drag the mouse selected node

  # Draw
  screen.fill(BLACK)
  Graph.drawGraph(gr, screen)

  pygame.display.flip()

