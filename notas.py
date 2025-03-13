num_provas = int (input( "Digite o número de provas:  "))
acumulado = 0

for  i in range (num_provas):
    acumulado += float (input( f"Digite a nota da prova {i+1}: "))

media = acumulado / num_provas

print ("A sua média é:" , media)



