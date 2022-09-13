#Projeto 05 - Decidr por mim
#Faça uma pergunta para o programa e ele dara uma resposta!!

import random
import PySimpleGUI as sg

class DecidaPorMim:
    
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe',
            'Não sei ainda, mas melhor Não fazer isso Não',
            'Acho que é o momento certo'
        ]

    def Iniciar(self):

        #layout
        layout =[
            [sg.Text('Faça uma Pergunta:')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Decida Por Mim')]
        
         ]
        # Criar uma janela
        self.janela = sg.Window('Decida Por Mim', layout = layout)

        while True:
            #Ler os valores
            self.eventos, self.valores = self.janela.Read()

            #Fazer algo com o valores
            if self.eventos == 'Decida Por Mim':
                print(random.choice(self.respostas))

decida = DecidaPorMim()
decida.Iniciar()
