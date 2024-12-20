# -*- coding: utf-8 -*-
"""Olá, este é o Colaboratory

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/AkyLast/9ce77d8e87e669617cf2c372e8c009b3/ol-este-o-colaboratory.ipynb
"""

from PIL import Image

input_file_jpg = "img_colorida.jpg"
saida_bmp = "img.bmp"
output_file = "img_gray.bmp"

def convert_to_bmp(input_file_jpg, saida_bmp, output_file):
  with Image.open(input_file_jpg) as img:
    img.save(saida_bmp, format = 'BMP')

  bmp_data = read_bmp(saida_bmp)
  manipulation_bmp = convert_to_grayscale(bmp_data, binary = 1)
  write_bmp(output_file, manipulation_bmp)

  return f"Imagem redimensionada e salva em {output_file}!"

def read_bmp(filename):
  with open(filename, "rb") as f:
    data = f.read()
    return data

def write_bmp(filename, data):
  with open(filename, "wb") as f:
    f.write(data)

def convert_to_grayscale(bmp_data, binary = 0):
  header = bmp_data[:54]
  pixel_data = bmp_data[54:]

  if binary == 0:
    manipulation_pixels = bytearray()
    for i in range(0, len(pixel_data), 3):
      b, g, r = pixel_data[i], pixel_data[i + 1], pixel_data[i + 2]
      gray = (r + g + b) // 3
      manipulation_pixels.extend([gray, gray, gray])

  else:
    manipulation_pixels = bytearray()
    for i in range(0, len(pixel_data), 3):
      b, g, r = pixel_data[i], pixel_data[i + 1], pixel_data[i + 2]
      gray = (r + g + b) // 3
      binary_pixel = 255 if gray > 128 else 0
      manipulation_pixels.extend([binary_pixel, binary_pixel, binary_pixel])

  return header + manipulation_pixels

redimencionar = convert_to_bmp(input_file_jpg, saida_bmp, output_file)
print(redimencionar)