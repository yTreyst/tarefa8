def ler_temperatura_celsius():
    temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
    return temperatura_celsius

def converter_celsius_para_fahrenheit(temperatura_celsius):
    temperatura_fahrenheit = (9 * temperatura_celsius + 160) / 5
    return temperatura_fahrenheit

def mostrar_temperatura_fahrenheit(temperatura_fahrenheit):
    print(f"A temperatura em graus Fahrenheit é: {temperatura_fahrenheit:.2f}")

temperatura_celsius = ler_temperatura_celsius()
temperatura_fahrenheit = converter_celsius_para_fahrenheit(temperatura_celsius)
mostrar_temperatura_fahrenheit(temperatura_fahrenheit)