'''
	Módulo Update
'''

import pickle

import global_var
import point
import vector
import line
import numpy as np

# Classe principal Update
class C_Update:
	def __init__(self):
		'''
			Função construct (Inicia todas as variáveis necessárias para a utilização da classe C_Update)
			Args:
				None
			Return:
				None
		'''
		self.pygame = None
		self.g_ui = None
		self.c_draw = None
		self.c_status = None
		
		self.auto_rot = [0.0, 0.0, 0.0]
		
		self.time_delta = 0.0
		
	def initClock(self):
		'''
			Função chamada uma única vez ao iniciar para dar inicio a contagem do tempo 
			para a utilização do controle de FPS
			Args:
				None
			Return:
				None
		'''
		self.clock = self.pygame.time.Clock()
		
	def gameUpdate(self):
		'''
			Função responsável por atualizar toda a lógica do jogo
			Args:
				None
			Return:
				None
		'''
		self.time_delta = self.clock.tick(60) / 1000.0
		
		self.clock
		
		if(self.c_status.automatic_rotate):
			self.setRotateSelected(self.c_status.obj_selected, self.auto_rot)
			self.auto_rot[0] += 0.5 * (global_var.random())
			self.auto_rot[1] += 0.5 * (global_var.random())
			self.auto_rot[2] += 0.5 * (global_var.random())
		else:
			self.auto_rot = [0.0, 0.0, 0.0]
		
		self.g_ui.fps_counter.set_text(f'FPS: {self.clock.get_fps():.2f}')
		
		self.g_ui.updateUI()
		
	def saveData(self, file_name):
		'''
			Salva as instância de ponto, linha e vetor em um arquivo
			Args:
				file_name: nome do arquivo a ser salvo
			Return:
				None
		'''
		with open('./files/' + file_name + '.alg', 'wb') as output:
			pickle.dump([self.c_draw.point_list, self.c_draw.line_list, self.c_draw.vector_list], output, pickle.HIGHEST_PROTOCOL)
		
	def loadData(self, file_name):
		'''
			Carrega um arquivo externo com as instâncias de pontos, vetores e linhas
			Args:
				file_name: nome do arquivo
			Return:
				None
		'''
		with open(file_name, 'rb') as input:
			data = pickle.load(input)
			
			self.c_draw.point_list 		= data[0] 
			self.c_draw.line_list 		= data[1]
			self.c_draw.vector_list 	= data[2]
			
			self.updateTransformList()
		
	def updateTransformList(self):
		'''
			Função responsável por atualizar a lista de transformações da caixa de transformações
			Args:
				None
			Return:
				None
		'''
		self.c_status.transform_list_text.clear()
		
		for l in self.c_draw.line_list:
			self.c_status.transform_list_text.append(f'{l[0]}(({l[1].M_A[0][0]:0.1f}, {l[1].M_A[1][0]:0.1f}, {l[1].M_A[2][0]:0.1f})), (({l[1].M_B[0][0]:0.1f}, {l[1].M_B[1][0]:0.1f}, {l[1].M_B[2][0]:0.1f}))')
				
		for v in self.c_draw.vector_list:
			x = v[1].M_A[0][0] - v[1].M_B[0][0]
			y = v[1].M_A[1][0] - v[1].M_B[1][0]
			z = v[1].M_A[2][0] - v[1].M_B[2][0]
			
			self.c_status.transform_list_text.append(f'{v[0]}({x:0.1f}, {y:0.1f}, {z:0.1f}) N = {np.sqrt(x*x + y*y + z*z):0.001f}')
			
		self.c_status.transform_list.set_item_list(self.c_status.transform_list_text)
			
	def setRotateSelected(self, selected, rot):
		'''
			Função responsável por fazer o setting da rotação dos vetores ou linhas selecionados
			Args:
				selected: Lista contendo todos os vetores e linhas selecionados
				scale: Tripla contendo a rotação (graus)
			Return:
				None
		'''
		for s in selected:
			for l in self.c_draw.line_list:
				if(s == l[0]):
					l[1].setRotate(rot)
					
			for v in self.c_draw.vector_list:
				if(s == v[0]):
					v[1].setRotate(rot)
	
	def setTranslateSelected(self, selected, trans):
		'''
			Função responsável por fazer o setting da translação dos vetores ou linhas selecionados
			Args:
				selected: Lista contendo todos os vetores e linhas selecionados
				scale: Tripla contendo a translação
			Return:
				None
		'''
		for s in selected:
			for l in self.c_draw.line_list:
				if(s == l[0]):
					l[1].setTranslate(trans)
					
			for v in self.c_draw.vector_list:
				if(s == v[0]):
					v[1].setTranslate(trans)
					
	def setScaleSelected(self, selected, scale):
		'''
			Função responsável por fazer o setting da escala dos vetores ou linhas selecionados
			Args:
				selected: Lista contendo todos os vetores e linhas selecionados
				scale: Tripla contendo a escala a ser aplicado 
			Return:
				None
		'''
		for s in selected:
			for l in self.c_draw.line_list:
				if(s == l[0]):
					l[1].setScale(scale)
					
			for v in self.c_draw.vector_list:
				if(s == v[0]):
					v[1].setScale(scale)
					
	def resetTL(self):
		'''
			Função responsável por resetar as transformações lineares aplicadas
			Args:
				None
			Return:
				None
		'''
		for l in self.c_draw.line_list:
			l[1].setRotate([0.0, 0.0, 0.0])
			l[1].setTranslate([0.0, 0.0, 0.0])
			l[1].setScale([1.0, 1.0, 1.0])
					
		for v in self.c_draw.vector_list:
			v[1].setRotate([0.0, 0.0, 0.0])
			v[1].setTranslate([0.0, 0.0, 0.0])
			v[1].setScale([1.0, 1.0, 1.0])
		
	def updateCommand(self, text):
		'''
			Função responsável por fazer a análise e execução dos comandos
			Arg:
				text: Comando que foi digitado
			Return:
				rtn: Enum RTN que contém os erros de returno
				_name: nome do vetor, ponto ou linha que foi dado
		'''
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
		
		# Pode ser usado comandos abreviados
		
		if (_cmd == 'V'):
			_cmd = 'Vector'
		elif (_cmd == 'L'):
			_cmd = 'Line'
		elif (_cmd == 'P'):
			_cmd = 'Point'
		elif (_cmd == 'RP'):
			_cmd = 'RPoint'
		elif (_cmd == 'RL'):
			_cmd = 'RLine'
		elif (_cmd == 'RV'):
			_cmd = 'RVector'
		
		# Verifica se o nome já existe, se sim, retorna (2), nome já existe
		
		if (_cmd == 'Vector') or (_cmd == 'Line') or (_cmd == 'Point'):
			for p in self.c_draw.point_list:
				if(p[1].name == _name):
					print('NAME_ALREADY')
					return global_var.RTN.NAME_ALREADY, 'none'
				
			for l in self.c_draw.line_list:
				if(l[1].name == _name):
					print('NAME_ALREADY')
					return global_var.RTN.NAME_ALREADY, 'none'
				
			for v in self.c_draw.vector_list:
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
			self.c_draw.point_list.append([_name, point.C_Point(x, y, z, (0, 0, 0), name=_name, visible=True)])
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
			for p in self.c_draw.point_list:
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
				self.c_draw.vector_list.append([_name, vector.C_Vector(p_b, p_a, name=_name, has_text=True)])
				rtn = global_var.RTN.SUCCESS_VECTOR
			elif _cmd =='Line':
				self.c_draw.line_list.append([_name, line.C_Line(p_a, p_b, name=_name, has_text=True)])
				rtn = global_var.RTN.SUCCESS_LINE
		# Remove um ponto
		elif _cmd == 'RPoint':
			# Verifica se o ponto está sendo usado antes de excluir
			for l in self.c_draw.line_list:
				if(l[1].p_a.name == _name or l[1].p_b.name == _name):
					print('POINT_IS_USED')
					return global_var.RTN.POINT_IS_USED, 'none'
				
			for v in self.c_draw.vector_list:
				if(v[1].p_a.name == _name or v[1].p_b.name == _name):
					print('POINT_IS_USED')
					return global_var.RTN.POINT_IS_USED, 'none'
					
			for p in self.c_draw.point_list:
				if p[0] == _name:
					self.c_draw.point_list.remove(p)
					break
			
			rtn = global_var.RTN.POINT_REMOVED
		# Remover uma linha
		elif _cmd == 'RLine':
			for p in self.c_draw.line_list:
				if p[0] == _name:
					self.c_draw.line_list.remove(p)
					break
			rtn = global_var.RTN.LINE_REMOVED
		# Remove um Vetor
		elif _cmd == 'RVector':
			for p in self.c_draw.vector_list:
				if p[0] == _name:
					self.c_draw.vector_list.remove(p)
					break
			rtn = global_var.RTN.VECTOR_REMOVED
		else:
			print('INVALID_CMD')
			return global_var.RTN.INVALID_CMD, 'none'
		
		self.updateTransformList()
		
		return rtn, _name