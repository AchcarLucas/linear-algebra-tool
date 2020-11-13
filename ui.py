'''
	Módulo User Interface
'''

import numpy as np

import global_var
import pygame_gui

from collections import deque

from pygame_gui import UIManager, PackageResource

from pygame_gui.elements import UIWindow
from pygame_gui.elements import UIButton
from pygame_gui.elements import UIHorizontalSlider
from pygame_gui.elements import UITextEntryLine
from pygame_gui.elements import UIDropDownMenu
from pygame_gui.elements import UIScreenSpaceHealthBar
from pygame_gui.elements import UILabel
from pygame_gui.elements import UIImage
from pygame_gui.elements import UIPanel
from pygame_gui.elements import UISelectionList

from pygame_gui.windows import UIMessageWindow

class Options:
    def __init__(self, width, height):
        self.resolution = (width, height)
        self.fullscreen = False

class UIMessageWindow(UIWindow):
	def __init__(self, rect, ui_manager, c_draw, c_update, c_status, options, title, message):
		super().__init__(	rect, 
						ui_manager,
						window_display_title=title,
						object_id='#ui_message_window',
						resizable=False)
						
		self.c_draw = c_draw
		self.c_update = c_update
		self.c_status = c_status
		
		self.options = Options(c_draw.SCREEN_WIDTH, c_draw.SCREEN_HEIGHT)
		
			
		# Label Message
		self.label = UILabel(c_draw.pygame.Rect(
												(20, 10),
												(450, 20)),
							message,
							self.ui_manager,
							object_id='#label_message',
							container=self)
			
	def update(self, time_delta):
		super().update(time_delta)
		
	def event(self, event):
		return True
		
class UIScaleWindow(UIWindow):
	def __init__(self, rect, ui_manager, c_draw, c_update, c_status, options):
		super().__init__(	rect, 
						ui_manager,
						window_display_title='Ferramenta - Escala',
						object_id='#ui_scale_window',
						resizable=False)
						
		self.c_draw = c_draw
		self.c_update = c_update
		self.c_status = c_status
		
		self.options = Options(c_draw.SCREEN_WIDTH, c_draw.SCREEN_HEIGHT)
		
		
		y = 5
		
		'''
			Escala Eixo X
		'''
		
		# Label Eixo X
		self.x_scale_label = UILabel(c_draw.pygame.Rect(
												(5, y),
												(60, 30)),
							"Eixo X: ",
							self.ui_manager,
							object_id='#label_x_scale',
							container=self)
							
							
		# Cria a caixa de dialogo para digitar a escala X
		self.x_entry_scale = UITextEntryLine(c_draw.pygame.Rect(
												(70, y),
												(190, -1)),
									self.ui_manager,
									object_id='#x_entry_scale',
									container=self)
									
		self.x_entry_scale.set_text('1.0')
									
									
		y += 30
										
		# Cria o botão para resetar os valores adicionados
		self.clear_axes_x_scale_button = UIButton(
								c_draw.pygame.Rect(
												(45, y),
												(200, 25)),
								'Resetar',
								self.ui_manager,
								object_id='#reset_axes_scale_x_clear',
								container=self)
		y += 45
								
		'''
			Escala Eixo Y
		'''
		
		# Label Eixo Y
		self.y_scale_label = UILabel(c_draw.pygame.Rect(
												(5, y),
												(60, 30)),
							"Eixo Y: ",
							self.ui_manager,
							object_id='#label_y_scale',
							container=self)
							
							
		# Cria a caixa de dialogo para digitar a escala Y
		self.y_entry_scale = UITextEntryLine(c_draw.pygame.Rect(
												(70, y),
												(190, -1)),
									self.ui_manager,
									object_id='#x_entry_scale',
									container=self)
									
		self.y_entry_scale.set_text('1.0')
									
									
		y += 30
											

		# Cria o botão para resetar os valores adicionados
		self.clear_axes_y_scale_button = UIButton(
								c_draw.pygame.Rect(
												(45, y),
												(200, 25)),
								'Resetar',
								self.ui_manager,
								object_id='#reset_axes_scale_y_clear',
								container=self)
		
		y += 45
								
		'''
			Escala Eixo Z
		'''
		
		# Label Eixo Z
		self.z_scale_label = UILabel(c_draw.pygame.Rect(
												(5, y),
												(60, 30)),
							"Eixo Z: ",
							self.ui_manager,
							object_id='#label_z_scale',
							container=self)
							
							
		# Cria a caixa de dialogo para digitar a translação Z
		self.z_entry_scale = UITextEntryLine(c_draw.pygame.Rect(
												(70, y),
												(190, -1)),
									self.ui_manager,
									object_id='#z_entry_scale',
									container=self)
									
		self.z_entry_scale.set_text('1.0')
									
									
		y += 30
											
		# Cria o botão para resetar os valores adicionados
		self.clear_axes_z_scale_button = UIButton(
								c_draw.pygame.Rect(
												(45, y),
												(200, 25)),
								'Resetar',
								self.ui_manager,
								object_id='#reset_axes_scale_z_clear',
								container=self)
		
		y += 30
		
				# Cria o botão para aplicar a escala no eixo Z
		self.apply_axes_scale_button = UIButton(
								c_draw.pygame.Rect(
												(45, y),
												(200, 25)),
								'Aplicar',
								self.ui_manager,
								object_id='#apply_axes_scale_z_button',
								container=self)
						
	def update(self, time_delta):
		super().update(time_delta)
		
	def event(self, event):
		if event.type == self.c_draw.pygame.USEREVENT:
			if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

				if event.ui_element == self.clear_axes_x_scale_button:
					self.x_entry_scale.set_text('1.0')
				if event.ui_element == self.clear_axes_y_scale_button:
					self.y_entry_scale.set_text('1.0')
				if event.ui_element == self.clear_axes_z_scale_button:
					self.z_entry_scale.set_text('1.0')
					
				if event.ui_element == self.apply_axes_scale_button:
					self.applyScale()
					
	def applyScale(self):
		t_x = float(self.x_entry_scale.get_text())
		t_y = float(self.y_entry_scale.get_text())
		t_z = float(self.z_entry_scale.get_text())
		
		self.c_update.setScaleSelected(self.c_status.obj_selected, [t_x, t_y, t_z])
		
