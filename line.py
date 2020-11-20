from copy import deepcopy
import linear_transform as TL
import matrices
import global_var

class C_Line:
	def __init__(self, p_a, p_b, color=(0, 0, 0), name='none', has_text=False, a_text=None, b_text=None):
		self.p_a = p_a
		self.p_b = p_b
		self.color = color
		self.name = name
		self.has_text = has_text
		self.a_text = a_text
		self.b_text = b_text
		
		self.translateXYZ = [0.0, 0.0, 0.0]
		self.scaleXYZ = [1.0, 1.0, 1.0]
		self.rotateXYZ = [0.0, 0.0, 0.0]
		
		self.c_TL = TL.C_LinearTransform()
		
	def render(self, c_draw, dText=True):
		MVP = matrices.C_Matrix.identity(4)
		
		MVP = self.c_TL.scaleXYZ(MVP, self.scaleXYZ[0], self.scaleXYZ[1], self.scaleXYZ[2])

		MVP = self.c_TL.rotateX(MVP, self.rotateXYZ[0])
		MVP = self.c_TL.rotateY(MVP, self.rotateXYZ[1])
		MVP = self.c_TL.rotateZ(MVP, self.rotateXYZ[2])
		
		MVP = self.c_TL.translateXYZ(MVP, self.translateXYZ[0], self.translateXYZ[1], self.translateXYZ[2])

		# Pega as posi��es atuais dos pontos A e B antes de mover a camera 
		T_P_A = self.c_TL.perspectiveProjection(MVP, self.p_a)
		T_P_B = self.c_TL.perspectiveProjection(MVP, self.p_b)

		self.p_a.m_point_modify = T_P_A.m_original_point
		self.p_b.m_point_modify = T_P_B.m_original_point

		# Faz mover a camera
		MVP = self.c_TL.rotateY(MVP, global_var.cam[1])
		MVP = self.c_TL.rotateZ(MVP, global_var.cam[2])
		MVP = self.c_TL.rotateX(MVP, global_var.cam[0])

		P_A = self.c_TL.perspectiveProjection(MVP, self.p_a)
		P_B = self.c_TL.perspectiveProjection(MVP, self.p_b)
		
		self.p_a.has_used = True
		self.p_b.has_used = True
	
		c_draw.pygame.draw.line(c_draw.screen, self.color, 
						(P_A.getScreenX() + c_draw.SCREEN_WIDTH / 2, P_A.getScreenY() + c_draw.SCREEN_HEIGHT / 2), 
						(P_B.getScreenX() + c_draw.SCREEN_WIDTH / 2, P_B.getScreenY() + c_draw.SCREEN_HEIGHT / 2))
		
		return P_A, P_B
						
	def setRotate(self, rotate=[0.0, 0.0, 0.0]):
		self.rotateXYZ[0] = rotate[0]
		self.rotateXYZ[1] = rotate[1]
		self.rotateXYZ[2] = rotate[2]
	
	def setTranslate(self, translate=[0.0, 0.0, 0.0]):
		self.translateXYZ[0] = translate[0]
		self.translateXYZ[1] = translate[1]
		self.translateXYZ[2] = translate[2]
		
	def setScale(self, scale=[1.0, 1.0, 1.0]):
		self.scaleXYZ[0] = scale[0]
		self.scaleXYZ[1] = scale[1]
		self.scaleXYZ[2] = scale[2]