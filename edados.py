#Crie um programa que a pessoa insira 3 notas do aluno, calcule a média e insira o nome e a situação do aluno em um dicionário.
#Média abaixo de 3, reprovado; Média de 4 a 6,9, Final; e Média 7 para cima, aprovado.

soma=0

for i in range(1,4):
    nota=int(input("Digite a {} nota do aluno: ".format(i)))
    soma += nota
    media = soma / 3
print('A media do aluno é: {:.1f}'.format(media))

if 6.9 > media >= 4:
    print('Reculperação')
if media <= 3:
    print("Reprovado")
if media >= 7:
    print("Aprovado")

dic={}
nome = input("Digite o nome do aluno:")
dic['Nome'] = nome
dic['Situação'] = input("Digite asituação do aluno:")
print(dic)

#Crie um programa que você insere a letra do primeiro e ultimo nome da pessoa e obtenha o nome hacker dessa pessoa.
#Utilize um dicionário de acordo com a figura em anexo.

novo={'a':'SH4DOW','b':'CHIEF','c':'CYBER','d':'M4STER','e':'PRIV4TE','f':'NULL','g':'GENERAL','h':'ACE','i':'TOXIC','j':'CRASH',
    'k':'STEALPH','l':'C4PT4IN','m':'UBER','n':'GRAY','o':'MR','p':'TROOL','q':'BLACK','r':'ROGUE','s':'NINJA','t':'LIQUID',
      'u':'NULL','v':'THE','w':'UBER','x':'N3TWORK','y':'FIRE','z':'ZERO'}
outro = {'a':'BET4', 'b':'ANGEL', 'c':'WIRE', 'd':'PL4GUE', 'e':'SKELETON',
            'f':'B4RCODE', 'g':'DESTROVER', 'h':'FRE4K', 'i':'BOT', 'j':'X',
            'k':'HYORA', 'l':'BYTE', 'm':'PH4TOM', 'n':'DELTA', 'o':'NIGHT',
            'p':'CRACK', 'q':'SHARK', 'r':'ZERO', 's':'ROOT', 't':'ANTRAX',
            'u':'VIRUS', 'v':'SILENCE', 'w':'SAINT', 'x':'L3G3ND', 'y':'OV3RORIVE',
            'z':'OMICRON'}

q = input("Digite o seu nome: ")
w = input('Digite a primeira letra do seu sobrenome: ')

print("Seu nome de hacker é:",novo[q[0]],outro[w[0]])

