#GESTION DE PELICULAR DE CINE

#Definimos la función para mostrar el menú principal
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("=====================================")

#Definimos la función para leer la opción del usuario
def leer_opcion():
    try:
        opcion = int(input("Ingrese una opción (1-6): "))
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 6.")
            return leer_opcion()
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")
        return leer_opcion()

#Funciones de validación de datos
def validar_titulo(titulo):
    cantidad_espacios = 0
    for i in titulo:    
        if " " == i:
            cantidad_espacios += 1
    if cantidad_espacios == len(titulo) or len(titulo) == 0:
        return True
    return False

#Función para validar la duración de la película
def validar_duracion(duracion):
    try:
        duracion = int(duracion)
        if duracion > 0:
            return False
        else:
            return True
    except ValueError:
        return True

#Función para validar la calificación
def validar_calificacion(calificacion):
    try:
        calificacion = float(calificacion)
        if 0 <= calificacion and calificacion <= 10:
            return False
        else:
            return True
    except ValueError:
        return True

#Función para evaluar si la calificación de la pelicula es mayor o igual a 7  
def disponibilidad(coleccion_peliculas):
    for pelicula in coleccion_peliculas:
        if float(pelicula['calificacion']) >= 7.0:
            pelicula['disponible'] = True
        else: 
            pelicula['disponible'] = False


#Función que permite agregar películas a la lista.
def agregar_pelicula(coleccion_peliculas):
    print("AGREGAR PELICULA")

    titulo = input("Ingrese el título de la película: ")
    if validar_titulo(titulo):
        print("Título inválido. No puede estar vacío ni contener solo espacios.")
        return
    duracion = input("Ingrese la duración de la película (en minutos): ")
    if validar_duracion(duracion):
        print("Duración inválida. Debe ser un número entero mayor que cero.")
        return 
        
    calificacion = input("Ingrese la calificación de la película (0-10): ")
    if validar_calificacion(calificacion):
        print("Calificación inválida. Debe ser un número decimal entre 0.0 y 10.0; ambos incluidos.")
        return
    
    nueva_pelicula = {
        "titulo": titulo,
        "duracion": duracion,
        "calificacion": calificacion,
        "disponible": False
        }

    coleccion_peliculas.append(nueva_pelicula)

    print("Película registrada exitosamente!")

#Función que permite buscar una película en la lista
def buscar_pelicula(coleccion_peliculas, titulo):
    titulo = titulo.lower()
    for i in range(len(coleccion_peliculas)):
        if coleccion_peliculas[i]["titulo"].lower() == titulo:
            return i
    return -1


#Creamos una lista de películas en blanco.
coleccion_peliculas = [ ]

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_pelicula(coleccion_peliculas)


    elif opcion == 2:
        print("BUSCAR PELICULA")
        titulo = input("Ingrese el título de la película que desea buscar: ")
        buscar = buscar_pelicula(coleccion_peliculas, titulo)
        if buscar == -1:
            print(f"La película {titulo} no se encuentra registrada")
        else: 
            print(f"La película {titulo} se encuentra en la posición {buscar}")
    

    elif opcion == 3:
        print("ELIMINAR PELICULA")
        titulo = input("Ingrese el título de la película que desea eliminar:")
        posicion = buscar_pelicula(coleccion_peliculas, titulo)
        if posicion == -1:
            print(f"La película {titulo} no se encuentra registrada")
        else:
            coleccion_peliculas.pop(posicion)
            print("Arriendo eliminado exitosamente.")

    elif opcion == 4:

        print("ACTUALIZAR DISPONIBILIDAD")
        print("Se están actualizando las disponibilidades...")
        disponibilidad(coleccion_peliculas)
        print("Se ha actualizado la disponibilidad correctamente")

    elif opcion == 5:
        print("MOSTRAR PELICULAS")
        disponibilidad(coleccion_peliculas)

        if len(coleccion_peliculas) == 0:
            print("No hay películas registradas para mostrar")
        else:
            print("\n=== LISTA DE PELICULAS ===")
            for pelicula in coleccion_peliculas:
                print(f"Título: {pelicula['titulo']}")
                print(f"Duración: {pelicula['duracion']}")
                print(f"Calificación: {pelicula['calificacion']}")
                if pelicula['disponible']:
                    print("Estado: DISPONIBLE")
                else: 
                    print("Estado: NO RECOMENDADA")
                 
                print("********************************************")


    elif opcion == 6:
        print("Saliendo del programa...")
        print("Gracias por usar el sistema. Vuelva pronto")
        break
