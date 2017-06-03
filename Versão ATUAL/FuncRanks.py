import pygame
from pygame.locals import *
from sys import exit
from random import *
from GeralFuncs import * #Arquivo com Funções Gerais
from classBotao import *
import time

pygame.init()#Inicia o uso do pygame

pygame.font.init()#inicia a fonte
game_font = pygame.font.Font("fonte/Isogul.otf", 72)
pygame.mixer.pre_init(44100, 32, 2, 4096)#Inicia o mixer sound do jogo

screen = pygame.display.set_mode((956, 560), 0, 32) #Definindo tamanho da Janela

background_filename = 'imagem/fundomenu.jpg'
background = pygame.image.load(background_filename).convert() #Definindo a imagem de Background da Janela
pygame.display.set_caption('Titulo')#Define o Titulo da janela

clock = pygame.time.Clock()#Cria um relogio que nos permite usar waits
FPS = 60 #Determina o FPS da janela

def Ranks():
	botaoVoltar = Botao("imagem/Voltar.png",(0,0),1)
	time.clock()
	flag = True
	save = loadgame()
	lista_personagens = []
	for z in range(0,8):lista_personagens.append(pygame.image.load("imagem/Persona" + str(z) + " Front1.png").convert_alpha())

	while flag:
		for event in pygame.event.get():#captura eventos na janela 
			if event.type == QUIT: #Verifica se o evento capturado é QUIT, que indica a intenção de fechar a janela pelo "x"
				exit()

		#Code here
		if botaoVoltar.Pressed(): flag = False
		#

		#blitz Here:
		screen.blit(background, (0, 0))#Definição da superfice da tela, area onde coisas podem acontecer
		count = 1
		for rank in save:
			if count <= 5:
				screen.blit(game_font.render(str(count)+"-" , False,(255, 255, 0)),(130,((count-1)*120)))
				screen.blit(game_font.render(rank[1] , False,(255, 255, 255)),(230,((count-1)*120)))
				screen.blit(game_font.render(str(rank[2]) , False,(255, 255, 255)),(450,((count-1)*120)))
				screen.blit(pygame.transform.scale(lista_personagens[rank[0]], (69, 90)), (530, (count-1)*120))
			else:	
				screen.blit(game_font.render(str(count)+"-" , False,(255, 255, 0)),(630,((count-6)*120)))
				screen.blit(game_font.render(rank[1] , False,(255, 255, 255)),(730,((count-6)*120)))
				screen.blit(game_font.render(str(rank[2]) , False,(255, 255, 255)),(950,((count-6)*120)))
				screen.blit(pygame.transform.scale(lista_personagens[rank[0]], (69, 90)), (1000, (count-6)*120))
			count += 1
		
		screen.blit(botaoVoltar.imagem,botaoVoltar.position)
		#

		pygame.display.update() #Atualiza a Janela
		clock.tick(FPS)# Wait .tick(x) Seg/x