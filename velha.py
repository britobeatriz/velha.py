# bibliotecas
from time import sleep
#  #  #  #

tabuleiro = [['_','_','_'],['_','_','_'],['_','_','_']]
jogador1 = "X"
jogador2 = "O"



# jogo
def jogo():
    print('--------------------------JOGO DA VELHA--------------------------')
    for i in range(0, 3):
        print()
        print('                         ',
              tabuleiro[i][0],'|', tabuleiro[i][1],'|', tabuleiro[i][2])
    print()
#  #  #  #

# menu 
def menu():
    print('Escolha uma das opções:\n1) Novo Jogo\n2) Instruçoes\n3) Sair')
    print('Digite: ')
    opcao = int(input())

    if opcao == 1:
        print('Vamos começar!!!')
        sleep(2)
        return jogo()
    elif opcao == 2:
        print('Ao selecionar "Novo Jogo" você será direcionado a escolher os nomes dos\njogadores,após escolher os nomes será feito um sorteio para decidir\nquem começa. Para jogar, o jogador selecionado para começar precisa escolher\na posição em que irá jogar de acordo com os numeros e assim sucesivamente.\nO objetivodo jogo é fazer uma sequência de três símbolos iguais, seja em\nlinha vertical, horizontal ou diagonal, quem fizer primeiro vence o jogo.\n')
        sleep(5)
        return menu()
    elif opcao == 3:
        print('Saindo... XD')
    else:
        print('Escolha uma das opçoes acima!!!')

menu()
#  #  #  #