class UITranslateWindow(UIWindow):
	def __init__(self, rect, ui_manager, c_draw, c_update, c_status, options):
		super().__init__(	rect, 
						ui_manager,
						window_display_title='Ferramenta - Translação',
						object_id='#ui_translate_window',
						resizable=False)
						
		self.c_draw = c_draw
		self.c_update = c_update
		self.c_status = c_status
		
		self.options = Options(c_draw.SCREEN_WIDTH, c_draw.SCREEN_HEIGHT)
		
		y = 5
		
		'''
			Translação Eixo X
		'''
		
		# Label Eixo X
		self.x_translate_label = UILabel(c_draw.pygame.Rect(
												(5, y),
												(60, 30)),
							"Eixo X: ",
							self.ui_manager,
							object_id='#label_x_translate',
							container=self)
							
							
		# Cria a caixa de dialogo para digitar a translação X
		self.x_entry_translate = UITextEntryLine(c_draw.pygame.Rect(
												(70, y),
												(190, -1)),
									self.ui_manager,
									object_id='#x_entry_translate',
									container=self)
									
		self.x_entry_translate.set_text('0.0')
									
									
		y += 30
											
		
		# Cria o botão para resetar os valores adicionados
		self.clear_axes_x_trans_button = UIButton(
								c_draw.pygame.Rect(
												(45, y),
												(200, 25)),
								'Resetar',
								self.ui_manager,
								object_id='#reset_axes_trans_x_clear',
								container=self)
		y += 45
								
		'''
			Translação Eixo Y
		'''
		
		# Label Eixo X
		self.y_translate_label = UILabel(c_draw.pygame.Rect(
												(5, y),
												(60, 30)),
							"Eixo Y: ",
							self.ui_manager,
							object_id='#label_y_translate',
							container=self)
							
							
		# Cria a caixa de dialogo para digitar a translação Y
		self.y_entry_translate = UITextEntryLine(c_draw.pygame.Rect(
												(70, y),
												(190, -1)),
									self.ui_manager,
									object_id='#x_entry_translate',
									container=self)
									
		self.y_entry_translate.set_text('0.0')
									
									
		y += 30

		# Cria o botão para resetar os valores adicionados
		self.clear_axes_y_trans_button = UIButton(
								c_draw.pygame.Rect(
												(45, y),
												(200, 25)),
								'Resetar',
								self.ui_manager,
								object_id='#reset_axes_trans_y_clear',
								container=self)
		
		y += 45
								
		'''
			Translação Eixo Z
		'''
		
		# Label Eixo Z
		self.z_translate_label = UILabel(c_draw.pygame.Rect(
												(5, y),
												(60, 30)),
							"Eixo Z: ",
							self.ui_manager,
							object_id='#label_z_translate',
							container=self)
							
							
		# Cria a caixa de dialogo para digitar a translação Z
		self.z_entry_translate = UITextEntryLine(c_draw.pygame.Rect(
												(70, y),
												(190, -1)),
									self.ui_manager,
									object_id='#z_entry_translate',
									container=self)
									
		self.z_entry_translate.set_text('0.0')
									
									
		y += 30
												
		# Cria o botão para resetar os valores adicionados
		self.clear_axes_z_trans_button = UIButton(
								c_draw.pygame.Rect(
												(45, y),
												(200, 25)),
								'Resetar',
								self.ui_manager,
								object_id='#reset_axes_trans_z_clear',
								container=self)
						
		y += 30
		
		# Cria o botão para aplicar a translação no eixo Z
		self.apply_axes_trans_button = UIButton(
								c_draw.pygame.Rect(
												(45, y),
												(200, 25)),
								'Aplicar',
								self.ui_manager,
								object_id='#apply_axes_trans_z_button',
								container=self)
						
	def update(self, time_delta):
		super().update(time_delta)
		
	def event(self, event):
		if event.type == self.c_draw.pygame.USEREVENT:
			if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

				if event.ui_element == self.clear_axes_x_trans_button:
					self.x_entry_translate.set_text('0.0')
				if event.ui_element == self.clear_axes_y_trans_button:
					self.y_entry_translate.set_text('0.0')
				if event.ui_element == self.clear_axes_z_trans_button:
					self.z_entry_translate.set_text('0.0')
					
				if event.ui_element == self.apply_axes_trans_button:
					self.applyTranslate()
					
	def applyTranslate(self):
		t_x = float(self.x_entry_translate.get_text())
		t_y = float(self.y_entry_translate.get_text())
		t_z = float(self.z_entry_translate.get_text())
		
		self.c_update.setTranslateSelected(self.c_status.obj_selected, [t_x, t_y, t_z])
		
