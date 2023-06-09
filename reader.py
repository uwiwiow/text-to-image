import sys
from PIL import Image

try:
    imagen = Image.open(sys.argv[1])
except IndexError:
    imagen = Image.open(input("De el path"))
pixeles = imagen.load()
bin = ''

for columna in range(imagen.height):
    for fila in range(imagen.width):
        valor_rgb = pixeles[(fila, columna)]
        if valor_rgb == (255, 255, 255):
            bin = bin + '0'
        if valor_rgb == (0, 0, 0):
            bin = bin + '1'

grupos_binarios = [bin[i:i+8] for i in range(0, len(bin), 8)]
texto = ''.join(chr(int(grupo_binario, 2)) for grupo_binario in grupos_binarios).encode('latin_1').decode('utf_8')

print(texto)