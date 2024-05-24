#lista de 15 nomes.
nomes = ["Emanuel","Natalia","Alex","Maria","Carlos","Silvio","Pedro","Thais","Carla","Samara","Mayara","Márcio","Marilia","Sabrina", "Endrick"]

#usuário informa o nome de que deseja pesquisar.
nome = input("Digite o nome a ser pesquisado:").capitalize()

try:
#retorna o índice do nome pesquisado.
    indice = nomes.index(nome)
    print(f'Nome encontrado: {nome}.')
#verifica se o nome está na lista ou não.

except:
    print(f'{nome} não encontrado na lista.')