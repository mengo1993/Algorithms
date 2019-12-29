import pygame as py
import miscellaneous as mis

EDGES_WIDTH = 2 # the thickness of the connections between nodes
EDGES_COLOR = (90, 95, 105)
EDGES_ARROW_SIZE = 7 # the size of the arrows pointing from one node to another

NODES_RADIUS = 15 # the radius of the nodes
NODES_COLOR = (190, 220, 230)
NODES_SELECTED_COLOR = (255, 250, 150)
NODES_HIGHL_COLOR = (100, 255, 150) # the color of the nodes when highlighted
NODES_FONT_COLOR = (5, 0, 10)

FONT = 'comicsan'
FONT_SIZE = 25


py.font.init()
fnt = py.font.SysFont(FONT, FONT_SIZE)

class Graph:

    def __init__(self, nodes_xy, edges, nodes_names = None):

        self.edges = edges
        self.nodes = []
        self.n_nodes = len(nodes_xy) # the number of nodes are as many as the coordinates

        for node_index in range(self.n_nodes):

            if nodes_names == None: node_name = node_index
            else: node_name = nodes_names[node_index]

            node_xy = nodes_xy[node_index]

            self.nodes.append(Node(node_name, node_xy))


    def drawEdges(self, screen): # display the edges on the screen
        for from_node_index in range(self.n_nodes):
            from_xy = self.nodes[from_node_index].center

            destinations_index = [destination_index for destination_index, value in enumerate(self.edges[from_node_index]) if value == 1] # get the connections with the current node
            for dest_node_index in destinations_index:
                to_xy = self.nodes[dest_node_index].center
                mis.displayConnection(from_xy, to_xy, EDGES_WIDTH, EDGES_COLOR, EDGES_ARROW_SIZE, NODES_RADIUS, screen)
    @staticmethod
    def drawGraph(graph, screen):
        graph.drawEdges(screen)
        Node.drawNodes(screen)




class Node(py.Rect):

    all_nodes = []

    def __init__(self, name, xy): #xy is the tuple identifying the center of the node
        x, y = xy[0] - NODES_RADIUS, xy[1] - NODES_RADIUS
        self.name = name
        py.Rect.__init__(self, x, y, 2 * NODES_RADIUS, 2 * NODES_RADIUS)
        self.text = fnt.render(str(self.name), True, NODES_FONT_COLOR)
        self.text_wh = (self.text.get_width(), self.text.get_height())
        self.selected = False
        self.highlighted = False
        Node.all_nodes.append(self)

    def deplace(self, new_xy): self.center = new_xy

    def mouseSelected(self, mouse_xy, click):
        if not (click and self.collidepoint(mouse_xy)): self.selected = False
        else:
            self.selected = True
            return True

    @staticmethod
    def updateNodes(mouse_xy, click, to_highl):
        for node in Node.all_nodes:
            if node.mouseSelected(mouse_xy, click): node.deplace(mouse_xy)
            node.highlighted = False
        Node.all_nodes[to_highl].highlighted = True

    def draw(self, screen):

        if self.selected: color = NODES_SELECTED_COLOR
        elif self.highlighted: color = NODES_HIGHL_COLOR
        else: color = NODES_COLOR

        py.draw.circle(screen, color, self.center, NODES_RADIUS) # display node circle

        txt_w, txt_h = self.text_wh[0], self.text_wh[1]
        x, y = self.centerx - txt_w // 2, self.centery - txt_h //2
        screen.blit(self.text, (x,y)) # display node text

    @ staticmethod
    def drawNodes(screen):
        for node in Node.all_nodes: node.draw(screen)





