import pygame 
from random import * 
from pygame.locals import *
from sys import exit
from Play import * #Arquivo principal do jogo
from FuncCredits import * #Arquivo da janela de Creditos
from FuncRanks import * #Arquivo da janela de Ranks
from GeralFuncs import * #Arquivo com Funções Gerais, Save and Load, etc
from FuncOptions import * #Arquivo da janela de Opções
from classBotao import * #Arquivo com a Classe dos botões

pygame.init()#Inicia o uso do pygame

pygame.font.init()#inicia a fonte

game_font = pygame.font.SysFont(pygame.font.get_default_font(), 72) #Inicia a fonte padrão do jogo

pygame.mixer.pre_init(44100, 32, 2, 4096)#Inicia o mixer sound do jogo

som_menu = pygame.mixer.Sound('sound/86_Dark_City.wav') # Define qual som sera tocado no menu
playingSom_Menu = False

screen = pygame.display.set_mode((1080, 700), 0, 32) #Definindo tamanho da Janela

background_filename = 'imagem/fundomenu.jpg'
background = pygame.image.load(background_filename).convert() #Definindo a imagem de Background da Janela
pygame.display.set_caption('Survival Dairy')#Define o Titulo da janela
clock = pygame.time.Clock()#Cria um relogio que nos permite usar waits

FPS = 60
botaoNew = Botao('imagem/novojogo.png',(100,300),1)#Iniciando Botao Jogar 
botaoCredito = Botao('imagem/creditos.png',(100,400),1)#Iniciando Botao Creditos
botaoHistorico = Botao('imagem/historico.png',(100,500),1)#Iniciando Botao Rank
botaoOptions = Botao('imagem/options.png',(100,600),1)#Iniciando Botao Opções
botaoNew_SOBRE = Botao('imagem/novojogo_SOBRE.png',(100,300),1)#Iniciando Botao Jogar com caracteristica SOBRE 
botaoCredito_SOBRE = Botao('imagem/creditos_SOBRE.png',(100,400),1)#Iniciando Botao Credito com caraacteristica SOBRE
botaoHistorico_SOBRE = Botao('imagem/historico_SOBRE.png',(100,500),1)#Iniciando Botao Historico com caracteristica SOBRE
botaoOptions_SOBRE = Botao('imagem/options_SOBRE.png',(100,600),1)#Iniciando Botao Opções com caracteristica SOBRE
botaoNew_PRESS = Botao('imagem/novojogo_PRESS.png',(100,300),1)#Iniciando Botao Jogar com caracteristica PRESS
botaoCredito_PRESS = Botao('imagem/creditos_PRESS.png',(100,400),1)#Iniciando Botao Creditos com caracteristica PRESS
botaoHistorico_PRESS = Botao('imagem/historico_PRESS.png',(100,500),1)#Iniciando Botao Rank com caracteristica PRESS
botaoOptions_PRESS = Botao('imagem/options_PRESS.png',(100,600),1)#Iniciando Botao Opções com caracteristica PRESS
Titulo = Botao('imagem/nome.png',(200, 50),1)#Iniciando Titulo

lista_botoes_PRESS = [botaoNew_PRESS,botaoCredito_PRESS,botaoHistorico_PRESS,botaoOptions_PRESS,Titulo] # Inicia lista de botões caracterizados com PRESS
lista_botoes_SOBRE = [botaoNew_SOBRE,botaoCredito_SOBRE,botaoHistorico_SOBRE,botaoOptions_SOBRE,Titulo] # Inicia lista de botões caracteizados com SOBRE
chartag = randint(0,8) # Selecioa um personagam aleatoriamente para iniciar a variavel chartag e mostrar para jogadores que não entrarem no menu Opções, que existem personagens diferentes

save = loadgame() # da Load no Rank

while True:
	som_menu.play() #Toca a musica do jogo
	for event in pygame.event.get():#captura eventos na janela 
		if event.type == QUIT: #Verifica se o evento capturado é QUIT, que indica a intenção de fechar a janela pelo "x"
			exit()

	#Code here
	if botaoNew.Pressed(): Play(chartag) #Abre o jogo principal
	elif botaoCredito.Pressed(): Creditos() #Abre a janela de creditos
	elif botaoHistorico.Pressed(): Ranks() #Abre a janela de Ranks
	elif botaoOptions.Pressed(): #Abre a janela de Opções
		chartag = Options() #A janela Opções retorna qual personagem o jogador escolheu

	lista_botoes = [botaoNew,botaoCredito,botaoHistorico,botaoOptions,Titulo]
	for button in lista_botoes: #Verifica se cada botão foi clicado
		if button.Sobre():
			lista_botoes[lista_botoes.index(button)] = lista_botoes_SOBRE[lista_botoes.index(button)]
			if button.Pressed():
				lista_botoes[lista_botoes.index(button)] = lista_botoes_PRESS[lista_botoes.index(button)]
	blitz(screen,background,lista_botoes,[],clock,FPS) #Blita os botoes

	pygame.display.update() #Atualiza a Janela
	clock.tick(FPS)# Wait .tick(x) Seg/x




