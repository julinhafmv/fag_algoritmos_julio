

numero = int (input ("Até que número você quer somar?  "))
soma = 0
''''
#Resolvendo com While

i = 1 #contador

while i <= numero:
    soma += numero
    numero -= 1

print (soma)


'''

for i in range (numero):
    soma += (i +1)
print (soma)
