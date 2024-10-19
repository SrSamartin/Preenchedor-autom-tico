import pyautogui
import time


# Passo 1 - Entrar no Site

pyautogui.PAUSE = 1

pyautogui.press("win")

pyautogui.write("opera")

pyautogui.press("enter")

time.sleep(1)

pyautogui.click(x=652, y=54)

pyautogui.write("WWW.SITEDAEMPRESA.COM")

pyautogui.press("enter")


# Passo 2 - Fazer login

time.sleep(3)

# OBS: CASO VOCÊ NÃO SAIBA AS POSIÇÕES DOS CLIQUES, UTILIZE O pegar_posicao.py PARA DESCOBRIR. APÓS ISSO, PREENCHA O DADO ABAIXO

pyautogui.click(x=503, y=337)

pyautogui.write("exemplo@email.com")

pyautogui.press("tab")

pyautogui.write("senha123")

pyautogui.press("tab")

pyautogui.press("enter")


# Passo 3 - Importar a Base de Dados

import pandas
# O COMANDO READ LERÁ A BASE DE DADOS QUE VOCê POSSUI. DEVE SER USADO DE ACORDO COM O TIPO DE ARQUIVO DA BASE DE DADOS, PORTANTO O FORMATO SERÁ: pandas.read_tipodoarquivo("Nome do Arquivo")
# Veja o exemplo abaixo:
tabela = pandas.read_csv("produtos.csv")


# Passo 4 - Repetir o proceso de cadastro até acabarem os produtos

# OBS: NÃO ALTERAR!!
linha = 0

while True:

    #  APÓS O LOGIN, SERÁ NECESSÁRIO CLICAR NA PRIMEIRA CAIXA DE PREENCHIMENTO DO FORMULÁRIO. CASO VOCÊ NÃO SAIBA AS POSIÇÕES DOS CLIQUES, UTILIZE O pegar_posicao.py PARA DESCOBRIR. APÓS ISSO, PREENCHA O DADO ABAIXO
    pyautogui.click(x=540, y=228)

    # OBS: OS ITENS ABAIXO DEVERÃO SEGUIR A LÓGICA DO FORMULÁRIO A SER PREENCHIDO, PORTANTO, PREENCHA DE ACORDO COM SUA BASE DE DADOS E ADAPTE DA FORMA QUE MELHOR FUNCIONAR:

    # Item 1
    item1 = tabela.loc[linha, "item1"]
    pyautogui.write(item1)
    pyautogui.press("tab")

    # Item 2
    item2 = tabela.loc[linha, "item2"]
    pyautogui.write(item 2)
    pyautogui.press("tab")

    # Item 3

    item3 = tabela.loc[linha, "item3"]
    pyautogui.write(item3)
    pyautogui.press("tab")

    # Item 4

    item4 = tabela.loc[linha, "item4"]
    # OBS: CASO O ITEM SEJA UM NÚMERO, ELE DEVERÁ SER CONVERTIDO PARA TEXTO ATRAVÉS DO str(). COMO FEITO ABAIXO:
    pyautogui.write(str(item4))
    pyautogui.press("tab")

    # Item 5

    item5 = tabela.loc[linha, "item5"]
    pyautogui.write(str(item5))
    pyautogui.press("tab")

    # Item 6

    item6 = tabela.loc[linha, "item6"]


    # EM CASO DA LACUNA DA BASE DE DADOS ESTEJA VAZIA:
    if not pandas.isna(item6):
        pyautogui.write(str(item6))

   # CASO SUA LISTA POSSUA MAIS ITENS A SEREM PREENCHIDOS, ADICIONE-OS ABAIXO DE ACORDO COM AS NECESSIDADES JÁ EXPLICADAS ACIMA!

  
   # NÃO ALTERAR!!!!!!
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(+ 15)

    linha = linha + 1

    # ATENÇÃO!!! PARA O SCRIPT SE ENCERRAR, COLOQUE O NÚMERO DE LINHAS QUE A BASE DE DADOS POSSUI NO LUGAR DE "295", QUE É UM NÚMERO EXEMPLO!
    if linha == 295:
        break
    continue
