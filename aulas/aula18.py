galera = []
dados = []

for c in range(3):
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    dados.append(nome)
    dados.append(idade)
    galera.append(dados[:])
    dados.clear()

for p in galera:
    nome = p[0]
    idade = p[1]
    if idade >= 21:
        print(f"{nome} é maior de idade.")
    else:
        print(f"{nome} é menor de idade.")
