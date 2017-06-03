import pygame
from pygame.locals import *
from GeralFuncs import * #Arquivo com Funções Gerais
from random import *
import math

#Função Get_rect vem do arquivo GeralFuncs.py

class Ghost:

	def __init__(self,Persona,blockList):
		self.HP = 30 #HP inicial do Zumbi
		self.dano = 1 #Dano que o Zumbi causa ao atingir o Persona
		self.Velo = randint(10,15)/10 #Potencial de velocidade normal do Fantasma
		self.imagemleft = []
		self.imagemright = []
		z = 0 #random.randint(0,1)
		for i in range(0,3):self.imagemleft.append(pygame.image.load("imagem/Ghost" +str(z)+ " Left" +str(i)+ ".png").convert_alpha())
		for i in range(0,3):self.imagemright.append(pygame.image.load("imagem/Ghost" +str(z)+ " Right" +str(i)+ ".png").convert_alpha())
		self.imagem = pygame.image.load("imagem/Ghost"+str(z)+ " Show.png").convert_alpha()
		self.countMove = 0
		self.countSprite = 0
		self.direction = "DOWN"

		self.speed = {"x": 0, "y": 0} #Velocidade atual do Zumbi
		
		#Definindo posição inicial aleatoria
		flag = True
		while flag:
			if randint(0,1):posX = -300
			else:posX = 1200
			posY = randint(Persona.position[1]-300,Persona.position[1]+300)
			flag = False
			for block in blockList:
				block_rect = get_rect(block)
				if Rect(posX,posY,self.imagem.get_width(),self.imagem.get_height()).colliderect(block_rect): flag = True
		#

		self.position = [posX,posY] #Posição inical do Fantasma
		self.rect = get_rect(self) #Rect do Fantasma (Normalmente utilizado para colisões)

	def Danificado(self,lista): #Metodo que verifica se o Fantasma colidiu com um projetil e já retira seu HP
		for projetil in lista:
			if self.rect.colliderect(get_rect(projetil)): self.HP -= projetil.dano
			if self.HP <= 0: return True

	def CausandoDano(self,persona,listaobject):
		if self.rect.colliderect(get_rect(persona)):
			flag = False
			for objeto in listaobject: 
				if self.rect.colliderect(get_rect(objeto)): flag = True
			if not flag: 
				#Pula no sentido oposto ao Persona
				if persona.position[0] > self.position[0]: self.position[0] += -self.Velo*12
				else: self.position[0] += self.Velo*12
				if persona.position[1] > self.position[1]: self.position[1] += -self.Velo*12
				else: self.position[1] += self.Velo*12


	def update(self,alvo,screen,blockList,projetilList,moved): #Metodo que atualiza os atributos do Zumbi
		self.rect = get_rect(self)

		self.Vel = (alvo.rect.center[0] - self.rect.center[0],alvo.rect.center[1] - self.rect.center[1]) #potencial de velocidade do Projetil
		
		if alvo.position[0] > self.position[0]:
			self.countMove += 1
			if self.direction != "RIGHT": self.countMove = 0
			if self.countMove == 0: self.imagem = self.imagemright[0]
			if self.countMove == 21: self.imagem = self.imagemright[1]
			if self.countMove == 41: 
				self.imagem = self.imagemright[2]
				self.countMove = 0
			self.direction = "RIGHT"

		elif alvo.position[0] < self.position[0]:
			self.countMove += 1
			if self.direction != "LEFT": self.countMove = 0
			if self.countMove == 0: self.imagem = self.imagemleft[0]
			if self.countMove == 21: self.imagem = self.imagemleft[1]
			if self.countMove == 41: 
				self.imagem = self.imagemleft[2]
				self.countMove = 0
			self.direction = "LEFT"

		vetor_resultante = math.sqrt(self.Vel[1]**2 + self.Vel[0]**2)
		self.speed["y"] = self.Velo*(self.Vel[1]/vetor_resultante)#Determina o delta x
		self.speed["x"] = self.Velo*(self.Vel[0]/vetor_resultante)#Determina o delta y

		self.position[0] += self.speed["x"] + moved[0]#Move-se para esquerda e para direita
		self.position[1] += self.speed["y"] + moved[1]#Move-se para cima e para baixo

		self.CausandoDano(alvo,blockList)
		if self.Danificado(projetilList): return "DEAD" #Verifica se foi atingido por um projetil e subtrai o dano e retorna True caso o Fantasma morra