# http://www.ic.uff.br/~aconci/Aula-7.pdf
# https://pt.wikipedia.org/wiki/Matriz_de_rota%C3%A7%C3%A3o
# Slide da professora de Álgebra Linear
# https://slideplayer.com.br/slide/377102/

import numpy as np
import matrices as mtc
import point
import global_var

class C_LinearTransform:
	
	def __init__(self):
		self.S = 1. / (np.tan((global_var.angleOfView / 2.) * (np.pi / 180.)))
	
	def rotateX(self, T_M, angle_degree):
		'''
			Matrix de rotação (Eixo X)
			T(x, y, z, w) M(4,4) * M(4,1) -> R^4
			
			T_z(x, y, z, w) = (x, y*cos(Theta) - z*sin(Theta), y*sin(Theta) + z*cos(Theta), 0)
			
			
						| 1				0			0	  	0 |		|	x	|
			T(x, y, z, w) = 	| 0			cos(Theta)		-sen(Theta) 	0 | 	* 	|	y	|
						| 0			sin(Theta)		cos(Theta)		0 |		|	z	|
						| 0			0				0 		1 |		|	0	|
						
						
			Entrada (Input): Classe C_Ponto e o ângulo para transformar
			Saída (Output): Classe Point
		'''
		
		Deg2Rad = np.pi / 180.0
		
		theta = angle_degree * Deg2Rad
		
		cos_theta = np.cos(theta)
		sin_theta = np.sin(theta)
		
		# A matrix de rotação Z é uma matrix de 4 linhas e 4 colunas
		t_rotate_z = [	[1, 			0, 			0,			0], 
					[0, 			cos_theta, 	-sin_theta,	0], 
					[0, 			sin_theta, 		cos_theta, 	0],
					[0, 			0, 			0,			1]]
		
		# Faz a transformação linear
		return mtc.C_Matrix.mul(t_rotate_z, T_M)
		
	def rotateY(self, T_M, angle_degree):
		'''
			Matrix de rotação (Eixo Y)
			T(x, y, z, w) M(4,3) * M(4,1) -> R^4
			
			T_z(x, y, z, w) = (x*cos(Theta) - z*sin(Theta), y, x*sin(Theta) + z*cos(Theta), 0)
			
			
						| cos(Theta)	0	 -sen(Theta)		0 |		|	x	|
			T(x, y, z) = 	| 0			1		0			0 | 	* 	|	y	|
						| sin(Theta)	0		cos(Theta)		0 |		|	z	|
						| 0			0			0 		1 |		|	0	|
						
						
			Entrada (Input): Classe C_Ponto e o ângulo para transformar
			Saída (Output): Classe Point
		'''
		
		Deg2Rad = np.pi / 180.0
		
		theta = angle_degree * Deg2Rad
		
		cos_theta = np.cos(theta)
		sin_theta = np.sin(theta)
		
		# A matrix de rotação Y é uma matrix de 4 linhas e 4 colunas
		t_rotate_y = [	[cos_theta, 	0, 	-sin_theta,	0], 
					[0, 	1, 	0,	0], 
					[sin_theta, 	0, 	cos_theta, 	0],
					[0, 	0, 	0,	1]]
		
		# Faz a transformação linear
		return mtc.C_Matrix.mul(t_rotate_y, T_M)
		
	def rotateZ(self, T_M, angle_degree):
		'''
			Matrix de rotação (Eixo Z)
			T(x, y, z, w) M(4,4) * M(4,1) -> R^4
			
			T_z(x, y, z, w) = (x*cos(Theta) - y*sin(Theta), x*sin(Theta) + y*cos(Theta), z, 0)
			
			
						| cos(Theta)	sen(Theta)	0		0 |		|	x	|
			T(x, y, z, w) = 	| -sin(Theta)	cos(Theta)		0 		0 | 	* 	|	y	|
						| 0			0			1 		0 |		|	z	|
						| 0			0			0 		1 |		|	0	|
						
						
			Entrada (Input): Classe C_Ponto e o ângulo para transformar
			Saída (Output): Classe Point
		'''
		
		Deg2Rad = np.pi / 180.0
		
		theta = angle_degree * Deg2Rad
		
		cos_theta = np.cos(theta)
		sin_theta = np.sin(theta)
		
		# A matrix de rotação X é uma matrix de 4 linhas e 4 colunas
		t_rotate_x = [	[ cos_theta, 	sin_theta, 	0, 	0], 
					[-sin_theta, 	cos_theta, 	0,	0], 
					[0, 	0,	1,	0],
					[0, 	0, 	0,	1]]
		
		# Faz a transformação linear
		return mtc.C_Matrix.mul(t_rotate_x, T_M)
	
	def scaleXYZ(self, T_M, scale_x=1.0, scale_y=1.0, scale_z=1.0):
		'''
			Matrix de escala (Eixo XYZ)
			T(x, y, z, w) M(4,4) * M(4,1) -> R^4
			
			T_z(x, y, z, w) = (scale_x*x, scale_y*y, scale_z*z, 0)
			
			
						| scale_x				0				0  			0 |		|	x	|
			T(x, y, z, w) = 	| 0					scale_y			0  			0 | 	* 	|	y	|
						| 0					0				scale_z 		0 |		|	z	|
						| 0					0				0 			1 |		|	0	|
						
						
			Entrada (Input): Classe C_Ponto e as escalas x, y e z
			Saída (Output): Classe Point
		'''
		
		# A matrix de escala X, Y e Z é uma matrix de 4 linhas e 4 colunas
		t_scale_xyz = [	[scale_x, 		0, 		0, 		0], 
					[0, 		scale_y, 		0, 		0], 
					[0, 		0,		scale_z, 		0], 
					[0, 		0, 		0, 			1]]
		
		# Faz a transformação linear
		return mtc.C_Matrix.mul(t_scale_xyz, T_M)
		
	def translateXYZ(self, T_M, position_x=0.0, position_y=0.0, position_z=0.0):
		'''
			Matrix de posição (Eixo XYZ)
			T(x, y, z, w) M(4,4) * M(4,1) -> R^4
			
			T_z(x, y, z, w) = (x - position_x, y - position_y, z - position_z, 0)
			
			
						| 1				0				0		-position_x |
			T(x, y, z, w) = 	| 0				1				0		-position_y | 	* 	T
						| 0				0				1		-position_z |
						| 0				0				0 		1 		 |
						
						
			Entrada (Input): Classe C_Ponto e as posições x, y e z
			Saída (Output): Classe Point
		'''
		
		# A matrix de posicionamento X, Y e Z é uma matrix de 4 linhas e 4 colunas
		t_position_xyz = [	[1, 		0, 		0, 		position_x], 
						[0, 		1, 		0, 		position_y], 
						[0, 		0,		1, 		position_z], 
						[0, 		0, 		0, 		1]]
		
		# Faz a transformação linear
		return mtc.C_Matrix.mul(t_position_xyz, T_M)
		
	def perspectiveProjection(self, T_M, t_point):
		'''
			Matrix de projeção Perspectiva
			T(x, y, z, w) M(4,4) * M(4,1) -> R^4
			
			T_z(x, y, z, w) = (x, y, z, 0)
			
			
						| d				0				0									0 	|		|	x	|
			T(x, y, z, w) = 	| 0				d				0									0 	| 	* 	|	y	|
						| 0				0				(-2 / (far - near))						0 	|		|	z	|
						| 0				0				0					-(far + near) / (far - near)  |		|	1	|
						
						
			Entrada (Input): Classe C_Ponto e as posições x, y e z
			Saída (Output): Classe Point
		'''
		
		r_3_3 = (-2 / (global_var.far - global_var.near))
		r_3_4 = -(global_var.far + global_var.near) / (global_var.far - global_var.near)  
		
		# A matrix de posicionamento X, Y e Z é uma matrix de 4 linhas e 4 colunas
		t_projection = [		[self.S, 		0, 		0, 		0], 
						[0, 		self.S, 		0, 		0], 
						[0, 		0,			r_3_3, 	r_3_4], 
						[0, 		0, 			-1, 		1]	]
		
						
		# Faz a transformação linear da projeção perspectiva
		T_AFTER = mtc.C_Matrix.mul(mtc.C_Matrix.mul(t_projection, T_M), t_point.m_original_point)
		
		return point.C_Point((T_AFTER[0][0] / T_AFTER[2][0])*global_var.factor, (T_AFTER[1][0] / T_AFTER[2][0])*global_var.factor, T_AFTER[2][0])
		