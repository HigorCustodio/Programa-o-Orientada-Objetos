Ao se utilizar a herança de uma classe é preciso levar em consideração a complexidade que essa classe irá trazer para a nossa aplicação:

Tinhamos feito a herança  de list na nossa classe Playlist, e com isso podemos dizer que Playlist é um list, e que o objeto Playlist absorve
todas as suas funcionalidades.

No entanto, list é uma classe conhecida como built-in, embutida no Python e pronta para o uso. E tivemos o benefício de reaproveitarmos vários códigos desta classe,
mesmo não conhecendo todas as suas funcionalidades e extensões. 

* Precisamos tomar cuidado ao fazermos esse tipo de herança!

No código, em relação a Playlist, utilizamos o __init__() para fazermos a chamada usando "nome" e "programas". Sendo assim, trata-se de um inicializador diferente de um inicializador de um
list.

Quando alguém for criar um objeto  de Playlist, terá de utilizar este inicializador, o que será um tanto confuso, pois por ser um list, deveria receber apenas a listagem dos items, ou de repente
um item, para começar uma lista, a qual possui um protocolo, uma interface diferente.
Um ponto positivo é que estamos criando uma playlist mas não nos limitaremos a um list só - a playlist tem mais significado para o nosso sistema, talvez possamos fazer uma busca por nome, uma filtragem para encontrar elementos que façam parte de uma categoria, como "série", por exemplo.

Estamos começando a perceber as particularidades de list e Playlist, e já notamos que é um tanto complexo utilizarmos um tipo built-in, uma classe que já está pronta no sistema, porque não sabemos as exceções que ela possui.

Por exemplo, list pode conter um método que permita o acesso a algum de seus itens, e ele pode ser protegido, por algum motivo. Muito em Python é implementado em CPython, então, pode ser que haja alguma função de list que seja protegida e não permita a sobrescrita. Mas para descobrirmos isto, teríamos que ler toda a documentação do list, e talvez isso nem nos ajude em nada no fim das contas.

No crescimento da nossa classe, teremos que nos preocupar com esses detalhes o tempo todo: será que esta função que vamos criar já existe em list? Será que estamos sobrescrevendo uma função preexistente, resultando em erro? Ou impedindo meu objeto de ter um len(), ou até de ser iterável?

Anteriormente tínhamos um design, uma visão muito mais simples e clara do que queríamos por meio de Playlist - que fosse menos complexo, contendo nome, programas e um tamanho. Vimos que list seria interno, possível de ser percorrido por algo, isto é, seria iterável.

Por algum tempo focamos nisso, mas acabamos criando complexidades ao optarmos pela herança. Também ficamos nos perguntando se valia a pena termos acesso a tudo que vem de list. Nesta situação, o ideal seria conseguirmos fazer algo parcialmente, aproveitando o melhor dos mundos, que seria Playlist não ser do tipo list e, de alguma maneira, ter vantagens que ele tem.

Para evitarmos as complexidades adquiridas da herança de list, olharemos no nosso código para entendermos o que pode ser feito. Se estamos herdando algo que é mais complexo do que esperávamos, com uma interface gigantesca, e que talvez não esteja preparado para fazer com que a nossa Playlist se adapte a ela, vamos desfazer a herança.

Precisamos ter controle do que estamos fazendo nas nossas classes, o que implica em uma boa prática de programação, ainda mais em se tratando de Orientação a Objetos.

Na classe Playlist, então, faremos algumas modificações, deletaremos o super(), voltando à necessidade de termos uma lista de programas, os quais não queremos que sejam acessíveis. Para isso, podemos incluir o _ (underscore) antes de programas:

```python
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
```

O underline acaba servindo de aviso também, pois é algo de que a pessoa externa não poderá depender. E também indica que podemos alterar programas a qualquer momento. Quando estávamos herdando de list, imagine que em vez de um list ordenado de programas, quiséssemos passar como parâmetro um dicionário, ou um set, qualquer outra estrutura do Python - como faríamos?

Com a herança, estávamos muito presos ao list e, no caso de mudanças, teríamos problemas ainda maiores, pois tudo que usasse a classe Playlist seria alterado também. Já que retiramos a herança e resolvemos incluir um programas que não tem livre acesso, teremos que criar alguma censura, como uma property, que chamará a definição de listagem.

Esta função retornará os programas, que ficarão protegidos, e representará a nossa listagem. Com ela, conseguimos exibir dados, e tudo o mais. Falta demonstrarmos o tamanho da listagem criando outra property, o que garante que agimos de acordo com as boas práticas, para representar o tamanho (exatamente o len() de programas da listagem), já que sabemos que, por enquanto e internamente, ela é um list:
```python
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)
```
No caso de usarmos um dicionário, mesmo com o len() funcionando neste caso, não importa ao usuário (externo), ao cliente daquela classe, como a nossa listagem de programas está sendo implementada internamente. A partir de agora temos a flexibilidade de fazermos alterações, caso desejemos.

Em list, até poderíamos sobrescrever os métodos, mas isto seria confuso, pois criaríamos um list com comportamentos estranhos.

Conseguimos resolver a questão da complexidade, porém nos deparamos com outro problema: quebramos a parte inferior do código, e não conseguimos mais fazer a execução em cima de playlist_fim_de_semana, sendo necessário chamar listagem após o .:
```python
print(f'Tamanho do playlist: {len(playlist_fim_de_semana.listagem)}')

for programa in playlist_fim_de_semana.listagem:
    print(programa)

```
O len() que colocamos mais acima também deixa de existir, assim como o in. É melhor ou pior dessa forma?

Se executarmos o código acima, ele funcionará, mas vocês viram que o código está bem esquisito? É porque ainda não estamos usando a parte legal do Python, de que falaremos muito em breve!