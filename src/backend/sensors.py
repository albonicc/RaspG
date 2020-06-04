import sys
import json
import time

sensor_values = {
        "temp": 1,
        "air_hum": 1,
        "soil_hum": 1,
        "lum": 1
    }

while True:
    print(json.dumps(sensor_values))
    sensor_values["temp"] += 1
    sensor_values["air_hum"] += 1
    sensor_values["soil_hum"] += 1
    sensor_values["lum"] += 1
    sys.stdout.flush()
    time.sleep(1)