frase = str(input('\nDigite uma palavra: ')).upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!\n')
else:
    print('A palavra não é um palíndromo!')
