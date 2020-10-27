import numpy as np

import pygame
import line
import point

arrow = pygame.image.load('img/arrow.png')

def drawArrow(c_draw, x, y, angle=0.0, scale=1):
	rect_arrow = arrow.get_rect()
	rotated_arrow = pygame.transform.rotate(arrow, angle)
	c_draw.screen.blit(rotated_arrow, [x - (rect_arrow[2] / 2) , y -  (rect_arrow[3] / 2)]) 
	
class C_Vector(line.C_Line):
	def __init__(self, p_a, p_b, color=(0, 0, 0)):
		super().__init__(p_a, p_b, color)
		
	def renderLine(self, c_draw):
		P_A, P_B = super().renderLine(c_draw)
		
		v_x =  P_A.getX() - P_B.getX()
		v_y =  P_A.getY() - P_B.getY()

		drawArrow(c_draw, P_B.getX(), P_B.getY(), np.arctan2(v_y, v_x))