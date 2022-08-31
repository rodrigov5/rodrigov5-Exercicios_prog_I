print('='*50);
print("Este programa realiza o calculo do peso ideal.")
print('='*50);
print('')

def idealM(altura):
    return (72.7 * altura) - 58

def idealH(altura):
    return (62.1 * altura) - 44.7


altura = float(input("Digite sua altura: "))

genero = input("Digite seu genero, (h - Homem), (m - Mulher): ")

if genero == 'h':
    ideal = idealH(altura)
    print(f'Seu pesso ideal é: {ideal: .2f} Kilos')

if genero == 'm':
    ideal = idealM(altura)
    print(f'Seu pesso ideal é: {ideal: .2f} Kilos')