temperature = input("please enter the temperature in C:")
temperature = int(temperature)
fahrenheit = (9.0/5.0*temperature+32)
print(fahrenheit)


fehrenheit = input("please enter the temperature in F:")
fehrenheit = int(fehrenheit)
celsius = (5/9*fehrenheit+32)
print(celsius)




account = (int(input("please enter the principle amount:")))
intrest = (int(input("please enter the annual rate of intrest:")))
year = int((input("please enter the time period:")))
print(type(account))
print(type(intrest))
print(type(year))
intrest_rate = (account *intrest *year/100)
print(intrest_rate) 