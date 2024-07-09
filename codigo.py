import pyautogui;
import time;
import pandas;

# pyautogui.click() - Clicar com o Mouse
# pyautogui.write() - Escrever Texto
# pyautogui.press() - Apertar a Tecla Comandada
# pyautogui.hotkey() - Combinação de Teclas (Ctrl + C)
# pyautogui.scroll() - Rolar a Tela

pyautogui.PAUSE = 0.5

# Passo 1 - Entrar no Sistema ->

# Passo 1.1 - Abrir o navegador ->

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Passo 1.2 - Entrar no Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login ->

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# Passo 2 - Efetuar o Login no Sistema ->

pyautogui.click(x=774, y=472)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("email@email.com.br")

# Passo 2.1 - Passar para o campo de Senha ->

pyautogui.press("tab")
pyautogui.write("123456")

# Passo 2.2 - Clicar em Login ->

pyautogui.click(x=960, y=679)

time.sleep(3)

# Passo 3 - Importar Base de Dados ->

DataBaseTable = pandas.read_csv("produtos.csv")

# Passo 4 - Cadastrar Um Produto ->

for Line in DataBaseTable.index:

    pyautogui.click(x=773, y=331)
    Code = str(DataBaseTable.loc[Line, "codigo"])
    pyautogui.write(Code)

    pyautogui.press("tab")
    Brand = str(DataBaseTable.loc[Line, "marca"])
    pyautogui.write(Brand)

    pyautogui.press("tab")
    Type = str(DataBaseTable.loc[Line, "tipo"])
    pyautogui.write(Type)

    pyautogui.press("tab")
    Category = str(DataBaseTable.loc[Line, "categoria"])
    pyautogui.write(Category)

    pyautogui.press("tab")
    UnitPrice = str(DataBaseTable.loc[Line, "preco_unitario"])
    pyautogui.write(UnitPrice)

    pyautogui.press("tab")
    Cost = str(DataBaseTable.loc[Line, "custo"])
    pyautogui.write(Cost)

    pyautogui.press("tab")
    Observation = str(DataBaseTable.loc[Line, "obs"])
    if Observation != "nan":
        pyautogui.write(Observation)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
    time.sleep(1)