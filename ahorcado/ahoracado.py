from random import *

palabras = ["jarra", "economia", "amarillo", "catorce", "panadero", "silla", "pierna"]
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas

def pedir_letras():
    letra_elegida = ""
    es_valida = False
    abecedario = "abcdefghijklmnñopqrstuwxyz"

    while not es_valida:
        letra_elegida = input("Elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")
    
    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append("_")
    
    print(" ".join(lista_oculta))

def corregir_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has encontrado esa letra, intenta con otra.")
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
    
    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    
    return vidas, fin, coincidencias

def perder():
    print("Te has quedad sin vidas")
    print("La palabra oculta era: " + palabra)

    return True

def ganar(palabra_descubrierta):
    mostrar_nuevo_tablero(palabra_descubrierta)
    print("Felicidades, has descubierto la palabra!!")

    return True

palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f"vidas: {intentos}")
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letras()

    intentos, terminado, aciertos = corregir_letra(letra, palabra, intentos, aciertos)
    juego_terminado = terminado