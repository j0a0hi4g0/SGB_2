class Livro:
    def __init__(self, titulo, autor, isbn, ano_publicacao, categoria):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        self.categoria = categoria


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        if livro.isbn in [livro.isbn for livro in self.livros]:
            print('O ISBN já existe na biblioteca')
        else:
            self.livros.append(livro)
            print('Livro adicionado à biblioteca.')

    def remover_livro(self, livro):
        self.livros.remove(livro)

    def buscar_livro_por_titulo(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None

    def buscar_livro_por_autor(self, autor):
        for livro in self.livros:
            if livro.autor == autor:
                return livro
        return None

    def buscar_livro_por_isbn(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro
        return None

    def buscar_livro_por_categoria(self, categoria):
        livros_encontrados = []
        for livro in self.livros:
            if livro.categoria == categoria:
                livros_encontrados.append(livro)
        return livros_encontrados

    def listar_livros(self):
        for livro in self.livros:
            print(f"{livro.titulo} - {livro.autor} - ISBN: {livro.isbn} - Ano da Publicação: {livro.ano_publicacao}  - Disponível: {livro.disponivel}")

    def registrar_emprestimo(self, livro):
        if not livro.disponivel:
            raise Exception("Este livro já está emprestado.")
        livro.disponivel = False
        print("Empréstimo registrado.")

    def registrar_devolucao(self, livro):
        if livro.disponivel:
            raise Exception("Este livro já está disponível.")
        livro.disponivel = True
        print("Devolução registrada.")

    def listar_livros_emprestados(self):
        for livro in self.livros:
            if not livro.disponivel:
                print(f"{livro.titulo} - {livro.autor} - ISBN: {livro.isbn} - Ano da Publicação: {livro.ano_publicacao} ")


class LivroComum(Livro):
    pass


class LivroRaro(Livro):
    def __init__(self, titulo, autor, isbn, ano_publicacao, categoria, edicao, estado):
        super().__init__(titulo, autor, isbn, ano_publicacao, categoria)
        self.edicao = edicao
        self.estado = estado

    def __str__(self):
        return f"{self.titulo}, {self.autor}, {self.isbn}, {self.ano_publicacao}, {self.disponivel}, {self.edicao}, {self.estado}"


biblioteca = Biblioteca()

while True:
    print("Selecione uma opção:")
    print("1 - Adicionar um livro comum à biblioteca")
    print("2 - Adicionar um livro raro à biblioteca")
    print("3 - Remover um livro da biblioteca")
    print("4 - Buscar um livro na biblioteca pelo título, autor, ISBN ou categoria")
    print("5 - Listar todos os livros da biblioteca")
    print("6 - Registrar um empréstimo de um livro")
    print("7 - Registrar a devolução de um livro")
    print("8 - Listar todos os livros emprestados")
    print("0 - Sair do programa")

    opcao = input()

    if opcao == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        isbn = input("Digite o ISBN do livro: ")
        ano_publicacao = input("Digite o Ano da publicação do livro: ")
        categoria = input("Digite a categoria do livro: ")
        livro = LivroComum(titulo, autor, isbn, ano_publicacao, categoria)
        biblioteca.adicionar_livro(livro)

    elif opcao == "2":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        isbn = input("Digite o ISBN do livro: ")
        ano_publicacao = input("Digite o Ano da publicação do livro: ")
        categoria = input("Digite a categoria do livro: ")
        edicao = input("Digite a edição do livro: ")
        estado = input("Digite o estado do livro: ")
        livro = LivroRaro(titulo, autor, isbn, ano_publicacao, categoria, edicao, estado)
        biblioteca.adicionar_livro(livro)

    elif opcao == "3":
        titulo = input("Digite o título do livro que deseja remover: ")
        livro = biblioteca.buscar_livro_por_titulo(titulo)
        if livro is not None:
            biblioteca.remover_livro(livro)
            print("Livro removido da biblioteca.")
        else:
            print("Livro não encontrado.")

    elif opcao == "4":
        termo = input("Digite o termo que deseja buscar: ")
        livros_encontrados = biblioteca.buscar_livro_por_titulo(termo)
        if not livros_encontrados:
            livros_encontrados = biblioteca.buscar_livro_por_autor(termo)
        if not livros_encontrados:
            livros_encontrados = biblioteca.buscar_livro_por_isbn(termo)
        if not livros_encontrados:
            livros_encontrados = biblioteca.buscar_livro_por_categoria(termo)

        if livros_encontrados:
            for livro in livros_encontrados:
                print(f"{livro.titulo} - {livro.autor} - ISBN: {livro.isbn} - Disponível: {livro.disponivel}")
        else:
            print("Nenhum livro encontrado.")

    elif opcao == "5":
        biblioteca.listar_livros()

    elif opcao == "6":
        titulo = input("Digite o título do livro que deseja emprestar: ")
        livro = biblioteca.buscar_livro_por_titulo(titulo)
        if livro is not None:
            try:
                biblioteca.registrar_emprestimo(livro)
            except Exception as e:
                print(e)
        else:
            print("Livro não encontrado.")

    elif opcao == "7":
        titulo = input("Digite o título do livro que deseja devolver: ")
        livro = biblioteca.buscar_livro_por_titulo(titulo)
        if livro is not None:
            try:
                biblioteca.registrar_devolucao(livro)
            except Exception as e:
                print(e)
        else:
            print("Livro não encontrado.")

    elif opcao == "8":
        biblioteca.listar_livros_emprestados()

    elif opcao == "0":
        break

    print()  # Adiciona uma linha em branco para melhorar a legibilidade
