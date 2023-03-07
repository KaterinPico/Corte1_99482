print('Escoja una de las siguientes opciones:\n ')
print('1. Numeros impares')
print('2. Numero factorial')
print('3. Numeros primos')
print('4. Salir')
OPC=input('Escoja una opción: ')
if OPC == '1':
    x=1
    NE=int(input('Ingrese un número entero q sea positivo: '))
    while x <= NE:
        if x % 2 == 1:
            print(x,end=',')
        x+=1
    print('Fin del proceso')

elif OPC == '2':
    N=int(input('Ingrese un número: '))
    Fac=1
    if N!=0:
        for i in range(1,N+1):
            Fac=Fac*i
        print('El factorial es: ',Fac)
        print('Fin del proceso')

elif OPC == '3':
    Num=int(input('Ingrese un número: '))
    x=1
    y=0
    for i in range(2,Num+1):
        primos = True
        for j in range(2,i): 
            if i == j:
                break
            elif i%j==0:
                primos=False
            else:
                continue
        if primos == True:
            print('',i,end='')
            y+=1
    print('\nHay %u números primos.' % y )
    x=1
    y=0
    while x<=Num:
        if Num % x == 0:
            y+=1
        x+=1
    if y == 2:
        print('El número',Num,'es primo')
    else:
        print('El número',Num,'no es primo')
    
    print('Fin del proceso')
