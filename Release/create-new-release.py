from driver_chrome import DriverChrome
from githuber import GitHuber
from secret import Secret
print(Secret)
driver = DriverChrome()
githuber = GitHuber(driver)
githuber.login()