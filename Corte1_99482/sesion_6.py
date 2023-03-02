print('Escoja una de las siguientes opciones:\n ')
print('1. For in range(final)')
print('2. For in range(inicio,final)')
print('3. For in range(inicio, final, paso)')

OPC=input('Escoja una opcion: ')

if OPC == '1':
    for i in range(10):
        print(i+1)
    print('Fin del proceso')

elif OPC == '2':
    for i in range(5):
        print(i+1)

elif OPC == '3':
    for i in range(10,21,2):
        print(i-1)
    print('Fin del proceso')
