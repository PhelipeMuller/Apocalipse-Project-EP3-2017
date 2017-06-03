import pygame
from pygame.locals import *
from classBotao import *
from GeralFuncs import *

def GameOver(Waves,chartag):
	pygame.mixer.Sound('sound/GAMEOVER.wav').play()
	GameOver_font = pygame.font.Font("fonte/Pirate Style.ttf", 144) #Inicia a fonte de Game Over
	NICK_font = pygame.font.Font("fonte/Chisel Mark.ttf", 144) #Inicia a fonte de Game Over
	letrinha_font = pygame.font.Font("fonte/Chisel Mark.ttf", 32) #Inicia a fonte de letrinha
	letra_font = pygame.font.Font("fonte/Chisel Mark.ttf",64) #Inicia a fonte de letrinha
	background_filename = 'imagem/fundomenu.jpg'
	background = pygame.image.load(background_filename).convert() #Definindo a imagem de Background da Janela
	NICK = ""
	while True:
		for event in pygame.event.get():#captura evescreen.blit(game_font.render("Isadora Costa", False,(255, 255, 255)),(150,550))ntos na janela 
			if event.type == QUIT: #Verifica se o evento capturado é QUIT, que indica a intenção de fechar a janela pelo "x"
				exit()
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[K_RETURN]:
			pressed_keys = 0
			clock.tick(2)# Wait .tick(x) Seg/x
			while len(NICK) < 3: NICK += " "
			savegame([chartag,NICK,Waves.WaveAtual-1]) 
			return True
		NICK = insert(NICK,3)
		clock.tick(12)# Wait .tick(x) Seg/x
		screen.blit(background, (0, 0))#Definição da superfice da tela, area onde coisas podem acontecer
		screen.blit(GameOver_font.render("GAME OVER", True,(255, 0, 0)),(250,50))

		screen.blit(letrinha_font.render("Digite seu Nick", True,(255, 0, 0)),(360,200))
		screen.blit(NICK_font.render(NICK, True,(255, 255, 0)),(500,300)) #Printa o NICK atual do Jogador


		screen.blit(letra_font.render("Waves sobrevividas:   {0}".format(Waves.WaveAtual-1), True,(255,255,255)),(320,400))
		screen.blit(letrinha_font.render("Pressione Enter para voltar para o Menu", True,(255, 255, 255)),(350,600))
		pygame.display.update() #Atualiza a Janela
		clock.tick(FPS)# Wait .tick(x) Seg/x