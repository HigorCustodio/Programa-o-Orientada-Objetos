# beecrowd | 1019
# Conversão de Tempo
# Adaptado por Neilor Tonin, URI  Brasil
# 
# Timelimit: 1
# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.
# 
# Entrada
# O arquivo de entrada contém um valor inteiro N.
# 
# Saída
# Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
class Tempo:
    def __init__(self, segundos):
        self.__segundos = segundos
    

    def segundos_para_minutos(self):
        minuto, segundo = divmod(self.__segundos, 60)
        hora, minuto = divmod(minuto, 60)
        return "%d:%d:%d" % (hora, minuto, segundo)
        # return str(datetime.timedelta(seconds= self.segundos)) com datetime faz o mesmo, porém, o resultado é apresentado de forma ligeiramente diferente o que não daria no beecrowd.

tempo_segundos = int(input())

conversor = Tempo(segundos = tempo_segundos)

tempo_convertido = conversor.segundos_para_minutos()

print(tempo_convertido)