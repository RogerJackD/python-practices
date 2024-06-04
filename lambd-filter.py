#ejemplo basico lambda
#lambda crea funciones() en variables
numeromulti = lambda x : x*2

multi = numeromulti(5)
print(multi)

#----------------#

numeros = [1,2,3,4,5,6]

#ejemplo filter:

#filter retorna solamente listas
#trabaja con iterables
#solo alamacena datos TRUE
def es_par(num):
    if(num%2==0):
        return True
  
numeros_pares = filter(es_par,numeros)
print (list(numeros_pares))


#funcion filter + lambda

numeros_pares = filter (lambda numero : numero % 2==0,numeros)
print(list(numeros_pares))







