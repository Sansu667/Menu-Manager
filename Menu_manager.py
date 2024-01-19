import os
from pathlib import Path
from os import system

finalizar_programa = False

# Bienvenida
cliente = input("Ingresa tu nombre: ")

# Mostrar la ruta de la carpeta de recetas
directorio_recetas = Path(Path.home(), "Recetas")

# Mostrar la cantidad de recetas dentro de la carpeta
def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador
total_recetas = contar_recetas(directorio_recetas)

# Sección de Inicio
def inicio():
    system("cls")
    print("\n")
    print("*" * 50)
    print("*" * 5 + f" Bienvenido, {cliente}\nEste es el administrador de menús " + "*" * 5)
    print("*" * 50)
    print("\n")
    print(f"- La ruta de la carpeta de recetas es la siguiente: {directorio_recetas}")
    print(f"- Hay {total_recetas} recetas")
    print("\n")

    eleccion_menu = "x"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opción: ")
        print("""
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoría nueva
        [4] - Eliminar receta
        [5] - Eliminar categoría
        [6] - Salir del programa""")
        eleccion_menu = input()
        print(f"- Has seleccionado la opción {eleccion_menu}")
    return int(eleccion_menu)

# ----------------Funciones----------------------

# -- Función de elegir dirección de categorías
def elegir_direccion(ruta):
    direccion_actual = os.chdir(directorio_recetas)
    todas_direcciones = os.listdir(direccion_actual)
    print("\n")
    print(f"- Las categorías son las siguientes: \n{todas_direcciones}")
    print("\n")
    direccion_elegida = ""
    direccion_usuario = input("Elige la categoría que quieras: ")
    if direccion_usuario in todas_direcciones:
        for file in todas_direcciones:
            if file == direccion_usuario:
                direccion_elegida = "".join(file)
        return Path(ruta / direccion_elegida)
    else:
        return "Error"
# -- Nombrar categorías
def nombrar_categoria(ruta):
    direccion_actual = os.chdir(ruta)
    categoria_nueva_usuario = input("Introduce el nombre de tu nueva categoria: ")
    categoria_nueva = os.mkdir(categoria_nueva_usuario)
    direccion_nueva = os.listdir(direccion_actual)
    return direccion_nueva
# -- Eliminar categoría
def eliminar_categoria(ruta):
    direccion_actual = os.chdir(directorio_recetas)
    eliminar_categoria_user = input("¿Quieres eliminar la categoría actual? ").lower()
    if eliminar_categoria_user == "si".lower() or "sí".lower():
        categoria_eliminada = os.removedirs(resultado_eleccion_categoria)
        print(f"- {resultado_eleccion_categoria.name} se ha eliminado correctamente")
        direccion_nueva = os.listdir(direccion_actual)
        return direccion_nueva
    else:
        return "Error"
# -- Mostrar recetas
def mostrar_recetas(ruta_categoria):
    direccion_nueva = os.chdir(ruta_categoria)
    todas_recetas = os.listdir(direccion_nueva)
    print(f"- Las recetas son: {todas_recetas}")
    return todas_recetas
# -- Nombrar receta
def crear_nombre_receta(resultado_categoria):
    direccion_actual = os.chdir(resultado_categoria)
    receta_nueva = input("Escribe el nombre de la nueva receta: ")
    creacion_receta = open(receta_nueva, "w")
    direccion_nueva = os.listdir(direccion_actual)
    for txt in direccion_nueva:
        if txt == receta_nueva:
            print("- ¡La receta ha sido creada satisfactoriamente!")
        else:
            pass
    return creacion_receta
# -- Elegir receta
def elegir_recetas(ruta_categoria, recetas):
    eleccion_receta_usuario = input("Elige la receta de tu preferencia: ")
    direccion_cate_recetas = ""
    if eleccion_receta_usuario in recetas:
        for receta in recetas:
            if receta == eleccion_receta_usuario:
                direccion_cate_recetas = "".join(receta)
        return Path(ruta_categoria / direccion_cate_recetas)
    else:
        return "Error"
# -- Leer receta
def leer_receta(resultado_receta):
    lectura_receta = open(resultado_receta, "r")
    return lectura_receta.read()
# -- Eliminar receta
def eliminar_receta(ruta_receta):
    receta_eliminar_user = input("¿Cuál receta quieres eliminar?: ")
    receta_eliminada = os.remove(receta_eliminar_user)
    return receta_eliminada
# -- Función de volver al inicio
def volver_inicio():
    eleccion_regresar = "x"
    while eleccion_regresar.lower() != "v":
        eleccion_regresar = input("Presione V para volver al menú: ")

# --------------- Fin de las funciones -------------

# Menú

while not finalizar_programa:
    menu = inicio()

    if menu == 1: # leer receta
        # elegir categoría
        resultado_eleccion_categoria = elegir_direccion(directorio_recetas)

        print("\n")

        # mostrar recetas
        resultado_mostrar_recetas = mostrar_recetas(resultado_eleccion_categoria)

        print("\n")

        # elegir recetas
        resultado_elegir_receta = elegir_recetas(resultado_eleccion_categoria,resultado_mostrar_recetas)

        print("\n")

        # leer receta
        print(f"- La receta dice lo siguiente:\n\t{leer_receta(resultado_elegir_receta)}")

        print("\n")

        # Volver al inicio
        volver_inicio()

    elif menu == 2: # crear receta
        # elegir categoría
        resultado_eleccion_categoria = elegir_direccion(directorio_recetas)

        print("\n")

        # crear nombre
        receta_nueva = crear_nombre_receta(resultado_eleccion_categoria)

        print("\n")

        # Volver al inicio
        volver_inicio()

    elif menu == 3: # crear categoría
        print("\n")

        # nombre categoría
        nombre_nuevo_categoria = nombrar_categoria(directorio_recetas)
        print("\n")
        print(f"Las categorías han sido actualizadas:\n\t{nombre_nuevo_categoria}")

        print("\n")

        # Volver al inicio
        volver_inicio()
    elif menu == 4: # eliminar receta
        # elegir categoría
        resultado_eleccion_categoria = elegir_direccion(directorio_recetas)

        print("\n")

        # mostrar recetas
        resultado_mostrar_recetas = mostrar_recetas(resultado_eleccion_categoria)

        print("\n")

        # eliminar receta
        receta_eliminada = eliminar_receta(resultado_eleccion_categoria)
        print(f"------- Se ha eliminado satisfactoriamente la receta -------")

        print("\n")

        # Volver al inicio
        volver_inicio()

    elif menu == 5: # eliminar categoría
        # elegir categoría
        resultado_eleccion_categoria = elegir_direccion(directorio_recetas)

        print("\n")

        # eliminar categoría
        print(f"- Las categorías han quedado así: {eliminar_categoria(resultado_eleccion_categoria)}")

        print("\n")

        # Volver al inicio
        volver_inicio()

    elif menu == 6: # finalizar programa
        print("\n")
        print("----- Gracias por utilizar el administrador de menús, hasta la próxima -----")
        finalizar_programa = True