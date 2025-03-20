def pedir_num_alunos ():
    num_alunos = int(input("Digite o número de alunos:"))
    return num_alunos 

def pedir_notas_aluno (num_alunos):
    notas = []
    for nota in range(num_alunos):
        nota = float(input(f"Digite as notas do aluno:"))
        notas.append(nota)
    return notas

def calcular_media_aluno(lista_notas):
    media = sum(lista_notas)/len(lista_notas)
    return media 

num_alunos = pedir_num_alunos()
notas = pedir_notas_aluno(num_alunos)
media = calcular_media_aluno(notas)

