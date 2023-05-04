import pyautogui as py
import pyperclip 
import time

py.PAUSE = 0.2

time.sleep(5)

i = 1
lojas = 480
while i < lojas:

    #Clica em Executar
    py.moveTo(x=98, y=548)
    py.click()
    #Clica em Fechar Auditoria
    py.moveTo(x=633, y=553)
    py.click()
    #Clica em Sim
    py.press("Enter")
    #Clica em Ok
    py.press("Enter")
    #Fechar Janela
    py.moveTo(x=753,y=99)
    py.click()
    #Descer uma loja
    py.press("Down")

    
    i += 1