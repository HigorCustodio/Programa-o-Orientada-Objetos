Herança Multipla:

Para exemplificar a implementação de uma herança multipla, podemos utilizar como base um cenário onde temos a classe Funcionário e as classe Alura e Caelum, que representam os funcionários de cada empresa;

Iremos considerar que dentro da empresa existem 3 níveis de funcionários: Júnior, Pleno e Senior. O funcionário Júnior terá acesso somente as funcionalidades da empresa Alura, já os funcionários Pleno e Senior, como recebem maior responsabilidade receberão as caracteristicas das duas empreseas (Alura e Caelum);

Sendo assim o Funcionário Júnior receberá uma herança única, enquanto os funcionários das classes Pleno e Senior receberão heranças multiplas das classes Mães Alura e Caelum;

Dentro da classe Funcionario temos os métodos registra_horas() e mostrar_tarefas(), métodos que basicamente irão realizar a impressão das horas trabalhadas e das tarefas executadas:
```python
class Funcionario:
    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')
```

As classes Caelum e Alura possuem formas diferentes de lidar com o método herdado mostrar_tarefas() onde cada uma sobreescreve a mensagem retornada do método para atender a suas necessidades específicas;

Temos também funcionalidades especificas de cada subclasse onde para Caelum temos busca_cursos_mes() que irá realizar a buscar dos cursos realizados através do mês passado como parâmetro do método;
```python
class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')
```

Já para a subclasse Alura temos o método específico busca_perguntas_sem_resposta(), que basicamente rotorna as perguntas não respondidas no fórum da Alura;
```python
class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')
```

### Implementação de herança multipla:
    - Basicamente a sintaxe da herança multipla é a mesma da herança normal, onde para realizar a herança de classes é preciso colocar entre parênteses o nome da classe que será herdada e caso tenha mais de uma classe herdada, separar as duas pelo separador ','(vígula):
    
```python
#Entrada:
class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

jose = Junior()
jose.busca_perguntas_sem_resposta()

luan = Pleno()
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()
#Saída:
>>>Mostrando perguntas não respondidas do fórum
>>>Mostrando perguntas não respondidas do fórum
>>>Mostrando cursos desse mês
>>>Fez muita coisa, Alurete!

```

# Problemas apresentados pela Herança multipla:
    Como podemos avaliar nas mensagens de respostas da execução das classes Júnior e Pleno, é esperado que a classe Júnior sobrescreva o método mostrar_tarefas() da classe Funcionário  pelo que é aplicano na classe Alura, porém, o que se pode esperar para a saída do mesmo método para o funcionário Pleno que recebe o método mostrar_tarefas() herdado tando da classe Alura quanto da classe Caelum??

    Isso pode gerar complexidade no código!

    Ao executarmos:
```python
    #Entrada:
    jose = Junior()
    jose.mostrar_tarefas()

    luan = Pleno()
    luan.mostrar_tarefas()

    #Saída:
    >>>Fez muita coisa, Alurete!
    >>>Fez muita coisa, Alurete!
```
    
    - Como observado o método está sendo implementado para os dois tipos e, em algum momento o programa tem que decidir qual delas utilizar.
    Porque a escolha foi sempre referênte a Alura?
    Quando definimos Pleno(), não designamos qual classe será considerada primeiro, se Alura ou Caelum. A ordem normalmente segue da esquerda para a direita, como em um leitura
    usual. Assim, a primeira opção é Alura.

# Algoritímo de busca MRO (Method Resolution Order):
    Para a tomada de decisão sobre qual método deverá ser executado quando temos diversas superclasses que o possuem, internamente, a versão 3 do Python usa um algoritmo chamado MRO (Method Resolution Order), com um funcionamento que começa a busca pela classe atual, que é a própria classe.

    Por exemplo, em Pleno, a primeira classe que será buscada neste caso é o próprio Pleno. Em seguida, o acesso será em sua classe mãe. No caso, ela possui duas mães, Alura e Caelum, e é aí que ocorre a primeira distinção - a primeira classe mãe é Alura, portanto ela será consultada primeiro.

    Além disto, o cálculo do algoritmo acessará não apenas esta classe, mas todas as classes mães de Alura, e assim por diante, hierarquicamente:

    Ordem de busca de método segundo MRO:   classe atual > classe herdada > classe anscestral > segunda classe herdada > classe ancestral;
    Ou seja, para o exemplo usado acima a ordem seria: Pleno > Alura > Funcionário > Caelum > Funcionário;

    Assim, é feita a verificação de qual método será chamado. Antes de executarmos o código novamente para confirmar se é isso mesmo, modificaremos a classe Alura comentando o trecho com o método mostrar_tarefas(), para vermos de onde será feita a chamada:

