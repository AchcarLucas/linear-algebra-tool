class C_Point:
	def __init__(self, x=0, y=0, z=0, color=(0, 0, 0)):		
		# O ponto é representado por uma matrix de 4 linhas e 1 coluna
		self.m_point_modify = [[x], [y], [z], [1]]
		self.m_original_point = self.m_point_modify.copy()
		
		self.color = color

	def debugPoint(self):
		print(f'Original Point {self.m_original_point}', end=' --- ')
		print(f'Modify Point {self.m_point_modify}')
		
	def getX(self):
		return self.m_point_modify[0][0]
		
	def getY(self):
		return self.m_point_modify[1][0]
		
	def getZ(self):
		return self.m_point_modify[2][0]
		
	def setX(self, x):
		self.m_point_modify[0][0] = x
		
	def setY(self, y):
		self.m_point_modify[1][0] = y
		
	def setZ(self, z):
		self.m_point_modify[2][0] = z
		
	def getCopy(self):
		return self.m_point_modify.copy()