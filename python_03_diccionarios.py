# --------------------------
# diccionarios
# --------------------------

dicc = {"abc":"Antonio", "qwe":"Javier", "asd":"Alba", "zxc":"Esther"}
print(dicc)

""" Operaciones con diccionarios
    diccionario.get('clave'): Devuelve el valor que corresponde con la clave
    diccionario.pop('valor'): Devuelve el valor que corresponde con la clave, y luego borra clave/valor
    diccionario.update({'clave':'valor'}): Inserta una clave o actualiza su valor si ya existiera
    'clave' in diccionario: Devuelve True/False) si la clave existe en el diccionario.
    'valor' in diccionario.values(): Devuelve True/False si valor existe en el diccionario
"""

print(dicc.get("asd"))
print(dicc.pop("asd")) # eliminar elemento
print(dicc)

dicc.update({"mmm":"Mario"}) #inserta, al no existir
dicc.update({"qwe":"Javi"}) #modifica, al existir ya
print(dicc)

print("mmm" in dicc) # True
print("xxx" in dicc) # False

print("Javi" in dicc.values()) # True
print("Fran" in dicc.values()) # False
