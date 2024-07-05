if __name__ == "__main__":
    from biblioteca import Biblioteca


    biblioteca = Biblioteca()

    # Carregar dados predefinidos
    dados_iniciais = [
        {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "editora": "Secker & Warburg"},
        {"titulo": "Brave New World", "autor": "Aldous Huxley", "ano": 1932, "editora": "Chatto & Windus"},
        {"titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "ano": 1953, "editora": "Ballantine Books"},
        {"titulo": "Animal Farm", "autor": "George Orwell", "ano": 1945, "editora": "Secker & Warburg"}]
    biblioteca.carga_dados(dados_iniciais)

    # Adicionar um novo livro
    novo_livro = {"titulo": "Dune", "autor": "Frank Herbert", "ano": 1965, "editora": "Chilton Books"}
    biblioteca.incluir_livro(novo_livro)

    # Buscar livro por título
    resultado_busca_simples = biblioteca.busca_simples("autor", "George Orwell")
    print("Busca Simples por Título '1984':", resultado_busca_simples)

    # Buscar livro por autor e ano
    resultado_busca_composta = biblioteca.busca_composta("autor", "George Orwell", "ano", 1949)
    print("Busca Composta por Autor 'George Orwell' e Ano '1949':", resultado_busca_composta)

    # Remover um livro por título
    biblioteca.remover_livro("titulo", "Brave New World")
    print("Todos os Livros após Remoção:")
    print(biblioteca.exibir_todos())

    # Exibir todos os livros
    print("Todos os Livros:")
    print(biblioteca.exibir_todos())