from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
PATH="\\chromedriver.exe"

driveroptions=webdriver.ChromeOptions()
driveroptions.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
driveroptions.add_argument("--log-level")
driveroptions.add_argument('--disable-application-cache')
driveroptions.add_argument('--load-extension=C:\\Users\\doruk\\Desktop\\SeleniumTest\\adblock')

driveroptions.binary_location= r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
ser=Service(PATH)

driver=webdriver.Chrome(options=driveroptions,service=ser)

driver.get("https://www.google.com")
time.sleep(3)
driver.get("https://www.youtube.com/watch?v=wMzIHuWh_I0&list=RDwMzIHuWh_I0&start_radio=1")

print(driver.title)
chwd=driver.current_window_handle 
driver.switch_to.window(chwd)
time.sleep(2)
while True:
    time.sleep(2)
    nextbutton=driver.find_element(by=By.CSS_SELECTOR,value=".ytp-next-button.ytp-button")
    nextbutton.click()
