print('='*50);
print("Este programa realiza a conversão de metros(m), para centimetros(cm).")
print('='*50);
print('')

def metrosPCm(metros):
    return metros * 100

def escreveResultado(r):
    print("{0} metros equivalem a {1} centimentros".format(metros, resultado))

try:
    metros = float(input("Qual o valor a ser convertido? "))
except ValueError:
    print("Digite Apenas Numeros")
    print("Tente Novamente!")
else:
    resultado = metrosPCm(metros)
    escreveResultado(resultado)