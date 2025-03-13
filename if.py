print ("Olá, seja bem vindo")

nome = str (input ( "Por gentileza, informe seu nome:"))
idade = int ( input ( "Agora, me informe sua idade: ") )
altura = float (input ( "Qual é a sua altura, em metros?:"))
autorização =  ( input ( "Você possui autorização? sim ou não?: "))

if autorização == 'sim':
    autorização = True
else:
    autorização = False

if idade >= 18 and altura >= 1.50 and autorização == True :
    print ( nome , " Acesso permitido. Você atende a todos os requisitos!")

elif idade >=18 and altura <1.50 and autorização == True :
   print ( nome, "Acesso negado. Altura inferior a 1.50")

elif idade >=18 and altura >= 1.50 and autorização == False:
    print ( nome, "Acesso negado. Você não tem autorização.")

elif idade <18 and altura >=1.50 and autorização == True :
    print ( nome, "Acesso negado. Você não tem 18 anos.")

elif idade <18 and altura < 1.50 and autorização == True :
    print ( nome, "Acesso negado. Você não tem 18 anos e sua altura é inferior a 1.50")

elif idade <18 and altura >=1.50 and autorização == False :
    print ( nome, "Acesso negado. Você não tem 18 anos e não tem autorização.")

elif idade >=18 and altura < 1.50 and autorização == False :
    print ( nome, "Acesso negado. Sua altura é inferior a 1.50 e você não tem autorização.")

elif idade < 18 and altura < 1.50 and autorização == False :
    print ( nome, "Acesso negado. Você não atende a nenhum dos requisitos")




