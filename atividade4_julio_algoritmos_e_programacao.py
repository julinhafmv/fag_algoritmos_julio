def coletar_num_alunos():
    num_alunos = int(input("DIGITE O NUMERO DE ALUNOS:"))
    return num_alunos

def coletar_notas(num_alunos):
    notas = []
    for nt in range(1, num_alunos + 1):
        nota = float(input(f"DIGITE A NOTA DO ALUNO {nt}:"))
        notas.append(nota)
    return notas

def dados(notas):
    media = sum(notas) / len(notas)

    maior_nota = max(notas)
    menor_nota = min(notas)

    classificacao = []
    for nota in notas:
        if nota < media:
            classificacao.append("ABAIXO DA MÉDIA")
        elif nota == media:
            classificacao.append("NA MÉDIA")
        
        else: classificacao.append("ACIMA DA MÉDIA")
        return media, maior_nota, menor_nota, classificacao
    
def exibir_relatorio(media,maior_nota,menor_nota,classificacao):
    print(f"MÉDIA DAS NOTAS: {media:2f}")

    print(f"A MAIOR NOTA É: {maior_nota}")
    print(f"A MENOR NOTA É:{menor_nota}")

    print(f"A CLASSIFICAÇÃO DAS NOTAS É:")
    for nt, status in enumerate(classificacao, 1):
        print(f"ALUNO {nt}: {status}")

    print("RELATÓRIO COMPLETO: ")
    print(f"MÉDIA DAS NOTAS: {media:.2f}")
    print(f"MAIOR NOTA: {maior_nota}")
    print(f"MENOR NOTA: {menor_nota}")
    
    for nt, status in enumerate(classificacao,1):
        print(f"ALUNO {nt} foi classificado como: {status}")

def main():
    num_alunos = coletar_num_alunos()
    notas = coletar_notas(num_alunos)

    media, maior_nota, menor_nota, classificacao = dados(notas)

    exibir_relatorio(media,maior_nota,menor_nota,classificacao)
    if __name__ == "__main__":
        main()




