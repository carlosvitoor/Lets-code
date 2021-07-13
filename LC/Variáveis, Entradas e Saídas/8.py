# Faça um programa que peça a temperatura em graus Fahrenheit (F),
# transforme e mostre a temperatura em graus Celsius (°C).
# °C = (5 * (F-32) / 9)
# Obs: Tente também fazer um programa que faça o inverso:
# peça a temperatura em graus Celsius e a transforme em graus Fahrenheit.

temp = float(input("Entre com a temperatura em graus Fahrenheit (F):"))
print((5 * (temp-32) / 9))

temp = float(input("Entre com a temperatura em graus Celsius (°C):"))
print((temp * 1.8) + 32)
