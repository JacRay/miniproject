from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome("C:\Users\jacra\Downloads\chromedriver_win32\chromedriver.exe")
# DRIVER = 'chromedriver'
#driver = webdriver.Chrome(DRIVER)
driver.get('https://www.spotify.com')
screenshot = driver.save_screenshot('my_screenshot.png')
driver.quit()