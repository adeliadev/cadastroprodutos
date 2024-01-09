import pyautogui
import time
import pandas

# Passo 1 - entrar no sitema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.PAUSE = 0.8

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

pyautogui.press("enter")

time.sleep(0.5)

# Passo 2 - fazer login no sistema

pyautogui.click(x=616, y=467)

pyautogui.write("meuemail@gmail.com")

pyautogui.press('tab')

pyautogui.write('senhatal')

pyautogui.position(x=969, y=657)

pyautogui.press("enter")

# Passo 3 - Importar a base de dados

tabela = pandas.read_csv("produtos.csv")
print(tabela)

time.sleep(2)

# Passo 5 - repetir isso até acabar a base de dados
for linha in tabela.index:
    # Passo 4 - cadastrar um produto
    pyautogui.click(x=704, y=323)
    # codigo
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)