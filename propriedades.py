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

    def saca(self, valor): 
        self.__saldo -= valor

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
    @limite.setterw
    
    def limite(self, limite):
        self._limite = limite

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