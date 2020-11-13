from enum import Enum

# Variáveis Globais
factor=100.
far=20. 
near=0.3
angleOfView = 90.0
cam = [270.0, 0.0, 0,0]
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