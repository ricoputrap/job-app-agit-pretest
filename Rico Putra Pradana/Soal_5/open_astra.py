from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager # automate chromedriver preparation
import chromedriver_binary  # adds chromedriver binary to path
import time

# instantiate the google chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# navigate to astra web page
driver.get("https://astra.co.id/")

# hold for 4 seconds
time.sleep(4)

# close the browser
driver.close()