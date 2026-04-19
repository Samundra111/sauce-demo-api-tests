class Login:
    def __init__(self,page):
        self.page=page
        self.username_field=page.locator("#user-name")
        self.password=page.locator("#password")
        self.login_field=page.locator("#login-button")
        self.error_msg= page.locator("[data-test='error']")
        self.page_title=page.locator(".title")
    def goto(self):
        self.page.goto("https://www.saucedemo.com")
    def login(self,username,password):
        self.username_field.fill(username)
        self.password.fill(password)
        self.login_field.click()
    def get_error_messege(self):
        return self.error_msg.inner_text()
    def get_page_title(self):
        return self.page_title.inner_text()


