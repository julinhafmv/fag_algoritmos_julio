'''
def cadastrar_alunos(alunos):
    while True:
        continuar = input("Quer cadastrar um aluno novo? (s/n)").lower()
        if continuar == "n":
            break
        nome = input("Qual o nome do aluno? ")
        p1 = float(input("Qual o nota da p1? "))
        p2 = float(input("Qual o nota da p2? "))
        p3 = float(input("Qual o nota da p3? "))
        alunos[nome] = {"p1": p1, "p2": p2, "p3": p3}
    return alunos
'''

def calcular_media(alunos):
    for aluno in alunos:
        alunos[aluno]["media"] = (alunos[aluno]["p1"] + alunos[aluno]["p2"])/2

def apagar_p3(alunos):
    notas_p3 = {}
    for chave, valor in alunos.items():
        notas_p3[chave] = alunos[chave].pop("p3")
    return notas_p3

def listar_alunos(alunos):
    for chave, valor in alunos.items():
        print(f"O aluno {chave} tirou:\n{valor["p1"]} na primeira prova\n{valor["p2"]} na segunda prova")
        print(f"A média final é {valor["media"]}")

def listar_aprovados(alunos):
    for chave, valor in alunos.items():
        if valor["media"] >= 7:
            print(f"Parabéns {chave}, você foi aprovado!")


#turma = {'Julio': {'p1': 4.0, 'p2': 5.0, 'media': 4.5}, 'Antonio': {'p1': 6.0, 'p2': 7.0, 'media': 6.5}}
#alunos = cadastrar_alunos(turma)
alunos = {'Julio': {'p1': 4.0, 'p2': 5.0, 'media': 4.5}, 
          'Antonio': {'p1': 10.0, 'p2': 7.0, 'media': 6.5}}
calcular_media(alunos)
#notas_p3 = apagar_p3(alunos)
listar_alunos(alunos)

listar_aprovados(alunos)