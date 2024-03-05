nome = str(input("Qual seu nome? "))
if nome == "Vitor":
    print("Que nome bonito!")
elif nome in ["Pedro", "Maria", "Paulo"]:
    print("Seu nome é bem popular no Brasil.")
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Belo nome feminino")
else:
    print("Seu nome é bem chato!")
print(f"Tenha um bom dia, {nome}!")
