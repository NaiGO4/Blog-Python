#Expreciones regulares


import re
man = open('hola.txt')
for linea in man:
    linea = linea.rstrip()
    if re.search('ˆHola', linea):
        print(linea)