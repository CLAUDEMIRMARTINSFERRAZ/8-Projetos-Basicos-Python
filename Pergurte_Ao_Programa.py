#Projeto 05 - Decidr por mim
#Faça uma pergunta para o programa e ele dara uma resposta!!

import random


class DecidaPorMim:
    
    def __init__(self):
        self.resposta = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe',
            'Não sei ainda, mas melhor Não fazer isso Não',
            'Acho que é o momento certo'
        ]

    def Iniciar(self):
        input('Faça sua Pergunta Agora:')
        print(random.choice(self.resposta))

decida = DecidaPorMim()
decida.Iniciar()
