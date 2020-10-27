'''
	Módulo Update
'''

# Classe principal Update
class C_Update:
	def __init__(self):
		self.pygame = None
		self.g_ui = None
		
		self.time_delta = 0.0
		
		
	def initClock(self):
		self.clock = self.pygame.time.Clock()
		
	def gameUpdate(self):
		self.time_delta = self.clock.tick(1000) / 1000.0
		
		self.clock
		
		self.g_ui.fps_counter.set_text(f'FPS: {self.clock.get_fps():.2f}')
		
		self.g_ui.updateUI()