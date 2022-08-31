import math

print('='*50);
print("Este programa realiza o calculo da quantitade de tinta necessario para pintar uma determinada area.")
print('='*50);
print('')

tamanhoMetrosQ = float(input("Digite o tamamho em metros quadrados da area a ser pintada: "))
coberturaEmlitros = (tamanhoMetrosQ) / 3

latas = math.ceil((coberturaEmlitros ) / 18)
preco = latas * 80

print(f'Sera necessario {coberturaEmlitros: .2f} litros de tinta')
print(f'Latas de tinta necessaria para pintar {latas: .2f} latas de tinta')
print(f'Preço {preco: .2f} Total')
