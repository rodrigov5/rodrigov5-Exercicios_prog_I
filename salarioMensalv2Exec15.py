print('='*50);
print("Este programa realiza o calculo do salrio mensal + descontos do Imposto de renda.")
print('='*50);
print('')

try:
    valorHoras = float(input("Qual o valor da hora trabalhada? "))
    horasMensais = float(input("Horas mensais trabalhadas? "))
except ValueError:
    print("Digite Apenas Numeros")
    print("Tente Novamente!")
else:
    salario = valorHoras * horasMensais

    impostoRenda = salario * 0.11
    inss = salario * 0.08
    sindicato = salario * 0.05

    descontos = impostoRenda + inss + sindicato

    salarioLiquido = salario - descontos

    print(f'+ Salario bruto {salario: .2f}')
    print(f'- IR (11%): {impostoRenda: .2f}')
    print(f'- Inss (8%): {inss: .2f}')
    print(f'- Sindicato (5%): {sindicato: .2f}')
    print(f'= Salário Liquido {salarioLiquido: .2f}')

    