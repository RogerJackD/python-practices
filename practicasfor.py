for i in range(11):
    print(i)
    
suma = 0
for i in range(1,101):
    
    suma +=i
    
print(f"la suma es: {suma}")

frutas = ["manzana", "naranja", "plátano", "cereza"]

for i in frutas:
    print(i)
    
numeros = [4, 7, 2, 8, 10, 3]
max = numeros[0]
for i in numeros:
    if i > max :
        max = i
print("mayor es:",max)

for i in range(21):
    i %2==0
    print(i)
    
for i in range(11):
    resultado = 5*i
    print(f"5 x {i} =",resultado)
#contar elementos
elementos = ["a", "b", "c", "d", "e"]
contador = 0
for i in elementos:
    contador +=1
print("cant elementos: ",contador)


cadena ="hola mundo"
cadena_invertida = ""
for caracter in cadena:
    cadena_invertida = caracter + cadena_invertida
    #aloh
print("La cadena invertida es:", cadena_invertida)








  
    
cadenas = ["perro", "elefante", "jirafa", "hipopótamo"]   
cadena_larga = ""   
for i in cadenas:
    if len(i) > len(cadena_larga):
        cadena_larga = i         
print("la cadena mas larga es =", cadena_larga)       
        
            

            
cadena = "a"

frecuencia = {}
for caracter in cadena:
    if caracter in frecuencia:
        frecuencia[caracter] += 1
    else:
        frecuencia[caracter] = 1

print("Frecuencia de caracteres:", frecuencia)       
    
    