#Expreciones regulares


import re
man = open('hola.txt')
for linea in man:
    linea = linea.rstrip()
    if re.search('Hola', linea):
        print(linea)