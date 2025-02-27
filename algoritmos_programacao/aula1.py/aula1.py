nota1 = float (input("Digite a nota da prova 1: ")) 
nota2 = float (input("Digite a nota da prova 2: ")) 
nota3 = float (input("Digite a nota da prova 3: ")) 

num_provas = 3

soma_notas = nota1 + nota2 + nota3
media = soma_notas / num_provas 

if media >= 7: 
    print ("Passou")
elif media >= 3: 
    print ("Recuperação")

    

print("Sua media é", media)