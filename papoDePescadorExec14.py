print('='*50);
print("Este programa realiza o calculo de multa por quilo excedente.")
print('='*50);
print('')

pesoPeixe = float(input("Digite o peso do peixe: "))

if pesoPeixe > 50:
    PesoExcedente = pesoPeixe - 50
    multa = PesoExcedente * 4
    print(f'Peso do peixe {pesoPeixe: .2f} Kilos')
    print('O peso limite é 50.00 kilos')
    print('valor da multa por kilo excedente: RS 4.00')
    print(f'Kilos excendentes {PesoExcedente: .2f}')
    print(f'Voce vai pagar {multa: .2f} Reais de multa')
else :
    print(f'Peso do peixe {pesoPeixe: .2f} Kilos')
    print('Sem excedente')