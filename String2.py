nome = 'Walafy'
idade = 29
profissao = 'administrador'
linguagem = 'Python'
nota = 9.80

dados = {'nome' : 'Walafy', 'idade' : 29, 'profissao': 'administrador'}

print('nome: {} idade: {} profissao: {}'.format(nome, idade, profissao))
print('nome: {1} idade: {0}'.format(idade, nome))
print('Nome: {nome} Idade: {idade} Profissao: {profissao}'.format(**dados))
print(f'Nome: {nome} Idade: {idade} Profissao: {profissao}')
print(f'Nome: {nome} Idade: {idade} Profissao: {profissao} Nota: {nota:.2f}')
