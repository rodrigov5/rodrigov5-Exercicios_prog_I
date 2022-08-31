print('='*50);
print("Este programa realiza o calculo de salario mensal.")
print('='*50);
print('')

try:
    valorHoras = float(input("Qual o valor da hora trabalhada? "))
    horasMensais = float(input("Horas mensais trabalhadas? "))
except ValueError:
    print("Digite Apenas Numeros")
    print("Tente Novamente!")
else:
    resultado = valorHoras * horasMensais
    print('O seu salario e de:', resultado)