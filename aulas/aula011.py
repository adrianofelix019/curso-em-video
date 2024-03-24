nome = "Adriano"
cores = {"limpar": "\033[m",
         "negrito": "\033[1m",
         "branco": "\033[30m",
         "vermelho": "\033[31m",
         "verde": "\033[32m"}
print("Muito prazer em te conhecer {}{}{}!!!".format(
    cores["negrito"], nome, cores["limpar"]))

x = 'curso de python no cursoemvideo'
print(x[:5])