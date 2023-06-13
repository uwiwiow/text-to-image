import sys
from PIL import Image, ImageDraw
import math

try:
    with open(sys.argv[1], 'r') as f:
        text = f.read()
except IndexError:
    print("De el texto a guardar")
    text = input()

bytes_utf8 = text.encode('latin_1')
bin = ''.join(format(byte, '08b') for byte in bytes_utf8)

side = math.sqrt(len(bin))

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
        positions.append((index-(x*side), x))

for index in range(len(bin), side*side):
    x = index // side
    rest.append((index - (x * side), x))

imagen = Image.new('RGB', (width, height), color='white')

dibujo = ImageDraw.Draw(imagen)

for pos in positions:
    dibujo.point(pos, fill='black')

for pos in rest:
    dibujo.point(pos, fill='red')

imagen.save(f'qr{len(bin)}gen.png')
