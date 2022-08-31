print('='*50);
print("11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:")
print("o produto do dobro do primeiro com metade do segundo.")
print("a soma do triplo do primeiro com o terceiro.")
print("o terceiro elevado ao cubo")
print('='*50);
print('')

inteiro1 = int(input("Digite um numro inteiro: "))
inteiro2 = int(input("Digite outro numero inteiro: "))
real = float(input("Digite um numero real: "))

num1 = (inteiro1 * 2) * (inteiro2/2)
num2 = (inteiro1 * 3) + (real)
num3 = real ** 3

print("o produto do dobro do primeiro com metade do segundo.", num1)
print("a soma do triplo do primeiro com o terceiro.", num2)
print("o terceiro elevado ao cubo", num3)