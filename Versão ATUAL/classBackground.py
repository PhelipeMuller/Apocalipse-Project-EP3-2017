import pygame
from pygame.locals import *
from GeralFuncs import * #Arquivo com Funções Gerais
from random import *
from Maps import * #Arquivo com função que retorna diversas caracteristicas do Mapa
import math

#Função Get_rect vem do arquivo GeralFuncs.py

class BackGround:

	def __init__(self):

		self.filename = MapaBase("FUNDO")
		self.imagem = pygame.image.load(self.filename).convert() #Definindo a imagem de Background da Janela
		
		posX = -1000
		posY = -500

		self.position = [posX,posY]



	def update(self,moved): #Metodo que atualiza o Background
		self.position[0] += moved[0]
		self.position[1] += moved[1]
		