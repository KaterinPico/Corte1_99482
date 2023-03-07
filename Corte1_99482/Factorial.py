def factorial(nro):
    i=1
    Fac=nro
    while Fac>1:
        i*=Fac
        Fac-=1
    return i
n=int(input('Ingrese un número: '))
m=int(input('Ingrese otro número: '))
num=factorial(n)
den=factorial(m)*factorial(n-m)
combi=num/den
print('Las combinaciones posibles son: ',combi)
        

