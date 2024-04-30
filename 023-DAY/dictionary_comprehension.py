weather_c = eval(input("Type day Temperature in dictionary list"))

weather_f = {day: temp * 9/5 * 32 for (day, temp) in weather_c.items()}
print(weather_f)
