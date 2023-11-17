def convert_temperature(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    print('celesuis : ',celsius)
    print('kelvin : ',kelvin)
    return 0
fahernheit = float(input('enter fahernhiet degrees : '))
convert_temperature(fahernheit)