class Filmes:
    def __init__ (self, nome, ano, duracao):
        self.__nome = nome
        self.__ano = ano
        self.__duracao = duracao
        self.__likes = 0
    
    @property
    def nome(self):
        return self.__nome.title()
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def duracao(self):
        return self.__duracao
    
    @property
    def likes(self):
        return self.__likes
    
    def dar_likes(self):
        self.__likes += 1
        
class Serie:
    def __init__ (self, nome, ano, temporadas):
        self.__nome = nome
        self.__ano = ano
        self.__temporadas = temporadas
        self.__likes = 0
    
    @property
    def nome(self):
        return self.__nome.title()
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def temporadas(self):
        return self.__temporadas
    
    @property
    def likes(self):
        return self.__likes
    
    def dar_likes(self):
        self.__likes += 1
        
vingadores = Filmes('vingadores', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

vingadores.dar_likes() 
atlanta.dar_likes()

print(f'Nome: {vingadores.nome}\n'
      f'Ano: {vingadores.ano}\n'
      f'Duração: {vingadores.duracao}\n'
      f'Likes: {vingadores.likes}\n')


print(f'Nome: {atlanta.nome}\n'
      f'Ano: {atlanta.ano}\n'
      f'Temporadas: {atlanta.temporadas}\n'
      f'Likes: {atlanta.likes}')