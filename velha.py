import random
from time import sleep

# menu 
def menu():
    print('Escolha uma das opções:\n1) Novo Jogo\n2) Instruçoes\n3) Historico\n4) Sair')
    print('Digite: ')
    opcao = int(input())

    if opcao == 1:
        print('Vamos começar!!!')
        sleep(2)
        return imprime_tabuleiro(tab)
    elif opcao == 2:
        print('Ao selecionar "Novo Jogo" você será direcionado a escolher os nomes dos\njogadores,após escolher os nomes será feito um sorteio para decidir\nquem começa. Para jogar, o jogador selecionado para começar precisa escolher\na posição em que irá jogar de acordo com os numeros e assim sucesivamente.\nO objetivodo jogo é fazer uma sequência de três símbolos iguais, seja em\nlinha vertical, horizontal ou diagonal, quem fizer primeiro vence o jogo.\n')
        sleep(5)
        return menu()
    elif opcao == 3:
        return historico()
    elif opcao == 4:
        print('Saindo... XD')
    else:
        print('Escolha uma das opçoes acima!!!')
#  #  #  #


# historico
def historico():
    print(imprime_tabuleiro(tab))
#  #  #  #

def imprime_tabuleiro(tab):
	print ("O status do tabuleiro é\n")

	for indice in range(len(tab)):
		print (tab[indice], end=" ")
		if indice == 2 or indice == 5 or indice == 8:
			print ("")
        

def verifica_tabuleiro(tab, jogador):
	
	# testando linhas
	if tab[0] == jogador and tab[1] == jogador and tab[2] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	if tab[3] == jogador and tab[4] == jogador and tab[5] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	if tab[6] == jogador and tab[7] == jogador and tab[8] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2

	# testando colunas
	if tab[0] == jogador and tab[3] == jogador and tab[6] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	if tab[1] == jogador and tab[4] == jogador and tab[7] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	if tab[2] == jogador and tab[5] == jogador and tab[8] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	
	# testando diagonais
	if tab[0] == jogador and tab[4] == jogador and tab[8] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	if tab[2] == jogador and tab[4] == jogador and tab[6] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2

	return 0


quantidade_escolhas = 0	

tab = ["_"] * 9

while True:

	escolha = int(input("Qual é a sua escolha?"))

	while tab[escolha-1] != "_":
		print ("Sua escolha foi inválida! Veja como está o tabuleiro:")
		imprime_tabuleiro(tab)
		escolha = int(input("Qual é a sua escolha? "))

	tab[escolha-1] = "X"
	quantidade_escolhas += 1

	vencedor = verifica_tabuleiro(tab,"X")

	if vencedor != 0:
		break

	if quantidade_escolhas == 9:
		break

	imprime_tabuleiro(tab)

	escolha_computador = random.randint(1,9)
	while tab[escolha_computador-1] != "_":
		escolha_computador = random.randint(1,9)

	tab[escolha_computador-1] = "O"
	quantidade_escolhas += 1

	vencedor = verifica_tabuleiro(tab,"O")
	if vencedor != 0:
		break
	imprime_tabuleiro(tab)

if vencedor == 1:
	print ("parabéns, você ganhou!")
elif vencedor == 2:
	print ("Você perdeu, o computador ganhou!")
else:
	print ("Deu velha, ninguém venceu, foi empate!")

imprime_tabuleiro(tab)

menu()