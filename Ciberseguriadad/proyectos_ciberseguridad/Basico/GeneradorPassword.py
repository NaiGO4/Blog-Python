#Importamos 2 modulos ramdon y string
import random
import string

#Definimos una funcion de generacion de contraseña
def generar_password(longitud = 16, incluir_mayusculas = True, incluir_numeros = True, incluir_sinbolos =True):
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_sinbolos:
        caracteres += string.punctuation

    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password

#Salicitar la contraseña

def main ():
    longitud = int(input("Introduce la longitud de la contraseña:"))
    incluir_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

    contrasena = generar_password(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
    print("Tu nueva contraseña es:", contrasena)

if __name__ == "__main__":
    main()