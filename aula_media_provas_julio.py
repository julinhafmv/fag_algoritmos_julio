n_provas =  int(input("Quantas provas você teve?"))
soma_notas = 0 

for prova in range (n_provas):
    while True:
        nota = float(input(f"Digite a nota da prova (prova +1):"))
        if nota > 10 or nota < 0:
            print("Nota iválida")
            continue 

        else:
            break

    soma_notas = soma_notas + nota 

media = soma_notas / n_provas 

if media >= 7:
    print("")
