#Arquivo que possui as armas em caracteristica, de forma que a função recebendo uma certa etrada, retornará uma devida caracteristica
def muito():
	return 100000000000000000000000000000000000000000000000000000
def Weapon(tag,entrada):
	if tag == 0:
		if entrada == "AMMO": return muito()
		if entrada == "DANO": return 5
		if entrada == "VELO": return 12
		if entrada == "RATE": return 0.7
		if entrada == "DURATION": return 2
		if entrada == "IMAGEM": return "imagem/pistola.png"
	if tag == 1:
		if entrada == "AMMO": return 100
		if entrada == "DANO": return 4
		if entrada == "VELO": return 20
		if entrada == "RATE": return 0.2
		if entrada == "DURATION": return 2
		if entrada == "IMAGEM": return "imagem/uzi.png"
	if tag == 2:
		if entrada == "AMMO": return 50
		if entrada == "DANO": return 5
		if entrada == "VELO": return 25
		if entrada == "RATE": return 0.1
		if entrada == "DURATION": return 2
		if entrada == "IMAGEM": return "imagem/metralhadora.png"
