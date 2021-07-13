# Faça um programa que peça o dia, o mês e o ano
# para o usuário e imprima a data completa no formato dd/mm/aaaa.

dia = "0" + str(int(input("Entre com o dia:")))
mes = "0" + str(int(input("Entre com o mês:")))
ano = int(input("Entre com o ano:"))

print("Data {}/{}/{}".format(dia[-2:], mes[-2:], ano))
