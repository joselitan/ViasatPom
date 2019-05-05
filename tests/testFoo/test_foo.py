from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://sso.teachable.com/secure/42299/checkout/342639/complete-javascript-guide")
sleep(2)

moveto = driver.find_element_by_xpath("//div[@class='form-group']")

driver.execute_script("arguments[0].scrollIntoView();", moveto)

driver.switch_to.frame("__privateStripeFrame5")
credit_card = driver.find_element_by_name("cardnumber")
print(credit_card)
credit_card.send_keys("342342")
driver.switch_to.default_content()

driver.switch_to.frame("__privateStripeFrame6")
exp_date = driver.find_element_by_name("exp-date")
exp_date.send_keys("0911")
driver.switch_to.default_content()

driver.switch_to.frame("__privateStripeFrame7")
cvc = driver.find_element_by_name("cvc")
cvc.send_keys("222")

sleep(2)
driver.quit()
driver.close()
