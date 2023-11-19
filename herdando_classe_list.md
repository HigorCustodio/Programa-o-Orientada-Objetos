Herdando a classe list em um objeto:
    Ao herdar a classe list para um objeto automaticamente ele se tornará iteravel, e herdará todas as funcionalidades de um list, ou seja, 
    a partir desse momento, um não iteravel se torna um iteravel, temos os ganhos das funcionalidades len(),  objeto in lista de objetos, e todas as funcionalidades
    existentes para a classe list;
    Como herdar a classe list?
        Sintaxe:
```python
        class MinhaClasse(list):
            def __init__(self, atributo, atributo_lista):
                self.atributo1 = atributo
                super().__init__(atributo_lista) -> Chamando o método inicializador da Super Classe, a classe que está herdando o objeto irá receber os atributos da classe herdada, 
                                                    ou seja, consigo manter os atributos originais da minha classe e ainda adicionar os atributos da classe herdada.

        lista_qualquer_coisa= [ 1,2,3,4]
        minha_classe = MinhaClasse(atributo='qualquercoisa', atributo_lista= lista_qualquer_coisa)
```
        ** Agora é possível realizar um for in usando a instância do objeto, pois ao herdar os atributos da classe list, automaticamente se torna iteravel;
        Ou seja, se realizar um print da instância do objeto minha_classe, será retornado :
   
    Sem Herdar o list:
``` python
    print(minha_classe)
    >>> <__main__.Playlist object at 0x000002139BF10310>
```
    Herdando o list
``` python
    print(minha_classe)
    >>>[1, 2, 3, 4]
```

    Usando o For in sem herdar a classe list:
``` python
    lista_qualquer_coisa= [ 1,2,3,4]
    minha_classe = MinhaClasse(atributo='qualquercoisa', atributo_lista= lista_qualquer_coisa)

    for classe in minha_classe:
        print(classe)
    
    saída:
    >>> Ocorreu uma exceção: TypeError
        'MinhaClasse' object is not iterable
          File "C:\Users\higor_custodio\Documents\Estudo\POO\POO_teorico_2\herdando_classe_list.py", line 89, in <module>
            for programa in playlist_fim_de_semana:
        TypeError: 'MinhaClasse' object is not iterable
```

    Usando o For in herdando a classe list:
```python
    
    playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

    for programa in playlist_fim_de_semana:
        print(programa) 
    
    saída:
    >>> vingadores - guerra infinita - 2018 - 160 temporadas - 1 Likes
        atlanta - 2018 - 2 temporadas - 3 Likes
        Demolidor - 2016 - 2 temporadas - 2 Likes
        Todo mundo em pânico - 1999 - 100 temporadas - 4 Likes
```
    Outras funcionalidades da classe list:
```python
    # Verificando se o objeto esta na lista de objetos:
    código:
        objeto in lista_objetos
    saída:
    >>>True|False

    # Verificando o tamanho da lista de objetos:
    código:
        len(lista_objetos)
    saída:
    >>> 5 (retorna um inteiro com o tamanho da lista)

```