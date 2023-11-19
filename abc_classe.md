    
## Classes abstratas ou ABCs Classes (Abstract Base Classe):

Interfaces no python diz respeito a um "contrato", onde, quando for realizada a implementação da subclasse (que herdará a classe ABCs) seja expressamente necessário a inserção de determinados métodos obrigatórios do tipo de classe abstrata herdada, caso os métodos não sejam implementados, na hora da instância do objeto o compilador do python retornará um erro informando não ser possível implementar a classe abstrada e quais os métodos que precisam ser implementados para que seja possível a criação do objeto;

Exemplo de importação:
#   from abc import ABC (Abstract base classes)
#   from collections.abc import MutableSequence (Abstract base classes)
#   from numbers import Complex


# O python nos indica à sempre que necessário realizar a criação de uma classe que dependa de outra, verificar dentro das coleções de classes abstratas se não existe alguma que se adeque ao nosso problema;


Exemplo de classe abstrada (ABCs):
    Lista mutavel:
```python
#Entrada:
    from collections.abc import MutableSequence

    class Playlist(MutableSequence):
        pass
'''
    Devido o python ser uma linguagem dinâmica, quando implementamos o conceito de classes abstratas, se executarmos o código da maneira que 
    está acima é de se esperar que o compilador retorne um erro já que a subclasse Playlist não implementa nenhum método da classe abstrata MutableSequence, porém, devido o python ser uma linguagem compilada e dinâmica, ao executarmos esse código o compilador não retornará nenhum erro.
'''
Saída:
    #Sem dados de saída;

``` 

- Para que seja realizado a validação se todos os métodos das classes abstratas foram implementadas ou não é necessário a realização da instância do objeto, e ai sim realizar a execução do código, onde, para o caso de faltar métodos a serem implementados o compilador do python retornará um exceção informando quais os métodos faltantes para que seja possível herdar o comportamento da classe abstrata;
Exemplo:

```python
#Entrada:
    from collections.abc import MutableSequence

    class Playlist(MutableSequence):
        pass

    play_list = Playlist()

Saída:
   #! Ocorreu uma exceção: TypeError
    # Can't instantiate abstract class Playlist with abstract methods __delitem__, __getitem__, __len__, __setitem__, insert
    
``` 

# Quando usar as ABCs Classes?

    - É indicado o uso das classes abstratas quando temos alguns comportamentos dentro de nossa subclasse que desejamos reforçar e/ou obrigar e serem utilizados;

# ABCs Classes X Duck Typing:

    - Vimos que no conceito de Duck typing é indicado que para a implementação de comportamento à nossas classes é mais indicado inserir determinado comportamento dentro da classe através de um dunder_method/magic_method, desta forma a nossa classe iria conseguir realizar as operações necessárias realizar a herança de classes nativas do python como 'list', onde se realizado a herança é almentado drasticamente a complexidade para a escala do código, onde, sempre será necessário na implementação de novos métodos consultar para ver se o que estamos criando existe ou fere fundamentos da classe Mae;
    
    - Desta forma o Duck typing usa de certa forma a filosofia 'se se comporta como pato, é um pato' onde o python entende que, se aquele objeto se comporta como um iteravel então ele pode ser iteravel, mesmo que o objeto não seja uma lista;

    O problema do Duck Typing é que, como o python é uma linguagem dinâmica e livre de diversas restrições existentes em liguagens como o 'Java', fica um pouco mais difícil que você consiga restringir o sua classe, a ser obrigada a receber determinadas informações para que possa se comportar da maneira esperada.

    Desta forma as Classes Abstratas ou ABCs Classes foram criadas para poder complementar o Duck Typing, suprindo essa necessidade de criar uma espécie de "contrato" para que o uso de nossa subclasse só seja possível se em sua implementação forem inseridos métodos que moldam os comportamentos da subclasse para com a implementação desses métodos "obrigatórios" a subclasse em questão se comporte como a Classe abstrata desejada;

    - É de grande valía que essas filosófias sejam implementadas em aplicações onde para que o fluxo de funcionamento daquela aplicação siga de forma correta e esperada, as informaçoes passadas para as subclasses sigam sempre um padrão especificado e esperado, onde a subclasse semrpe terá os mesmos comportamentos.

# Em Resumo:
    - Servem para estabelecer através da herança de uma classe abstrata, quais os métodos necessários para que a subclasse tenha posteriormente na hora da implementação determinado comportamento, e para que não seja possível instânciar o objeto da subclasse caso o objeto não atenda aos comportamentos estabelecidos dentro da classe abstrata.

    Situação onde devo aplicar os conceitos e implementação de ABCs Classes:
        Preciso herdar um comportamento de alguem?
        - Sim.
        Tenho que garantir esse comportamento?
        - Sim.

        Se as duas respostas forem um 'Sim', seria uma situação onde seria indicado o uso de uma ABCs(Abstract Base Classe);

        Caso só exista a necessidade de herdar um comportamento, deve se realizar a analíse do problema e verificar qual a possíbilidade de resolver o problema utilizando somente o conceito do Duck Typing.

# Método com implementação feita de forma interna na classe Abstrata:
```python

#Exemplo de método implementado internamente na classe abstrata:
    from numbers import Complex

    class Numero(Complex):
        def __getitem__(self, item):
            super().__getitem__()

    numero = Numero()    
``` 

- Vimos que em ABCs classes para que seja possível a implementação de uma subclasse que herde comportamentos de uma classe abstrata, é necessário a implementação dos métodos obrigatórios da classe Mae(ABCs) para que ela assuma o comportamento da classe Mae, porém, em alguns casos a classe abstrata possuí uma implementação interna de alguns métodos obrigatórios.

- Esses métodos obrigatórios já implementados dentro da classe abstrata servem como um ínicio para para poder realizar determinado comportamento;

- Só é possível descobrir quais classes ABC possuem implementações internas e como irão se comportar, através da documentação da ABCs Classe.

### Exemplo de Problema:

