n_sensores = int(input("Digite a quantidade de sensores: "))
soma_temps = 0


temperaturas = []

for sensor in range(n_sensores):
    temperatura = float(input(f"Digite a temperatura do sensor {sensor + 1}: "))
    temperaturas.append(temperatura)


for temp in temperaturas:
    soma_temps = soma_temps + temp
    

media = soma_temps / n_sensores
media_arredondada = round(media,2)
print (f"A temperatura média é {media_arredondada} C°")


temperatura_max = max(temperaturas)
temperatura_min = min(temperaturas)
print (f"A temperatura máxima é de {temperatura_max}")
print (f"A temperatura mínima é de {temperatura_min}")

for classificação in temperaturas:
    if classificação <= 15 :
        print (f"Baixa:{classificação}")
    elif classificação > 15 and classificação <= 30 :
        print (f"Normal:{classificação}")
    elif classificação > 30 :
        print (f"Alta:{classificação}")