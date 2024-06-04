cadena = "aaab"
comprimida = ""
comprimida += cadena[2] + str(3)

print(comprimida)



lista = (78,0,3,8,4,88,3,2,1)
nose = sorted(lista)
print( nose)
print(nose[0])


#Tienes una lista de diccionarios donde cada diccionario representa 
# un estudiante con su nombre y su calificación. Ordena esta lista
# de estudiantes por sus calificaciones de manera ascendente usando sorted() con lambda y key.
estudiantes = {
    "Ana": 88,
    "Luis": 92,
    "Sofía": 85,
    "Pedro": 90
}

# Convertir el diccionario en una lista de tuplas
lista_estudiantes = list(estudiantes.items())

# Ordenar la lista de tuplas por la calificación (el segundo elemento de cada tupla)
ordenar = sorted(lista_estudiantes, key = lambda x:x[1])

for i in ordenar:
    print( i[0], ":", i[1] )


print(lista_estudiantes)

print(ordenar)



#ordenar = sorted(estudiantes, key=lambda estudiante: estudiante["calificacion"])


#for i in ordenar:
 #   print(i["nombre"],":",i["calificacion"])

    
    
    

    
    
    
    
    
    





