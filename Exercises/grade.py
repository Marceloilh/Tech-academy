'''Feito por mim em 17/05/2022'''

nome = str(input("Escreva o nome do aluno:"))
notatotal=0
media = 7
nota1 = float(input ("Digite a primeira nota:"))
nota2 = float(input ("Digite a Segunda nota:"))
nota3 = float(input ("Digite a Terceira nota:"))
nota4 = float(input ("Digite a Quarta nota:"))
qnotas = 4

notatotal = (nota1 + nota2 + nota3 + nota4)/qnotas;
if notatotal < media:
    print(nome,"eprovado com nota:", notatotal)
elif  notatotal >= media :
    print(nome, "aprovado com nota:", notatotal)

'''Feito pelo professor'''

prova1 = int(input('Digite a nota da prova 1:'))
trab = int(input('Digite a nota do trabalho:'))
prova2 = int(input('Digite a nota da prova 2:'))

media =((prova1* 2 ) +trab +(prova2 * 2))/5

if media >= 6:
    print('Aluno aprovado!')
else:
    if media > 3:
        print('Aluno em recuperação')
    else:
        print('Aluno em recuperação')

