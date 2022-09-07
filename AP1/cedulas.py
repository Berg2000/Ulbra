valor=int(input("Digite um valor: "))
cedulas=0
valorcedulaatual=100
valoraserentregue=valor 
while True:
        if valorcedulaatual <= valoraserentregue:
            cedulas +=1
            valoraserentregue -= valorcedulaatual
        else:
            print("%d cédulas(s) de R$ %5.2f" % (cedulas, valorcedulaatual))
            if valoraserentregue == 0:
                break
            if valorcedulaatual == 100:
                valorcedulaatual = 50
            elif valorcedulaatual == 50:
                valorcedulaatual = 20
            elif valorcedulaatual == 20:
                valorcedulaatual = 10
            elif valorcedulaatual == 10:
                valorcedulaatual = 5
            elif valorcedulaatual == 5:
                valorcedulaatual = 2
            elif valorcedulaatual == 2:
                    valorcedulaatual = 1
            cedulas = 0 

