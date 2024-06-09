from data_stark import lista_personajes
from data_stark_funciones import *


def menu_principal():
    while True:
        print('\nMenú de opciones:')
        print('1. Mostrar nombres de superhéroes')
        print('2. Mostrar nombres y alturas de superhéroes')
        print('3. Determinar el superhéroe más alto')
        print('4. Determinar el superhéroe más bajo')
        print('5. Calcular la altura promedio de los superhéroes')
        print('6. Informar el nombre del superhéroe más alto y más bajo')
        print('7. Determinar el superhéroe más pesado y menos pesado')
        print('8. Salir')

        opcion = input('Elija una opción: ')

        match opcion:
            case '1':
                mostrar_nombres(lista_personajes)
            case '2':
                mostrar_nombres_y_alturas(lista_personajes)
            case '3':
                mas_alto = buscar_mas_alto(lista_personajes)
                print(f'El superhéroe más alto es {mas_alto['nombre']} con una altura de {mas_alto['altura']} cm')
            case '4':
                mas_bajo = buscar_mas_bajo(lista_personajes)
                print(f'El superhéroe más bajo es {mas_bajo['nombre']} con una altura de {mas_bajo['altura']} cm')
            case '5':
                altura_promedio = calcular_altura_promedio(lista_personajes)
                print(f'La altura promedio de los superhéroes es {altura_promedio:.2f} cm')
            case '6':
                mas_alto = buscar_mas_alto(lista_personajes)
                mas_bajo = buscar_mas_bajo(lista_personajes)
                print(f'El superhéroe más alto es {mas_alto['nombre']}')
                print(f'El superhéroe más bajo es {mas_bajo['nombre']}')
            case '7':
                mas_pesado = buscar_mas_pesado(lista_personajes)
                menos_pesado = buscar_menos_pesado(lista_personajes)
                print(f'El superhéroe con mas peso es {mas_pesado['nombre']} y pesa {mas_pesado['peso']} kg')
                print(f'El superhéroe con menos peso es {menos_pesado['nombre']} y pesa {menos_pesado['peso']} kg')
            case '8':
                print('Abanadonando programa...')
                break
            case _:
                print('Esa opcion es invalida. Elija del 1 al 8')

menu_principal()
