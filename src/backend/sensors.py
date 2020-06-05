import sys
import json
import time
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess

RST = None 

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding
x = 0
font = ImageFont.load_default()

sensor_values = {
        "temp": 1,
        "air_hum": 1,
        "soil_hum": 1,
        "lum": 1
    }

while True:
    print(json.dumps(sensor_values))
    
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Write two lines of text.

    draw.text((x, top),       "Temp:              " + str(sensor_values["temp"]),  font=font, fill=255)
    draw.text((x, top+8),     "Air hum:           " + str(sensor_values["air_hum"]), font=font, fill=255)
    draw.text((x, top+16),    "soil hum:          " + str(sensor_values["soil_hum"]),  font=font, fill=255)
    draw.text((x, top+25),    "lum:               " + str(sensor_values["lum"]),  font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(.1)
    
    sensor_values["temp"] += 1
    sensor_values["air_hum"] += 1
    sensor_values["soil_hum"] += 1
    sensor_values["lum"] += 1
    sys.stdout.flush()
    time.sleep(1)
