import pygame
from pygame.locals import *
from Drops import * #Arquivo que possui uma função INPUT-OUTPUT de informa~ções e caracteristicas dos itens
from GeralFuncs import * #Arquivo com Funções Gerais


class Item:

	def __init__(self,tag,p,Persona,Arma,time):
		self.ArmaTag = Drop(tag,"ARMATAG",Persona,Arma)
		self.tag = tag
		self.TimeOrigem = time

		self.Duration = Drop(self.tag,"TIME",Persona,Arma)
		self.imagem = pygame.image.load(Drop(self.tag,"IMAGEM",Persona,Arma)).convert_alpha() #Imagem do Objeto

		self.position = p #Posição o Objeto
		self.rect = get_rect(self) #Rect do Objeto (geralmente usado para colisões)

	def colidir(self,Persona): #Metodo que verifica colisões com Objetos
		self.rect = get_rect(self)
		obj_Persona = get_rect(Persona)
		if self.rect.colliderect(obj_Persona):return True
		return False

	def update(self,Persona,Arma,moved,time):
		if self.colidir(Persona):
			if self.tag == 0 or self.tag == 1: 
				Drop(self.tag,"EFEITO",Persona,Arma)
				return True
			if self.tag == 2 or self.tag == 3:
				return "ARMA"
		if time >= self.TimeOrigem + self.Duration: return True
		self.position[0] += moved[0]/2#Move-se para esquerda e para direita
		self.position[1] += moved[1]/2#Move-se para cima e para baixo
