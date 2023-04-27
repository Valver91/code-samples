import os
from pathlib import Path
from os import system

ruta_recetas = Path("D:\Programacion\Curso Phyton\zz\proyecto dia 6\Recetas")

def cuenta_recetas(ruta):
    cantidad = 0
    for txt in Path(ruta).glob("**/*.txt"):
        cantidad += 1
    return cantidad

def inicio():
    system('cls')
    print('\n' + '*' * 20 + '\n')
    print("¡¡Bienbenido a tu recetario!!\n")
    print(f"La ruta donde se encuentra las recetas es: \n{ruta_recetas}")
    print('\n' + '*' * 20 + '\n')
    print(f"Dispode de {cuenta_recetas(ruta_recetas)} recetas.")
    print('\n' + '*' * 20 + '\n')

    seleccion_menu = '0'
    while not seleccion_menu.isnumeric() or int(seleccion_menu) not in range(1,7):
        print("*** Menu Principal ***")
        print("1.- Ver recetas")
        print("2.- Nueva receta")
        print("3.- Crear categoria")
        print("4.- Eliminar receta")
        print("5.- Eliminar categoria")
        print("6.- Finalizar codigo")
        seleccion_menu = input("Ingrese a que menu desea acceder: ")
    return int(seleccion_menu)

def categorias(ruta):
    print("Categorias: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias

def elegir_categorias(lista):
    corrector = 's'
    while not corrector.isnumeric() or int(corrector) not in range(1, len(lista) + 1):
        corrector = input("\n Seleccione categoria: ")
    return lista[int(corrector) - 1]

def recetas(ruta):
    print("Recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas

def elegir_recetas(lista):
    corrector = 'y'
    while not corrector.isnumeric() or int(corrector) not in range(1, len(lista) + 1):
        corrector = input("\n Seleccione receta: " )
    return lista[int(corrector) - 1]        

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False
    while not existe:
        print("Nombre de tu receta: ")
        nombre_receta = input() + ".txt"
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        crear_ruta = Path(ruta, nombre_receta)

        if not os.path.exists(crear_ruta):
            Path.write_text(crear_ruta, contenido_receta)
            print(f"La receta {nombre_receta} ya ha sido creada")
            existe = True
        else:
            print("Esa receta ya existe")

def crear_categoria(ruta):
    existe = False
    while not existe:
        print("Nombre de tu categoria: ")
        nombre_categoria = input()
        crear_ruta = Path(ruta, nombre_categoria)

        if not os.path.exists(crear_ruta):
            Path.mkdir(crear_ruta)
            print(f"La categoria {nombre_categoria} ya ha sido creada")
            existe = True
        else:
            print("Esa categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    volver = 'y'
    while volver.lower() != 'v':
        volver = input("\nPresione 'V' para volver al inicio: ")

cerrar_programa = False
while not cerrar_programa:
    menu = inicio()
    if menu == 1:
        mis_categorias = categorias(ruta_recetas)
        mi_categoria = elegir_categorias(mis_categorias)
        mis_recetas = recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("No hay recetas en esta categoria.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_receta(mi_receta) 
        volver_inicio()
    elif menu == 2:
        mis_categorias = categorias(ruta_recetas)
        mi_categoria = elegir_categorias(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
    elif menu == 3:
        crear_categoria(ruta_recetas)
        volver_inicio()
    elif menu == 4:
        mis_categorias = categorias(ruta_recetas)
        mi_categoria = elegir_categorias(mis_categorias)
        mis_recetas = recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
    elif menu == 5:
        mis_categorias = categorias(ruta_recetas)
        mi_categoria = elegir_categorias(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
    elif menu == 6:
        cerrar_programa = True