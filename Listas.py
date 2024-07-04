#Listas

print("Listas")

frutas = ["fresa", "manzana", "pera", "mandarina", "platano"]
quesos = ["Chedar", "Edam", "Gouda"]
print(frutas)
print(quesos)

print("-----------------------")
print("Las listas son mutables")

print(frutas[0])
print(quesos[2])

print("-----------------------")
print("Recorriendo una lista")

for queso in quesos:
    print(queso)


print("-----------------------")
print("Operaciones de listas")

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

print("-----------------------")
print("Rebanado de listas")


t = ["a", "b", "c", "d", "e", "f"]
print(t[1:3])
print(t[:])

print("-----------------------")
print("Métodos de listas")

print("append")
# append agrega un nuevo elemento al final de una lista:
t = ["a", "b", "c"]
t.append("z")
print(t)

print("-----------------------")
#extend toma una lista como argumento y agrega todos los elementos:
print("extend")
t1 = ["a", "b", "c"]
t2 = ["d", "e", "f"]

t1.extend(t2)
print(t1)

print("-----------------------")
print("ELIMINANDO ELEMENTOS")
print("sort")
# sort ordena los elementos de la lista de menor a mayor:
l = ['d', 'c', 'e', 'b', 'a']
print(l)
l.sort()
print(l)

print("-----------------------")
print("Eliminando elementos")
print("pop")
#Hay varias formas de eliminar elementos de una lista. Si sabes el índice del elemento que quieres, puedes usar pop:

t = ["a", "b", "c"]
print(t)
x = t.pop(1)
print(t)

#Si sabes qué elemento quieres remover (pero no sabes el índice), puedes usar remove:
# t = ['a', 'b', 'c']
t.remove('b')
print(t)
