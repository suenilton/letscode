# arquivo = open(r'D:\Suenilton\Pessoal\tibia\regeneração.txt')

# text = arquivo.read()

# print(text)
# arquivo.close()
#------------------------------------------------------------------
# utilizando o with faz com que o arquivo seja aberto e posteriormente fechado, sem necessidade de termos que fechar ele
# com o função .close().
# with open(r'D:\Suenilton\Pessoal\tibia\regeneração.txt', 'a') as arquivo2:
#     arquivo2.write('\ntexto inserido com sucesso')

# with open(r'D:\Suenilton\Pessoal\tibia\regeneração.txt', 'r') as arquivo3:
#     print (arquivo3.read())

#--------------------------------------------------------------------
# import csv

# with open (r'D:\Suenilton\Pessoal\Projetos Python\lets code\brasil_covid.csv', 'r') as arquivo:
#     leitor = csv.reader(arquivo)
#     # esse comando faz com que a primeira linha da iteração seja pulada
#     header = next(leitor)
#     for linha in leitor:
#         if float(linha[2]) > 1:
#             print(linha)
#--------------------------------------------------------------------
# import csv

# with open ('aula_letscode.csv', 'w', newline='') as arquivo_users:
#     escritor = csv.writer(arquivo_users)
#     escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
#     escritor.writerow(['Suenilton', 'Cipriano', 'sueniltonjunior@gmail.com ', 'masculino'])
#---------------------------------------------------------------------
# import csv

# header = ['nome', 'sobrenome']
# dados = []
# opc = int(input('Digite 1 para cadastrar e 2 para sair.\n'))

# while opc != 2:
#     nome = input('Digite o nome\n')
#     sobrenome = input('Digite o sobrenome\n')
#     dados.append([nome, sobrenome])
#     opc = int(input('Digite 1 para cadastrar e 2 para sair.\n'))

# print(dados)

# with open('nomes.csv', 'w', newline='') as arquivo_nomes:
#     escritor = csv.writer(arquivo_nomes)
#     escritor.writerow(header)
#     escritor.writerow(dados)

# with open('nomes.csv', 'r') as arquivo_nomes:
#     leitor = csv.reader(arquivo_nomes, delimiter=',')
#     for linha in leitor:
#         print(linha)
#----------------------------------------------------------------------
