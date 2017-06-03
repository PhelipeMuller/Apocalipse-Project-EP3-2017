import pygame
from pygame.locals import *

pygame.init()#Inicia o uso do pygame

pygame.font.init()#inicia a fonte
font_name = pygame.font.get_default_font()#Define a fonte usada no jogo
game_font = pygame.font.SysFont(font_name, 72)
pygame.mixer.pre_init(44100, 32, 2, 4096)#Inicia o mixer sound do jogo

screen = pygame.display.set_mode((956, 560), 0, 32) #Definindo tamanho da Janela

pygame.display.set_caption('Titulo')#Define o Titulo da janela

clock = pygame.time.Clock()#Cria um relogio que nos permite usar waits
FPS = 60 #Determina o FPS da janela

def get_rect(obj):#Função que retorna o rect do objeto dado (Geralmente usado para Colisões)
	return Rect(obj.position[0],
		obj.position[1],
		obj.imagem.get_width(),
		obj.imagem.get_height())
	
def blitz(screen,background,lista_botoes,lista_texto,clock,FPS):
	#font_name = pygame.font.match_font("PokemonGB", bold=False, italic=False)
	screen.blit(background, (0, 0))#Definição da sufice da tela, area onde coisas podem acontecer
	for botao in lista_botoes:
		screen.blit(botao.imagem, botao.position)
	for texto in lista_texto:
		game_font = pygame.font.SysFont(font_name, texto[1])
		screen.blit(game_font.render(texto[0], False, texto[2]),texto[3])
	pygame.display.update() #Atualiza a Janela
	clock.tick(FPS)# Wait .tick(x) Seg/x

def insert(string,limite):
	key = pygame.key.get_pressed()
	if key[K_BACKSPACE]: string = ""
	elif len(string) < limite:
		if key[K_q]: string += "Q" 
		elif key[K_w]: string += "W"
		elif key[K_e]: string += "E"
		elif key[K_r]: string += "R"
		elif key[K_t]: string += "T"
		elif key[K_y]: string += "Y"
		elif key[K_u]: string += "U"
		elif key[K_i]: string += "I"
		elif key[K_o]: string += "O"
		elif key[K_p]: string += "P"
		elif key[K_a]: string += "A"
		elif key[K_s]: string += "S"
		elif key[K_d]: string += "D"
		elif key[K_f]: string += "F"
		elif key[K_g]: string += "G"
		elif key[K_h]: string += "H"
		elif key[K_j]: string += "J"
		elif key[K_k]: string += "K"
		elif key[K_l]: string += "L"
		elif key[K_z]: string += "Z"
		elif key[K_x]: string += "X"
		elif key[K_c]: string += "C"
		elif key[K_v]: string += "V"
		elif key[K_b]: string += "B"
		elif key[K_n]: string += "N"
		elif key[K_m]: string += "M"
		elif key[K_0]: string += "0"
		elif key[K_1]: string += "1"
		elif key[K_2]: string += "2"
		elif key[K_3]: string += "3"
		elif key[K_4]: string += "4"
		elif key[K_5]: string += "5"
		elif key[K_6]: string += "6"
		elif key[K_7]: string += "7"
		elif key[K_8]: string += "8"
		elif key[K_9]: string += "9"
		elif key[K_SPACE]: string += " "
	return string

def loadgame():
	arq = open('save/save.txt', 'r')
	presave = arq.readlines()
	arq.close()

	save = []
	for linha in presave:
		if not linha == "FINAL":
			lista = [0]*3
			lista[0] = int(linha[0])
			lista[1] = linha[1:4]
			lista[2] = int(linha[4:-1])
			save.append(lista)
	return save

def savegame(info):
	presave = loadgame()
	presave.append(info)
	save = []
	while len(presave) > 0:
		maior = -1
		for rank in presave:
			if rank[2] > maior: 
				maior = rank[2]
				melhor = rank
		save.append(melhor)
		presave.remove(melhor)
	if len(save) > 10: save = save[:-1]
	save.append("FINAL")

	arq = open('save/save.txt',"w")
	for rank in save:
		if rank == "FINAL": arq.writelines(rank)
		else: arq.writelines(str(rank[0])+str(rank[1])+str(rank[2])+"\n")
	arq.close()