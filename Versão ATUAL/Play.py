import pygame
from pygame.locals import *
from sys import exit
from random import *
import time
from classPersona import * #Arquivo com a Classe do Jogador
from classZumbi import * #Arquivo com a Classe dos Zumbis
from classGhost import * #Arquivo com a Classe dos Fantasmas
from classObjeto import * #Arquivo com a Classe de Objetos, como paredes e afins
from classProjetil import * #Arquivo com a Classe dos Tiros
from classItem import * #Arquivo com a Classe dos Itens
from classArma import * #Arquivo com a Classe das Armas
from classBotao import * #Arquivo com a Classe de Botões
from classWave import * #Arquivo com as Classe de Waves
from classBackground import * #Arquivo com Classe de Background
from GeralFuncs import * #Arquivo com Funções Gerais
from FuncGameOver import * #Arquivo com a janela de Game Over
from Maps import * #Arquivo com funções de design de mapas

pygame.init()#Inicia o uso do pygame

pygame.font.init()#inicia a fonte
font_name = pygame.font.get_default_font()#Define a fonte usada no jogo
game_font = pygame.font.SysFont(font_name, 72)
pygame.mixer.pre_init(44100, 32, 2, 4096)#Inicia o mixer sound do jogo

screen = pygame.display.set_mode((956, 560), 0, 32) #Definindo tamanho da Janela


pygame.display.set_caption('Titulo')#Define o Titulo da janela

clock = pygame.time.Clock()#Cria um relogio que nos permite usar waits
FPS = 60 #Determina o FPS da janela

def GameMenu(): #Função do pause-menu in game
	background_filename = 'imagem/fundomenu.jpg'
	background = pygame.image.load(background_filename).convert() #Definindo a imagem de Background da Janela
	botaoVoltar = Botao("imagem/Voltar.png",(0,0),1) #Criando botão Voltar
	botaoQuit = Botao('imagem/nome.png',(200, 50),1) #Criando botão Quit
	while True:
		for event in pygame.event.get():#captura eventos na janela 
			if event.type == QUIT: #Verifica se o evento capturado é QUIT, que indica a intenção de fechar a janela pelo "x"
				exit()
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[K_ESCAPE]: #Se ESC for press fecha menu e pausa o jogo
			pressed_keys = 0
			clock.tick(2)# Wait .tick(x) Seg/x 
			return False
		if botaoVoltar.Pressed(): #Se Botão voltar for precionado Fecha o Menu
			background_filename = 'imagem/fundomenu.jpg'
			background = pygame.image.load(background_filename).convert() #Definindo a imagem de Background da Janela 
			return False
		elif botaoQuit.Pressed(): #Se o Botão Quit for precionado Fecha o Menu
			background_filename = 'imagem/fundomenu.jpg'
			background = pygame.image.load(background_filename).convert() #Definindo a imagem de Background da Janela
			return True
		else:	
			screen.blit(background, (0, 0))#Definição da superfice da tela, area onde coisas podem acontecer
			screen.blit(botaoVoltar.imagem,botaoVoltar.position) #blita Botão Voltar
			screen.blit(botaoQuit.imagem,botaoQuit.position) #Blita Botão Quit
			pygame.display.update() #Atualiza a Janela
			clock.tick(FPS)# Wait .tick(x) Seg/x

