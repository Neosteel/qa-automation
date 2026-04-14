class LoginPage: 
    
    def __init__(self, page):
        self.page = page
        self.userid = '[name="uid"]'
        self.password = '[name="password"]'
        self.login_btn = '[name="btnLogin"]'

    def login(self , userid , password):
        self.page.locator(self.userid).fill(userid)
        self.page.locator(self.password).fill(password)
        self.page.locator(self.login_btn).click()