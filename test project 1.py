from idlelib import browser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

path = Service(r"C:\Users\indra\PycharmProjects\chromedriver\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=path)
driver.get("https://dummy-tickets.com/")
driver.maximize_window()
driver.implicitly_wait(15)
wait = WebDriverWait(driver, 60)

driver.find_element(By.XPATH, "//*[@class='button button_big']").click()
driver.find_element(By.XPATH, "//div[@class='f_h_both']").click()

# wait until element is clicakble
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@class='return_trip']")))
driver.find_element(By.XPATH, "//*[@class='return_trip']").click()

driver.find_element(By.XPATH, "//input[@id='origin1']").send_keys("BER")

wait.until(expected_conditions.element_to_be_clickable((By.XPATH, " //input[@id='destination1']"))).send_keys("DEL")
driver.find_element(By.XPATH, "//mark[text()='DEL']").click()



#dest = driver.find_element(By.XPATH, " //input[@id='destination1']").text
#print(dest)

#check in date

driver.find_element(By.XPATH, '(//*[@class="selected-date"])[1]').click()
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '(//*[contains(@class,"next")])[1]'))).click()

while True:
    driver.find_element(By.XPATH, '(//*[contains(@class,"next")])[1]').click()
    month = driver.find_element(By.ID, 'date1').get_attribute("data-changemy")
    if 'May' in month:
        driver.find_element(By.XPATH, '(//*[text()="15"])[1]').click()
        break

#check out date

driver.find_element(By.XPATH, '(//*[@class="selected-date"])[2]').click()
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '(//*[contains(@class,"next")])[2]'))).click()
while True:
    driver.find_element(By.XPATH, '(//*[contains(@class,"next")])[2]').click()
    month = driver.find_element(By.ID, 'return_date').get_attribute("data-changemy")
    if 'Jun' in month:
        driver.find_element(By.XPATH, '(//*[text()="26"])[2]').click()
        break


#hotel check in

driver.find_element(By.XPATH, '(//*[@class="selected-date"])[3]').click()
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '(//*[contains(@class,"next")])[3]'))).click()

while True:
    driver.find_element(By.XPATH, '(//*[contains(@class,"next")])[3]').click()
    month = driver.find_element(By.ID, 'checkIn1').get_attribute("data-changemy")
    if 'May' in month:
        driver.find_element(By.XPATH, '(//*[text()="17"])[3]').click()
        break

#hotel check out

driver.find_element(By.XPATH, '(//*[@class="selected-date"])[4]').click()
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '(//*[contains(@class,"next")])[4]'))).click()
while True:
    driver.find_element(By.XPATH, '(//*[contains(@class,"next")])[4]').click()
    month = driver.find_element(By.ID, 'checkOut1').get_attribute("data-changemy")
    if 'May' in month:
        driver.find_element(By.XPATH, '(//*[text()="20"])[4]').click()
        break


#city
driver.find_element(By.XPATH, " //input[@id='hotelCity1']").send_keys("Delhi")
driver.find_element(By.XPATH, "//*[text()='Delhi']").click()

#total bill
bill = driver.find_element(By.XPATH, "//h2[@id='TotalAmountINR']")
print(bill.text)





time.sleep(10)
driver.quit()
