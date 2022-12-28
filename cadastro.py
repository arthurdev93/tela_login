from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('LightBlue')

# abaixo, 3 linhas [] e 2 colunas
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar login? ')],
    [sg.Button('Entrar')]
]

# Janela (o layout abaixo, é da variavel ali de cima chamada layout)
janela = sg.Window('Tela de Login', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'arthur' and valores['senha'] == '123456':
            print('Bem vindo ao sistema!')
