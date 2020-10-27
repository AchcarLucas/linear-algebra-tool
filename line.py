import linear_transform as TL
import matrices

class C_Line:
	def __init__(self, p_a, p_b, color=(0, 0, 0)):
		self.p_a = p_a
		self.p_b = p_b
		self.color = color
		
		self.translateXYZ = [0.0, 0.0, 0.0]
		self.scaleXYZ = [1.0, 1.0, 1.0]
		self.rotateXYZ = [0.0, 0.0, 0.0]
		
		self.c_TL = TL.C_LinearTransform()
		
	def renderLine(self, c_draw):
		MVP = matrices.C_Matrix.identity(4)
		
		MVP = self.c_TL.scaleXYZ(MVP, self.scaleXYZ[0], self.scaleXYZ[1], self.scaleXYZ[2])
		
		MVP = self.c_TL.rotateX(MVP, self.rotateXYZ[0] + 45.0)
		MVP = self.c_TL.rotateY(MVP, self.rotateXYZ[1])
		MVP = self.c_TL.rotateZ(MVP, self.rotateXYZ[2] + 45.0)
		
		MVP = self.c_TL.translateXYZ(MVP, self.translateXYZ[0], self.translateXYZ[1], self.translateXYZ[2])
		
		P_A = self.c_TL.perspectiveProjection(MVP, self.p_a)
		P_B = self.c_TL.perspectiveProjection(MVP, self.p_b)
		
		P_A.setX(P_A.getX() + c_draw.SCREEN_WIDTH / 2)
		P_A.setY(P_A.getY() + c_draw.SCREEN_HEIGHT / 2)
		
		P_B.setX(P_B.getX() + c_draw.SCREEN_WIDTH / 2)
		P_B.setY(P_B.getY() + c_draw.SCREEN_HEIGHT / 2)
		
		c_draw.pygame.draw.line(c_draw.screen, self.color, 
						(P_A.getX(), P_A.getY()), 
						(P_B.getX(), P_B.getY()))
		return P_A, P_B
						
	def setRotate(self, rotate=[0.0, 0.0, 0.0]):
		self.rotateXYZ = rotate
	
	def setTranslate(self, translate=[0.0, 0.0, 0.0]):
		self.translateXYZ = translate
		
	def setScale(self, scale=[0.0, 0.0, 0.0]):
		self.scaleXYZ = scale