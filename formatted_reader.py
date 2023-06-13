import sys
from PIL import Image

try:
    imagen = Image.open(sys.argv[1])
except IndexError:
    imagen = Image.open(input("De el path"))
pixeles = imagen.load()
w, h = imagen.width, imagen.height
Matrix = [[0 for x in range(w)] for y in range(h)]

red = 0

for columna in range(imagen.height):
    for fila in range(imagen.width):
        valor_rgb = pixeles[(fila, columna)]
        if valor_rgb == (255, 255, 255):
            Matrix[columna][fila] = '0'
        if valor_rgb == (0, 0, 0):
            Matrix[columna][fila] = '1'
        if valor_rgb == (255, 0, 0):
            red += 1

filas = len(Matrix)
columnas = len(Matrix[0])
for fila in range(filas):
    for columna in range(columnas):
        if ((fila * columna) % 3 + fila + columna) % 2 == 0:
            if Matrix[fila][columna] == '1':
                Matrix[fila][columna] = '0'
            elif Matrix[fila][columna] == '0':
                Matrix[fila][columna] = '1'

bin = ""

for fila in Matrix:
    for elemento in fila:
        bin += str(elemento)
grupos_binarios = [bin[i:i+8] for i in range(0, len(bin) - red, 8)]
texto = ''.join(chr(int(grupo_binario, 2)) for grupo_binario in grupos_binarios).encode('latin_1').decode('utf_8')

print(texto)