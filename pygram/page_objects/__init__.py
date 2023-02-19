from selenium import webdriver

# Instancia o Driver e define pressets do webdriver do selenium
options = webdriver.ChromeOptions()
options.add_argument('lang=pt-br')
driver = webdriver.Chrome(
    executable_path=r'pygram\page_objects\chromedriver.exe'
)
