############################# contar os alunos #############################

def coleta_alunos():
    num_alunos = int(input('Quantos alunos tem? '))
    return num_alunos

############################# pedir notas ############################# 

def coleta_notas(num_alunos):
    notas = []
    for a in range(num_alunos):
        recebe_notas = float(input(f'Qual a nota do aluno {a + 1}? '))
        notas.append(recebe_notas)
    return notas

############################# calcular a media #############################

def media(notas):
    return sum(notas) / len(notas)

############################## nota max/min #############################

def notamax(notas):
    return max(notas)

def notamin(notas):
    return min(notas)

############################# classificar notas #############################

def classificar(notas, media):
    classificação = []
    for b in notas:
        if b < media:
            classificação.append("abaixo da média")
        elif b == media:
            classificação.append('na média')
        else:
            classificação.append('acima da média')
    return classificação

############################## retorno de todos os dados #############################

def dados(notas, media, notamax, notamin, classificação):
    print("")
    print(f"As notas são: {notas}")
    print("")
    print(f"Média das notas: {media:.2f}")
    print("")
    print(f"A maior nota é: {notamax}")
    print(f"A menor nota é: {notamin}")
    print("")
    print("Notas Classificadas:")
    for i, c in enumerate(classificação, 1):
        print(f"Aluno {i}: {c}")
    print("")

############################## Execução ##############################

num_alunos = coleta_alunos()
notas = coleta_notas(num_alunos)
media_valor = media(notas)
max_nota = notamax(notas)
min_nota = notamin(notas)
classificação = classificar(notas, media_valor)
dados(notas, media_valor, max_nota, min_nota, classificação)
