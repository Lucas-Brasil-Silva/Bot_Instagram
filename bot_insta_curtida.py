import webbrowser
import pyautogui
from time import sleep
import keyboard

# Função que deslogar do Instagram:
def logout(imagem1,imagem2):
    pyautogui.press('esc')
    sleep(1)
    click_coord(imagem1)
    sleep(1)
    click_coord(imagem2)
    sleep(1)
    pyautogui.hotkey('ctrl', 'w')

# Função que usando biblioteca OpenCV encontra a localização de uma imagem desejada na tela e clicar: 
def click_coord(modelo):
    from PIL import ImageGrab
    import cv2
    import numpy as np

    imagem = np.array(ImageGrab.grab(all_screens=True))
    modelo = cv2.imread(modelo)

    resultado = cv2.matchTemplate(imagem, modelo, cv2.TM_CCOEFF_NORMED)
    coords = cv2.minMaxLoc(resultado)
    pyautogui.click(coords[3][0], coords[3][1], duration=1)

# Obtém informações do usuário:
email = pyautogui.prompt(text='Digite seu E-mail de login do Instagram:',title='Instagram')
senha = pyautogui.password(text='Digite sua senha de login do Instagram:',title='Instagram',mask='*')
pesquisar = pyautogui.prompt(text='Quem você gostaria de Curtir?',title='Pesquisar')
comentario = pyautogui.prompt(text='Qual seria seu comentario?',title='Comentario')

while keyboard.is_pressed('space') == False:
    # Abre um nova guia com o site Instagram :
    webbrowser.open('https://www.instagram.com/')
    sleep(7)
    # Encontrar os campos de e-mail e senha e digita os dados nos respectivos campos:
    click_coord('email.PNG')
    keyboard.write(email)
    sleep(1)
    pyautogui.press('tab')
    keyboard.write(senha)
    sleep(1)
    pyautogui.press('enter')
    # Encontra o campo pesquisar e realiza a pesquisar:
    sleep(7)
    click_coord('pesquisa.PNG')
    sleep(3)
    keyboard.write(pesquisar)
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press('enter')
    sleep(6)
    # Clicar sobre a ultima postagem :
    pyautogui.click(2180,721,clicks=1,duration=1,button='left')
    sleep(6)
    # Curtindo caso não tenha sido curtido, se já estiver curtido finaliza o processo:
    try:
        click_coord('naocurtido.PNG')
        sleep(1)
        pyautogui.press('tab')
        sleep(1)
        pyautogui.press('enter')
        sleep(0.5)
        keyboard.write(comentario)
        sleep(1)
        pyautogui.press('enter')
        pyautogui.alert(text='Postagem Curtida e Comentada com sucesso!.',title='Postagem Curtida e Comentada',timeout=5000)
        sleep(1)
        logout('mais.PNG','sair.PNG')
        # Aguarda 24h para fazer todo o processo novamente:
        sleep(86400)
    except:
        pyautogui.alert(text='A Postagem já foi Curtida.',title='Postagem Curtida',timeout=5000)
        sleep(1)
        logout('mais.PNG', 'sair.PNG')
        # Aguarda 24h para fazer todo o processo novamente:
        sleep(86400)