import pygame
from pygame.locals import *
from GeralFuncs import * #Arquivo com Funções Gerais
from classZumbi import * #Arquivo com a classe dos Zumbis
from classGhost import * #Arquivo com a classe dos Fantasmas
from random import *
import math


class Wave:

	def __init__(self):
		self.WaveAtual = 1 #Wave Atual
		self.ZumbiQnt = 5 #Qunatidade de Zumbis na Wave
		self.GhostQnt = 1 #Quantidade de Ghosts na Wave
		self.ZumbiMaxTela = 7 #"Maximo" de Zumbis na tela
		self.GhostMaxTela = 4 #"Maximo" de ghosts na tela
		self.TimeOrigem = 0
		self.TimePausa = 3 #Tempo de descanço entre uma Wave e outra, em segundos

	def NewWave(self,Persona,objetolist,time):#Função que inicia cada Wave
		self.WaveAtual += 1
		self.ZumbiQnt = self.WaveAtual*5
		self.GhostQnt = self.WaveAtual*2
		self.TimeOrigem = time


	def update(self,Persona,zumbilist,ghostlist,objetolist,time):
		if time <= self.TimeOrigem + self.TimePausa*60: return True
		if len(zumbilist) <= self.ZumbiMaxTela and len(zumbilist) < self.ZumbiQnt:
			zumbilist.append(Zumbi(Persona,objetolist))
		elif randint(0,100000000000000000000) == 0 and len(zumbilist) < self.ZumbiQnt: zumbilist.append(Zumbi(Persona))
		
		if len(ghostlist) <= self.GhostMaxTela and len(ghostlist) < self.GhostQnt:
			ghostlist.append(Ghost(Persona,objetolist))
		elif randint(0,100000000000000000000) == 0 and len(ghostlist) < self.GhostQnt: ghostlist.append(Ghost(Persona))
		

		if self.ZumbiQnt <= 0 and self.GhostQnt <= 0: 
			self.NewWave(Persona,objetolist,time)
