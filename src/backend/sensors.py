import sys
import json
import time
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess
from smbus import SMBus


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

bus = SMBus(1);
address = 0x20

dataF = bus.read_i2c_block_data(address, 0, 4)

air_humid = dataF[0:4]
air_temp = dataF[4:8]
hum_dirt = dataF[8:12]
light = dataF[12:16]



sensor_values = {
        "temp": air_humid,
        "air_hum": air_temp,
        "soil_hum": hum_dirt,
        "lum": light
    }

while True:
    
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Write two lines of text.

    draw.text((x, top),       "Temp:            " + str(sensor_values["temp"]),  font=font, fill=255)
    draw.text((x, top+8),     "Air hum:         " + str(sensor_values["air_hum"]), font=font, fill=255)
    draw.text((x, top+16),    "soil hum:        " + str(sensor_values["soil_hum"]),  font=font, fill=255)
    draw.text((x, top+25),    "lum:             " + str(sensor_values["lum"]),  font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(.1)
    
    
    dataF = bus.read_i2c_block_data(address, 0, 16)
    
    air_humid = dataF[0:4]
    air_temp = dataF[4:8]
    hum_dirt = dataF[8:12]
    light = dataF[12:16]
    
    air_humid_blank = []
    air_temp_blank = []
    hum_dirt_blank = []
    light_blank = []
    
    air_humid_joined = ""
    air_temp_joined = ""
    hum_dirt_joined = ""
    light_joined = ""
    
    for i in range(len(air_humid)):
        air_humid_blank.append(chr(air_humid[i]))
    air_humid_joined = air_humid_joined.join(air_humid_blank)
    for i in range(len(air_temp)):
        air_temp_blank.append(chr(air_temp[i]))
    air_temp_joined = air_temp_joined.join(air_temp_blank)
    for i in range(len(hum_dirt)):
        hum_dirt_blank.append(chr(hum_dirt[i]))
    hum_dirt_joined = hum_dirt_joined.join(hum_dirt_blank)
    for i in range(len(light)):
        light_blank.append(chr(light[i]))
    light_joined = light_joined.join(light_blank)
    sensor_values["temp"] = air_temp_joined
    sensor_values["air_hum"] = air_humid_joined
    sensor_values["soil_hum"] = hum_dirt_joined
    sensor_values["lum"] = light_joined
    
    print(json.dumps(sensor_values))
    sys.stdout.flush()
    
    air_humid_blank = []
    air_temp_blank = []
    hum_dirt_blank = []
    light_blank = []
    
    time.sleep(1)
