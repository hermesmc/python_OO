class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

'''
Forma de acessar informações que não saõ comuns entre os objetos do tipo programa:

filmes_e_series = [filme1, filme2, serie1, serie2]

for programa in filmes_e_series:
    detalhe = programa.duracao if hasattr(programa,'duracao') else programa.temporada
    print(f'Programa: {programa.nome} - {detalhe} - {programa.likes}')
'''
