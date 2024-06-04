ejemplo = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
claves = ["edad","ciudad","nombre","edad"]

for i in claves:
    print(ejemplo[i])
    
    
    
cadena = "abracadabra"

frecuencia = {}
for caracter in cadena:
    if caracter in frecuencia:
        frecuencia[caracter] += 1
    else:
        frecuencia[caracter] = 1

print("Frecuencia de caracteres:", frecuencia)


n = 30

primos = []
for num in range(2, n + 1):
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(num)

print("Números primos hasta", n, ":", primos)


        
        
###
N = 5
Arreglo = [0] * N
for i in range(N):
    Arreglo[i] = i

print(Arreglo)
####


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpuesta = [] # = [ [1,4,7],[2,5,7]... ]
for i in range(len(matriz[0])): #range de (0-3)
    fila_transpuesta = []
    for fila in matriz: # recorrer 3 veces 
        fila_transpuesta.append(fila[i])
    transpuesta.append(fila_transpuesta)

print("Matriz transpuestaa:", transpuesta)



#####
cadena = "aaab"

comprimida = ""
contador = 1 #3


for i in range(1, len(cadena)):
    if cadena[i] == cadena[i - 1]: #cadena[3]="b"     == cadena[2]
        contador += 1
    else:             #cadena[2]+  comprimida 5
        comprimida += cadena[i - 1] + str(contador)
        contador = 1

comprimida += cadena[-1] + str(contador)
print("Cadena comprimida:", comprimida)

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
        

        
        
