Herança em um built-in:
    Quando realizamos a herança de uma classe, herdamos todos os comportamentos daquela Super Classe, porém, nem sempre vou precisar | nem sempre vou querer utilizar todos na minha classe,
    fora que se ocorrer alguma mudança na classe herdada, isso poderá afetar o comportamento da minha classe.

O que é necessário para a Classe Playlist é aplicar uma idéia de encapsulamento da lista no meu objeto Playlist, porém, sem depender tanto da classe List, a qual não conheço todas suas
caracteristicas.

Usando for in no objeto original:
```python
    #Entrada:
    for programa in playlist_fim_de_semana.listagem:
        print(programa)

    #Saída:
    >>> vingadores - 2018 - 160 temporadas - 1 Likes
    >>> atlanta - 2018 - 2 temporadas - 1 Likes
```
Para que seja possível utilizar o for in da maneira original do objeto, é necessário a criação de uma lista contendo os objetos da classe Programa,
para que não seja retornado um erro pois o objeto playlist_fim_de_semana não é iterável sozinha como demonstrado no exemplo abaixo:

```python
    #Entrada:
    for programa in playlist_fim_de_semana:
        print(programa)

    #Saída:
    >>> TypeError: playlist_fim_de_semana not iterable!
```

A lógica desta aplicação indica que faz todo o sentido eu poder iterar o objeto playlist_fim_de_semana, já que é uma playlist obviamente deveria retornar uma lista de 
programas, porém, como posso fazer o objeto playlist_fim_de_semana ser  um iterável (poder realizar for in e in) sem que ele fique vulneravel as restrições e mudanças da classe List através da herança?

No Python não é obrigatório o uso de herança em casos onde preciso somente transformar minha classe em iterável, ou seja, quando tudo que é preciso é aplicar o comportamento de um iterável à uma classe, eu preciso saber qual o comportamento de um iterável e aplicar esse comportamento a minha classe sem necessáriamente precisar herdar diversos outros comportamentos para que isso seja possível;

Como posso aplicar um comportamento de iterável a uma classe no Python?
    Utilizando um dunder_method(magic_method) para aplicar um comportamento à uma classe:
        __getitem__: Aplicando esse método a uma classe, posso dizer e assumir que a minha classe receberá o comportamento de um iterável;
            -   Esse método define que alguem(algum objeto) se tornará iterável;
        Sintaxe:
```python
                def __getitem__(self, item):
                    return self._programas[item]
                # Pegue os itens atribuidos a self._programas e crie uma lista de classes com esses items, lista que será atribuida ao objeto na instância da classe;
```
        Desta forma aplicamos o comportamento de iterável, onde, minha classe playlist_fim_de_semana irá conter uma lista dos programas recebidos no parâmetro self._programas resultando assim
        em a classe playlist_fim_de_semana contém uma lista de programas ao invés de ser uma classe com comportamento de lista;

        Com a aplicação deste dunder_method à classe PlayList, agora é possível aplicar o objeto playlist_fim_de_semana diretamente À um "for in" ou um 'in', já que agora a classe PlayList 
        possuí um comportamento de iterável;

Realizando um laço de repetição "for in" direto na instância da classe:
```python
    #Uso do for in:
    #Entrada:
    for programa in playlist_fim_de_semana:
        print(programa)

    #Saída:
    >>> vingadores - 2018 - 160 temporadas - 1 Likes
    >>> atlanta - 2018 - 2 temporadas - 1 Likes
```

Buscando de um valor existe dentro de um objeto iterável:
```python
    #Uso do in:
    #Entrada:
    print(demolidor in playlist_fim_de_semana)
       
    #Saída:
    >>> False
```

Agora também é possível acessar os programas por um ìndice semelhante ao de uma lista:
```python
    #Entrada:
    print(playlist_fim_de_semana[0])
       
    #Saída:
    >>> vingadores - 2018 - 160 temporadas - 1 Likes
```

