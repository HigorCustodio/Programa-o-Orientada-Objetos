Existe uma maneira de representar objetos como textos no python usando dunder methods (funções especiais do python ex:__init__), o método usado
para representar um objeto em forma de texto é o __str__ que é uma função especial do python que retornara o valor do objeto em forma de str;
- Desta forma iremos substituir os prints dos objetos nos métodos nas funções imprime() para que ao invés de ser printado o valor, essa função __str__ retorne
o valor do objeto de forma textual;
- Vamos printar o 'programa' dentro do for para validar se o valor em formato de texto foi atribuido ao objeto;

Além do __str__ também existe um método não tão visual para demonstrar o valor de objeto, esse método é usado para debug e log de um objeto, esse método
se chama representação e é usado: __repr__;
O retorno do método __repr_ ao invés de uma string do tipo : 'Filme: Vingadores de 2018 - 160 min' irá retornar um texto que é exatamente igual a realização de uma instância de um
objeto: Filme(nome='Vingadores', ano=2018, duracao=160);
Essa forma de representação textual deixa muito claro o funcionamento do código e também facilita na recriação do objeto ja que esta mostrando a instância com todas as informações;

Outra forma de uso para o repr é usa-lo para identificar o que é esperado em uma lista  ex: 
lista = [0,1,2,3] 
print(repr(lista))

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
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'
    
class Filmes(Programa):             
    def __init__ (self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao
    
    @property
    def duracao(self):
        return self._duracao
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'
        
class Serie(Programa):
    def __init__ (self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas
       
    @property
    def temporadas(self):
        return self._temporadas

    def __str__(self):
        f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'
        
vingadores = Filmes('vingadores', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

vingadores.dar_likes() 
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta]
for programa in filmes_e_series:
    print(programa)

