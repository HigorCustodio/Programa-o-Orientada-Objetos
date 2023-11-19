# beecrowd | 1020
#* Idade em Dias
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

# Entrada
# O arquivo de entrada contém um valor inteiro.

# Saída
# Imprima a saída conforme exemplo fornecido.

class Idade:
    def __init__(self, dias):
        self.__dias = dias
    
    @property
    def dias(self):
        return self.__dias
    
    @dias.setter
    def dias(self, dias):
        self.__dias = dias
    
    def transforma_ano(self):
        ano = self.__dias // 365
        restante_ano = self.__dias % 365
        
        return ano, restante_ano
        
    def transforma_mes(self):
        mes = self.__dias // 30
        restante_mes = self.__dias % 30
        return mes, restante_mes
    
    def anos(self):
        ano, restante_dias = self.__transforma_ano()
        return ano, restante_dias
    
    def meses(self):
        mes, restante_dias = self.__transforma_mes()
        
        return mes, restante_dias
    
    def dia_mes_ano(self):
        
        if self.__dias >= 365:
            ano, resto_ano = self.__anos()
            print(f'{ano} anos(s)')
            
            return ano, resto_ano
        
        elif resto_ano >= 30:
            mes, resto_mes = self.__meses()
            print(f'{mes} mes(es)')
            
            return mes, resto_mes
        
        else:
            dia = resto_mes
            print(f'{dia} dia(s)')
            
            return dia

idade_dias = int(input())

idade = Idade(dias = idade_dias)

def descobrir_anos(dias:int = idade_dias):
    try:
        if dias >= 365:
            ano, resto_ano = idade.transforma_ano()
            print(f'{ano} ano(s)')

        idade.dias = resto_ano      
    except:
        resto_ano = idade.dias
        ano = 0
        print(f'{ano} ano(s)')    
    
    return resto_ano

def descobrir_mes(resto_ano:int):
    try:
        if resto_ano >= 30:
            mes, resto_mes = idade.transforma_mes()
            print(f'{mes} mes(es)')
      
        idade.dias = resto_mes
        
    except:
        resto_mes = idade.dias
        meses = 0
        print(f'{meses} mes(es)')
    
    return resto_mes

def descobrir_dia(resto_mes:int):
    
    if resto_mes > 0:
        dia = resto_mes
        print(f'{dia} dia(s)')

        repetir = False
    else:
        dia = 0
        print(f'{dia} dia(s)')
        
        repetir = False
    
    return repetir
         
repetir = True

while repetir:
    resto_ano = descobrir_anos()
    resto_mes = descobrir_mes(resto_ano = resto_ano)
    repetir = descobrir_dia(resto_mes = resto_mes)

    
    
    