import pygame
from pygame.locals import *
from GeralFuncs import * #Arquivo com Funções Gerais

class Botao:
	def __init__(self,imagem,position,alpha):
		if alpha: self.imagem = pygame.image.load(imagem).convert_alpha()
		else: self.imagem = pygame.image.load(imagem).convert()
		self.position = position

	def Sobre(self):#Metodo que verifica se o mouse esta sobre o botão
		botao_rect = get_rect(self)
		CursorPosition = pygame.mouse.get_pos()
		if CursorPosition[0] in range(botao_rect[0],(botao_rect[2]+botao_rect[0])):
			if CursorPosition[1] in range(botao_rect[1], (botao_rect[3]+botao_rect[1])):
				return True
		return False

	def Pressed(self):#Metodo que verica se o botão foi clicado
		bMouse1 = 0
		botao_rect = get_rect(self)
		bMouse1,bMouse2,bMouse3 = pygame.mouse.get_pressed()
		CursorPosition = pygame.mouse.get_pos()
		if bMouse1:
			if self.Sobre():
				return True		
		return False