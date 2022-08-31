print('='*50);
print("Este programa realiza o calculo de media de quatro notas bimestrais.")
print('='*50);
print('')

nota = "1"
count = 0
notas = []

while len(notas) < 4:
    count += 1
    print("Nota", count,": ", end="")
    try: 
        nota = int(input())
    except ValueError:
        print("Digite apenas numeros")
        print("Reinicie o programa!")
        break
    else:
        if nota > 10:
            print("Apenas notas menores que 10")
            print("Reinicie o programa!")
            break
        else:
            notas.append(nota)

sum = 0
           
for i in notas:
    sum = sum + i

media = sum/4
print("A media do aluno foi ",media)

if media > 5: 
    print("Aprovado")
else: 
    print('Reprovado')

