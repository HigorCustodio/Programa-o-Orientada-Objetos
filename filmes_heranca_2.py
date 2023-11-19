class Programa:
    def __init__(self, nome, ano):
        self._nome = nome  #Atributos privados vão para a classe filha se estiver com 1 underlines SEM O USO DO name mangling-->
        self.ano = ano
        self._likes = 0 #Atributos privados vão para a classe filha se estiver com 1 underlines SEM O USO DO name mangling-->

    @property
    def nome(self):
        return self._nome.title()
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    # @property
    # def ano(self):
    #     return self._ano

    @property
    def likes(self):
        return self._likes
    
    def dar_likes(self):
        self._likes += 1
    
class Filmes(Programa):             
    def __init__ (self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao
    
    @property
    def duracao(self):
        return self._duracao
        
class Serie(Programa):
    def __init__ (self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas
       
    @property
    def temporadas(self):
        return self._temporadas

        
vingadores = Filmes('vingadores', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

vingadores.dar_likes() 
atlanta.dar_likes()

print(f'Nome: {vingadores.nome}\n'
      f'Ano: {vingadores.ano}\n'
      f'Duração: {vingadores.duracao}\n'
      f'Likes: {vingadores.likes}\n')


print(f'Nome: {atlanta.nome}\n'
      f'Ano: {atlanta.ano}\n'
      f'Temporadas: {atlanta.temporadas}\n'
      f'Likes: {atlanta.likes}')