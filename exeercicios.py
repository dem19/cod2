#Crie uma lista contendo 100 números inteiros aleatórios entre 0 e 1000 (usando iteração, ´´append´´ e o módulo random).
# Escreva uma função media que recebe uma lista de números como parâmetros e retorna a média dos valores na lista.
# Dica: from random import randint

from random import *
lista=[]
media = lista
for i in range(1, 100+1):
    lista.append(randrange(0, 1000))
print(lista)

soma=0
for nota in media:
    soma += nota
    d = soma / 100
print('A media dos valores é {:.2f}'.format(d))


#Escreva uma função que recebe a lista de inteiros do exercício anterior e retorna o maior valor na lista.
# (Observação: existe uma a função nativa max que faz o serviço, mas você não deve usá-la.)

print("-="*20)
num = lista
maior = 0
for x in num:
    if x > maior:
        print(num)
print("O maior valor na lista", maior)





