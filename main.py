'''
	Módulo Main
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

# Initializa as instâncias das classes que serão importantes na utilização do sistema
c_status = ui_status.UIStatus()
c_draw = draw.C_Draw()
c_update = update.C_Update()
g_ui = ui.GeneralUI(c_draw, c_update, c_status)

def initGame():
	'''
		Função responsável por inicializar as instâncias de todos os objetos que serem utilizados
		ao logo do software
		Args:
			None
		Return:
			None
	'''
	pygame.init()
	
	# Envia as instâncias nas classes que serão utilizadas
	
	c_draw.pygame = pygame
	c_draw.g_ui = g_ui
	c_draw.c_status = c_status
	
	c_update.pygame = pygame
	c_update.g_ui = g_ui
	c_update.c_draw = c_draw
	c_update.c_status = c_status
	
	c_draw.screen = pygame.display.set_mode((c_draw.SCREEN_WIDTH, c_draw.SCREEN_HEIGHT))
	
	pygame.display.set_caption("Ferramenta Visual - Álgebra Linear")
	
	pygame.font.init() 
	global_var.myfont = pygame.font.SysFont('Arial', 9) 
	
	# Initializa Clock Update
	
	c_update.initClock()
	
	# Initializa o User Interface
	g_ui.initUI()
	g_ui.createUI()
	
def gameLoop():
	'''
		Função principal que ficará em loop até o programa ser fechado
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
			
				
		# Atualiza as ações
		c_update.gameUpdate()
		
		# Desenha na tela
		c_draw.gameDraw()

				
def __main__():
	initGame()
	gameLoop()

__main__()