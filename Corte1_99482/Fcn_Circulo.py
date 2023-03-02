def area(r):
    pi= 3.1416
    A=pi*(r**2)
    return A

def volumen(h,r):
    pi= 3.1416
    A=area(r)
    V=A*h
    return V

r=int(input('Ingrese el valor del radio: '))
h=int(input('Ingrese la altura: '))

A = area(r)
V = volumen(h,r)

print(f'El area es {A} y el volumen es {V}')


