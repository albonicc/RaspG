import sys
import json

sensor_values = {
    "temp": "24 C",
    "air_hum": "32%",
    "soil_hum": "88%",
    "lum": "90%"
}

print(json.dumps(sensor_values))

sys.stdout.flush()