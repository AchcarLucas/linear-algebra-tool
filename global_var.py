'''
	Módulo Global 
	Módulo responsável por salvar todas as variáveis de status para uso de todos os outros módulos sem nenhuma restrição
'''

from enum import Enum

from random import seed
from random import random

seed(1)

# Vari�veis Globais
factor=100.
far=100. 
near=1.0
angleOfView = 90.0
cam = [45.0, 0.0, 135,0]
rel_mouse = [0.0, 0.0]
pos_mouse = [0.0, 0.0]
myfont = None

# Enum contendo os erros de retorno
class RTN(Enum):
	NAME_ALREADY = 3
	CMD_FAILED = 2
	SUCCESS_POINT = 8
	SUCCESS_LINE = 7
	SUCCESS_VECTOR = 1
	INVALID_CMD = 4
	ERROR_CMD = 5
	POINT_DOES_EXIST = 6
	POINT_IS_USED = 9
	POINT_REMOVED = 10
	LINE_REMOVED=11
	VECTOR_REMOVED=12