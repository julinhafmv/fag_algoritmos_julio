############################# contar os alunos #############################

def coleta_alunos():
    num_alunos = int(input('quantos alunos tem?'))
    return num_alunos

############################# pedir notas ############################# 

def coleta_notas(num_alunos):
    notas = []
    for a in range(num_alunos):
        recebe_notas = float(input(f'qual a nota {a +1}?')) 
        notas.append (recebe_notas)
    return notas

############################# calcular a media #############################

def media(notas):
    media = float((sum(notas)) / num_aluno)
    return media 

############################## nota max/min #############################

def notamax(notas):
    notamax = max(notas)
    return notamax

def notamin(notas):
    notamin = min(notas)
    return notamin

############################# classificar notas #############################

def classificar(notas, media):

    classificação = []
    for b in notas:
        if b < media:
            classificação.append("abaixo da média")
        if b == media:
            classificação.append('na média')
        if b > media:
            classificação.append('acima da média')

    return classificação

############################## retorno de todos os dados #############################

def dados(notas, media, notamax, notamin, classificação):
    print(f"As notas são:{notas}")
    print(f"Média das notas: {media:2f}")

    print(f"A maior nota é: {notamax}")
    print(f"A menor nota é: {notamin}")

    print("Notas Classificadas:")
    for c in classificação:
        print(f"Aluno {c + 1} {classificação}")
    

## Execução


num_aluno = coleta_alunos()
notas = coleta_notas(num_aluno)
notas = media(notas)
notamax = notamax(notas)
notamin = notamin(notas)
classificação = classificar (notas, media)
dados(notas, media, notamax, notamin, classificação)




