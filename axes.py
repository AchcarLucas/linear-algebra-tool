import point
import line
import vector

class C_Axes:
	def __init__(self):
		self.createAxes()
		
	def createAxes(self):
		AXES_X_A = point.C_Point(1.0, 0.0, 0.0)
		AXES_X_B = point.C_Point(-1.0, 0.0, 0.0)

		AXES_Y_A = point.C_Point(0.0, 1.0, 0.0)
		AXES_Y_B = point.C_Point(0.0, -1.0, 0.0)

		AXES_Z_A = point.C_Point(0.0, 0.0, 1.0)
		AXES_Z_B = point.C_Point(0.0, 0.0, -1.0)

		self.V1 = vector.C_Vector(AXES_X_A, AXES_X_B, (255, 0, 0)) # X Vermelho
		self.V2 = vector.C_Vector(AXES_Y_A, AXES_Y_B, (0, 255, 0)) # Y Verde
		self.V3 = vector.C_Vector(AXES_Z_A, AXES_Z_B, (0, 0, 255)) # Z Azul
		
		color_x = (255,0,0)
		color_y = (0,255,0)
		color_z = (0,0,255)
		
		self.list_p = [
				# Eixo X
				point.C_Point(-2.5, 0.0, 0.0, visible=True, color=color_x, has_text=True, text='-2.5'),
				point.C_Point(-2.0, 0.0, 0.0, visible=True, color=color_x, has_text=True, text='-2.0'),
				point.C_Point(-1.5, 0.0, 0.0, visible=True, color=color_x, has_text=True, text='-1.5'),
				point.C_Point(-1.0, 0.0, 0.0, visible=True, color=color_x, has_text=True, text='-1.0'),
				point.C_Point(-0.5, 0.0, 0.0, visible=True, color=color_x, has_text=True, text='-0.5'),
				point.C_Point(0.5, 0.0, 0.0, visible=True, color=color_x, has_text=True, text='0.5'),
				point.C_Point(1.0, 0.0, 0.0, visible=True, color=color_x, has_text=True, text='1.0'),
				point.C_Point(1.5, 0.0, 0.0, visible=True, color=color_x, has_text=True, text='1.5'),
				point.C_Point(2.0, 0.0, 0.0, visible=True, color=color_x, has_text=True, text='2.0'),
				
				# Eixo Y
				point.C_Point(0.0, -2.5, 0.0, visible=True, color=color_y, has_text=True, text='-2.5'),
				point.C_Point(0.0, -2.0, 0.0, visible=True, color=color_y, has_text=True, text='-2.0'),
				point.C_Point(0.0, -1.5, 0.0, visible=True, color=color_y, has_text=True, text='-1.5'),
				point.C_Point(0.0, -1.0, 0.0, visible=True, color=color_y, has_text=True, text='-1.0'),
				point.C_Point(0.0, -0.5, 0.0, visible=True, color=color_y, has_text=True, text='-0.5'),
				point.C_Point(0.0, 0.5, 0.0, visible=True, color=color_y, has_text=True, text='0.5'),
				point.C_Point(0.0, 1.0, 0.0, visible=True, color=color_y, has_text=True, text='1.0'),
				point.C_Point(0.0, 1.5, 0.0, visible=True, color=color_y, has_text=True, text='1.5'),
				point.C_Point(0.0, 2.0, 0.0, visible=True, color=color_y, has_text=True, text='2.0'),
				
				# Eixo Z
				point.C_Point(0.0, 0.0, -2.5, visible=True, color=color_z, has_text=True, text='-2.5'),
				point.C_Point(0.0, 0.0, -2.0, visible=True, color=color_z, has_text=True, text='-2.0'),
				point.C_Point(0.0, 0.0, -1.5, visible=True, color=color_z, has_text=True, text='-1.5'),
				point.C_Point(0.0, 0.0, -1.0, visible=True, color=color_z, has_text=True, text='-1.0'),
				point.C_Point(0.0, 0.0, -0.5, visible=True, color=color_z, has_text=True, text='-0.5'),
				point.C_Point(0.0, 0.0, 0.5, visible=True, color=color_z, has_text=True, text='0.5'),
				point.C_Point(0.0, 0.0, 1.0, visible=True, color=color_z, has_text=True, text='1.0'),
				point.C_Point(0.0, 0.0, 1.5, visible=True, color=color_z, has_text=True, text='1.5'),
				point.C_Point(0.0, 0.0, 2.0, visible=True, color=color_z, has_text=True, text='2.0')
		]
	
	def renderAxes(self, c_draw):
		self.V1.setScale([2.5, 2.5, 2.5])
		self.V2.setScale([2.5, 2.5, 2.5])
		self.V3.setScale([2.5, 2.5, 2.5])
		
		self.V1.render(c_draw)
		self.V2.render(c_draw)
		self.V3.render(c_draw)
		
		for p in self.list_p:
			p.render(c_draw)
		