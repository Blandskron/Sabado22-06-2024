#Diccionario 
#          Clave   :  Valor, Clave :     Valor
frutas = {'manzana': 'rojo', 'platano': 'amarillo', 'uva': 'morado'}

print("Por defecto")
for fruta in frutas:
    print(fruta)

print("Inprimiendo la Clave")
for clave in frutas.keys():
    print(clave)

print("Imprimiendo el Valor")
for valor in frutas.values():
    print(valor)
 
print("Imprimiendo Clave y Valor")
for clave, valor in frutas.items():
    print(f'La {clave} es de color {valor}')
    