def coletar_notas():
    n_alunos = int(input("Digite o número de alunos: "))
    return n_alunos


def coletar_notas(n_alunos):
    notas = []
    for nt in range(1, n_alunos + 1):
        nota = float(input(f"Digite a nota do aluno {nt}: "))
        notas.append(nota)
    return notas


def dados(notas):
    media = sum(notas) / len(notas)

    maior_nota = max(notas)
    menor_nota = min(notas)

    classificacao = []
    for nota in notas:
        if nota < media:
            classificacao.append("Abaixo da média")
        elif nota == media:
            classificacao.append("Na média")
        else:
            classificacao.append("Acima da média")
    return media, maior_nota, menor_nota, classificacao


def exibir_relatorio(media, maior_nota, menor_nota, classificacao):
    print(f"Média das notas: {media:2f}")

    print(f"A maior nota é: {maior_nota}")
    print(f"A menor nota é: {menor_nota}")

    print(f"a Classificação das notas é:")
    for nt, status in enumerate(classificacao, 1):
        print(f"Aluno {nt}: {status}")
    
    print("Relatório completo: ")
    print(f"Média das notas: {media:.2f}")
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")
    for nt, status in enumerate(classificacao, 1):
        print(f"Aluno {nt} foi classificado como: {status}")


def main():
    notas = dados()
    
    media, maior_nota, menor_nota, classificacao = dados(notas)

    exibir_relatorio(media, maior_nota, menor_nota, classificacao)

    main()