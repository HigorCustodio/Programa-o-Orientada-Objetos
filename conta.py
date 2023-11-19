
#Classe
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
        
#instancias do objeto
conta1 = Conta(123, "Nico", 55.5, 1000.00)
conta2 = Conta(124, "Higor", 100000000, 15000000)
conta3 = Conta(125, "Joao", 150, 1000.00)
conta4 = Conta(126, "jose", 350, 1000.00)

#Chamando um método de uma classe
conta1.extrato()
conta2.extrato()

conta1.deposita(100)
conta2.deposita(10)

conta1.saca(100)
conta2.saca(10000000)

