import random
import string

print("=== GENERADOR DE CONTRASEÑAS (AVANCE) ===")

longitud = int(input("Ingrese la longitud de la contraseña: "))

caracteres = string.ascii_lowercase  # Por ahora solo minúsculas

contrasena = ""

# Estructura repetitiva
for i in range(longitud):
    contrasena += random.choice(caracteres)

print("Contraseña generada:", contrasena)

print("Nota: En la siguiente versión se agregarán más opciones.")