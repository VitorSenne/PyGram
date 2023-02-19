import PySimpleGUI as sg


def Interface():
    sg.theme('Reddit')
    # Layout
    layout = [
        [sg.Text('Usuario'), sg.Input(key='user')],
        [sg.Text('Senha'), sg.Input(key='password', password_char='•')],
        [sg.Text('Hashtag'), sg.Input(key='hashtag')],
        [sg.Button('Enviar')],
    ]
    # Janela
    janela = sg.Window('Robo Instagram').layout(layout)

    # Extracao dos valores inputados pelo usuário
 
    valores = janela.Read()

    user_inputs = {
        "valores" : valores['user'],
        "password": valores['password'],
        "hashtag": valores['hashtag'],
    }

    return user_inputs
