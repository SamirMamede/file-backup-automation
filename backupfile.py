# DESAFIO:
#   AUTOMATIZAR BACKUP DE ARQUIVOS DO SISTEMA

# DEFININDO PASSOS:
#   ABRIR O GOOGLE DRIVE NO MEU COMPUTADOR
#       ENTRAR NO LOCAL ONDE ESTÁ O ARQUIVO
#           CLICAR NO ARQUIVO E ARRASTAR PARA DENTRO DO GOOGLE DRIVE
#               ENQUANTO ESTIVER ARRASTANDO MUDAR PARA O GOOGLE DRIVE
#                   LARGAR O ARQUIVO NO GOOGLE DRIVE
#                       ESPERAR 5 SEGUNDOS

# RESULTADO ESPERADO:
#   BACKUP NO GOOGLE DRIVE CONLUÍDO

import pyautogui, pymsgbox, time

pymsgbox.alert(text='O código vai começar, clique em ok e não mexa mais no mouse e teclado !!')
pyautogui.PAUSE = 0.5

pyautogui.press('winleft')
pyautogui.write('Crome')
pyautogui.press('enter')
pyautogui.write('drive.google.com/drive/my-drive')
pyautogui.press('enter')
pyautogui.hotkey('winleft', 'up')
pyautogui.hotkey('winleft', 'd')
pyautogui.moveTo(1851, 42)                              #print(pyautogui.position())
pyautogui.mouseDown()
pyautogui.moveTo(859, 797)                              #print(pyautogui.position())
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.mouseUp()
time.sleep(3)

pymsgbox.alert(text='O código acabou de rodar. =) Pode usar o computador normalmente agora !!')