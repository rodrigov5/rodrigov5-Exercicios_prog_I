print('='*50);
print("Este programa realiza o calculo do pesso ideal de uma pessoa.")
print('='*50);
print('')

altura = float(input("Digite Sua altura: "))

pesoIdeal = (altura * 72.7) - 58

print(f'O seu pesso ideal é: {pesoIdeal: .2f} Kilos')