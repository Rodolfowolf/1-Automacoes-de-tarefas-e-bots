# bibliotecas = pacotes de codigos prontos que a gente pode usar
# Passo a passo do seu programa com python e pyautogui

from ast import While

import pyautogui  
import os
print(os.getcwd) 

import time
import pandas
import pyautogui

# Configura uma pequena pausa de 0.5 segundos entre os comandos do pyautogui
# Isso evita que o Python atropele o sistema operacional
pyautogui.PAUSE = 0.7

print("Iniciando monitoramento... Pressione Ctrl + C para encerrar.")

while True:
    tabela = pandas.read_csv("CadastroID.csv") 
    print("\n--- Nova Leitura da Tabela ---")
    
    houve_alteracao = False
    
    for index, linha in tabela.iterrows():
        codigo = linha["ID"]
        status = linha["STATUS"]
        
        if status != "ok":
        #    print(f"Código {codigo}: Status está OK!")
        #else:
            #print(f"Código {codigo}: Status NÃO está ok. Iniciando automação...")
            
            # 1. Dá um clique duplo na coordenada para focar/selecionar o campo
            pyautogui.doubleClick(x=1140, y=220)
            
            # 2. Seleciona todo o texto existente no campo (Ctrl + A)
            pyautogui.hotkey('command', 'a')

            # 3. Escreve o ID correspondente da planilha
            # Convertemos para string (texto) para garantir que o pyautogui consiga digitar
            pyautogui.write(str(codigo))
            
            # 4. Pressiona Enter para confirmar a ação na sua tela/sistema
            pyautogui.press("enter")
            
            pyautogui.click(x=595, y=925)
            pyautogui.click(x=595, y=925)
            # 5. Atualiza o status para "ok" na memória
            tabela.at[index, "STATUS"] = "ok"
            houve_alteracao = True
            print(f"-> Automação executada para o ID {codigo}.")
            
    if houve_alteracao:
        tabela.to_csv("CadastroID.csv", index=False)
        print("Planilha salva com os status atualizados!")
            
    time.sleep(5)





































"""
# Passo 0: abrir o navegador e entrar no site da empresa
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

for linha in tabela.index:
# Passo 4: cadastrar 1 produto
    pyautogui.click(x=1140, y=220 ) 
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
 """
# Passo 5: repetir o passo 4 ate acaber a lista de produtos.  