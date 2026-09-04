def saludar(nombre):
    """Función que saluda al usuario"""
    return f"¡Hola, {nombre}! Bienvenido al mundo de Python."


# Ejemplo de uso de la función
print(saludar("Estudiante"))


# Ejemplo de lista y bucle
numeros = [1, 2, 3, 4, 5]

print("Lista de números:")

for num in numeros:
    print(f" - {num} al cuadrado es {num**2}")


# Ejemplo de condicional
edad = 20

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")