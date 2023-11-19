class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self._numero = numero 
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    def extrato(self):
        print("Saldo de {} do titular{}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    ''' 
        Método privado, quando colocamos o underline na frente do método significa que o mesmo é privado e 
        não deve ser utilizado fora de funções internas do objeto.
    '''
    def _pode_sacar(self, valor_a_sacar):
        valor_disponivel_sacar = self.limite + self._saldo
        return valor_a_sacar <= valor_disponivel_sacar
    
    def saca(self, valor): 
        if self._pode_sacar(valor_a_sacar=valor):
            self._saldo -= valor
        else:
            print('Valor de saque solicitado maior que o limite disponivel')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def titular(self):
        return self._titular  

    '''Já vimos que podemos criar getters e setters para acessar e alterar o valor de atributos privados. No python existe uma forma mais comum de criar estes getters e setters, diferente de Java, onde se coloca get ou set como prefixo de um método, usamos Propriedades.'''

    ''' Através do @property conseguimos chamar o método get_limite, sem precisar chamar o metodo fora da classe, consigo chama-lo apenas acessando o nome do atributo
    ex: conta1.limite e ele irá fazer o get do limite e retornar a metodo limite, para isso é necessario retirar o get do nome do metodo e atribuir ao atributo como privado'''
    @property
    def limite(self):
        return self._limite


    '''Existindo o @property, podemos tambem usar a mesma logica para aplicar o metodo set e chamar direto da classe.atributo atribuindo o novo valor como se fosse uma variavel
    ex: conta1.limite = valor, ele irá alterar o valor do limite utilizando o metodo limite(), porem, sem ser preciso chamar o metodo fora da classe'''
    @limite.setter
    def limite(self, limite):
        self._limite = limite
        
    ''' Quando precisamos acessar um método fora da classe onde não é necessario instanciar um objeto, onde só é preciso um valor expecifico fora da classe
    podemos usar os MÉTODOS DAS CLASSES OU MÉTODOS ESTÁTICOS, que consistem em um método da propria classe e não do objeto, utilizamos o decorator @staticamethod para declarar
    que se trata de um método da classe e sua chamada é feita de forma simples: nomeClass.metodo_estatico()'''
    
    #!'''Nosso foco está nos métodos estáticos que são da classe, e mesmo sem o objeto, conseguimos executar o método. Em algumas situações isso pode ser útil.                             Porém, precisamos ser cautelosos com o uso dos métodos estáticos.                                                                                                                            A ideia do mundo OO é criar objetos.Se usarmos apenas a classe Conta, sem ter um objeto, deixaremos de trabalhar com Orientação a Objeto.                                                Quando todos os objetos compartilham algo em comum, faz sentido usar esses métodos — como no exemplo em que compartilhamos todos os códigos do banco.                                       Mas se utilizarmos apenas métodos estáticos, não utilizaremos mais objetos e nos aproximaremos do mundo procedural.'''
    
    @staticmethod
    def codigo_bancos():
        return{'BB':'001', 'CAIXA': '104', 'BRADESCO': '237'}    

#EX:
#Instanciando a classe através da função construtora:
conta1 = Conta(123, "Nico", 100, 1000.00)

#Chamando antigo método get_limite() diretamente a propriedade @property:
conta1.limite
print(conta1.limite)  

#Alterando valor do limite no que anteriormente seria o método set_limite() através da propriedade usando o @limite.setter:  
conta1.limite = 2000.00
print(conta1.limite)    
print(conta1.saldo) 
print(conta1.titular)    

conta1.saca(valor=3000)
print(conta1.saldo) 

#ex usar @staticmethod :
cod_bancos = Conta.codigo_bancos()
print(cod_bancos['BB'])
print(cod_bancos['CAIXA'])
print(cod_bancos['BRADESCO'])