class UIRotateWindow(UIWindow):
	def __init__(self, rect, ui_manager, c_draw, c_update, c_status, options):
		super().__init__(	rect, 
						ui_manager,
						window_display_title='Ferramenta - Rotação',
						object_id='#ui_rotate_window',
						resizable=False)
						
		self.c_draw = c_draw
		self.c_update = c_update
		self.c_status = c_status
		
		self.options = Options(c_draw.SCREEN_WIDTH, c_draw.SCREEN_HEIGHT)
		
		self.UIListRotateX = []
		self.UIListRotateX
		
		y = 5
		
		'''
			Rotação Eixo X
		'''
		
		# Cria a label (Rotação - Eixo X)
		self.label_x_axes = UILabel(c_draw.pygame.Rect(
												(45, y),
												(170, 25)),
							"Rotação - Eixo X",
							self.ui_manager,
							object_id='#label_x_axes',
							container=self)
		y += 25
		
		# Slider para a rotação no eixo X
		self.angle_x_slider = UIHorizontalSlider(
									c_draw.pygame.Rect(
													(38, y),
													(190, 25)),
									50.0,
									(0.0, 100.0),
									self.ui_manager,
									object_id='#angle_x_slider',
									container=self)
			
		# Label (- 2PI)
		self.label_plus_pi_x = UILabel(c_draw.pygame.Rect(
												(0, y),
												(30, 25)),
							" - 2\u03C0",
							self.ui_manager,
							object_id='#label_x_axes',
							container=self)
							
		
		# Label (+ 2PI)
		self.label_minus_pi_x = UILabel(c_draw.pygame.Rect(
												(230, y),
												(30, 25)),
							" + 2\u03C0",
							self.ui_manager,
							object_id='#label_x_axes',
							container=self)
							
				

		y += 25
							
		# Label º (Graus)
		self.x_angle_label = UILabel(c_draw.pygame.Rect(
												(5, y),
												(60, 30)),
							"Graus (º): ",
							self.ui_manager,
							object_id='#label_x_angle',
							container=self)
							
							
		# Cria a caixa de entrada para o ângulo do eixo X
		self.x_angle_entry = UITextEntryLine(c_draw.pygame.Rect(
												(70, y),
												(190, -1)),
									self.ui_manager,
									object_id='#entry_x_angle',
									container=self)
									
		self.x_angle_entry.set_text('0.0')
		self.x_angle_entry.disable()
							
							
		y += 30
				
		
		# Cria o botão para resetar os valores adicionados
		self.clear_axes_x_rotate_button = UIButton(
								c_draw.pygame.Rect(
												(45, y),
												(200, 25)),
								'Resetar',
								self.ui_manager,
								object_id='#reset_axes_x_rotate_clear',
								container=self)
								
		
				
		y += 40
		
		self.UIListRotateX.append(self.label_x_axes)
		self.UIListRotateX.append(self.angle_x_slider)
		self.UIListRotateX.append(self.label_minus_pi_x)
		self.UIListRotateX.append(self.label_plus_pi_x)
		self.UIListRotateX.append(self.x_angle_label)
		self.UIListRotateX.append(self.clear_axes_x_rotate_button)
												
		'''
			Rotação Eixo Y
		'''
		
		# Cria a label (Rotação - Eixo Y)
		self.label_y_axes = UILabel(c_draw.pygame.Rect(
												(45, y),
												(170, 25)),
							"Rotação - Eixo Y",
							self.ui_manager,
							object_id='#label_y_axes',
							container=self)
		
		y += 25
		
		# Slider para a rotação no eixo Y
		self.angle_y_slider = UIHorizontalSlider(
									c_draw.pygame.Rect(
													(38, y),
													(190, 25)),
									50.0,
									(0.0, 100.0),
									self.ui_manager,
									object_id='#angle_y_slider',
									container=self)
									
									
		# Label (- 2PI)
		self.label_plus_pi_y = UILabel(c_draw.pygame.Rect(
												(0, y),
												(30, 25)),
							" - 2\u03C0",
							self.ui_manager,
							object_id='#label_y_axes',
							container=self)
							
		# Label (+ 2PI)
		self.label_minus_pi_y = UILabel(c_draw.pygame.Rect(
												(230, y),
												(30, 25)),
							" + 2\u03C0",
							self.ui_manager,
							object_id='#label_y_axes',
							container=self)
				

		y += 25
							
		# Label º (Graus)
		self.y_angle_label = UILabel(c_draw.pygame.Rect(
												(5, y),
												(60, 30)),
							"Graus (º): ",
							self.ui_manager,
							object_id='#label_y_angle',
							container=self)
							
							
		# Cria a caixa de entrada para o ângulo do eixo Y
		self.y_angle_entry = UITextEntryLine(c_draw.pygame.Rect(
												(70, y),
												(190, -1)),
									self.ui_manager,
									object_id='#entry_y_angle',
									container=self)
									
		self.y_angle_entry.set_text('0.0')
		self.y_angle_entry.disable()
							
							
		y += 30

		
		# Cria o botão para resetar os valores adicionados
		self.clear_axes_y_rotate_button = UIButton(
								c_draw.pygame.Rect(
												(45, y),
												(200, 25)),
								'Resetar',
								self.ui_manager,
								object_id='#reset_axes_y_rotate_clear',
								container=self)
						
		y += 40
			
		self.UIListRotateX.append(self.label_y_axes)
		self.UIListRotateX.append(self.angle_y_slider)
		self.UIListRotateX.append(self.label_minus_pi_y)
		self.UIListRotateX.append(self.label_plus_pi_y)
		self.UIListRotateX.append(self.y_angle_label)
		self.UIListRotateX.append(self.clear_axes_y_rotate_button)
												
		'''
			Rotação Eixo Z
		'''
		
		# Cria a label (Rotação - Eixo Z)
		self.label_z_axes = UILabel(c_draw.pygame.Rect(
												(45, y),
												(170, 25)),
							"Rotação - Eixo Z",
							self.ui_manager,
							object_id='#label_z_axes',
							container=self)
		
		y += 25
		
		# Slider para a rotação no eixo Z
		self.angle_z_slider = UIHorizontalSlider(
									c_draw.pygame.Rect(
													(38, y),
													(190, 25)),
									50.0,
									(0.0, 100.0),
									self.ui_manager,
									object_id='#angle_z_slider',
									container=self)
									
									
		# Label (- 2PI)
		self.label_plus_pi_z = UILabel(c_draw.pygame.Rect(
												(0, y),
												(30, 25)),
							" - 2\u03C0",
							self.ui_manager,
							object_id='#label_z_axes',
							container=self)
							
		# Label (+ 2PI)
		self.label_minus_pi_z = UILabel(c_draw.pygame.Rect(
												(230, y),
												(30, 25)),
							" + 2\u03C0",
							self.ui_manager,
							object_id='#label_z_axes',
							container=self)
				

		y += 25
							
		# Label º (Graus)
		self.z_angle_label = UILabel(c_draw.pygame.Rect(
												(5, y),
												(60, 30)),
							"Graus (º): ",
							self.ui_manager,
							object_id='#label_z_angle',
							container=self)
							
							
		# Cria a caixa de entrada para o ângulo do eixo Z
		self.z_angle_entry = UITextEntryLine(c_draw.pygame.Rect(
												(70, y),
												(190, -1)),
									self.ui_manager,
									object_id='#entry_z_angle',
									container=self)
														
		self.z_angle_entry.set_text('0.0')
		self.z_angle_entry.disable()
							
							
		y += 30

		# Cria o botão para resetar os valores adicionados
		self.clear_axes_z_rotate_button = UIButton(
								c_draw.pygame.Rect(
												(45, y),
												(200, 25)),
								'Resetar',
								self.ui_manager,
								object_id='#reset_axes_z_rotate_clear',
								container=self)
		
		y += 50

		self.UIListRotateX.append(self.label_z_axes)
		self.UIListRotateX.append(self.angle_z_slider)
		self.UIListRotateX.append(self.label_minus_pi_z)
		self.UIListRotateX.append(self.label_plus_pi_z)
		self.UIListRotateX.append(self.z_angle_label)
		self.UIListRotateX.append(self.clear_axes_z_rotate_button)

		'''
			Random Rotate
		'''
		
		# Cria o botão para aplicar a rotação randomica (Inativo)
		self.random_rotate_button_actived = UIButton(
								c_draw.pygame.Rect(
												(10, y),
												(250, 25)),
								'Rotação Randômica (Desativo)',
								self.ui_manager,
								object_id='#random_rotate_button_inactived',
								container=self)
								
		# Cria o botão para aplicar a rotação randomica (Ativo)
		self.random_rotate_button_inactived = UIButton(
								c_draw.pygame.Rect(
												(10, y),
												(250, 25)),
								'Rotação Randômica (Ativado)',
								self.ui_manager,
								object_id='#random_rotate_button_actived',
								container=self)
											
		self.statusAutomaticRotate(c_status.automatic_rotate)
		self.applyRotate()
											
	def update(self, time_delta):
		super().update(time_delta)
		
	def event(self, event):
		if event.type == self.c_draw.pygame.USEREVENT:
			if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
				if event.ui_element == self.random_rotate_button_actived:
					self.statusAutomaticRotate(True)
				if event.ui_element == self.random_rotate_button_inactived:
					self.statusAutomaticRotate(False)
				
				if event.ui_element == self.clear_axes_x_rotate_button:
					self.angle_x_slider.set_current_value(50.0)
					self.x_angle_entry.set_text('0.0')
				if event.ui_element == self.clear_axes_y_rotate_button:
					self.angle_y_slider.set_current_value(50.0)
					self.y_angle_entry.set_text('0.0')
				if event.ui_element == self.clear_axes_z_rotate_button:
					self.angle_z_slider.set_current_value(50.0)
					self.z_angle_entry.set_text('0.0')
					
				if event.ui_element == self.clear_axes_x_rotate_button or event.ui_element == self.clear_axes_y_rotate_button or event.ui_element == self.clear_axes_z_rotate_button:
					self.applyRotate()

			if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
				if event.ui_element == self.angle_x_slider:
					angle_x = self.mapFromTo(float(self.angle_x_slider.get_current_value()), 0.0, 100.0, -360.0, 360.0)
					self.x_angle_entry.set_text(f'{angle_x:0.1f}')
					self.applyRotate()
				if event.ui_element == self.angle_y_slider:
					angle_y = self.mapFromTo(float(self.angle_y_slider.get_current_value()), 0.0, 100.0, -360.0, 360.0)
					self.y_angle_entry.set_text(f'{angle_y:0.1f}')
					self.applyRotate()
				if event.ui_element == self.angle_z_slider:
					angle_z = self.mapFromTo(float(self.angle_z_slider.get_current_value()), 0.0, 100.0, -360.0, 360.0)
					self.z_angle_entry.set_text(f'{angle_z:0.1f}')
					self.applyRotate()
			
	def mapFromTo(self, x,a,b,c,d):
		y=(x-a)/(b-a)*(d-c)+c
		return y
		
	def applyRotate(self):
		angle_x = self.mapFromTo(float(self.angle_x_slider.get_current_value()), 0.0, 100.0, -360.0, 360.0)
		angle_y = self.mapFromTo(float(self.angle_y_slider.get_current_value()), 0.0, 100.0, -360.0, 360.0)
		angle_z = self.mapFromTo(float(self.angle_z_slider.get_current_value()), 0.0, 100.0, -360.0, 360.0)
		
		self.c_update.setRotateSelected(self.c_status.obj_selected, [angle_x, angle_y, angle_z])
	
	def statusAutomaticRotate(self, status):
		if(status):
			self.random_rotate_button_inactived.show()
			self.random_rotate_button_actived.hide()
			
			# Quando o botão de random rotate estiver ativo, desabilita todos os outros
			for v in self.UIListRotateX:
				v.disable()
		else:	
			self.random_rotate_button_inactived.hide()
			self.random_rotate_button_actived.show()
			
			# Quando o botão de random rotate estiver desativado, desabilita todos os outros
			for v in self.UIListRotateX:
				v.enable()
				
		self.c_status.automatic_rotate = status
	
