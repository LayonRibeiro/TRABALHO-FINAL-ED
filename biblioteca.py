import json

# Estrutura básica para a biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []

    def carga_dados(self, dados):
        self.livros.extend(dados)

    def busca_simples(self, coluna, valor):
        resultados = [livro for livro in self.livros if livro.get(coluna) == valor]
        return resultados

    def busca_composta(self, coluna1, valor1, coluna2, valor2):
        resultados = [livro for livro in self.livros if livro.get(coluna1) == valor1 and livro.get(coluna2) == valor2]
        return resultados

    def incluir_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, coluna, valor):
        self.livros = [livro for livro in self.livros if livro.get(coluna) != valor]

    def exibir_todos(self):
        return self.livros

# Função para carregar dados a partir de um arquivo JSON
def carregar_dados_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados