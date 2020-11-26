import numpy as np

import pygame
import line
import point
import global_var

arrow = pygame.image.load('img/arrow.png')

'''
	Classe C_Vector possui herança da classe C_Line
'''
class C_Vector(line.C_Line):
	def __init__(self, p_a, p_b, color=(0, 0, 0), name='none', has_text=False, text=None):
		'''
			Função construct (Inicia todas as variáveis necessárias para a utilização da classe C_Vector)
			Args:
				None
			Return:
				None
		'''
		super().__init__(p_a, p_b, color, name, has_text)
		self.text = text
		
	def drawArrow(self, c_draw, x, y, angle=0.0, scale=1):
		'''
			Função responsável por desenhar a seta dos vetores
			Args:
				c_draw: Instância do C_Draw
				x: posição x da tela
				y: posição y da tela
				angle: ângulo de rotação
				scale: tamanho da seta
			Return:
				None
		'''
		rect_arrow = arrow.get_rect()
		rotated_arrow = pygame.transform.rotate(arrow, angle * 180 / np.pi)
		c_draw.screen.blit(rotated_arrow, [x - (rect_arrow[2] / 2) , y -  (rect_arrow[3] / 2)]) 

	def render(self, c_draw, vText=True):
		'''
			Função responsável por renderizar o vetor
			Args:
				c_draw: Instância do C_Draw
				vText: Status que indica se deve ou não exibir os textos na tela
			Return:
				None
		'''
		P_A, P_B = super().render(c_draw, False, vText)
		
		screenX = P_A.getScreenX() + c_draw.SCREEN_WIDTH / 2
		screenY = P_A.getScreenY() + c_draw.SCREEN_HEIGHT / 2
		
		v_x =  P_A.getScreenX()  - P_B.getScreenX()
		v_y =  P_A.getScreenY()  - P_B.getScreenY()
		
		# Exibe a posição atual do vetor
		if(self.has_text):
			t_text = None
			if(self.text != None):
				t_text = global_var.myfont.render(self.text, 1, (0, 0, 0))
			elif(vText):
				t_text = global_var.myfont.render(f'{self.name}({self.M_A[0][0] - self.M_B[0][0]:0.1f}, {self.M_A[1][0] - self.M_B[1][0]:0.1f}, {self.M_A[2][0] - self.M_B[2][0]:0.1f})', 1, (0, 0, 0))	
			
			if(t_text != None):
				c_draw.screen.blit(t_text, (int((P_A.getScreenX() + c_draw.SCREEN_WIDTH / 2.0) + 8), int((P_A.getScreenY() + c_draw.SCREEN_HEIGHT / 2.0))))
			
		# Desenha o arrow do vetor
		self.drawArrow(c_draw, screenX, screenY, np.arctan2(v_x, v_y) + np.pi)