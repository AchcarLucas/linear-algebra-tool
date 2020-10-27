'''
	Módulo Draw 
'''

import render
import point
import vector
import line

# Classe principal DRAW
class C_Draw:
	def __init__(self):
		self.screen = None
		self.pygame = None
		self.g_ui = None
		
		self. SCREEN_WIDTH = 800
		self.SCREEN_HEIGHT = 600
		
		self.c_render = render.C_Render(self)
		
		point_list = []
		point_vector = []
		point_line = []
		
	def gameDraw(self):
		self.screen.fill(self.pygame.Color('#FFFFFF'))
		
		self.c_render.render()
		
		self.g_ui.drawUI()
		
		self.pygame.display.update()