Tipos de Herança:

            Interface X Reuso

    Interface: Tipo de herança feita para quando é necessário absorver a idéia de polimorfismo, pode-se dizer que quando é feita a herança de classes pensando no polimorfismo(possibilidade
    de uso em loops) essa herança é feita baseando-se na interface;

    Reuso: Tipo de herança feita quando é necessário a remoção de duplicação de código, ou seja, quando uma herança é feita pensando somente em não realizar a duplicação de código através do reuso 
    dos meétodos de uma Super Classe, essa herança é baseada em Reuso;

    Ex:
        No caso da PlayList, tinhamos somente o motivo de aplicar algumas funcionalidades de um objeto list para a classe PlayList, para que assim fosse possivel utilizar algumas operações
        que são passiveis de uso em objetos list, como : 'for in' 'in' 'len';

        Esse pensamento me levou a implementar uma herança pensando somente no reuso de funcionalidades, onde eu poderia com algumas linhas de código adicionar a funcionalidade que eu gostaria
        adicionando uma lista manualmente, porém, decidi por herdar essas mesmas caracteristicas do objeto List. Devido a isso me deparei com algumas possibilidades de futuros erros, e/ou complicações no código caso alguma funcionalidade interna da classe List fosse alterada, já que se isso ocorresse poderia ser necessário mudar toda a lógica do código;

    Quando eu for fazer o uso de Herança é necessário me atentar sempre aos dois tipos de herança, ou seja, sempre que surgir a possibilidade de realizar a herança de uma classe, devo
    levar em consideração se a minha situação atende aos dois tipos de herança, onde minha herança será aplicada devido a uma necessidade de facilitar a manipulação da classe através do polimorfismo e que utilize de reuso para que não seja feita duplicação em códigos existentes;

    Formas de Reuso:
                Composição X Extensão

        Composição: É quando atribuimos a funcionalidade que desejamos para dentro do nosso objeto onde, o meu objeto tem determinada funcionalidade e não necessáriamente ele é da classe dessa funcionalidade, ou seja, minha classe não é uma lista, porém, contém dentro de si uma lista;

        Com isso é obtido as funcionalidades desejadas sem necessáriamente precisar transformar minha classe em um determinado objeto;

        Sendo mais claro: Tenho uma playlist que se comporta como uma list/iterável;

        Exemplo de composição : dunder_method(magic_method) __getitem__()


        Extensão: É quando a minha classe assume a forma de uma Super Classe, ou seja, se minha classe herda uma Super Classe list, automaticamente ela é um objeto list;
        É quando utilizamos de herança para extender as funcionalidades de um objeto através da herança das funcionalidades de uma Super Classe, ou seja, pego uma classe genérica e realizo a extensão dela para a classe desejada.

        Pontos a levar em consideração:     
            Ao se utilizar a Extensão como forma de reuso de código, será herdado todo o código da Super Classe herdada e seus comportamentos, ou seja, caso eu não deseje algum comportamento herdado, terei que forçadamente sobrescrever esse comportamento para que ocorra da forma desejada, o que pode trazer mais complexidade ao código;

            Nesse método de reuso de código é realizado uma ligação muito forte entre a Super Classe e a classe que irá herdar os comportamentos, ou seja, se torna um relacionamento com muito acoplamento e influência da Super classe na classe final, onde se algo muda dentro da Super Classe pode afetar e quebrar as funcionalidades da classe final.

            Não tem muito controle das variáveis que podem quebrar o código;

        Sendo mais claro: Tenho uma playlist que é uma list;
        

Duck Typing:
    É o termo usado para a caracteristica do Python de não precisar usar necessáriamente uma herança para que determinado objeto possa ser usado em operações especificas como no caso de um iterável, se o objeto se comporta como uma determinada classe automaticamente o python consegue realizar a operação que é travada para determinado tipo de objeto;

    Sendo mais claro: O python não precisa ter a certeza de que é um "Pato", se se comporta como um "Pato" pode ser utilizado em operações restritas á um objeto Pato;
    Ex: Para que seja necessário realizar operações como "for in" é necessário que minha classe seja do tipo List, porém, se meu objeto não é uma List, mas, se comporta como uma List, logo o python assume que esse objeto é um iterável e consegue realizar a operação; 
    Não é travada pela tipagem da classe;

    Pode se utilizar a função dunder_method __getitem__();

Python Data Model:
    Protocolos em python:
    Todo objeto em python pode se comportar para que fique compativel e/ou mais proximo da linguagem e de toda ideia idiomatica (caracteristicas especificas da linguagem);

    Exemplos de dunder_methods que são usados no Data Model:
        
    Inicialização de classe: __init__;
        ex: 
            - obj = Novo(): inicialização de um novo obj.

        Representação textual da classe: __str__, __repr__;
        ex: 
            - print(obr): mensagem que irá aparecer ao printar o objeto, mensagem implementada pelo __str__;
        
            - str(obj): imprime representação textual do obj  pelo __str__;
        
            - repr(obj): Irá imprimir uma representação textual, porém, é indicado que essa representação seja uma representação da inicialização daquele objeto pelo __repr__;

    Container, se comportar como sequencia: __contains__, __iter__, __len__, __getitem__;
        ex:
            - len(obj): torna possível o acesso ao tamanho do objeto através do dunder_method __len__;

            - item in obj: torna possível a verificação se aquele item está dentro do objeto através do dunder_method __contains__;

            - for i in obj: torna o objeto iterável através do dunder_method __iter__;

            - obj[2:3]: Consegue realizar o slice interno o objeto, ou seja se é o caso de um objeto semelhante à uma PlayList onde esse objeto é uma lista de objetos, é possível acessar somente os items internos desejados implementando o dunder_method __getitem__ (Fatiamento da lista de itens).

            Na verdade o __getitem__ ao ser implementado atribuí ao objeto as funcionalidades do __iter__ e __contains__ também, não sendo obrigatória a implementação desses;
                    

    Implementar o funcionamento de operações aritimeticas em objetos: __add__, __sub__, __mul__, __mod__;
        ex:
            Ao implementar os dunder_methods Númericos é possível programar como será o comportamento daquela quase em contato com operadores, é possivel ditar como será o comportamente de uma operação que levará o operador + | - | * e etc...

            - obj + obj: Por padrão ao realizar uma soma de objetos ele não retornará nada, porém, ao implementar o dunder_method __add__ é possível ditar como uma operação de soma entre objetos irá se comportar, podendo ser implementado de forma á se comportar como um append de uma lista (obj_1.append(obj_2));
            
    Duck typing pode ser implementado parcialmente, não é necessário implementar o protocolo completo; 



