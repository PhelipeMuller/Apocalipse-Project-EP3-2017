import pygame
from pygame.locals import *
from GeralFuncs import * #Arquivo com Funções Gerais
from random import *
import math

#Função Get_rect vem do arquivo GeralFuncs.py

class Zumbi:

	def __init__(self,Persona,blockList):
		self.HP = 30 #HP inicial do Zumbi
		self.dano = 1 #Dano que o Zumbi causa ao atingir o Persona
		self.Velo = randint(10,20)/10 #Potencial de velocidade normal do Zumbi
		self.Imovel = False #Carcterisca referente a se o Zumbi esta parado
		self.ImovelCnt = 0 #Contador de a quantos loops o Zumbi esta parado
		self.imagemleft = [] 
		self.imagemright = []
		z = randint(0,7) #Seleciona aleatoriamente entre as sprites disponiveis para o Zumbi
		for i in range(0,3):self.imagemleft.append(pygame.image.load("imagem/Zombie" +str(z)+ " Left" +str(i)+ ".png").convert_alpha())
		for i in range(0,3):self.imagemright.append(pygame.image.load("imagem/Zombie" +str(z)+ " Right" +str(i)+ ".png").convert_alpha())
		self.imagem = pygame.image.load("imagem/zombie"+str(z)+ " Show.png").convert_alpha()
		self.countMove = 0 #Contador que guarda a quantos loops o zumbi esta andando na mesma direção
		self.countSprite = 0 #Contador que guarda em qual parte da animação de movimento o Zumbi esta
		self.direction = "LEFT" #Define em qual direção o Zumbi esta

		self.speed = {"x": 0, "y": 0} #Velocidade atual do Zumbi
		
		#Definindo posição inicial aleatoria
		flag = True
		while flag:
			#Define aleatoriamente onde o zumbi vai aparecer, proximo ao inicio da tela á direita e esquerda
			if randint(0,1):posX = -300
			else:posX = 1200
			posY = randint(Persona.position[1]-300,Persona.position[1]+300)
			flag = False
			for block in blockList:
				block_rect = get_rect(block)
				if Rect(posX,posY,self.imagem.get_width(),self.imagem.get_height()).colliderect(block_rect): flag = True
		#

		self.position = [posX,posY] #Posição inical do zumbi
		self.rect = get_rect(self) #Rect do Zumbi (Normalmente utilizado para colisões)

	def colidir(self,lista): #Metodo que verifica colisões com Objetos
		self.rect = get_rect(self)
		x_potencial = self.speed["x"]
		y_potencial = self.speed["y"]
		self.rect.x += x_potencial
		self.rect.y += y_potencial
		for objeto in lista:
			objeto_rect = get_rect(objeto)
			if self.rect.colliderect(objeto_rect):
				if self.speed["x"] > 0: 
					self.speed["x"] = 0
				if self.speed["x"] < 0: 
					self.speed["x"] = 0
				if self.speed["y"] > 0: 
					self.speed["y"] = 0
				if self.speed["y"] < 0: 
					self.speed["y"] = 0
		self.rect.x -= x_potencial
		self.rect.y -= y_potencial
		if self.speed["x"] == 0 and self.speed["y"] == 0: self.Imovel = True
		else: 
			self.Imovel = False
			self.ImovelCnt = 0

	def Danificado(self,lista): #Metodo que verifica se o Zumbi colidiu com um projetil e já retira seu HP
		for projetil in lista:
			if self.rect.colliderect(get_rect(projetil)): self.HP -= projetil.dano
			if self.HP <= 0: return True

	def CausandoDano(self,persona,listaobject):#Metodo que verifica se o Zumbi bateu no Persona
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
		if self.Imovel: self.ImovelCnt += 1
		if self.ImovelCnt >= 180: return "IMOVEL"
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

		self.colidir(blockList)
		self.position[0] += self.speed["x"] + moved[0]/2#Move-se para esquerda e para direita
		self.position[1] += self.speed["y"] + moved[1]/2#Move-se para cima e para baixo

		self.CausandoDano(alvo,blockList)
		if self.Danificado(projetilList): 
			return "DEAD" #Verifica se foi atingido por um projetil e subtrai o dano e retorna True caso o Zumbi morra