import pygame
from pygame.locals import *
from GeralFuncs import * #Arquivo com Funções Gerais

#Função Get_rect vem do arquivo GeralFuncs.py

class Objeto:

	def __init__(self,UnBreakble,imagem,p):
		self.HP = 100 #HP do Objeto
		self.unbreakble = UnBreakble #Variavel que define se o objeto é quebravel ou não

		self.imagem = pygame.image.load(imagem).convert_alpha() #Imagem do Objeto

		self.x = self.imagem.get_width()
		self.y = self.imagem.get_height()
		self.position = [p[0]*self.x,p[1]*self.y] #Posição o Objeto
		self.rect = get_rect(self) #Rect do Objeto (geralmente usado para colisões)

	def Danificado(self,listaPro,listaZumbi): #Metodo que verifica se o objeto foi danificado por um Zumbi ou Projetil e já retira seu HP
		for projetil in listaPro:
			if self.rect.colliderect(get_rect(projetil)): self.HP -= projetil.dano
			if self.HP <= 0: return True
		for zumbi in listaZumbi:
			if self.rect.colliderect(get_rect(zumbi)): self.HP -= zumbi.dano
			if self.HP <= 0: return True

	def update(self,listaPro,listaZumbi,moved):
		if self.Danificado(listaPro,listaZumbi): return True
		if self.unbreakble: self.HP = 1000
		self.position[0] += moved[0] #Move-se para esquerda e para direita
		self.position[1] += moved[1]#Move-se para cima e para baixo
