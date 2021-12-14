from selenium import webdriver

opcoes = webdriver.ChromeOptions()
opcoes.add_argument("--incognito")
navegador = webdriver.Chrome(options=opcoes)
navegador.get('https://google.com')
navegador.maximize_window()
