from copy import deepcopy
import linear_transform as TL
import matrices as mtc
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
		
	def render(self, c_draw, dText=True, vText=True):
		MVP = mtc.C_Matrix.identity(4)
		
		MVP = self.c_TL.scaleXYZ(MVP, self.scaleXYZ[0], self.scaleXYZ[1], self.scaleXYZ[2])

		MVP = self.c_TL.rotateX(MVP, self.rotateXYZ[0])
		MVP = self.c_TL.rotateY(MVP, self.rotateXYZ[1])
		MVP = self.c_TL.rotateZ(MVP, self.rotateXYZ[2])
		
		MVP = self.c_TL.translateXYZ(MVP, self.translateXYZ[0], self.translateXYZ[1], self.translateXYZ[2])
		
		# Antes de aplicar a transformação de projeção, temos que saber onde esse ponto irá parar em relação 
		# ao nosso novo sistema de coordenadas
		M_A = mtc.C_Matrix.mul(MVP, self.p_a.m_original_point)
		M_B = mtc.C_Matrix.mul(MVP, self.p_b.m_original_point)

		# Faz mover a camera
		MVP = self.c_TL.rotateY(MVP, global_var.cam[1])
		MVP = self.c_TL.rotateZ(MVP, global_var.cam[2])
		MVP = self.c_TL.rotateX(MVP, global_var.cam[0])

		# Aplica a projeção 3D
		P_A = self.c_TL.perspectiveProjection(MVP, self.p_a)
		P_B = self.c_TL.perspectiveProjection(MVP, self.p_b)
		
		self.p_a.has_used = True
		self.p_b.has_used = True
	
		c_draw.pygame.draw.line(c_draw.screen, self.color, 
						(P_A.getScreenX() + c_draw.SCREEN_WIDTH / 2, P_A.getScreenY() + c_draw.SCREEN_HEIGHT / 2), 
						(P_B.getScreenX() + c_draw.SCREEN_WIDTH / 2, P_B.getScreenY() + c_draw.SCREEN_HEIGHT / 2))
		
		if(dText and self.has_text):
			p_a_text = None
			p_b_text = None
			
			if(self.a_text != None):
				p_a_text = global_var.myfont.render(self.a_text, 0, (0, 0, 0, 0))
			elif(vText):
				p_a_text = global_var.myfont.render(f'{self.p_a.name} ({M_A[0][0]:0.1f}, {M_A[1][0]:0.1f}, {M_A[2][0]:0.1f})', 1, (0, 0, 0))
				
			if (self.b_text != None):
				p_b_text = global_var.myfont.render(self.b_text, 0, (0, 0, 0, 0))
			elif(vText):
				p_b_text = global_var.myfont.render(f'{self.p_b.name} ({M_B[0][0]:0.1f}, {M_B[1][0]:0.1f}, {M_B[2][0]:0.1f})', 1, (0, 0, 0))

			if(p_a_text != None):
				c_draw.screen.blit(p_a_text, (int(P_A.getScreenX() + c_draw.SCREEN_WIDTH / 2) + 15,  int(P_A.getScreenY() + c_draw.SCREEN_HEIGHT / 2)))
			
			if(p_b_text != None):
				c_draw.screen.blit(p_b_text, (int(P_B.getScreenX() + c_draw.SCREEN_WIDTH / 2) + 8,  int(P_B.getScreenY() + c_draw.SCREEN_HEIGHT / 2)))
				
		return P_A, P_B, M_A, M_B
						
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