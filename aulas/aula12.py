nome = str(input("Qual é o seu nome? "))

if nome == "Vitor":
    print("Que nome bonito!")
elif nome in "Pedro Maria Paulo":
    print("Seu nome é bem popular no Brasil.")
elif nome in "Ana Claúdia Jéssica e Juliana":
    print("Belo nome feminino")
else:
    print("Seu nome é bem normal!")

print("Tenha um bom dia, {}!".format(nome))