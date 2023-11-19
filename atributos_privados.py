''' Para deixar um atributo privado é utilizado de um convensão entre a comunidade python, onde para dizer que aquele atributo
não deverá ser usado fora dos métodos da classe'''

#? Sintaxe
# É adicionado 2 underlines na frente do atributo :

atributo = 'atributo global'
__atributo = 'atributo privado da classe'


'''Desta forma o acesso ao atributo ainda é possivel de fora da classe, porém, na hora de chamar o atributo ele irá ser formatado pelo python de forma diferente,
indicando que o acesso deste atributo não sendo pelos proprios métodos da classe é um ato errado.
ex: 'referencia._classe__atributo'  '''

class atributosPrivados:
    def __init__(self, atributo:str):
        self.__atributo = atributo
        

atributos_privados = atributosPrivados(atributo='privado')

print(atributos_privados._atributosPrivados__atributo)
#saída: >>> privado


class Retangulo:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__area = x * y

    def obter_area(self):
        return self.__area
    
r = Retangulo(7,6)
r.area = 7
print(r.obter_area())

#saída: >>> 42

'''A classe Retangulo está correta e define os atributos __x, __y e __area, além do construtor e o método obter_area(). Nada impede então criar um objeto:

r = Retangulo(7,6)

Agora, se você tenta acessar um atributo area, que na verdade não declaramos, o Python cria automaticamente um novo atributo e inicializa com o valor 7:

r.area = 7

Na linha em cima o objeto ganha um novo atributo com o nome area. Ou seja, temos um atributo __area E um novo com o nome area. 

No entanto, ao chamar r.obter_area(), continuamos acessar o atributo __area que foi inicializado com o produto de 7*6!
'''