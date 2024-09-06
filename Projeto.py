from tkinter import Event
import PySimpleGUI as sg

#criando o layout
def Criar_janela_inicial():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''),sg.Input('')]
    ]
    layout = [
        [sg.Frame('Treino',layout=linha,key='container')],
        [sg.Button('Novo Exercicio'),sg.Button('Limpar')]
    ]
    
    return sg.Window('Treino Express', layout=layout, finalize=True)

#criar a janela

janela = Criar_janela_inicial()

#criar as regras dessa janela

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Novo Exercicio':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])
    elif event =='Limpar':
        janela.close()
        janela = Criar_janela_inicial()