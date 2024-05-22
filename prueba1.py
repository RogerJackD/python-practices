def crear_Contraseña_random(num):
    chars = "adfsegihj"
    num_entero = str(num)
    num = int (num_entero[0])
    c1= num - 2
    c2= num 
    c3= num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num 
#desempaquetar
password,primer_numero = crear_Contraseña_random("5")  

print(f"tu primera contra es {password}")
print(f"el numero usado fue {primer_numero}")

#sga10