def Play(chartag): #Função principal do jogo
		letrinha_font = pygame.font.Font("fonte/Isogul.otf", 32) #Inicia a fonte de letra pequena
		letrao_font = pygame.font.Font("fonte/Isogul.otf", 144) #Inicia a fonte de letra grande
		projetillist = [] #Lista de Projeteis
		zumbilist = [] #Lista de Zumbis
		ghostlist = [] #Lista de Fantasmas
		droplist = [] #Lista de Drops
		objetolist = MapaBase("OBJETO") #Lista de Objetos
		Persona = Personal(chartag) # Criando Personagem do jogador
		Background = BackGround() #Inicia o Background como um objeto para poder mover adequadamente 
		Arma = Armas(1) #Inicia a Arma atual como uma UZI
		Waves = Wave() #Inicia as Waves do jogo
		time.clock() #Inicia o relogio
		flag = True 
		shoted = False #Variavel que verifica se o jogador disparou durante o ultimo loop
		positionHeart = [850,890,930,970,1010,810,770,730,690,650,610,570,530,490,450,410,370,330,290,250,210,170] # lita de pontos em X onde os corações de HP do player são blitados
		timer = 0
		while flag:
			
			for event in pygame.event.get():#captura eventos na janela 
				if event.type == QUIT: #Verifica se o evento capturado é QUIT, que indica a intenção de fechar a janela pelo "x"
					exit()
			pressed_keys = pygame.key.get_pressed()
			if pressed_keys[K_ESCAPE]:
				if GameMenu(): flag = False

			#Code here
			if Waves.update(Persona,zumbilist,ghostlist,objetolist,timer): blitWave = True #Da Update nas Waves, verificando se precisa printar na tela qua a Wave mudou
			else: blitWave = False

			PersonaUpdate_return = Persona.update(screen,objetolist,zumbilist+ghostlist) #Faz update do personagem do jogador. Se move, toma dano e etc
			if PersonaUpdate_return == "DEAD":	
				GameOver(Waves,chartag)
				flag = False
			else: moved = PersonaUpdate_return

			for zumbi in zumbilist: 
				if zumbi.update(Persona,screen,objetolist,projetillist,moved) == "DEAD": #Faz update de cada um dos zumbis. Se move, toma dao e etc
					if randint(0,21) > 12: 
						tag =  randint(0,3)
						droplist.append(Item(tag,zumbi.position,Persona,Arma,time.clock()))
					zumbilist.remove(zumbi)
					Waves.ZumbiQnt -= 1
				if zumbi.update(Persona,screen,objetolist,projetillist,moved) == "IMOVEL":
					zumbilist.remove(zumbi)

			for ghost in ghostlist: 
				if ghost.update(Persona,screen,objetolist,projetillist,moved) == "DEAD": #Faz update de cada um dos fantasmas. Se move, toma dao e etc
					ghostlist.remove(ghost)
					Waves.GhostQnt -= 1

			for drop in droplist: #Faz update para cada um dos itens dropados dos zumbis
				if drop.update(Persona,Armas,moved,time.clock()) == True: droplist.remove(drop)
				if drop.update(Persona,Armas,moved,time.clock()) == "ARMA":
					Arma = Armas(drop.ArmaTag)
					droplist.remove(drop)
			
			pressed_keys = pygame.key.get_pressed()
			if pressed_keys[K_UP] and Persona.LastShot + Persona.RateShot < time.clock(): 
				projetillist.append(Projetil(Persona,time.clock(),"UP",Arma)) #Dispara um projetil se o jogador clicou o bMouse1 e não possui o limite de projeteis na tela
				shoted = True
			elif pressed_keys[K_LEFT] and Persona.LastShot + Persona.RateShot < time.clock(): 
				projetillist.append(Projetil(Persona,time.clock(),"LEFT",Arma)) #Dispara um projetil se o jogador clicou o bMouse1 e não possui o limite de projeteis na tela
				shoted = True
			elif pressed_keys[K_DOWN] and Persona.LastShot + Persona.RateShot < time.clock(): 
				projetillist.append(Projetil(Persona,time.clock(),"DOWN",Arma)) #Dispara um projetil se o jogador clicou o bMouse1 e não possui o limite de projeteis na tela
				shoted = True
			elif pressed_keys[K_RIGHT] and Persona.LastShot + Persona.RateShot < time.clock(): 
				projetillist.append(Projetil(Persona,time.clock(),"RIGHT",Arma)) #Dispara um projetil se o jogador clicou o bMouse1 e não possui o limite de projeteis na tela
				shoted = True

			if Arma.update(shoted): Arma = Armas(0) #Usando a variavel Shoted para saber se retira munição e etc, da Arma
			shoted = False #Torna a Variavel Shoted Falsa, para não repetir no proximo loop o mesmo comando
			for projetil in projetillist: #Para cada projetil na tela, verifica se ele colidiu com algo e se o tempo in tela acabou
				if projetil.update(screen,objetolist+zumbilist+ghostlist,time.clock(),moved): projetillist.remove(projetil) 
			
			for objeto in objetolist: 
				if objeto.update(projetillist,zumbilist,moved): objetolist.remove(objeto) #Para cada Objeto, faz seu update (Retirando seu HP e possivelmente o destruindo)

			Background.update(moved)
			#


			#blitz Here:
			screen.blit(Background.imagem, Background.position)#Definição da superfice da tela, area onde coisas podem acontecer
			for drop in droplist: screen.blit(drop.imagem, drop.position)#Blita cada um dos Drops na tela
			for zumbi in zumbilist: screen.blit(zumbi.imagem, zumbi.position) #Blitz dos Zumbis
			screen.blit(Persona.imagem, Persona.position) #Blit do Personagem do jogador
			for objeto in objetolist: screen.blit(objeto.imagem, objeto.position) #Blitz dos Objetos (Passar para ultimo Blitz, disfarça Bug)
			for ghost in ghostlist: screen.blit(ghost.imagem, ghost.position) #Blitz dos Fantasmas
			for projetil in projetillist: screen.blit(projetil.imagem, projetil.position) #Blitz para cada um dos projeteis
			screen.blit(Arma.imagem,(10,570)) #Blita o incone da arma no carnto inferiro esquerdo
			if Arma.MaxAmmo > 1000000: screen.blit(letrinha_font.render("Ammo: Infinita",False,(255,255,255)),(0,670)) #Blita a quantidade de munição na arma
			else: screen.blit(letrinha_font.render("Ammo: "+str(Arma.Ammo),False,(255,255,255)),(0,670))
			for i in range(Persona.HP):screen.blit(Persona.HPmark,[positionHeart[i],0]) #Blita cada um dos Hearts de Vida no canto superiro da tela
			if blitWave: screen.blit(letrao_font.render("WAVE  " + str(Waves.WaveAtual), False,(255, 255, 255)),(250,250)) 
			else: screen.blit(letrinha_font.render("WAVE  " + str(Waves.WaveAtual), False,(255, 255, 255)),(0,0)) #Blita na esquerda superior a Wave Atual
			#
			pygame.display.update() #Atualiza a Janela
			clock.tick(FPS)#Seg/x
			timer += 1
		del(Persona)
		del(zumbilist)
		del(objetolist)
		del(droplist)
		del(projetillist)