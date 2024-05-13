import pyautogui
import time
pyautogui.PAUSE = 0.5
    
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=-1422, y=356)
pyautogui.write("mesquitacamis3@gmail.com")
pyautogui.press("tab")  
pyautogui.write("12345")
pyautogui.press("tab") 
pyautogui.press("enter")
time.sleep (3)

import pandas as pd
tabela = pd.read_csv("produtos.csv")
print (tabela)

for linha in tabela.index:
    pyautogui.click(x=-1353, y=231)

    time.sleep(1)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
        
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":                                       
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000) 


