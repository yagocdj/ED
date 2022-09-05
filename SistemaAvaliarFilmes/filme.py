class Filme:
    # construtor
    def __init__(self, id, titulo, nota, preco):
        self.id = id
        self.titulo = titulo
        self.nota = nota
        self.preco = preco

    def reajustarPreco(self, novoPreco):
        self.preco = novoPreco

    def avaliar(self, novaNota):
        self.nota = novaNota

    # método especial que permite apresentar uma descrição personalizada do
    # objeto que recebe um print()
    def __str__(self):
        return f'{self.id}-{self.titulo}, R$ {self.preco}'

# __name__ é uma variável embutida de Python que, neste exemplo, está sendo
# utilizada para verificar se o programa principal está sendo executado
# a partir do arquivo no qual a classe está contida


if __name__ == '__main__':
    # Instanciando objetos na memória a partir da classe Filme
    filme1 = Filme(1, 'Tropa de Elite', None, 21.5)
    print('Acessando a propriedade de instância pública "título":', filme1.titulo)
    filme1.nota = -1
    print('Modifiquei o conteúdo de uma propriedade pública:', filme1.nota)

    filme2 = Filme(2, 'Toy Story 3', None, 15.00)

    filmes = [Filme(1, 'Tropa de Elite', None, 21.5),
              Filme(1, 'Tropa de Elite', None, 21.5)]

    # conferindo a tipagem dos objetos
    print('filme1: ', type(filme1))
    print('filme2: ', type(filme2))

    # aqui teremos o método __str__() em ação
    print(filme1)
    print(filme2)

    filme1.reajustarPreco(55)
    print(filme1)
    filme2.reajustarPreco(100)
    print(filme2)
