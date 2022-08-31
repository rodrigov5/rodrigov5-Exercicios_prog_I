

arquivoMB = int(input("Digite o tamanho do arquivo em MB: "))
internetMbps = int(input('Digite a velocidade da sua internet em Mbps: '))

arquivomb = (arquivoMB * 8) / internetMbps

tempo = arquivomb / 60

print(f'O tempo necessario de download é: {tempo: .2f} minutos')