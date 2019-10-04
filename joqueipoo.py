
print("---JO,KEN,PO---\n")
from random import randint
from time import sleep

itens = ("pedra", "papel", "tesoura")
computador = randint(0, 2)
print("""Suas opções:
[0] pedra
[1] papel
[2] tesoura""")
jogador = int(input("Qual é a sua jogada? "))
print("-=" * 11)
sleep(1)
print("Jo")
sleep(1)
print("Ken")
sleep(1)
print("Po\n")
sleep(1)
print("-=" * 11)
print("jogador jogou {}".format(itens[jogador]))
print("Computador jogou {}".format(itens[computador]))
print("-=" * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA!')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA!\n')