class UIToolbarWindow(UIWindow):
	def __init__(self, rect, ui_manager, c_draw, c_update, c_status, options):
		super().__init__(	rect, 
						ui_manager,
						window_display_title='Ferramentas',
						object_id='#ui_main_window',
						resizable=False)
		
		self.c_draw = c_draw
		self.c_update = c_update
		self.c_status = c_status
		
		self.options = Options(c_draw.SCREEN_WIDTH, c_draw.SCREEN_HEIGHT)
		
		self.ui_rotate_window = None
		self.ui_translate_window = None
		self.ui_scale_window = None
														
		y = 5
									
		# Cria o botão rotação
		self.rotate_button = UIButton(
								c_draw.pygame.Rect(
												(45, y),
												(130, 25)),
								'Rotação',
								self.ui_manager,
								object_id='#button_rotate',
		
								container=self)
						
		y += 30
		
		# Cria o botão translação
		self.translate_button = UIButton(
								c_draw.pygame.Rect(
												(45, y),
												(130, 25)),
								'Translação',
								self.ui_manager,
								object_id='#button_translate',
								container=self)
			
		y += 30
		
		# Cria o botão escala
		self.scale_button = UIButton(
								c_draw.pygame.Rect(
												(45, y),
												(130, 25)),
								'Escala',
								self.ui_manager,
								object_id='#button_scale',
								container=self)
		y += 30
		
		# Cria o botão resetar transformações lineares
		self.reset_button = UIButton(
								c_draw.pygame.Rect(
												(45, y),
												(130, 25)),
								'Resetar (T.L)',
								self.ui_manager,
								object_id='#button_reset',
								container=self)
		
		y += 30
		
		# Cria a label (Comando)
		self.fps_counter = UILabel(c_draw.pygame.Rect(
												(45, y),
												(130, 25)),
							"Comando",
							self.ui_manager,
							object_id='#label_cmd',
							container=self)
							
		y += 20
		
		# Cria a caixa de entrada para os comandos
		self.entry_cmd = UITextEntryLine(c_draw.pygame.Rect(
												(20, y),
												(180, -1)),
									self.ui_manager,
									object_id='#entry_cmd',
									container=self)
		y += 30
		
		# Cria o botão para enviar o comando (Pode ser enviado com a tecla enter)
		self.apply_button = UIButton(
								c_draw.pygame.Rect(
												(30, y),
												(80, 25)),
								'Aplicar',
								self.ui_manager,
								object_id='#button_apply',
								container=self)
		
		# Cria o botão para apagar todo o comando
		self.clear_button = UIButton(
								c_draw.pygame.Rect(
												(110, y),
												(80, 25)),
								'Limpar',
								self.ui_manager,
								object_id='#button_clear',
								container=self)
					

		y += 30
		
		# Cria a label 'Lista de Pontos'
		self.fps_counter = UILabel(c_draw.pygame.Rect(
												(45, y),
												(130, 25)),
							"Lista de Pontos",
							self.ui_manager,
							object_id='#label_point',
							container=self)
			
		y += 20
		point_list_height = 100
										
		# Cria a lista contendo todos os pontos
		self.point_list = UISelectionList(
								c_draw.pygame.Rect(
												(20, y),
												(180, point_list_height)),
								self.c_status.text_point_list,
								self.ui_manager,
								object_id='#select_list_point',
								allow_multi_select=False,
								allow_double_clicks=False,
								container=self)
		y += point_list_height + 10
		
		self.point_list.disable()
		
		# Cria a label 'Lista de Objetos'
		self.obj_list_label = UILabel(c_draw.pygame.Rect(
												(45, y),
												(130, 25)),
							"Lista de Objetos",
							self.ui_manager,
							object_id='#label_point',
							container=self)
			
		y += 20
		obj_list_height = 100
		
		# Cria a lista contendo vetores e linhas denominados objetos
		self.obj_list = UISelectionList(
								c_draw.pygame.Rect(
												(20, y),
												(180, obj_list_height)),
								self.c_status.text_obj_list,
								self.ui_manager,
								object_id='#select_list_obj',
								allow_multi_select=True,
								allow_double_clicks=False,
								container=self)	

		y += obj_list_height + 10
		
		# Cria o botão resetar transformações lineares
		self.load_file_point = UIButton(
								c_draw.pygame.Rect(
												(10, y),
												(200, 25)),
								'Importar Pontos/Objetos',
								self.ui_manager,
								object_id='#import_file',
								container=self)
		
		y += 30
		
		# Cria o botão resetar transformações lineares
		self.load_file_point = UIButton(
								c_draw.pygame.Rect(
												(10, y),
												(200, 25)),
								'Exportar Pontos/Objetos',
								self.ui_manager,
								object_id='#export_file',
								container=self)
								
		self.updateLists()
					
	def update(self, time_delta):
		super().update(time_delta)
		
	def event(self, event):
		if(self.ui_rotate_window is not None):
			self.ui_rotate_window.event(event)
			
		if(self.ui_translate_window is not None):
			self.ui_translate_window.event(event)
	
		if(self.ui_scale_window is not None):
			self.ui_scale_window.event(event)
		
		if event.type == self.c_draw.pygame.USEREVENT:
			if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
				if event.ui_element == self.rotate_button:
					self.ui_rotate_window = self.createRotateWindow()
				if event.ui_element == self.translate_button:
					self.ui_translate_window = self.createTranslateWindow()
				if event.ui_element == self.scale_button:
					self.ui_translate_window = self.createScaleWindow()
				if event.ui_element == self.apply_button:
					self.updateCommand()
					self.entry_cmd.set_text('')
					
			if(event.user_type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION):
				if event.ui_element == self.obj_list:
					self.c_status.obj_selected.clear()
					for v in  self.obj_list.get_multi_selection():
						a, b = v.replace(' ', '').split('=')
						self.c_status.obj_selected.append(a)
						
					print(self.c_status.obj_selected)
					
			if(event.user_type == pygame_gui.UI_SELECTION_LIST_DROPPED_SELECTION):
				if event.ui_element == self.obj_list:
					self.c_status.obj_selected.clear()
					for v in  self.obj_list.get_multi_selection():
						a, b = v.replace(' ', '').split('=')
						self.c_status.obj_selected.append(a)
						
					print(self.c_status.obj_selected)
					
			if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
				if event.ui_element == self.entry_cmd:
					self.updateCommand()
					self.entry_cmd.set_text('')
					
	
	def updateCommand(self):
		rtn, name = self.c_update.updateCommand(self.entry_cmd.get_text())
		if rtn == global_var.RTN.ERROR_CMD:
			self.createMessageWindow('Erro', 'O comando digitado não existe')
		elif rtn == global_var.RTN.INVALID_CMD:
			self.createMessageWindow('Erro', 'O comando digitado é inválido')
		elif rtn == global_var.RTN.POINT_DOES_EXIST:
			self.createMessageWindow('Erro', 'Um ou mais pontos não existem')
		elif rtn == global_var.RTN.NAME_ALREADY:
			self.createMessageWindow('Erro', 'O nome utilizado já está em uso')
		elif rtn == global_var.RTN.POINT_IS_USED:
			self.createMessageWindow('Erro [Remover Ponto]', 'O ponto está sendo usado')
		elif rtn == global_var.RTN.CMD_FAILED:
			self.createMessageWindow('Erro', 'Existem erros no comando digitado')
		elif 	((rtn == global_var.RTN.SUCCESS_POINT) or 
			(rtn == global_var.RTN.SUCCESS_VECTOR) or 
			(rtn == global_var.RTN.SUCCESS_LINE) or
			(rtn == global_var.RTN.LINE_REMOVED) or
			(rtn == global_var.RTN.VECTOR_REMOVED) or
			(rtn == global_var.RTN.POINT_REMOVED)):
			self.updateLists()
		
			
	def updateLists(self):
		self.c_status.text_obj_list.clear()
		for p in self.c_draw.point_list:
			self.c_status.text_obj_list.append((f'{p[1].name} = P({p[1].getOriginalScreenX():0.1f}, {p[1].getOriginalScreenY():0.1f}, {p[1].getOriginalScreenZ():0.1f})', p[1].name))
		
		self.point_list.set_item_list(self.c_status.text_obj_list)
		
		self.c_status.text_obj_list.clear()
		for p in self.c_draw.vector_list:
			self.c_status.text_obj_list.append((f'{p[1].name} = V({p[1].p_b.name}, {p[1].p_a.name})', p[1].name))
		
		for p in self.c_draw.line_list:
			self.c_status.text_obj_list.append((f'{p[1].name} = L({p[1].p_b.name}, {p[1].p_a.name})', p[1].name))
		
		self.obj_list.set_item_list(self.c_status.text_obj_list)
		
		
	
	def createRotateWindow(self):
		return UIRotateWindow(	self.c_draw.pygame.Rect((self.options.resolution[0]  / 2 - 150,  self.options.resolution[1]  / 2 - 150), 
								(300, 480)), 
								self.ui_manager, 
								self.c_draw, 
								self.c_update,
								self.c_status,
								self.options)
								
	def createTranslateWindow(self):
		return UITranslateWindow(	self.c_draw.pygame.Rect((self.options.resolution[0]  / 2 - 150,  self.options.resolution[1]  / 2 - 150), 
								(300, 320)), 
								self.ui_manager, 
								self.c_draw, 
								self.c_update,
								self.c_status,
								self.options)
								
	def createScaleWindow(self):
		return UIScaleWindow(	self.c_draw.pygame.Rect((self.options.resolution[0]  / 2 - 150,  self.options.resolution[1]  / 2 - 150), 
								(300, 320)), 
								self.ui_manager, 
								self.c_draw, 
								self.c_update,
								self.c_status,
								self.options)
								
	def createMessageWindow(self, title, message):
		return UIMessageWindow(	self.c_draw.pygame.Rect((self.options.resolution[0]  / 2 - 150,  self.options.resolution[1]  / 2 - 150), 
								(450, 30)), 
								self.ui_manager, 
								self.c_draw, 
								self.c_update,
								self.c_status,
								self.options,
								title,
								message)
								
