class Conta:
    #função construtora:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    #Métodos:
    def extrato(self):
        print(f'Saldo {self.saldo} do títular {self.titular}')
    
    def deposita(self, valor):
        self.saldo += valor
        print(self.saldo)
    
    def saca(self, valor):
        self.saldo -= valor
        print(self.saldo)
        
    
    # #encapsulando para um método sem refatorar:
    # def transferir(self, valor, origem, destino):
    #     origem.saca(valor)
    #     destino.deposita(valor)  
    
    #usando o self para chamar função deixando o método mais legivel:
    def transferir(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
            #   
#instancias do objeto
conta1 = Conta(123, "Nico", 100, 1000.00)
conta2 = Conta(124, "Higor", 100, 15000000)

#transferir:
conta2.saca(10)
conta1.deposita(10)
#saída:90
#saída:110

#chamando encapsulamento sem refatorar:
conta2.transferir(10, conta2, conta1)
#saída:90
#saída:110

#Chamando método de encapsulamento refatorado usando self:
conta2.transferir(valor=10, destinho=conta1)
#saída: 90
#saída: 110