```python
    class Alura(Funcionario):
    # def mostrar_tarefas(self):
        # print('Fez muita coisa, Alurete!')
```

    Receberemos "Fez muita coisa..." e, mais abaixo, "Fez muita coisa, Caelumer". A Alura não tem mais a implementação de "Fez muita coisa...", e como executamos para Junior e para Pleno, o primeiro chama "Fez muita coisa..." , que vem de Alura (que não possui implementação), portanto seu ancestral foi acessado, Funcionario.

    -No caso de Pleno, deveria ser feito o mesmo, ou seja, começado por Alura, que não tem implementação, passando para Funcionario. No entanto, ele passou para Caelum. Por que isto aconteceu?
        Há duas etapas para a verificação do algoritmo MRO, que exige uma noção de que há uma repetição nesta lista, como no caso de Funcionario. Esta repetição precisa ser removida para que seja possível encontrar o local de onde acessaremos o método que está sendo implementado.

    No nosso caso, em vez de Funcionario, Caelum é que foi acessado, pois a parte da remoção da duplicidade verifica se Funcionario é "uma boa cabeça" (good head). Caso positivo, quer dizer que poderemos mantê-la. Como o primeiro Funcionario não é uma good head, iremos removê-la:

    Nova Ordem MRO: Pleno > Alura > Caelum > Funcionario

    "Boa cabeça" indica que não há nenhuma outra classe que seja da mesma hierarquia, ou seja, que esteja abaixo de Funcionario (neste caso), e que possa ser utilizada. Já que Caelum também herda de Funcionario, podemos utilizá-la no lugar desta.

    Para entendermos melhor, vamos voltar ao código, na parte em que definimos Pleno, cuja hierarquia é Alura, seguida de Caelum. Sendo assim, não é muito intuitivo seguir de Alura para Funcionario, e é por isto que se vai para Caelum, de hierarquia mais específica.

    Para tornar isso mais explícito, no Python 3, quando a duplicata é removida, é feita uma verificação da existência de alguma outra classe que herde desta. Por exemplo, será que tem alguma classe que herde de Funcionario na lista? Tem, Caelum. Assim, ela é removida, pois este não é seu lugar, já que existe uma classe em que ela pode caber melhor.

    Caelum seria um good head. É por isto que houve aquela confusão, sobre termos recebido "Fez muita coisa, Caelumer!" quando deveria ser a mensagem referente a Alura. 

    Poderia acontecer de termos classes em que não conseguimos resolver a busca do método. A herança múltipla, e a forma como lidaremos com ela aqui será mais focada para o uso, para quando trabalhamos com uma classe que pode ser provida como herança, mas não criaremos muitas classes, pois normalmente estes recursos um pouco mais avançados são utilizados na criação de frameworks, ou de um conceito de aplicação a ser utilizada por muitas pessoas.

    Neste caso, estamos simplesmente fazendo uso da herança múltipla - temos várias classes e queremos usá-las como herança, e então tomaremos cuidados adequados e aplicaremos boas práticas.

    Neste exemplo visto aqui já temos uma solução que funciona: precisaremos saber como este cálculo de MRO funciona. 

#    Quando é mais vantajoso utilizar a herança múltipla?

    A ideia é juntarmos comportamentos distintos, e que fazem sentido para uma classe única. Porém, há outros casos - Caelum e Alura fazem parte da mesma hierarquia, mas e se quiséssemos dizer que temos mais informações sobre Funcionarios, como Desenvolvedor ou UX, por exemplo? 
    - De que forma trabalharíamos com isso?

# MIXINS:
    Mixins são classes menores, que tem um comportamento especifíco, onde esse comportamento não é o mais importante para a aplicação. Elas são bastante utilizadas em Python no caso de precisarmos compartilhar algum comportamento que não é o mais importante desta classe.
    Mixins São classe que não são instânciadas em novos objetos, mas, são herdadas por outras classe.
    Exemplo:
```python
    class Hipster:
        def __str__(self) -> str:
            return f'Hipster, {self.nome}'
```
    - Como podemos ver essa classe Hipster tem a função somente de retornar um comportamento específico, nesse caso, de retornar uma mensagem, sendo assim, seu comportamento não tem grande impacto no funcionamento de uma aplicação, além de exibir uma mensagem.

    Se quiséssemos, poderíamos implementar um log() para que toda vez que alguém for chamar registra_horas(), o log() do sistema seja feito em algum arquivo, e fosse feita uma auditoria. Para tal, criaríamos uma classe que faria um Logger, que disponibilizaria o log() para a nossa classe.

    Desta forma, não precisaremos implementar o log() para cada classe que temos. Se tivéssemos que colocá-lo em Funcionario, por exemplo, não poderíamos reutilizar este código - do log() - em outras classes que precisassem deste comportamento também.
    
    Neste caso, pode ser interessante utilizarmos este tipo de herança. Mas lembre-se de que o mixin envolve a ideia de não termos que instanciar um objeto desta classe. Em Hipster, isto nem funcionaria direito, porque ela está dependendo de um nome para que o nome, ou o texto deste objeto, seja alterado.
    
    Assim, fechamos um pouco o assunto de classes com herança múltipla, e seus usos.