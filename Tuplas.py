t = 'a', 'b', 'c', 'd', 'e'

print(t) #outpud: ('a', 'b', 'c', 'd', 'e')


#Para crear una tupla con un solo elemento, es necesario incluir una coma al final
t1 = ('a',)
print(type(t1))#outpud: <class 'tuple'>

#Sin la coma, Python considera ('a') como una expresión con una cadena entre paréntesis que es evaluada como de tipo cadena (string):

t1 = ('a')
print(type(t1)) #outpud: <class 'str'>

#como crear una tupla vacia

t = tuple()
print(t) #output: ()

t = tuple('amanecer')
print(t)#output: ('a', 'm', 'a', 'n', 'e', 'c', 'e', 'r')
#index
print(t[0]) #output: a