# Lista de edades
contador = 0
cantidad = int(input("Cuantos valores para edad quiere ingresar: "))

while contador < cantidad:
    edad = int(input(f"Ingrese la edad n {contador + 1}: "))
    if edad < 13:
        print(f'{edad} años: Niño')
    elif 13 <= edad < 18:
        print(f'{edad} años: Adolescente')
    else:
        print(f'{edad} años: Adulto')
    contador += 1
