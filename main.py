from selenium import webdriver
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


driver.get("https://downloads.adblockplus.org/devbuilds/adblockpluschrome/")

time.sleep(6)

driver.get("https://youtu.be/tEXYfT_G0W0")
driver.implicitly_wait(10)

time.sleep(2)
print(driver.title)
chwd=driver.current_window_handle
driver.switch_to.window(chwd)

while True:
    pass