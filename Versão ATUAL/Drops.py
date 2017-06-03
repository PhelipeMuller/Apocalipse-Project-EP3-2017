#Função que retorna caracteristicas dos Drops de acordo com a entrada
from classObjeto import * #Arquivo com a Classe Objeto
from classArma import * #Arquivo com a Classe Arma
def muito():
	return 100000000000000000000000000000000000000000000000000000
def Drop(tag,entrada,Persona,Arma):
	if tag == 0:
		if entrada == "IMAGEM": return "imagem/HeartDrop.png"
		if entrada == "TIME": return 5
		if entrada == "ARMATAG": return 0
		if entrada == "EFEITO":
			if Persona.HP < Persona.HPMax: Persona.HP += 1

	if tag == 1:
		if entrada == "IMAGEM": return "imagem/HeartConteinerDrop.png"
		if entrada == "TIME": return muito()
		if entrada == "ARMATAG": return 0
		if entrada == "EFEITO":
			if Persona.HPMax < Persona.ReallyMAXHP: 
				Persona.HPMax += 1
				Persona.HP += 1
	if tag == 2:
		if entrada == "IMAGEM": return "imagem/uziMini.png"
		if entrada == "TIME": return 10
		if entrada == "ARMATAG": return 1
		if entrada == "ARMA": return Arma(1)
	if tag == 3:
		if entrada == "IMAGEM": return "imagem/metralhadoraMini.png"
		if entrada == "TIME": return 10
		if entrada == "ARMATAG": return 2
		if entrada == "ARMA": return Arma(2)
