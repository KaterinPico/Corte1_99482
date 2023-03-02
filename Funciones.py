def suma(a,b):
    resultado= a+b
    return resultado
def imprimir(nombre):
    print(nombre,'su resultado es: ')

n = 'si'
while n== 'si': 
    nombre = input('Ingrese su nombre: ')
    a=int(input('Ingrese un numero: '))
    b=int(input('Ingrese un numero: '))
    res = suma(a,b)
    imprimir(nombre)
    print(res)
    n = input('¿Quiere sumar otro número? (si/no): ')
    
    