import sys
from PIL import Image, ImageDraw
import math

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

side = math.sqrt(len(bin) - red)

if side.is_integer():
    side = int(side)
else:
    side = int(side) + 1

width = side
height = side

positions = []
rest = []

for index, num in enumerate(bin):
    if num == '1':
        x = index // side
        positions.append((index - (x * side), x))

for index in range(len(bin) - red, side * side):
    x = index // side
    rest.append((index - (x * side), x))

imagen = Image.new('RGB', (width, height), color='white')

dibujo = ImageDraw.Draw(imagen)

for pos in positions:
    dibujo.point(pos, fill='black')

for pos in rest:
    dibujo.point(pos, fill='red')

imagen.save(f'qr{len(bin) - red}for.png')
