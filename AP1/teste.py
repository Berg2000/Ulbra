print("Olá Bem Vindo a Calculadora Simplificada")

v1=float(input("Para começar insira o primeiro valor do seu calculo: "))
v2=float(input("Insira o segundo valor de seu calculo: "))




print("Perfeito, agora vamos escolher qual sera a operação matematica")
print("DIVISÃO, MULTIPLICAÇÃO, ADIÇÃO OU SUBTRAÇÃO")
operacao=str(input("Qual a sua escolha? "))
divisao="DIVISÃO"
multi="MULTIPLICAÇÃO"
sub="SUBTRAÇÃO"
ad="ADIÇÃO"


if (operacao == divisao):
        print("O resultado da DIVISÃO é:", v1/v2)
elif (operacao == multi):
        print("O resultado da MULTIPLICAÇÃO é:", v1*v2)
elif (operacao == ad):
        print("Ovalor da ADIÇÃO é:", v1+v2)
elif (operacao == sub): 
        print("O resultado da SUBTRAÇÃO é:", v1-v2)
else :
    print("Digite uma operaao valida! ")

    