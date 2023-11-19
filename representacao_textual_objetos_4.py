
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome  
        self.ano = ano
        self._likes = 0 
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
    
    def __str__(self): #* dunder method para atribuir valor em forma de texto para o objeto
        return f'{self._nome} - {self.ano} - {self._likes} Likes'
    
    def __repr__(self) -> str:
        return "Programa(nome=%r, ano=%r, likes=%r)" % (self._nome, self.ano, self._likes)
    
class Filmes(Programa):             
    def __init__ (self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao
    
    @property
    def duracao(self):
        return self._duracao
    
    def __str__(self): #* dunder method para atribuir valor em forma de texto para o objeto
        return f'{self._nome} - {self.ano} - {self._duracao} temporadas - {self._likes} Likes'
    
    def __repr__(self) -> str:
        return "Filmes(nome=%r, ano=%r, duracao=%r)" % (self.nome, self.ano, self._duracao)
    
class Serie(Programa):
    def __init__ (self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas
       
    @property
    def temporadas(self):
        return self._temporadas

    def __str__(self): #* dunder method para atribuir valor em forma de texto para o objeto
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'
    
    def __repr__(self) -> str:
        return "Serie(nome=%r, ano=%r, temporadas=%r)" % (self.nome, self.ano, self._temporadas)
    
vingadores = Filmes('vingadores', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

vingadores.dar_likes() 
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta]
for programa in filmes_e_series:
    
    print(repr(programa)) #Exibindo objeto
    print(programa) #Exibindo objeto
# exemplos de representação de texto usando __repr__ e repr()

lista = [0,1,2,3] 
print(repr(lista))