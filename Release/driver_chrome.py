from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class DriverChrome:
	def __init__(self,headless = False):
		self.headless = headless
		options = Options()
		options.headless = headless
		self.driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')

	def goto(self,site):
		self.driver.get(site)

	def click(self,xpath):
		elem = self._find(xpath)
		elem.click()

	def send_keys(self, xpath, keys):
		elem = self._find(xpath)
		elem.send_keys(keys)

	def get_value(self,xpath,attribute):
		elem = self._find(xpath)
		return elem.get_attribute(attribute)

	def is_selected(self, xpath):
		elem = self._find(xpath)
		return elem.is_selected()

	def refresh(self):
		self.driver.refresh()

	def _find(self, xpath):
		return self.driver.find_element_by_xpath(xpath)