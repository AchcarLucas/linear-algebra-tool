'''
	Módulo Draw 
'''
import global_var

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
		
		self.point_list = []
		self.point_list.append(['A', point.C_Point(0,0,0, (0, 0, 0), name='A', visible=True)])
		self.point_list.append(['B', point.C_Point(1,1,1, (0, 0, 0), name='B', visible=True)])
		
		self.vector_list = []
		self.vector_list.append(['V1', vector.C_Vector(self.point_list[1][1], self.point_list[0][1], name='V1')])
		
		self.test = 0
		
		self.line_list = []
		
	def gameDraw(self):
		self.screen.fill(self.pygame.Color('#FFFFFF'))
		
		self.c_render.render()
		
		self.g_ui.drawUI()

		self.test += 0.1
		
		for l in self.line_list:
			l[1].render(self)
		
		for v in self.vector_list:
			v[1].setRotate([self.test,0,0])
			v[1].render(self)
			
		for p in self.point_list:
			p[1].render(self)
			
		
		self.pygame.display.update()
		
	def updateCommand(self, text):
		try:
			text = text.replace(' ', '')
			
			_name, _rest = text.split('=')
			_cmd, _axes = _rest.split('(')
		
			_param = _axes.replace(',', ' ').replace('(', '').replace(')', '')
		except:
			return global_var.RTN.INVALID_CMD, 'none'
			
		print(f'Nome [{_name}]')
		print(f'CMD [{_cmd}]')
		print(f'_PARAM [{_param}]')
		
		# Verifica se o nome já existe, se sim, retorna (2), nome já existe
		
		if (_cmd == 'Vector') or (_cmd == 'Line') or (_cmd == 'Point'):
			for p in self.point_list:
				if(p[1].name == _name):
					print('NAME_ALREADY')
					return global_var.RTN.NAME_ALREADY, 'none'
				
			for l in self.line_list:
				if(l[1].name == _name):
					print('NAME_ALREADY')
					return global_var.RTN.NAME_ALREADY, 'none'
				
			for v in self.vector_list:
				if(v[1].name == _name):
					print('NAME_ALREADY')
					return global_var.RTN.NAME_ALREADY, 'none'
		
		rtn = None
		
		# Adiciona um ponto
		if _cmd == 'Point':
			try:
				x, y, z = _param.split(' ')
				
				x = float(x)
				y = float(y)
				z = float(z)
			except:
				print('ERROR_CMD')
				return global_var.RTN.CMD_FAILED, 'none'
				
			print(f'X {x} Y {y} Z {z}')
				
			# Cria o ponto
			self.point_list.append([_name, point.C_Point(x, y, z, (0, 0, 0), name=_name, visible=True)])
			rtn = global_var.RTN.SUCCESS_POINT
		# Adiciona um Vetor ou uma Linha
		elif _cmd == 'Vector' or _cmd == 'Line':
			try:
				P_A, P_B = _param.split(' ')
			except:
				print('ERROR_CMD')
				return global_var.RTN.CMD_FAILED, 'none'
				
			print(f'Point {P_A} Point {P_B}')
			
			p_a = None
			p_b = None
			
			# Verifica se os pontos existem
			for p in self.point_list:
				if(p[0] == P_A):
					p_a = p[1]
				elif(p[0] == P_B):
					p_b = p[1]
			
			# Se alguns dos pontos não existir, não cria o vetor
			if(p_a == None or p_b == None):
				print('POINT_DOES_EXIST')
				return global_var.RTN.POINT_DOES_EXIST, 'none'
				
			# Cria o vetor
			if _cmd == 'Vector':
				self.vector_list.append([_name, vector.C_Vector(p_a, p_b, name=_name)])
				rtn = global_var.RTN.SUCCESS_VECTOR
			elif _cmd =='Line':
				self.line_list.append([_name, line.C_Line(p_a, p_b, name=_name)])
				rtn = global_var.RTN.SUCCESS_LINE
		# Remove um ponto
		elif _cmd == 'RPoint':
			# Verifica se o ponto está sendo usado antes de excluir
			for l in self.line_list:
				if(l[1].p_a.name == _name or l[1].p_b.name == _name):
					print('POINT_IS_USED')
					return global_var.RTN.POINT_IS_USED, 'none'
				
			for v in self.vector_list:
				if(v[1].p_a.name == _name or v[1].p_b.name == _name):
					print('POINT_IS_USED')
					return global_var.RTN.POINT_IS_USED, 'none'
					
			for p in self.point_list:
				if p[0] == _name:
					self.point_list.remove(p)
					break
			
			rtn = global_var.RTN.POINT_REMOVED
		# Remover uma linha
		elif _cmd == 'RLine':
			for p in self.line_list:
				if p[0] == _name:
					self.line_list.remove(p)
					break
			rtn = global_var.RTN.LINE_REMOVED
		# Remove um Vetor
		elif _cmd == 'RVector':
			for p in self.vector_list:
				if p[0] == _name:
					self.vector_list.remove(p)
					break
			rtn = global_var.RTN.VECTOR_REMOVED
		else:
			print('INVALID_CMD')
			return global_var.RTN.INVALID_CMD, 'none'
		
		return rtn, _name