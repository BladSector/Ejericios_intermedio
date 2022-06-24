'''
listas_1.py
script de Python que permita administrar operaciones sobre una lista.
Dentro del programa existira una lista para almacenar el nombre de distintas
frutas. Para el control de la lista se mostrara un menu con las opciones:
Agregar
Insertar
Mostrar lista
Buscar una frutas
Eliminar el registro
Ordenar lista
Limpiar lista
Salir
'''
import os

frutas = ['Mandarina', 'Naranja', 'Banana', 'Manzana', 'Ciruela', 'Pera']

AGREGAR = 1
INSERTAR = 2
MOSTRAR = 3
BUSCAR = 4
ELIMINAR_R = 5
ORDENAR = 6
LIMPIAR = 7
SALIR = 8

def menu():
    os.system('cls')
    print(f'        Esta es la lista: {frutas}')
    print(f'''    ------------Menu------------
        {AGREGAR})Agregar una fruta
        {INSERTAR})Insertar una fruta en una posicion en especifico
        {MOSTRAR})Mostrar lista
        {BUSCAR})Buscar una fruta o que fruta hay en una posicion
        {ELIMINAR_R})Eliminar registro
        {ORDENAR})Ordenar lista
        {LIMPIAR})Limpiar lista
        {SALIR})Salir
        ''')



def menu_agregar():
    print('       ---Agregar---')
    f_a = input('        Que fruta quieres agregar?: ')
    frutas.append(f_a)
    input('        Registro agregado con exito.')

def menu_insertar():
    print('         ---Insertar---')
    f_i = input('        Que fruta quiere insertar?: ')
    pos = int(input('        En que posicion de la lista?: '))
    pos = pos - 1
    frutas.insert(pos, f_i)
    input('        Registro insertado en la posicion indicada con exito.')

def menu_mostrar():
    print('        ---Mostrar---')
    if len(frutas) > 0:
        for fruta in frutas:
            print(f'         {fruta}')
        else:
            print('')
            input('        No se han agregado frutas a la lista.')

def menu_buscar():
    f_b = input('        Que fruta quiere buscar en la lista?: ')
    print(f'        Su fruta {f_b} esta en la lista?: {f_b in frutas}')
    print(f'        Su fruta esta en la posicion: {frutas.index(f_b)+1}')

    input('')

def menu_eliminar():
    print('        ---Eliminar registro---')
    f_e = input('        Que fruta desea eliminar?: ')
    frutas.remove(f_e)
    input('        Se elimino con exito la fruta seleccionada.')

def menu_ordenar():
    print('        ---Ordenar lista---')
    frutas.sort()
    print(frutas)
    input('')

def menu_limpiar():
    print('        ---Limpiar lista---')
    frutas.clear()
    input('        Se elimino el contenido de la lista con exito.')

def menu_salir():
    print('        Saliendo del programa...')
    exit()


while True:
    menu()
    opc = int(input('        Selecciona una opcion: '))

    if opc == AGREGAR:
        menu_agregar()
    elif opc == INSERTAR:
        menu_insertar()
    elif opc == MOSTRAR:
        menu_mostrar()
    elif opc == BUSCAR:
        menu_buscar()
    elif opc == ELIMINAR_R:
        menu_eliminar()
    elif opc == ORDENAR:
        menu_ordenar()
    elif opc == LIMPIAR:
        menu_limpiar()
    elif opc == SALIR:
        menu_salir()
    else:
        input('        Opcion no valida. Vuelva a intentar.')
