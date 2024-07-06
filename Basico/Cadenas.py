#Cadenas: Una cadena es una secuencia de caracteres.


#La segunda sentencia extrae el carácter en la posición del indice 1 de la variable fruta y la asigna a la variable letra.
fruta = 'fresa'
letra = fruta[1]

print(letra)#output: r
#valor no permitido 1.2 figura error, la pocision comieza en 0 has la ultima letras 4
#Ejemplo
print("-----------------------")
print(fruta[0])
print(fruta[1])
print(fruta[2])
print(fruta[3])
print(fruta[4])
print("-----------------------")
print("Obtener el tamaño de una cadena usando len")
print(len(fruta))
print("-----------------------")
#Para obtener la última letra de una cadena, podrías estar tentado a probar algo como esto:
print("Para obtener la última letra de una cadena")
size = len(fruta)
ultimo = fruta[size - 1]
print(ultimo)


print("-----------------------")
print("Recorriendo una cadena mediante un bucle")

indice = 0
while indice < len(fruta):
    letra = fruta[indice]
    print(letra)
    indice = indice + 1

print("-----------------------")
print("Métodos de cadenas")

palabra = "Luz"
nuevaPalabra = palabra.upper()
print(palabra)
print("-----------------------")
print("Utilizando upper")
print(nuevaPalabra)
print("-----------------------")
print("Utiliznado find")
indece = palabra.find("z", 1)

print(indece)
print(palabra.find("uz"))
print("-----------------------")
print("Utiliznado strip")
linea = " Hola como estas "
print(linea.strip())
print("-----------------------")
print("Utiliznado startswith")
#El metodo startswith devuelven valores booleanos.
linea1 = "Que frio hace el dia de hoy"

print(linea1.startswith("Que"))
print(linea1.startswith("q"))

