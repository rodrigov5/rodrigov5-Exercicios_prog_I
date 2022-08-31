import math

print('='*50);
print("Este programa realiza o calculo da quantitade de tinta necessario para pintar uma determinada area.")
print('='*50);
print('')

tamanhoMetrosQ = float(input("Digite o tamanho da area a ser pintada: "))
litrosNecessarios = tamanhoMetrosQ / 6

latas = int(litrosNecessarios/18)
galoes = int(litrosNecessarios/3.6)



if latas % 18 != 0:
    latas += 1

if galoes % 3.6 != 0:
    galoes += 1

precoLatas = latas * 80
precoGaloes = galoes * 25

misturaLata = litrosNecessarios / 18.0
misturaGalao = (litrosNecessarios - (misturaLata * 18)) / 3.6


folga = litrosNecessarios * 0.1
litrosNecessariosFolga = litrosNecessarios - folga
if litrosNecessariosFolga - (misturaLata * 18) % 3.6 != 0:
    misturaGalao += 1



print('Tamanho a serem pintados', tamanhoMetrosQ)
print('Litros de tinta necessarios', litrosNecessarios)
print('_' * 30,)

print()
print(f'Usando apenas {latas} Latas, preço {precoLatas}')
print(f'Usando apenas {galoes} galoes, preço {precoGaloes}')


misturaLata = int(litrosNecessariosFolga / 19.0)
misturaGalao = int((litrosNecessariosFolga - (misturaLata * 18)) / 3.6)

if litrosNecessariosFolga - (misturaLata * 18) % 3.6 != 0:
    misturaGalao += 1



print(f"Mistura {latas} latas e {galoes} galoes preco {(misturaGalao * 25) + (misturaLata * 80)}")