# Classe Principal da Interface de Usuário
class GeneralUI:
	def __init__(self, c_draw, c_update, c_status):
		self.c_draw = c_draw
		self.c_update = c_update
		self.c_status = c_status
		
		self.options = Options(c_draw.SCREEN_WIDTH, c_draw.SCREEN_HEIGHT)
		
		self.fps_counter = None
		self.ui_toolbar_window = None
								
	def initUI(self):
		self.ui_manager = UIManager(	
								self.options.resolution, 
								PackageResource(package='data.themes', resource='theme_0.json')
								)
								
	def createToolbarWindow(self):
		return UIToolbarWindow(	self.c_draw.pygame.Rect((self.options.resolution[0] - 250,  0), 
								(250, 600)), 
								self.ui_manager, 
								self.c_draw, 
								self.c_update,
								self.c_status,
								self.options)
		
	def createUI(self):
		self.toolbar_window = self.createToolbarWindow()

		self.fps_counter = UILabel(self.c_draw.pygame.Rect(self.options.resolution[0] - 120,
							5,
							100,
							44),
							"FPS: 0",
							self.ui_manager,
							object_id='#fps_counter')
					
		self.button_toolbar = UIButton(
								self.c_draw.pygame.Rect(self.options.resolution[0] - 140,
													self.options.resolution[1] - 30,
													130,
													25),
								'Ferramentas',
								self.ui_manager,
								object_id='#ui_main_bar')
							
								
	def drawUI(self):
		self.ui_manager.draw_ui(self.c_draw.screen)

	def eventUI(self, event):
		self.ui_manager.process_events(event)
		
		if(self.toolbar_window is not None):
			self.toolbar_window.event(event)
		
		if event.type == self.c_draw.pygame.USEREVENT:
			if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
				if event.ui_element == self.button_toolbar:
					self.toolbar_window = self.createToolbarWindow()
					
	def updateUI(self):
		self.ui_manager.update(self.c_update.time_delta)