from pages.login import Login
from views.view import Interface

"""
1.
    Selenium fica com coisas de selenium
2. Não temos página (PO)
3. PageElement

Responsabilidades
    - SeleniumMethods
        - url?
        - webdriver
"""


class Executer:
    # Instanceia os inputs do usuário = dict()
    def __init__(self, userinput=None):
        self.userinput = userinput

    def callbacks(self):
        Login.login_on_insta(
            username=self.userinput['username'],
            password=self.userinput['password'],
        )


if __name__ == '__main__':
    Executer(Interface()).callbacks()
