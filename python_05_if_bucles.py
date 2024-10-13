# --------------------------
# bifurcación: if
# --------------------------

# Importancia de indentación para definir bloques (no hay {})
# No hay sentencia de bifurcación switch/case

pos=int(input("¿En qué posición terminaste la carrera? "))

if pos == 1:
    print("¡Enhorabuena!")
    print("¡Ganaste!")
elif pos == 2:
    print("¡Muy bien!")
    print("¡Quedar segundo es un buen puesto!")
else:
    print("Lo importante es participar")
    print("Sigue entrenando")
    
# --------------------------
# bucle: while
# --------------------------

i=1
while(i<11):
    print("8 X",i,"=",8*i)
    i=i+1 # también es posible i+=1

# no hay bucle "repite"
    
# --------------------------
# bucle: for
# --------------------------

for i in range(1,11):
    print("5 X",i,"=",5*i)

for i in range(10,0,-1):
    print("3 X",i,"=",3*i)

# Recorrer listas
Clientes2020=["Juan","Luis","María","Carmen"]

for i in Clientes2020:
    print(i)

for i in range(0,len(Clientes2020)):
    print("Cliente",i,Clientes2020[i])

#Recorrer diccionarios (claves)
dicc = {"abc":"Antonio", "qwe":"Javier", "asd":"Alba", "zxc":"Esther"}

for clave in dicc:
    print("Clave:",clave)

for clave in dicc.keys():
    print("Clave (con keys):",clave)
     
#Recorrer diccionarios (valores)
for clave in dicc:
    print("Valor:",dicc[clave])

for valor in dicc.values():
    print("Valor (con values):",valor)

#Recorrer diccionarios (claves y valores)
for clave in dicc:
    print("Clave:",clave,"- Valor:",dicc[clave])

for clave,valor in dicc.items():
    print("Clave (con items):",clave,"- Valor (con items):",valor)
	