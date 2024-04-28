n = int(input('Quantos termos da sequência de Fibonacci deseja visualizar? '))
t1 = 0
t2 = 1
proximo = t1 + t2
contador = 2  # Iniciando em 2 porquê já foram calculados 2 termos.
print(t1, end=' ⇨ ')
print(t2, end=' ⇨ ')

while contador < n:
    print(proximo, end=' ⇨ ')
    t1 = t2
    t2 = proximo
    proximo = t1 + t2
    contador += 1

print('FIM')
