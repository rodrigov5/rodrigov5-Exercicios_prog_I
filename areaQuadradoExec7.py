
print('='*50);
print("Este programa recebe o lado de um quadrado e retorna sua area e posteriomente o dobro da area.")
print('='*50);
print('')

def calcAreaQuadrado(lado):
    return lado * lado

def dobraArea(resultado):
    return resultado * 2

try:
    lado = int(input("Qual o valor do lado? "))
except ValueError:
    print("Digite Apenas Numeros")
    print("Tente Novamente!")
else:
    resultado = calcAreaQuadrado(lado)
    dobro = dobraArea(resultado)
    print('A area do quadado e igual a: {0}'.format(resultado))
    print('O dobro da area do quadado e igual a: {0}'.format(dobro))
