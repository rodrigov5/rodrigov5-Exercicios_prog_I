import math

print('='*50);
print("Este programa recebe o raio de um circulo e retorna sua area.")
print('='*50);
print('')

pi = 3.14

def calcAreaCirculo(a):
    return pi * math.pow(raio, 2)

def escreveResultado(r):
    print(f'A area do circulo é: {resultado: .2f}')

try:
    raio = float(input("Qual o valor do raio? "))
except ValueError:
    print("Digite Apenas Numeros")
    print("Tente Novamente!")
else:
    resultado = calcAreaCirculo(raio)
    escreveResultado(resultado)