from datetime import date


nome = str(input('Nome: '))
ano_de_nascimento = int(input('Ano de nascimento: '))
carteira_de_trabalho = int(input('Carteira de trabalho: '))

ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento

funcionario = {
    'nome': nome,
    'idade': idade,
    'ctps': carteira_de_trabalho
}

if carteira_de_trabalho != 0:
    funcionario['contratacao'] = int(input('Ano de contratação: '))
    funcionario['aposentadoria'] = (35 - (ano_atual - funcionario['contratacao'])) + idade
    funcionario['salario'] = float(input('Salário: '))

print('-=' * 50)
for k, v in funcionario.items():
    print(f'{k} tem o valor {v}')
