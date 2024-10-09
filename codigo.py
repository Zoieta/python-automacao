# passo 1 :  Entrat no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
#biblioteca pyautogui
#atalho de teclado pyautogui.hotkey(ctrol,c)
import pyautogui
import time
pyautogui.PAUSE = 0.5


#abrir o navegador
#apertar a tecla windows
pyautogui.press("win")

pyautogui.write("chrome")
pyautogui.press("enter")

# acessar o link https://dlp.hashtagtreinamentos.com/python/intensivao/login

# passo 2: Fazer login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# quero da uma pausa aqui.
time.sleep(3)   
pyautogui.click(x=622, y=423)
pyautogui.write("bella@gmail.com")
#passar para o proximo campo
pyautogui.press("tab")
pyautogui.write("2345678")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

# passo 3: Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")

# passo 4: cadastrar 1 produto
#para cada linha da minha tabela, faca:

for linha in tabela.index:
#texto = string = str()
#codigo
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.click(x=614, y=304)
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obsrvacao
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    #clicar no botao enviar
    pyautogui.press("enter")
    pyautogui.scroll(4000)

# Passo 5: repertir o processo de cadastramento dos produtos

