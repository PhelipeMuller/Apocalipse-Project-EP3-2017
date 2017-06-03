import pygame
from pygame.locals import *
from sys import exit
from random import *
from GeralFuncs import * #Arquivo com Funções Gerais
from classBotao import * #Arquivo com a Classe dos Botões
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

def Options():
	botaoVoltar = Botao("imagem/Voltar.png",(0,0),1)
	time.clock()
	flag = True
	save = loadgame()
	chartag = 2
	lista_personagens = []
	clock = pygame.time.Clock()
	for z in range(0,8):lista_personagens.append(pygame.image.load("imagem/Persona" + str(z) + " Front1.png").convert_alpha())

	while flag:
		for event in pygame.event.get():#captura eventos na janela 
			if event.type == QUIT: #Verifica se o evento capturado é QUIT, que indica a intenção de fechar a janela pelo "x"
				exit()

		#Code here
		if botaoVoltar.Pressed(): flag = False #Sai se botão de Voltar for clicado

		#Ajusta o personagem que sera usado
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[K_LEFT]: chartag -= 1
		if pressed_keys[K_RIGHT]: chartag += 1
		if pressed_keys[K_RETURN]: flag = False
		clock.tick(10)
		if chartag == -1: chartag = len(lista_personagens)-1
		if chartag == len(lista_personagens): chartag = 0


		personagem_imagem = pygame.transform.scale(lista_personagens[chartag], (69, 90))
		WASD_imagem = pygame.image.load("imagem/WASDControls.png").convert_alpha() #define a iamgem de WSAD
		Setas_imagem = pygame.image.load("imagem/ArrowsControls.png").convert_alpha() #define a imagagem de Arrows
		#

		#blitz Here:
		screen.blit(background, (0, 0))#Definição da superfice da tela, area onde coisas podem acontecer
		screen.blit(game_font.render("Escolha seu Personagem" , False,(255, 255, 0)),(130,60)) 
		screen.blit(game_font.render("Com as Setas" , False,(255, 255, 0)),(130,120))
		screen.blit(personagem_imagem, (940, 60)) #Blita a imagem do persoangem atual
		screen.blit(game_font.render("Controles:" , False,(255, 255, 0)),(130,200))
		screen.blit(WASD_imagem, (130, 300)) #Blita a imagem de WSAD
		screen.blit(Setas_imagem, (530, 300)) #Blita a imagem das Arrows
		screen.blit(game_font.render("Movimenta" , False,(255, 255, 0)),(130,400))
		screen.blit(game_font.render("Atira" , False,(255, 255, 0)),(530,400))
		screen.blit(botaoVoltar.imagem,botaoVoltar.position) #Blita o botão de voltar
		#

		pygame.display.update() #Atualiza a Janela
		clock.tick(FPS)# Wait .tick(x) Seg/x
	return chartag