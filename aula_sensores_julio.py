num_sensores = int(input(f"Digite o número de sensores:"))

# PEDIR AS TEMPERATURAS DOS SENSORES E SALVAR UMA LISTA 
temperaturas = []


for sensor in range(num_sensores):
    temperatura = float(input(f"Digite a temperatura do sensor {sensor + 1}: "))
    temperaturas.append(temperatura)

print(temperaturas)

# SOMAR O NUMERO DE SENSORES 
# for temp in temperaturas:
    #print(temp, "C°")
    #print("Proximo loop")

soma_temps = 0 
for temp in temperaturas:
    soma_temps = soma_temps + temp

media = soma_temps / num_sensores
print (f"A temperatura média dos sensores é {media} C°")
   










    






