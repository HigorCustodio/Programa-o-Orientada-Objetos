# beecrowd | 1018
# Cédulas
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

# Saída
# Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
class CedulasMoedas:
    def __init__(self, valor):
        self.__valor = valor
        
    def nota_100(self, valor):
        if valor >= 100:
            notas_100 = valor // 100
            resto = valor % 100
            resto_100 = format(resto,'.2f')
            return notas_100, resto_100
        else:
            return False
    
    def notas(self, resto:int, valor_nota:int):
        resto = float(resto)
        valor_nota = float(valor_nota)
        
        if resto >= valor_nota:
            notas_nota = resto // valor_nota
            resto_nota = resto % valor_nota
            
            return notas_nota,resto_nota
        else:
            notas_nota = 0
            return notas_nota,resto
        
    def moedas(self, resto:int, valor_moedas:int):
        resto = float(resto)
        valor_moedas = float(valor_moedas)
        
        if resto >= valor_moedas:
            notas_moedas = resto // valor_moedas
            resto_moedas = resto % valor_moedas

            return notas_moedas,resto_moedas
        else:
            notas_moedas = 0
            return notas_moedas,resto
     
    def numero_notas(self, notas:int, valor_nota:str):
        return print('{} nota(s) de R$ {}.00'.format(int(notas), valor_nota))    
    
    def numero_moedas(self, moedas:int, valor_moedas:str):
        return print('{} moeda(s) de R$ {:.2f}'.format(int(moedas), valor_moedas))    
        
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
cedulas_moedas = CedulasMoedas(valor = 0)
valor_total =  float(input())

if 0 <= valor_total <= 1000000:
    print('NOTAS:')
    
    cedulas_moedas.valor = float(valor_total)
    print('{:.2f}'.format(cedulas_moedas.valor))

    cedulas_valor = cedulas_moedas.valor

    if cedulas_valor >= 100:
        notas_100, resto_100 = cedulas_moedas.nota_100(valor = cedulas_valor)
        cedulas_moedas.numero_notas(notas=notas_100, valor_nota=100)
    else:
        cedulas_moedas.numero_notas(notas=0, valor_nota=100)
        resto_100 = cedulas_valor

    lista_notas = [50, 20, 10, 5, 2 ]
    
    for i in lista_notas:  
        if i == 50:

            valor_resto = resto_100
            
            nota,resto = cedulas_moedas.notas(resto= valor_resto, valor_nota= i)
            cedulas_moedas.numero_notas(notas= nota, valor_nota = i)  
            valor_resto = resto

        else:
            nota,resto_divisão_i = cedulas_moedas.notas(resto= valor_resto, valor_nota= i)
            cedulas_moedas.numero_notas(notas= nota, valor_nota = i)   

            valor_resto = resto_divisão_i
        

    lista_moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    print('MOEDAS:')
    for i in lista_moedas:  
        if i <= 1:
            moedas,resto_divisão_i = cedulas_moedas.moedas(resto= valor_resto, valor_moedas= i)
            cedulas_moedas.numero_moedas(moedas= moedas, valor_moedas = i)   

            valor_resto = resto_divisão_i
        
  
    

