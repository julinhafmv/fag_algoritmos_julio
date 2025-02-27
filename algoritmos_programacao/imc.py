pessoa_peso = float(input("Qual o peso?"))
pessoa_altura = float(input("Qual a altura?:"))

soma_imc = pessoa_peso /  (pessoa_altura * pessoa_altura)

if soma_imc <= 20: 
    print("Abaixo do peso")

elif soma_imc >= 100:
    print("Acima do peso")

else soma_imc <= 50:
    print("Peso ideal")