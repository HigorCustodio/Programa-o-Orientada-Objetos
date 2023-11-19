
Código inicial:
```python
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
```
# Usando Polimorfismo para criar uma playlist de programas:
    Problematica abordada: Como posso criar uma lista de objetos que irá me apresentar os programas, sendo que nessa lista existirão Series e Filmes que contém atributos
    diferentes em seus objetos?

# 1° Passo - Criar uma lista com os programas existentes:
    ```python
    filmes_e_series = [vingadores, atlanta]
    ```
# Uma vantagem de utilizar a idéia de Herança:
    Ao ter uma classe "Mãe/Pai" as classe que herdam os atributos, ou seja, as classes filhas, podem ser consideradas do mesmo tipo da classe "Mãe/Pai", o que isso quer dizer?
        - Objetos filhos tem um relacionamento com a classe "Mãe/Pai" esse relacionamento é chamado de "É UM", ou seja, uma classe filho é do mesmo tipo de sua classe "Mãe/Pai". 
        - Esse relacionamento pode ser apresentado da seguinte maneira:
            
                                            Classe ("Mãe/Pai") Programa
            Classe ("Filho") Filmes ------>         É UM Programa       <------ Classe ("Filho") Series
            
            Ou seja, um Filme é um Programa e uma Serie é um Programa, porém, um Filme não é uma Serie, nem uma Serie é um Filme;

# Como Usar Essa Caracteristica de Herança:
    Devido as Classes "Filhos" serem do mesmo tipo da classe "Mãe", isso nos permite utilizar um "for" em uma lista que é composta tanto por Filmes, quanto por Series, algo que NÃO seria possível na maioria dos casos devido os atributos especificos das classes Filhas serem DIFERENTES;
    Exemplo:
```python
        for programa in filmes_e_series:
            print(f'{programa.nome} - {programa.temporada}: - {programa.likes})
```
    Ao executar esse loop for, será retornado um erro, isso ocorre devido ao fato de que nem todas as classes Filhas possuem o atributo "temporada", logo, quando o loop buscou esse atributo dentro do objeto da classe Filha Filmes e não encontrou ele retorna um "AttributeError".

## O que é o POLIMORFISMO?
    Apesar de termos classes Filhas com alguns atributos especificos, elas tendo uma estrutura semelhante, podemos usa-las em um loop apesar de serem objetos diferentes, isso se da graças a serem do mesmo Tipo da classe Mãe, ou seja, sempre que for preciso posso fazer um for onde será abordado os atributos compartilhados da classe Mãe.

    Se for preciso aplicar um for contendo também os atributos especificos das Classes Filhos, esses atributos terão de ter algum tipo de tratamento para reconhecer qual é a Classe Filha sendo executada para que não ocorra um Erro.

## Como faço para poder buscar as duas classes Filhas dentro do loop mesmo tendo atributos diferentes?
    Posso verificar qual é a classe em questão verificando se a classe contém ou não determinado atributo, posso fazer isso utilizando a função built-in do python chamada
    de "hass attibute".

    Sintaxe:  
```python
    hasattr(objeto, nome_do_atributo) -> bool: 
```
    "Dentro desse objeto, existe determinado atributo?"


    Exemplo:
```python
        for programa in filmes_e_series:
            detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
            print(f'{programa.nome} - {detalhes} D: - {programa.likes})
```

    Logo o retorno desse loop será:
    >>> Vingadores - Guerra Infinita - 160 D - 1
    >>> Atlanta - 2 D - 2

    Onde para a classe filha Filmes o detalhes assumiu programa.duracao e para a classe filha Series programa.temporadas.

# Como reduzir os if's do código com herança?
    No código acima, temos um if ternário para realizar a verificação se o programa tem duração ou temporada como atributo da classe filha em questão, porém, se fosse preciso realizar a validação
    ou a busca de varios atributos, possivelmente o código receberia um aumento consideravel no numero de If's;

    No caso de retornar a informação sobre temporadas ou duração do programda, queremos imprimir informações acerca dos objetos, mas estamos nos aprofundando demais sem necessidade.
    Queremos saber se o objeto possui duracao ou temporadas e estamos lidando com Programa, um tipo de objeto.

    Nesse caso não precisamos saber se programas têm temporadas ou durações, eles simplismente precisam ser exibidos. De certa forma, as classes Filme e Séries deveriam ser responsáveis por
    realizar suas impressões. 

    *Quando vamos modelar uma classe e objetos sempre devemos levar em consideração suas responsabilidades!*

    Cada classe deve ter sua responsabilidade com clareza, quando isto ocorre, é possível chama-la de "classe coesa", ou seja, quando ela sabe qual é a sua responsabilidade e não faz mais do que aquilo a que se propõe a fazer.

    No caso em questão, tanto a classe Filmes, quanto a classe Series devem saber se imprimir de forma usual.

    No Python, existem várias maneiras de imprimir o valor de um objeto. Para fins de exemplo, podemos fazer uma definição em Programa:
```python
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self._likes} Likes')
```

    Com isso, mudaremos o fim do código para não precisarmos mais do if que estávamos usando anteriormente, já que usaremos o método imprime():

    ```python
    for programa in filmes_e_series:
        programa.imprime()
    ```
    Executaremos a aplicação, e será impresso:

    >>> Vingadores - Guerra Infinita - 2018 - 1 Likes
    >>> Atlanta - 2018 - 2 Likes
    >>> Process finished with exit code 0

    Resolvemos uma parte do problema! Agora, precisaremos não só imprimir o dado de um programa genérico, e sim para cada tipo diferente existente. No entanto, não poderemos herdar este comportamento de imprime() do Programa. Teremos que definir um método para cada uma das classes filhas.

    Neste caso, faremos uma sobrescrita de imprime() da classe mãe, porque não queremos utilizá-lo. No caso de Filme, incluiremos portanto a duracao:

    ```python
    class Filme(Programa):
        def __init__(self, nome, ano, duracao):
            super().__init__(nome, ano)
            self.duracao = duracao

        def imprime(self):
            print(f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes')
    ```

    E para Serie, aplicaremos o mesmo, apenas substituindo as informações sobre a duração para temporadas:

```python
    class Serie(Programa):
        def __init__(self, nome, ano, temporadas):
            super().__init__(nome, ano)
            self.temporadas = temporadas

        def imprime(self):
            print(f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes')
```

    Desta vez, temos um imprime() diferente para cada uma das classes filhas. 

# Esta é a ideia do polimorfismo: 
    Por meio de um for, conseguimos mostrar que, a cada iteração a ser executada, estaremos com Filme ou Serie, e quando o imprime() for chamado, não importa qual o tipo deste objeto, o método será chamado de acordo com quem o tiver.

    Vamos fazer um teste executando o código. Veremos:

    >>> Vingadores - Guerra Infinita - 2018 - 160 min - 1 Likes
    >>> Atlanta - 2018 - 2 temporadas - 2 Likes
    >>> Process finished with exit code 0