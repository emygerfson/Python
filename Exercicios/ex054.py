'''frase = str(input('Digite uma frase ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('TEMOS UM PALIMETRO')
else:
    print('NÂO E PALIMETRO')'''

frase = str(input('Digite uma frase ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('O inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('TEMOS UM PALIMETRO')
else:
    print('NÂO E PALIMETRO')

