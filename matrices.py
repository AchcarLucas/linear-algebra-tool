'''
	Módulo Matrices
	C_Matrix é a classe responsável pela manipulação das matrizes
'''


class C_Matrix:
	'''
		Função que multiplica duas matrizes quadradas de ordem N enviadas por parâmetros
	'''
	def mul(m1, m2):
		'''
			Função que multiplica duas matrizes quadradas de ordem N enviadas por parâmetros
			
			Entrada (Input): m1: M(n, n), m2: M(n, n)
			Saída (Output): m: M(n, n)
		'''
		result = []

		for i in range(len(m1)):
			result.append([])
			for j in range(0, len(m2[0])):
				sum = 0
				for k in range(0, len(m1[0])):
					sum += m1[i][k] * m2[k][j]
				result[i].append(sum)
		return result
	
	def identity(n):
		'''
			Função que cria uma matriz identidade quadrada de ordem N
			
			Entrada (Input): inteiro
			Saída (Output): M(n, n) (i == j = 1) e (i != j = 0)
		'''
		
		result = []
		
		for i in range(n):
			result.append([])
			for j in range(n):
				if(i == j):
					result[i].append(1)
				else:
					result[i].append(0)
		return result