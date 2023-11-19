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
    
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self._likes} Likes')
    
class Filmes(Programa):             
    def __init__ (self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao
    
    @property
    def duracao(self):
        return self._duracao
    
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes')
        
class Serie(Programa):
    def __init__ (self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas
       
    @property
    def temporadas(self):
        return self._temporadas

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes')
        
vingadores = Filmes('vingadores', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

vingadores.dar_likes() 
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta]
for programa in filmes_e_series:
    programa.imprime()