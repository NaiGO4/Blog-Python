#Diccionarios

print("Diccionarios")

#los valores no tiene orden 
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)#output: {'three', 'uno', 'one', 'dos', 'two', 'tres'}

#si quieres llamar a una varia que esta dentro del direccionario no vas a tener problemas 
print(eng2sp['two']) #output: dos

#pero si quieres llamar a un valor que no se encuentra no figurar error
#print(eng2sp['four'])
# #output: KeyError: 'four'


#La función len funciona en diccionarios; ésta regresa el número de pares clave-valor:
print(len(eng2sp))



palabra = 'brontosaurio'
d = dict()
for c in palabra:
    if c not in d:
        d[c] = 1
else:
    d[c] = d[c] + 1
print(d)


cuentas = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
print(cuentas.get('jan', 0))

print(cuentas.get('tim', 0))