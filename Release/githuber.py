
from secret import Secret
class GitHuber():
    def __init__(self, driver):
        self.driver = driver
    
    def login(self):
        self.driver.goto('https://github.com/login')
        self.driver.send_keys('//*[@id="login_field"]',Secret.email)
        self.driver.send_keys('//*[@id="password"]',Secret.github_password)
        self.driver.click('//*[@id="login"]/div[4]/form/div/input[12]')