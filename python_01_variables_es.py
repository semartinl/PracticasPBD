# comentario
"""" comentario en
varias líneas """

# --------------------------
# variables, entrada/salida
# --------------------------

# variables no tipadas
i = 24
print(i)
i = "Hola"
print(i)
i = 3.14
print(i)
i = False
print(i)

print ("Cadenas")
print (28) #números

# declaración con tipo
num1=int(12)
num2=float(2.5)

# cadenas
txt1="Hola" #comillas dobles
txt2='Buenos días' #comillas simples
txt3=str(8)

print(num1)
print(num2)
print(txt1)
print(txt2)
print(txt3)

print(txt1+", "+txt2)
print(txt1+", "+txt2+txt3)

print(txt1+", "+txt2+str(num1)) #ojo no funciona sin str
#print(txt1+", "+txt2+num1) #ojo no funciona sin str

nombre = input("Escribe tu nombre: ")
print(nombre)
print("Tu nombre tiene",len(nombre),"letras")
print("Tu nombre empieza por",nombre[0],"y termina por",nombre[len(nombre)-1])
