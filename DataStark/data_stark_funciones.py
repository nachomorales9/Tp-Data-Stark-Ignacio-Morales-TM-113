from data_stark import *


for personaje in lista_personajes:
    personaje['altura'] = float(personaje['altura'])
    personaje['peso'] = float(personaje['peso'])

def calcular_altura_promedio(lista):
    total_altura = sum(personaje['altura'] for personaje in lista)
    return total_altura / len(lista)

def buscar_menos_pesado(lista):
    if not lista:
        return None
    menos_pesado = lista[0]
    for personaje in lista[1:]:
        if personaje['peso'] < menos_pesado['peso']:
            menos_pesado = personaje
    return menos_pesado
   
def mostrar_nombres(lista):
    for personaje in lista:
        print(personaje['nombre'])

def buscar_mas_pesado(lista):
    if not lista:
        return None
    mas_pesado = lista[0]
    for personaje in lista[1:]:
        if personaje['peso'] > mas_pesado['peso']:
            mas_pesado = personaje
    return mas_pesado

def mostrar_nombres_y_alturas(lista):
    for personaje in lista:
        print(f"{personaje['nombre']} - {personaje['altura']} cm")

def buscar_mas_alto(lista):
    if not lista:
        return None
    mas_alto = lista[0]
    for personaje in lista[1:]:
        if personaje['altura'] > mas_alto['altura']:
            mas_alto = personaje
    return mas_alto

def buscar_mas_bajo(lista):
    if not lista:
        return None
    mas_bajo = lista[0]
    for personaje in lista[1:]:
        if personaje['altura'] < mas_bajo['altura']:
            mas_bajo = personaje
    return mas_bajo
