import pygame
import math


# display the connection between two nodes,
#if the connection is from 'A' to 'B', draw an arrow pointing to 'B'

def displayConnection(start_xy, end_xy, width, col, arrow_size, node_r,  screen):
    angle = math.degrees(math.atan2(start_xy[1]-end_xy[1], end_xy[0]-start_xy[0]))
    cos, sin = math.cos(math.radians(angle)), math.sin(math.radians(angle))
    _segment_length = segment_length(start_xy, end_xy)
    arrow_length = _segment_length - node_r - arrow_size
    end_xy = (start_xy[0] + cos * arrow_length, start_xy[1] - sin * arrow_length)
    draw_arrow(screen, col, start_xy, end_xy, width, arrow_size)


def draw_arrow(screen, colour, start, end, line_width, arrow_size):
    pygame.draw.line(screen,colour,start,end,line_width)
    rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0]))+90
    pygame.draw.polygon(screen, colour, ((end[0]+arrow_size*math.sin(math.radians(rotation)), end[1]+arrow_size*math.cos(math.radians(rotation))), (end[0]+arrow_size*math.sin(math.radians(rotation-120)), end[1]+arrow_size*math.cos(math.radians(rotation-120))), (end[0]+arrow_size*math.sin(math.radians(rotation+120)), end[1]+arrow_size*math.cos(math.radians(rotation+120)))))

def segment_length(start_xy, end_xy):
    delta_x, delta_y = end_xy[0]-start_xy[0], end_xy[1]-start_xy[1]
    return math.sqrt(delta_y ** 2 + delta_x ** 2)



