import numpy as np
import linear_transform
import matrices

import point
import line
import vector
import axes
import global_var

class C_Render:
	def __init__(self, c_draw):
		'''
			Função construct (Inicia todas as variáveis necessárias para a utilização da classe C_Render)
			Args:
				None
			Return:
				None
		'''
		self.c_draw = c_draw
		self.axes = axes.C_Axes()
		
	def render(self):
		# Desenha as linhas de guia (Axes)
		self.axes.renderAxes(self.c_draw)