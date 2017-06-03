import pygame
from pygame.locals import *
from GeralFuncs import * #Arquivo com Funções Gerais

#Função Get_rect vem do arquivo GeralFuncs.py

class Personal:

	def __init__(self,chartag):
		self.ReallyMAXHP = 22
		self.HPMax = 5 #Pontos maximos de Vida
		self.HP = 5 #Pontos de Vida
		self.Vel = 5 #Potencial de velocidade do Jogador
		self.ProjetilLimit = 0 #Limite de Disparos na Tela
		self.speed = {"x": 0, "y": 0} #Velociadade atual do jogador
		self.position = [540,350] #Posição inicial do jogador
		self.LastShot = 0 #Variavel que define quando foi disparado o ultimo tiro
		self.RateShot = 0 #Variavel que define o intervalo entre os tiros
		self.imagemfront = []
		self.imagemback = []
		self.imagemleft = []
		self.imagemright = []
		for i in range(0,3):self.imagemfront.append(pygame.image.load("imagem/Persona" +str(chartag)+ " Front"+str(i)+".png").convert_alpha()) #Imagem do jogador
		for i in range(0,3):self.imagemback.append(pygame.image.load("imagem/Persona" +str(chartag)+ " Back"+str(i)+".png").convert_alpha())
		for i in range(0,3):self.imagemleft.append(pygame.image.load("imagem/Persona" +str(chartag)+ " Left"+str(i)+".png").convert_alpha())
		for i in range(0,3):self.imagemright.append(pygame.image.load("imagem/Persona" +str(chartag)+ " Right"+str(i)+".png").convert_alpha())
		self.imagem = pygame.image.load("imagem/Persona" +str(chartag)+ " Front0.png").convert_alpha()
		self.HPmark = pygame.image.load("imagem/HPmark.png").convert_alpha() #Imagem de HPmark
		self.rect = get_rect(self) #Rect do jogador (Usado para colisões, principalmente)
		self.countMove = 0 #Variavel que conta a quantos loops o Persona esta se movendo á mesma direção
		self.countSprite = 0 #Variavel que guarda em qual etapa da animação o Persona esta
		self.direction = "DOWN" #Variavel que guarda em qual direção o Personagem esta olhando

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
		self.moved[0] -= self.speed["x"] #Move-se para esquerda e direita
		self.moved[1] -= self.speed["y"] #Move-se para cima e para baixo

	def Danificado(self,listazumbi,listaobject): #Metodo que verifica se o Persona colidiu com um Zumbi e já retira seu HP
		for zumbi in listazumbi:
			if self.rect.colliderect(get_rect(zumbi)): 
				self.HP -= zumbi.dano #recebe o dano do zumbi e fantasmas
				flag = False
				for objeto in listaobject: 
					rect_objeto1 = get_rect(objeto)
					rect_objeto1.x += self.Vel*6
					rect_objeto1.y += self.Vel*6
					rect_objeto2 = get_rect(objeto)
					rect_objeto2.x -= self.Vel*6
					rect_objeto2.y -= self.Vel*6
					if self.rect.colliderect(rect_objeto1): flag = True
					if self.rect.colliderect(rect_objeto2): flag = True
				if not flag: 
					#Pula no sentido oposto ao zumbi
					if zumbi.position[0] > self.position[0]: self.moved[0] -= -self.Vel*6
					else: self.moved[0] -= self.Vel*6
					if zumbi.position[1] > self.position[1]: self.moved[1] -= -self.Vel*6
					else: self.moved[1] -= self.Vel*6

				if self.HP == 0: return "DEAD"


	def update(self,screen,blockList,zumbilist): #Metodo que atualiza os atributos do Personagem
		self.moved = [0]*2
		#Sequencia de linhas que fazem o personagem se mover e não atravesar paredes
		self.rect = get_rect(self)
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[K_w]: #Aumenta a velocidade atual para cima
			self.countMove += 1
			if self.direction != "UP": self.countMove = 0
			if self.countMove == 0: self.imagem = self.imagemback[0]
			if self.countMove == 21: self.imagem = self.imagemback[1]
			if self.countMove == 41: 
				self.imagem = self.imagemback[2]
				self.countMove = 0
			self.direction = "UP"
			self.speed["y"] = -self.Vel

		elif pressed_keys[K_s]: #Aumenta a velocidade atual para baixo
			self.countMove += 1
			if self.direction != "DOWN": self.countMove = 0
			if self.countMove == 0: self.imagem = self.imagemfront[0]
			if self.countMove == 21: self.imagem = self.imagemfront[1]
			if self.countMove == 41: 
				self.imagem = self.imagemfront[2]
				self.countMove = 0
			self.direction = "DOWN"
			self.speed["y"] = self.Vel
		else: self.speed["y"] = 0

		if pressed_keys[K_a]: #Aumenta a velocidade atual para a Esquerda
			self.countMove += 1
			if self.direction != "LEFT": self.countMove = 0
			if self.countMove == 0: self.imagem = self.imagemleft[0]
			if self.countMove == 21: self.imagem = self.imagemleft[1]
			if self.countMove == 41: 
				self.imagem = self.imagemleft[2]
				self.countMove = 0
			self.direction = "LEFT"
			self.speed["x"] = -self.Vel

		elif pressed_keys[K_d]: #aumenta a velocidade atual para a direita
			self.countMove += 1
			if self.direction != "RIGHT": self.countMove = 0
			if self.countMove == 0: self.imagem = self.imagemright[0]
			if self.countMove == 21: self.imagem = self.imagemright[1]
			if self.countMove == 41: 
				self.imagem = self.imagemright[2]
				self.countMove = 0
			self.direction = "RIGHT"
			self.speed["x"] = self.Vel
		else: self.speed["x"] = 0
		
		self.colidir(blockList)

		if self.Danificado(zumbilist,blockList): return "DEAD" #Verifica se foi atingido por um zumbi e subtrai o dano
		return self.moved