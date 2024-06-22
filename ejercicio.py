
# Modifique los ejercicios de Clave Morse y de Codigo Cesar y uselos para que el usuario pueda ingresar una palabra y el programa le devuelva la palabra en clave morse y en codigo cesar sin importar el tamaño de la palabra.

# Puede usar estas listas

morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", ".....", "-....",]

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

abcdedarioo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Tabla
# i  morse - lista - abcdedarioo
# 0   .-       a         a
# 1  -...      b         b
# 2  -.-.      c         c

palabra = input("Ingrese una palabra: ").lower()
#print(palabra)
convertir_a_morse = []
#print(convertir_a_morse)
for i in palabra:
    for abc in range(len(lista)):
        #print(abc)
        if i == lista[abc]:
            #print(i, abc)
            convertir_a_morse.append(morse[abc])

#print(convertir_a_morse)
print(f'La palabra {palabra} en clave Morse es: {convertir_a_morse}')
#for m in morse:
#    for abc in abcdedarioo:
#       print(m, abc)
palabraclave = input("Ingrese una palabraclave: ").lower()
#print(palabraclave)
convertir_a_cesar = []
#print(convertir_a_morse)
for i in palabraclave:
    for abc in range(len(lista)):
        #print(abc)
        if i == lista[abc]:
            print(i, abc)
            convertir_a_cesar.append(abc)

#print(convertir_a_morse)
print(f'La palabraclave {palabraclave} en clave Cesar es: {convertir_a_cesar}')
#for m in morse:
#    for abc in abcdedarioo:
#       print(m, abc)
