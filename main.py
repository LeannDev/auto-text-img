import datetime
import locale
import csv
from pathlib import Path
from PIL import Image, ImageFont, ImageDraw

#BASE_DIR = Path(__file__).resolve().parent.parent

def card(fecha_format):
    
  # Abrir imagen en la ruta
  img = Image.open('tarjeta.png')


  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype('Mitr-Medium.ttf', size=30, encoding='unic')

  text = fecha_format

  xcenter = img.width/2 
  ycenter = img.height/2
  ycenter = ycenter + 100

  width_position = ( 90 * img.width ) / 100
  height_position = ( 80 * img.height ) / 100 

  draw.text((width_position, height_position), text, fill=(0,0,0,0), anchor="rs", font=font)
  #draw.text((xcenter, 400), text2, (22, 109, 154), anchor="ms", font=font2)
  #draw.text((xcenter, ycenter), text, (22, 109, 154), anchor="md", size=200)

  img.save('tarjeta2.png')

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
time_data = datetime.datetime.now()
data_format = time_data.strftime("%d/%m/%Y")

date_birthday = time_data.strftime("Buenos Aires, %d de %B del %Y")

with open('fechas.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    if row['fecha'] == data_format:
      print(row['nombre'], row['fecha'])
      card(date_birthday)
            