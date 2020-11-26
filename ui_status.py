'''
	Módulo UI STATUS
'''

'''
	Essa classe é criada globalmente e salva todos as variáveis de status da UI
'''

class UIStatus:
	def __init__(self):
	    self.automatic_rotate = False
	    self.text_point_list = []
	    self.text_obj_list = []
	    self.obj_selected = []
	    self.text_point_list_transform = []
	    self.vText = True