# from collections.abc import MutableSequence


# class Playlist(MutableSequence):
#     pass

# play_list = Playlist()

# from numbers import Complex

# class Numero(Complex):
#     def __getitem__(self, item):
#         super().__getitem__()
        
# numero = Numero()
#* Exemplo de implementação correta de uma Abstract Base Classe:
# Utilizando uma ideia de atribuir um tamanho a uma subclasse.

from collections.abc import Sized


class Tarefa:
    def __init__(self, tarefa) -> None:
        self.tarefa = tarefa
    
    def __str__(self):
        return f'{self.tarefa}'
    

class MinhaListagem(Sized):
    def __init__(self, descricao, listagem):
        self.descricao = descricao
        self.listagem = listagem

    def __str__(self):
        return f'\n {self._tarefas()}'

    def __len__(self):
        return self.listagem
    
    def _tarefas(self):
        lista_descrições = []
        print(f'{self.descricao}: \n') 
        for tarefa in self.listagem:
            print(f'-  {tarefa}')
        return 'Fim da lista'
            
        
        
        
limpar_casa = Tarefa(tarefa='Limpar a Casa')
limpar_carro = Tarefa(tarefa='Limpar o Carro')
estudar = Tarefa(tarefa='Estudar python')

lista_tarefas = [limpar_casa,limpar_carro,estudar]

lista = MinhaListagem(descricao='Tarefas a realizar', listagem=lista_tarefas)

print(lista)
