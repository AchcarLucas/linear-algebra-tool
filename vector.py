import numpy as np

import pygame
import line
import point
import global_var
	
arrow = pygame.image.load('img/arrow.png')

class C_Vector(line.C_Line):
	def __init__(self, p_a, p_b, color=(0, 0, 0), name='none'):
		super().__init__(p_a, p_b, color, name)
		
	def drawArrow(self, c_draw, x, y, angle=0.0, scale=1):
		rect_arrow = arrow.get_rect()
		rotated_arrow = pygame.transform.rotate(arrow, angle * 180 / np.pi)
		c_draw.screen.blit(rotated_arrow, [x - (rect_arrow[2] / 2) , y -  (rect_arrow[3] / 2)]) 
	
	def render(self, c_draw):
		P_A, P_B = super().render(c_draw)
		
		screenX = P_A.getScreenX() + c_draw.SCREEN_WIDTH / 2
		screenY = P_A.getScreenY() + c_draw.SCREEN_HEIGHT / 2
		
		v_x =   P_A.getScreenX()  - P_B.getScreenX()
		v_y =  P_A.getScreenY()  - P_B.getScreenY()
		
		# Desenha o arrow do vetor
		self.drawArrow(c_draw, screenX, screenY, np.arctan2(v_x, v_y) + np.pi)