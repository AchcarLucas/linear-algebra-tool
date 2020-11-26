'''
	M√≥dulo Main
'''
import global_var

import pygame
import pygame.freetype

import draw
import update
import ui_status
import ui

# Carrega as locals keys
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initializa as inst√¢ncias das classes que ser√£o importantes na utiliza√ß√£o do sistema
c_status = ui_status.UIStatus()
c_draw = draw.C_Draw()
c_update = update.C_Update()
g_ui = ui.GeneralUI(c_draw, c_update, c_status)

def initGame():
	'''
		FunÁ„o respons·vel por inicializar as inst‚ncias de todos os objetos que ser„o utilizados
		ao logo do software
		Args:
			None
		Return:
			None
	'''
	pygame.init()
	
	# Envia as inst√¢ncias nas classes que ser√£o utilizadas
	
	c_draw.pygame = pygame
	c_draw.g_ui = g_ui
	c_draw.c_status = c_status
	
	c_update.pygame = pygame
	c_update.g_ui = g_ui
	c_update.c_draw = c_draw
	c_update.c_status = c_status
	
	c_draw.screen = pygame.display.set_mode((c_draw.SCREEN_WIDTH, c_draw.SCREEN_HEIGHT))
	
	pygame.display.set_caption("Ferramenta Visual - √Ålgebra Linear")
	
	pygame.font.init() 
	global_var.myfont = pygame.font.SysFont('Arial', 9) 
	
	# Initializa Clock Update
	
	c_update.initClock()
	
	# Initializa o User Interface
	g_ui.initUI()
	g_ui.createUI()
	
def gameLoop():
	'''
		FunÁ„o principal que ficar· em loop atÈ o programa ser fechado
		Args:
			None
		Return:
			None
	'''
	running = True
	
	# Loop Principal
	while running:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
			elif event.type == QUIT:
				running = False
			
			global_var.rel_mouse = pygame.mouse.get_rel()
			global_var.pos_mouse = pygame.mouse.get_pos()
			
			if pygame.mouse.get_pressed()[1]:
				global_var.cam[2] -= global_var.rel_mouse[0]
				global_var.cam[0] -= global_var.rel_mouse[1]
				
			g_ui.eventUI(event)
			
				
		# Atualiza as a√ß√µes
		c_update.gameUpdate()
		
		# Desenha na tela
		c_draw.gameDraw()

				
def __main__():
	initGame()
	gameLoop()

__main__()