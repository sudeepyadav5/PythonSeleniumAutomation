import time
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service("C:/Users/3Embed/Python_Ast/WebDriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.dezy.com/in")
driver.maximize_window()
wait = WebDriverWait(driver, 10, poll_frequency=1,
                     ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                         ElementNotSelectableException])

assert "Best Dental Clinic & Dentist near me, Nearest Dental Clinic - Dezy" in driver.title, "Title is not Match  "
time.sleep(2)

ClinicsLink = wait.until(lambda x: x.find_element(By.XPATH, "//div[@class='mx-4 text-white md:mx-6'][3]"))
ClinicsLink.click()
time.sleep(2)

# x = 0  # X-coordinate
# y = 780  # Y-coordinate
# driver.execute_script(f"window.scrollTo({x}, {y});")

time.sleep(2)
Root_Canal = wait.until(
    lambda x: x.find_element(By.XPATH, '//*[@id="test-service-item-0"]/div/div/span/img'))
Root_Canal.click()
actions = ActionChains(driver)
actions.move_to_element(Root_Canal).perform()

time.sleep(2)
Book_an_appointment = wait.until(lambda x: x.find_element(By.XPATH, "//button[@id='id_ctabar_btn']"))
Book_an_appointment.click()

# Details
time.sleep(2)
Name = wait.until(lambda x: x.find_element(By.XPATH, "//input[@placeholder='Enter name']"))
Name.send_keys("Sudeep Yadav")

time.sleep(2)
Mobile = wait.until(lambda x: x.find_element(By.XPATH, "//input[@placeholder='Enter phone']"))
Mobile.send_keys("8460905553")

time.sleep(2)
CityDD = wait.until(lambda x: x.find_element(By.XPATH, "//div[@class='flex w-full text-sm']"))
CityDD.click()
time.sleep(2)

# CityLists = wait.until(lambda x: x.find_elements(By.XPATH, "//div/div[@class='flex px-2 py-2 text-sm border-b "
#                                                            "cursor-pointer hover:bg-zinc-200']/div"))
time.sleep(2)
CityLists = wait.until(lambda x: x.find_elements(By.XPATH, "//div[@class='mt-1']"))

for CityList in CityLists:
    CityName = CityList.text
    print(CityName)
    if CityName == "Bangalore":
        ActionChains(driver).move_to_element(CityList).perform()
        CityList.click()
        break

ProceedBtn = wait.until(lambda x: x.find_element(By.XPATH, "// *[ @ id = 'pageContent'] / div / div[2] / div[2] / div[""1] / button / span / span"))
ProceedBtn.click()

Otp_Screen = wait.until(lambda x: x.find_element(By.XPATH, "//*[@id='mainModalContainer']/div[3]/div/div/div["
                                                           "2]/div/div/input"))
Otp_Screen.click()
time.sleep(15)

VerifyOtpBtn = wait.until(lambda x: x.find_element(By.XPATH, "//*[@id='mainModalContainer']/div[3]/div/div/div["
                                                             "2]/div/button/span/span"))
VerifyOtpBtn.click()
time.sleep(2)

"""x1 = 0  # X1-coordinate
y1 = 230  # Y1-coordinate
driver.execute_script(f"window.scrollTo({x1}, {y1});")"""

Select_Clinic = wait.until(lambda x: x.find_element(By.XPATH, "//div/div[2]/div[2]/div[3]/div[1]/div["
                                                              "2]/div/button/span/span/p[text()='View availabilty']["
                                                              "1][1]"))
Select_Clinic.click()
actions.move_to_element(Select_Clinic).perform()

"""x2 = 0  # X2-coordinate
y2 = 700  # Y2-coordinate
driver.execute_script(f"window.scrollTo({x2}, {y2});")"""

time.sleep(5)
Select_Date = wait.until(lambda x: x.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[3]/div[2]/nav/div/div[2]/div[2]/div[2]/div/div[1]/div/button[2]"))
Select_Date.click()
actions.move_to_element(Select_Date).perform()
time.sleep(2)

Select_Time = wait.until(lambda x: x.find_element(By.XPATH, "//*[@id='clinic-detail-scrollable-element']/div[2]/div[2]/div[2]/div[1]/div[4]/div[7]/p"))
Select_Time.click()

time.sleep(10)
driver.minimize_window()
driver.quit()
