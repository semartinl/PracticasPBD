# --------------------------
# conjuntos
# --------------------------

pares={2,4,6,8,10}
impares={1,3,5,7,9}
primos={1,2,3,5,7}

""" Operaciones con conjuntos
    A | B: Unión entre conjuntos
    A & B: Intersección entre conjuntos
    A – B: Diferencia entre conjuntos (los elementos que están en A pero no están en B)
    A ^ B: Diferencia simétrica entre el conjunto A y B (los elementos que están en A o en B pero no en los dos)
""" 

print(pares)
print(impares)
print(primos)

print("Pares e impares",pares|impares)
print("Impares primos",impares&primos)
print("Impares no primos",impares-primos)
print("Diferencia simétrica",impares^primos)
