
class Data:
    def __init__(self, d:int) -> None:
        self.d = d
    
    def formatada(self):
        d_formatada = self.d
        d_fim = d_formatada.replace(',','/')
        print(d_fim)
        
        
        

data = Data('21,11,2007')
data.formatada()