# bibliotecas = pacotes de codigos prontos que a gente pode usar
# Passo a passo do seu programa com python e pyautogui

import pyautogui  
import time
import os
print(os.getcwd) 

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo 1: entrar no sistema da empresa
#pyautogui.press("win")
pyautogui.hotkey("Command", "Space")
#pyautogui.write("safari")
os.system("open -a Safari ")
#pyautogui.write("safari")
pyautogui.press("enter")
# atalho pra barra de endereços

# entrar no link

#pyautogui.write ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.write(link) 
pyautogui.press("enter")
time.sleep(3) 

#pyautogui.hotkey("ctrl", "command", "f")  

# clicar no campo de email
pyautogui.click(x=494, y=392 ) 
pyautogui.write("email@empresa.com")
pyautogui.press("tab")
pyautogui.write("senha aqui")
#pyautogui.press("Tab")
pyautogui.press("enter")

# fazer uma pausa maior pro site carregar
time.sleep(4)

# Passo 2: fazer login 
# Passo 3: abrir a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv") 
print(tabela)  

for linha in tabela.index:
# Passo 4: cadastrar 1 produto
    pyautogui.click(x=535, y=256 ) 
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
 
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    tipo = str(tabela.loc[linha, "tipo"])    
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
 
    preco = str(tabela.loc[linha, "preco_unitario"]) 
    pyautogui.write(preco)
    pyautogui.press("tab")
    
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    obs = str(tabela.loc[linha, "obs"]) 
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("enter") 
    pyautogui.scroll(5000) # rolar a tela pra cima
 
# Passo 5: repetir o passo 4 ate acaber a lista de produtos.  