import pygame
from pygame.locals import *
from sys import exit
from random import *
from GeralFuncs import * #Arquivo com Funções Gerais
from classBotao import *
import time

pygame.init()#Inicia o uso do pygame

pygame.font.init()#inicia a fonte
game_font = pygame.font.Font("fonte/KGLifeisMessy.ttf", 36)
pygame.mixer.pre_init(44100, 32, 2, 4096)#Inicia o mixer sound do jogo

screen = pygame.display.set_mode((956, 560), 0, 32) #Definindo tamanho da Janela

background_filename = 'imagem/fundomenu.jpg'
background = pygame.image.load(background_filename).convert() #Definindo a imagem de Background da Janela
pygame.display.set_caption('Titulo')#Define o Titulo da janela

clock = pygame.time.Clock()#Cria um relogio que nos permite usar waits
FPS = 60 #Determina o FPS da janela

def Creditos():
	botaoVoltar = Botao("imagem/Voltar.png",(0,0),1)
	time.clock()
	flag = True

	while flag:
		for event in pygame.event.get():#captura eventos na janela 
			if event.type == QUIT: #Verifica se o evento capturado é QUIT, que indica a intenção de fechar a janela pelo "x"
				exit()

		#Code here
		if botaoVoltar.Pressed(): flag = False
		#

		#blitz Here:
		screen.blit(background, (0, 0))#Definição da superfice da tela, area onde coisas podem acontecer
		screen.blit(game_font.render("Princesa Jujuba Zumbi:                              Sabrina Machado", False,(255, 255, 255)),(30,150))
		screen.blit(game_font.render("O Ceifador:                                                         Matteo Iannoni", False,(255, 255, 255)),(30,200))
		screen.blit(game_font.render("Tigre de Niflheim:                                                  Phelipe Müller", False,(255, 255, 255)),(30,250))

		screen.blit(game_font.render("Agradecimentos especiais:", False,(255, 255, 255)),(150,500))
		screen.blit(game_font.render("Isadora Costa", False,(255, 255, 255)),(250,550))
		screen.blit(game_font.render("Camila F. Achutti", False,(255, 255, 255)),(250,600))
		screen.blit(game_font.render("e Luciano P. Soares", False,(255, 255, 255)),(250,650))
		screen.blit(botaoVoltar.imagem,botaoVoltar.position)#Blita o botão voltar
		#

		pygame.display.update() #Atualiza a Janela
		clock.tick(FPS)# Wait .tick(x) Seg/x