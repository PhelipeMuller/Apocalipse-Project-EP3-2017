import pygame
from pygame.locals import *
from Weapons import * #Arquivo que retorna varias caracteristicas de acordo com a entrada 
from GeralFuncs import * #Arquivo com Funções Gerais

#Função Get_rect vem do arquivo GeralFuncs.py

class Armas:

	def __init__(self,tag):
		self.MaxAmmo = Weapon(tag,"AMMO")
		self.Ammo = Weapon(tag,"AMMO")
		self.Dano = Weapon(tag,"DANO")
		self.Velo = Weapon(tag,"VELO")
		self.Rate = Weapon(tag,"RATE")
		self.Duration = Weapon(tag,"DURATION")
		self.imagem = pygame.image.load(Weapon(tag,"IMAGEM")).convert_alpha()

	def update(self,shoted):
		if shoted: self.Ammo -= 1
		if self.Ammo <= 0: return True