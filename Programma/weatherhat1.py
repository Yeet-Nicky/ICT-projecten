import weatherhat 
import time
import csv
from datetime import datetime
import os
import subprocess

sensor = weatherhat.WeatherHAT()

with open('weather_data.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Tijdstip", "Apparaat Temperatuur (°C)", "Temperatuur (°C)",
                     "Luchtdruk (hPa)", "Luchtvochtigheid (%)", "Lichtintensiteit (lux)", 
                     "Windsnelheid (m/s)", "Windrichting (graden)"])

def check_waarde(waarde):
    return "nvt" if waarde == 0 else round(waarde, 2)

while True:
    tijdstip = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    apparaat_temperatuur = check_waarde(sensor.device_temperature) 
    tempratuur = check_waarde(sensor.temperature)
    druk = check_waarde(sensor.pressure)
    vochtigheid = check_waarde(sensor.humidity)
    lux = check_waarde(sensor.lux)
    windkracht = check_waarde(sensor.wind_speed)
    windrichting = check_waarde(sensor.wind_direction)
    
    if apparaat_temperatuur != "nvt":
        print(f"Apparaat temperatuur: {apparaat_temperatuur:.2f} °C")
    else:
        print("Apparaat temperatuur: nvt")
 
    if tempratuur != "nvt":
        print(f"Temperatuur: {tempratuur:.2f} °C")
    else:
        print("Temperatuur: nvt")
 
    if druk != "nvt":
        print(f"Luchtdruk: {druk:.2f} hPa")
    else:
        print("Luchtdruk: nvt")
 
    if vochtigheid != "nvt":
        print(f"Luchtvochtigheid: {vochtigheid:.2f} %")
    else:
        print("Luchtvochtigheid: nvt")
 
    if lux != "nvt":
        print(f"Lichtintensiteit: {lux:.2f} lux")
    else:
        print("Lichtintensiteit: nvt")
 
    if windkracht != "nvt":
        print(f"Windsnelheid: {windkracht:.2f} m/s")
    else:
        print("Windsnelheid: nvt")
 
    if windrichting != "nvt":
        print(f"Windrichting: {windrichting:.2f} graden")
    else:
        print("Windrichting: nvt")
    
    with open('weather_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([tijdstip, apparaat_temperatuur, tempratuur, 
                            druk, vochtigheid, lux, windkracht, windrichting])
            print("weggeschreven!")
            
    os.popen('/bin/auto_push.sh')
    print("git push succesvol!")

    sensor.update(interval=5)
    time.sleep(10)

    
""" 
    repo_path = "/home/rpi/weatherhat-python/ICT-projecten/Programma"
    os.chdir(repo_path)

    os.system("git add .")
    os.system(f'git commit -m "auto"')
    os.system("git push origin main") """

