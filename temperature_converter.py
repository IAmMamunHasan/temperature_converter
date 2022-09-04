temperature = float(input('Enter temperature you want to convert (in number only) '))
unit = input('What is the unit of the temperature you entered (enter c for celsius or f for fahrenheit or k for kelvin)? ').lower()
convert = input('In which unit you want to convert (enter c for celsius or f for fahrenheit or k for kelvin)? ').lower()
# celsius to kelvin
if unit == "c" and convert == "k":
    c_to_k = temperature + 273
    print("your temperature in kelvin is " + str(c_to_k))
# kelvin to celsius
if unit == "k" and convert == "c":
    k_to_c = temperature - 273
    print("your temperature in celsius is " + str(k_to_c))
# celsius to fahrenheit
if unit == "c" and convert == "f":
    c_to_f = ((temperature * 9) / 5) + 32
    print("your temperature in fahrenheit is " + str(c_to_f))
# fahrenheit to celsius
if unit == "f" and convert == "c":
    f_to_c = ((temperature - 32) * 5) / 9
    print("your temperature in celsius is " + str(f_to_c))
# fahrenheit to kelvin
if unit == "f" and convert == "k":
    f_to_k = ((temperature + 459.67) * 5) /9
    print("your temperature in kelvin is " + str(f_to_k))
# kelvin to fahrenheit
if unit == "k" and convert == "f":
    k_to_f = 1.8 * (temperature - 273.15) + 32
    print("your temperature in fahrenheit is " + str(k_to_f))
if unit == convert:
    print("Wrong entry (both entered units can not be same) Try again!")
print("Thanks for using temperature converter.")