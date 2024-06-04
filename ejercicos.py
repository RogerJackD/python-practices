#------------------------------#
#ingresar nombre y edad: el mayor es el profesor y el menor el asistente:

#funcion para obetener al asistente y al profesor  segun la edad

#def cantidad_de_compañeros:
#crear la lista con las personas
    
def obtener_compañeros(cantidad_de_personas):
    # Crear una lista vacía para almacenar las personas
    personas = []
    
    # Recoger datos de los usuarios
    for i in range(cantidad_de_personas):
        nombre = input("Ingrese nombre: ")
        edad = int(input("Ingrese edad: "))
        persona = (nombre, edad)
        personas.append(persona)
    
    # Ordenar la lista de personas por edad
    ordenar = sorted(personas, key=lambda x: x[1])
    mayor = ordenar[-1]  # La persona con mayor edad
    menor = ordenar[0]   # La persona con menor edad
    
    # Crear las cadenas descriptivas
    profesor = f"El profesor es {mayor[0]} con edad {mayor[1]}."
    asistente = f"El asistente es {menor[0]} con edad {menor[1]}."
 
    return profesor, asistente

# Solicitar la cantidad de personas
cant = int(input("Ingresa cantidad de personas que están presentes: "))   

# Obtener y imprimir los resultados
a, b = obtener_compañeros(cant)
print(a)
print(b)

