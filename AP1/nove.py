a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
c = int(input("Digite outro valor: "))

maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(maior)




