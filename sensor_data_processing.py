# Simulated sensor readings (sample data)
altitude = [50.0, 52.5, 54.0, 53.2, 55.1]
airspeed = [12.0, 12.4, 12.8, 12.2, 13.1]
battery_voltage = [12.4, 12.3, 12.2, 12.1, 12.0]


def analyze_sensor(sensor_name, readings, unit):
    print("\n" + sensor_name)
    print("Readings:", readings)

    average = sum(readings) / len(readings)
    minimum = min(readings)
    maximum = max(readings)

    print("Average:", round(average, 2), unit)
    print("Minimum:", minimum, unit)
    print("Maximum:", maximum, unit)


print("GLIDER & UAV SENSOR DATA PROGRAM")
print("Using simulated data only")

analyze_sensor("Altitude", altitude, "m")
analyze_sensor("Airspeed", airspeed, "m/s")
analyze_sensor("Battery Voltage", battery_voltage, "V")
