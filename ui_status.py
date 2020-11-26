'''
	MÃ³dulo UI STATUS
'''

'''
	Essa classe Ã© criada globalmente e salva todos as variÃ¡veis de status da UI
'''

class UIStatus:
	def __init__(self):
		'''
			Função construct (Inicia todas as variáveis necessárias para a utilização da classe UIStatus)
			Args:
				None
			Return:
				None
		'''
	    self.automatic_rotate = False
	    self.text_point_list = []
	    self.text_obj_list = []
	    self.obj_selected = []
	    self.vText = False
	    
	    self.transform_list_text = []
	    self.transform_list = None