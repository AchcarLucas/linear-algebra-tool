import matrices
import linear_transform as TL
import global_var

class C_Point:
	def __init__(self, x=0, y=0, z=0, color=(0, 0, 0), name='none', visible=False, scale=4.0, has_text=False, text=None):		
		# O ponto é representado por uma matrix de 4 linhas e 1 coluna
		# Ponto original (sem rotação da camera)
		self.m_point_modify = [[x], [y], [z], [1]]
		# Ponto original sem transformação
		self.m_original_point = self.m_point_modify.copy()
		self.name = name
		self.visible = visible
		self.color = color
		self.scale=scale
		self.has_text = has_text
		self.text = text
		
		# Se uma linha ou um vetor estiver utilizando o ponto, o mesmo não será exibido na tela
		self.has_used = False
		
		self.c_TL = TL.C_LinearTransform()
	
	def debugPoint(self):
		print(f'Original Point {self.m_original_point}', end=' --- ')
		print(f'Modify Point {self.m_point_modify}')
		
	def render(self, c_draw):
		if self.visible:
			MVP = matrices.C_Matrix.identity(4)

			MVP = self.c_TL.rotateY(MVP, global_var.cam[1])
			MVP = self.c_TL.rotateZ(MVP, global_var.cam[2])
			MVP = self.c_TL.rotateX(MVP, global_var.cam[0])

			P = self.c_TL.perspectiveProjection(MVP, self)
				
			color = self.color
			if(self.has_used):
				color = (255, 0, 0)
			else:
				self.m_point_modify = self.m_original_point
				
			c_draw.pygame.draw.circle(c_draw.screen, color, [int(P.getScreenX() + c_draw.SCREEN_WIDTH / 2),  int(P.getScreenY() + c_draw.SCREEN_HEIGHT / 2)], int(self.scale), 0)

			# Só exibe a posição atual do ponto se não estiver sendo usado
			#if(not self.has_used):
			if(self.has_text and self.text != None):
				coordenateText = global_var.myfont.render(self.text, 0, (0, 0, 0, 0))
			else:
				coordenateText = global_var.myfont.render(f'{self.name} ({self.getOriginalScreenX():0.1f}, {self.getOriginalScreenY():0.1f}, {self.getOriginalScreenZ():0.1f})', 1, (0, 0, 0))
				
			c_draw.screen.blit(coordenateText, (int(P.getScreenX() + c_draw.SCREEN_WIDTH / 2) + 8,  int(P.getScreenY() + c_draw.SCREEN_HEIGHT / 2)))
			
		# Sempre desativa essa flag, se alguém ativar, significa que o ponto está sendo utilizado
		self.has_used = False
		
	def getScreenX(self):
		return self.m_point_modify[0][0]
		
	def getScreenY(self):
		return self.m_point_modify[1][0]
		
	def getScreenZ(self):
		return self.m_point_modify[2][0]
		
	def getOriginalScreenX(self):
		return self.m_original_point[0][0]
		
	def getOriginalScreenY(self):
		return self.m_original_point[1][0]
		
	def getOriginalScreenZ(self):
		return self.m_original_point[2][0]
		
	def setScreenX(self, x):
		self.m_original_point[0][0] = x
		
	def setScreenY(self, y):
		self.m_original_point[1][0] = y
		
	def setScreenZ(self, z):
		self.m_point_modify[2][0] = z
		
	def getNormalizedX(self):
		return self.getScreenX() / global_var.factor
		
	def getNormalizedY(self):
		return self.getScreenY() / global_var.factor
		
	def getNormalizedZ(self):
		return self.getScreenZ() / global_var.factor
		
	def getCopy(self):
		return self.m_point_modify.copy()