import time

from page_objects.pages_object import Page, PageElement


class Login:
    def login_on_insta(username, password):

        Page.open('https://www.instagram.com/')

        # Clica na caixa de logitn "usuario", e insere o usuario (self.user)
        username_input = PageElement.find_element_wait(
            locator='//*[@id="loginForm"]/div/div[1]/div/label/input',
        )

        PageElement.click(username_input)
        PageElement.send_keys(username_input, username)

        # Clica na caixa de login "senha", e insere a senha (self.password)
        password_input = PageElement.find_element_wait(
            locator="//input[@name='password']",
        )
        PageElement.click(password_input)
        PageElement.send_keys(password_input, password)

        # clica no botao entrar para efetuar o login
        login = PageElement.find_element_wait(
            locator="//button[@type='submit']",
        )

        PageElement.click(login)
        time.sleep(30)
