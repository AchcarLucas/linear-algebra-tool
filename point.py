import global_var

class C_Point:
	def __init__(self, x=0, y=0, z=0, color=(0, 0, 0)):		
		# O ponto é representado por uma matrix de 4 linhas e 1 coluna
		self.m_point_modify = [[x], [y], [z], [1]]
		self.m_original_point = self.m_point_modify.copy()
		
		self.color = color

	def debugPoint(self):
		print(f'Original Point {self.m_original_point}', end=' --- ')
		print(f'Modify Point {self.m_point_modify}')
		
	def getScreenX(self):
		return self.m_point_modify[0][0]
		
	def getScreenY(self):
		return self.m_point_modify[1][0]
		
	def getScreenZ(self):
		return self.m_point_modify[2][0]
		
	def setScreenX(self, x):
		self.m_point_modify[0][0] = x
		
	def setScreenY(self, y):
		self.m_point_modify[1][0] = y
		
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