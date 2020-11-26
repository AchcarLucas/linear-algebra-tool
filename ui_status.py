'''
	Módulo UI STATUS
'''

'''
	Essa classe é criada globalmente e salva todos as variáveis de status da UI
'''

class UIStatus:
	def __init__(self):
		'''
			Fun��o construct (Inicia todas as vari�veis necess�rias para a utiliza��o da classe UIStatus)
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