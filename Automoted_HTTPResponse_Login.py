import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.keys import Keys
import time 

def http_response():
    
    enter_url = 'url-goes-here'
    response = requests.get(f'{enter_url}')
    print(response)
    print(response.status_code)


service = Service('C:/ProgramData/chocolatey/bin/chromedriver.exe')
def get_drvier():

    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service ,options=options)
    driver.get(f"{enter_url}")
    return driver 

def clean_text(text):
    """Extract only temp from text"""
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_drvier()
    
    driver.find_element(by="xpath", value="/html/body/div[1]/div/form/fieldset[1]/div[1]/input").send_keys("username-goes-here")
    time.sleep(2)
    driver.find_element(by="xpath", value='//*[@id="password"]').send_keys("password-goes-here" + Keys.RETURN)
    time.sleep(2)

pas_http_response()
main()