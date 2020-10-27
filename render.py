import numpy as np
import linear_transform
import matrices

import point
import line
import vector

AXES_X_A = point.C_Point(1.0, 0.0, 0.0)
AXES_X_B = point.C_Point(-1.0, 0.0, 0.0)

AXES_Y_A = point.C_Point(0.0, 1.0, 0.0)
AXES_Y_B = point.C_Point(0.0, -1.0, 0.0)

AXES_Z_A = point.C_Point(0.0, 0.0, 1.0)
AXES_Z_B = point.C_Point(0.0, 0.0, -1.0)

AXES_X = line.C_Line(AXES_X_A, AXES_X_B, (255, 0, 0))
AXES_Y = line.C_Line(AXES_Y_A, AXES_Y_B, (0, 255, 0))
AXES_Z = line.C_Line(AXES_Z_A, AXES_Z_B, (0, 0, 255))

A = point.C_Point(1.0, 1.0, 1.0, (0, 0, 0))
B = point.C_Point(1.0, -1.0, 1.0, (0, 0, 0))
C = point.C_Point(-1.0, -1.0, 1.0, (0, 0, 0))
D = point.C_Point(-1.0, 1.0, 1.0, (0, 0, 0))

E = point.C_Point(1.0, 1.0, -1.0, (0, 0, 0))
F = point.C_Point(1.0, -1.0, -1.0, (0, 0, 0))
G = point.C_Point(-1.0, -1.0, -1.0, (0, 0, 0))
H = point.C_Point(-1.0, 1.0, -1.0, (0, 0, 0))

a = line.C_Line(A, B)
b = line.C_Line(B, C)
c = line.C_Line(C, D)
d = line.C_Line(D, A)

e = line.C_Line(E, F)
f = line.C_Line(F, G)
g = line.C_Line(G, H)
h = line.C_Line(H, E)
		
i = line.C_Line(A, E)
j = line.C_Line(B, F)
k = line.C_Line(C, G)
l = line.C_Line(D, H)

v1 = vector.C_Vector(AXES_X_A, AXES_X_B, (255, 0, 0))
v2 = vector.C_Vector(AXES_Y_A, AXES_Y_B, (0, 255, 0))
v3 = vector.C_Vector(AXES_Z_A, AXES_Z_B, (0, 0, 255))

class C_Render:
	def __init__(self, c_draw):
		self.c_draw = c_draw
		self.test = 0
	
	def render(self):
		
		self.test += 0.1 
		
		# Desenha as linhas de guia (Axes)
		
		v1.setScale([2.5, 2.5, 2.5])
		v2.setScale([2.5, 2.5, 2.5])
		v3.setScale([2.5, 2.5, 2.5])
		
		#AXES_X.setScale([3, 3, 3])
		#AXES_Y.setScale([3, 3, 3])
		#AXES_Z.setScale([3, 3, 3])
		
		v1.setRotate([self.test, 1, self.test])
		v2.setRotate([self.test, 1, self.test])
		v3.setRotate([self.test, 1, self.test])
		
		#AXES_X.renderLine(self.c_draw)
		#AXES_Y.renderLine(self.c_draw)
		#AXES_Z.renderLine(self.c_draw)
		
		a.setRotate([self.test, 0, self.test])
		b.setRotate([self.test, 0, self.test])
		c.setRotate([self.test, 0, self.test])
		d.setRotate([self.test, 0, self.test])
		
		e.setRotate([self.test, 0, self.test])
		f.setRotate([self.test, 0, self.test])
		g.setRotate([self.test, 0, self.test])
		h.setRotate([self.test, 0, self.test])
		
		i.setRotate([self.test, 0, self.test])
		j.setRotate([self.test, 0, self.test])
		k.setRotate([self.test, 0, self.test])
		l.setRotate([self.test, 0, self.test])
		
		a.renderLine(self.c_draw)
		b.renderLine(self.c_draw)
		c.renderLine(self.c_draw)
		d.renderLine(self.c_draw)
		
		e.renderLine(self.c_draw)
		f.renderLine(self.c_draw)
		g.renderLine(self.c_draw)
		h.renderLine(self.c_draw)
		
		i.renderLine(self.c_draw)
		j.renderLine(self.c_draw)
		k.renderLine(self.c_draw)
		l.renderLine(self.c_draw)
		
		v1.renderLine(self.c_draw)
		v2.renderLine(self.c_draw)
		v3.renderLine(self.c_draw)