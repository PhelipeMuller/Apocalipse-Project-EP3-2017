#Função que retorna, de acordo com a entrada, a posição de cada um dos blocks, imagem de fundo e etc
from classObjeto import *
def MapaBase(entrada):
	Objetos = [0]*91
	Objetos[0] = Objeto(True,"imagem/wall.png",[0,0])
	Objetos[1] = Objeto(True,"imagem/wall.png",[1,0])
	Objetos[2] = Objeto(True,"imagem/wall.png",[2,0])
	Objetos[3] = Objeto(True,"imagem/wall.png",[3,0])
	Objetos[4] = Objeto(True,"imagem/wall.png",[4,0])
	Objetos[5] = Objeto(True,"imagem/wall.png",[5,0])
	Objetos[6] = Objeto(True,"imagem/wall.png",[6,0])
	Objetos[7] = Objeto(True,"imagem/wall.png",[7,0])
	Objetos[8] = Objeto(True,"imagem/wall.png",[8,0])
	Objetos[9] = Objeto(True,"imagem/wall.png",[9,0])
	Objetos[10] = Objeto(True,"imagem/wall.png",[10,0])
	Objetos[11] = Objeto(True,"imagem/wall.png",[11,0])
	Objetos[12] = Objeto(True,"imagem/wall.png",[12,0])
	Objetos[13] = Objeto(True,"imagem/wall.png",[12,1])
	Objetos[14] = Objeto(True,"imagem/wall.png",[12,2])
	Objetos[15] = Objeto(True,"imagem/wall.png",[12,3])
	Objetos[16] = Objeto(True,"imagem/wall.png",[12,4])
	Objetos[17] = Objeto(True,"imagem/wall.png",[12,5])
	Objetos[18] = Objeto(True,"imagem/wall.png",[12,6])
	Objetos[19] = Objeto(True,"imagem/wall.png",[12,7])
	Objetos[20] = Objeto(True,"imagem/wall.png",[12,8])
	Objetos[21] = Objeto(True,"imagem/wall.png",[12,9])
	Objetos[22] = Objeto(True,"imagem/wall.png",[12,10])
	Objetos[23] = Objeto(True,"imagem/wall.png",[12,11])
	Objetos[24] = Objeto(True,"imagem/wall.png",[12,12])
	Objetos[25] = Objeto(True,"imagem/wall.png",[11,12])
	Objetos[26] = Objeto(True,"imagem/wall.png",[10,12])
	Objetos[27] = Objeto(True,"imagem/wall.png",[9,12])
	Objetos[28] = Objeto(True,"imagem/wall.png",[8,12])
	Objetos[29] = Objeto(True,"imagem/wall.png",[7,12])
	Objetos[30] = Objeto(True,"imagem/wall.png",[6,12])
	Objetos[31] = Objeto(True,"imagem/wall.png",[5,12])
	Objetos[32] = Objeto(True,"imagem/wall.png",[4,12])
	Objetos[33] = Objeto(True,"imagem/wall.png",[3,12])
	Objetos[34] = Objeto(True,"imagem/wall.png",[2,12])
	Objetos[35] = Objeto(True,"imagem/wall.png",[1,12])
	Objetos[36] = Objeto(True,"imagem/wall.png",[0,12])
	Objetos[37] = Objeto(True,"imagem/wall.png",[0,11])
	Objetos[38] = Objeto(True,"imagem/wall.png",[0,10])
	Objetos[39] = Objeto(True,"imagem/wall.png",[0,9])
	Objetos[40] = Objeto(True,"imagem/wall.png",[0,8])
	Objetos[41] = Objeto(True,"imagem/wall.png",[0,7])
	Objetos[42] = Objeto(True,"imagem/wall.png",[0,6])
	Objetos[43] = Objeto(True,"imagem/wall.png",[0,5])
	Objetos[44] = Objeto(True,"imagem/wall.png",[0,4])
	Objetos[45] = Objeto(True,"imagem/wall.png",[0,3])
	Objetos[46] = Objeto(True,"imagem/wall.png",[0,2])
	Objetos[47] = Objeto(True,"imagem/wall.png",[0,1])

	Objetos[48] = Objeto(True,"imagem/wall.png",[1,5])
	Objetos[49] = Objeto(True,"imagem/wall.png",[1,8])
	Objetos[50] = Objeto(True,"imagem/wall.png",[2,5])
	Objetos[51] = Objeto(True,"imagem/wall.png",[2,8])
	Objetos[52] = Objeto(True,"imagem/wall.png",[3,5])
	Objetos[53] = Objeto(True,"imagem/wall.png",[3,8])
	Objetos[54] = Objeto(True,"imagem/wall.png",[3,9])
	Objetos[55] = Objeto(True,"imagem/wall.png",[3,10])
	Objetos[56] = Objeto(True,"imagem/wall.png",[4,1])
	Objetos[57] = Objeto(True,"imagem/wall.png",[4,2])
	Objetos[58] = Objeto(True,"imagem/wall.png",[4,4])
	Objetos[59] = Objeto(True,"imagem/wall.png",[4,5])
	Objetos[60] = Objeto(True,"imagem/wall.png",[4,7])
	Objetos[61] = Objeto(True,"imagem/wall.png",[4,8])
	Objetos[62] = Objeto(True,"imagem/wall.png",[5,1])
	Objetos[63] = Objeto(True,"imagem/wall.png",[5,4])
	Objetos[64] = Objeto(True,"imagem/wall.png",[5,7])
	Objetos[65] = Objeto(True,"imagem/wall.png",[5,10])
	Objetos[66] = Objeto(True,"imagem/wall.png",[6,1])
	Objetos[67] = Objeto(True,"imagem/wall.png",[6,4])
	Objetos[68] = Objeto(True,"imagem/wall.png",[6,7])
	Objetos[69] = Objeto(True,"imagem/wall.png",[6,10])
	Objetos[70] = Objeto(True,"imagem/wall.png",[7,1])
	Objetos[71] = Objeto(True,"imagem/wall.png",[7,4])
	Objetos[72] = Objeto(True,"imagem/wall.png",[7,10])
	Objetos[73] = Objeto(True,"imagem/wall.png",[8,1])
	Objetos[74] = Objeto(True,"imagem/wall.png",[8,4])
	Objetos[75] = Objeto(True,"imagem/wall.png",[8,5])
	Objetos[76] = Objeto(True,"imagem/wall.png",[8,7])
	Objetos[77] = Objeto(True,"imagem/wall.png",[8,10])
	Objetos[78] = Objeto(True,"imagem/wall.png",[9,1])
	Objetos[79] = Objeto(True,"imagem/wall.png",[9,4])
	Objetos[80] = Objeto(True,"imagem/wall.png",[9,5])
	Objetos[81] = Objeto(True,"imagem/wall.png",[9,6])
	Objetos[82] = Objeto(True,"imagem/wall.png",[9,7])
	Objetos[83] = Objeto(True,"imagem/wall.png",[10,1])
	Objetos[84] = Objeto(True,"imagem/wall.png",[10,7])
	Objetos[85] = Objeto(True,"imagem/wall.png",[10,10])
	Objetos[86] = Objeto(True,"imagem/wall.png",[11,1])
	Objetos[87] = Objeto(True,"imagem/wall.png",[11,2])
	Objetos[88] = Objeto(True,"imagem/wall.png",[11,3])
	Objetos[89] = Objeto(True,"imagem/wall.png",[11,4])
	Objetos[90] = Objeto(True,"imagem/wall.png",[11,10])




	Fundo = 'imagem/MainFloor.png'

	if entrada == "OBJETO":return Objetos
	if entrada == "FUNDO": return Fundo