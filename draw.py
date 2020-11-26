'''
	Módulo Draw 
	C_Draw é a classe responsável por desenhar todos os objetos na tela
'''

import global_var

import render
import point
import vector
import line

# Classe principal DRAW
class C_Draw:
	def __init__(self):
		'''
			Função construct (Inicia todas as variáveis necessárias para a utilização da classe C_Draw)
			Args:
				None
			Return:
				None
		'''
		self.screen = None
		self.pygame = None
		self.g_ui = None
		self.myfont = None
		self.c_status = None
		
		self. SCREEN_WIDTH = 1024
		self.SCREEN_HEIGHT = 600
		
		self.c_render = render.C_Render(self)
		
		
		self.point_list = [
						#['A', point.C_Point(1.0, 0.0, 0.0, name='A', visible=True)],
						#['O', point.C_Point(0.0, 0.0, 0.0, name='O', visible=True)],
						#['B', point.C_Point(1.0, 1.0, 0.0, name='B', visible=True)]
					]
				
		self.vector_list = [
						#['V1', vector.C_Vector(self.point_list[0][1], self.point_list[1][1], name='V1', has_text=True)]
					]
		self.line_list = [
						#['L1', line.C_Line(self.point_list[0][1], self.point_list[2][1], name='L1', has_text=True)]
					]
		
		
	def gameDraw(self):
		'''
			Função responsável por chamar as funções de renderização das classes de exibição (C_Point, C_Line, C_Vector, Axes etc)
			Args:
				None
			Return:
				None
		'''
		self.screen.fill(self.pygame.Color('#FFFFFF'))
		
		self.c_render.render()
		
		for p in self.point_list:
			p[1].render(self)
			
		for l in self.line_list:
			l[1].render(self, vText=self.c_status.vText)
		
		for v in self.vector_list:
			v[1].render(self, vText=self.c_status.vText)
		
		self.g_ui.drawUI()
		
		self.pygame.display.update()
		