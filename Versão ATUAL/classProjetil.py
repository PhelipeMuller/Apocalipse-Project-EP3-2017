import pygame
from pygame.locals import *
from GeralFuncs import * #Arquivo com Funções Gerais
import math

class Projetil:

	def __init__(self,atirador,tempo_nascimento,direction,Arma):
		self.dano = Arma.Dano #Dano causado ao atingir algo
		self.tempo_de_nascimento = tempo_nascimento #Marca o momento no clock que o projetil foi disparado
		self.Velo = Arma.Velo #Velocidade de movimento do projetil
		self.duration = Arma.Duration #Duração que o projetil existe
		atirador.LastShot = tempo_nascimento #Define que a Variavel LastShot, que marca quando foi disparado o ultimo tiro é igual ao clock atual
		atirador.RateShot = Arma.Rate #Define que o Rate fire é igual ao rate fire deste projetil

		self.speed = {"x": 0, "y": 0} #Velocidade Atual do Projetil
		self.position = [atirador.position[0]+10,atirador.position[1]+10] #Posição de Origem do projetil
		self.memory_position = self.position
		self.imagem = pygame.image.load("imagem/disparo.png").convert_alpha() #Imagem do Projetil
		self.rect = get_rect(self) #Rect do Projetil (Usado para colisões)

		if direction == "RIGHT": self.speed["x"] = +self.Velo
		elif direction == "LEFT": self.speed["x"] = -self.Velo
		elif direction == "UP": self.speed["y"] = -self.Velo
		elif direction == "DOWN": self.speed["y"] = +self.Velo

	def colidir(self,lista): #Metodo que verifica colisões com Objetos
		for objeto in lista:
			obj_rect = get_rect(objeto)
			if self.rect.colliderect(obj_rect):
				return True
		return False

	def update(self,screen,BlockList,tempo_nomomento,moved): #Metodo que atualiza atributos do Projetil
		self.tempo_nomomento = tempo_nomomento
		if tempo_nomomento - self.tempo_de_nascimento > self.duration:
			return True
		self.rect = get_rect(self)

		self.position[0] += self.speed["x"] + moved[0] #Move-se para esquerda e direita
		self.position[1] += self.speed["y"] + moved[1] #Move-se para cima e para baixo


		if self.colidir(BlockList): return True #Retorna True para desaparecer, se bater em um objeto ou zumbi
		if self.position[0] in range(self.alvo_position[0]-5,self.alvo_position[0]+5):
			if self.position[1] in range(self.alvo_position[1]-5,self.alvo_position[1]+5): return True #Retorna True para desaparecer, se chegou no ponto que o mouse clicou
