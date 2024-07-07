#Hashing y Verificación de Contraseñas 

#El hashing y la verificación de contraseñas son componentes esenciales de la seguridad en aplicaciones. 

#Se utilizara la bibloteca bcrypt se intalara con el siente comando "pip install bcrypt"

import bcrypt

#Primero se solcita la contraseña:

password = input('Introcuce una contraseña:')

#La contraseña la convertimos a bytes
password_bytes = password.encode('utf-8')

#Generemos un sal(salt), 
#Una sal es un valor aleatorio añadido a una contraseña antes de hashearla para garantizar que incluso contraseñas idénticas generen hashes únicos.
salt = bcrypt.gensalt()

#Hashear la contraseña, Proceso de convertir datos de entrada en una cadena de longitud fija.
hashed_password = bcrypt.hashpw(password_bytes, salt)

#Mostrar la contraseña hasheada
print(f"Contraseña haseada: {hashed_password.decode('utf-8')}")

# Verificación de la contraseña
password_check = input("Introduce de nuevo la contraseña para verificación: ")
password_check_bytes = password_check.encode('utf-8')

#Usamos un flujo de control para salidar la contraseña
if bcrypt.checkpw(password_check_bytes, hashed_password):
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")