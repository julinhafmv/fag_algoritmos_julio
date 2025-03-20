

num_sensores = int(input("Digite o numero de sensores: "))
soma_temps = 0 

temperaturas = []

for sensor in range(num_sensores):
    temperatura = float(input("Digite a temperatura do sensor {sensor + 1}:"))
    temperaturas.append(temperatura)

for temp in temperaturas:
    soma_temps = soma_temps + temp 

media = soma_temps / num_sensores
media_arredondada = round(media,2)
print (f"A temperatura média é {media_arredondada} C°")

temp_max = max(temperatura)
temp_min = min(temperatura)
print(f"A temperatura máxima é {temp_max}C°")
print(f"A temperatura mínima é {temp_min}C°")

for classe in temperaturas:
    if classe <= 15:
        print(f"Temperatura Baixa:{classe}")
    elif classe > 15:
        print(f"Temperatura Normal:{classe}")
    elif classe > 30:
        print(f"Temperatura Alta:{classe}")



