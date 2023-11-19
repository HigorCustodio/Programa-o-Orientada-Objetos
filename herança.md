Herança em Orientações a Objetos com Python:

Objetivos:
    - Menos duplicação e mais reuso de código;

Hierarquia de classes:

- Name mangling: 
        Ao usar os dois underlines na frente de uma variavel é aplicado a ela o name mangling que altera a variavel para dificultar o uso externo 
        da mesma.
        ex:
        class Programa:    
            def __init__(self, nome, ano):
                self.__nome = nome <!-- Para acessar a variavel de forma externa seria preciso acessa-la como: _Programa__nome ao inves de __nome>

        Para resolver esse problema gerado pelo name mangling envolvendo a herança de classes, podemos alterar o atributo privado de 2 underlines(__nome), para 1 underline(_nome), onde o underline na frente da variavel indicaria para os programadores que irão utilizar o código que é um atributo privado devido ao uso do underline, porém, não ativaria o recurso do name_mangling do Python alterando a variavel, logo resolveria o problema de herança

    COM NAME MANGLING:
        class Programa:
            def __init__(self, nome, ano):
                self.__nome = nome.title() <!-- Atributos privados não vão para a classe filha se estiver com dois underlines devido ao name mangling-->
                self.ano = ano
                self.__likes = 0 <!-- Atributos privados não vão para a classe filha se estiver com dois underlines devido ao name mangling-->

        class Filme(Programa): <!-- Dentro do parenteses fica a classe que será o "PAI"-->
            def __init__(self, nome, ano, duracao):
                self.__nome = nome.title() <!-- gerará um erro ao herdar o atributo do pai devido ao uso do name mangling-->
                self.ano = ano
                self.duracao = duracao
                self.__likes = 0 <!-- gerará um erro ao herdar o atributo do pai devido ao uso do name mangling-->


    SEM O NAME MANGLING:
        class Programa:
            def __init__(self, nome, ano):
                self._nome = nome <!-- Atributos privados vão para a classe filha se estiver com 1 underlines SEM O USO DO name mangling-->
                self.ano = ano
                self._likes = likes <!-- Atributos privados vão para a classe filha se estiver com 1 underlines SEM O USO DO name mangling-->

        class Filme(Programa): <!-- Dentro do parenteses fica a classe que será o "PAI"-->
            def _init__(self, nome, ano, duracao):
                self._nome = nome.title() <!-- gerará um erro ao herdar o atributo do pai devido ao uso do name mangling-->
                self.ano = ano
                self.duracao = duracao
                self._likes = 0 <!-- gerará um erro ao herdar o atributo do pai devido ao uso do name mangling-->


Usando o Super para resolver a duplicação de código:
    -   O objetivo de diminuir a replicação do mesmo código é diminuir possiveis alterações em pontos de falha do código replicado, onde caso precise ser alterado um atributo teremos que alterar em diversos pontos do código, logo o que é uma má prática dentro do mundo da programação;

    -   A alteração realizada acima para retirar o name mangling resolve o problema dos atributos serem herdados para as Classes Filhas, pórem, não resolve o problema da replicação do mesmo código nas funções construtoras das Classes Filhas;
    
    - Para resolver esse problema podemos:
    
    Super classe(PAI):
        class Programa:
            def __init__(self, nome, ano):
                self._nome = nome
                self.ano = ano
                self._likes = likes 

    Classe filha:
        class Filme(Programa): <!-- Dentro do parenteses fica a classe que será o "PAI"-->
            def _init__(self, nome, ano, duracao):
                super().__init__(nome, ano) --> Chama o construtor com os parametros da classe mãe
                self.duracao = duracao
               
