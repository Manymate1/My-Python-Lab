# Un método en Python es una función que está asociada a un objeto o a una clase y define las acciones que este puede realizar

# Definición: Es un bloque de código reutilizable escrito dentro de una clase.

# Diferencia con una función: Una función es independiente, mientras que un método pertenece a un objeto o tipo de dato específico y se llama usando un punto (.).

# Notación: Se escribe objeto.metodo()

texto = 'Hola Mundo'
print(texto.upper())
print(texto.lower())

print(texto.find('M')) # Find encuentra la letra o cadena de texto que le indiques, mostrando desde que indice se encuentra / Devuelve Indice

# Una alternativa a find puede ser:

print("Mundo" in texto) # Devuelve booleano

print(texto.replace('Mundo', 'Python')) # si encuentras la linea ( primera parte ), Reemplazara por ( segunda parte )

nuevotexto = texto.replace('Mundo', 'Python') # si encuentras la linea ( primera parte ), Reemplazara por ( segunda parte )

print(texto, nuevotexto)