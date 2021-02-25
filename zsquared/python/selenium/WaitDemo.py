from selenium import webdriver
# WaitDemo.py is a sample program to show use of wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

veggielist = []
veggielist2 = []
driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/seleniumPractise")

driver.implicitly_wait(8)
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(count)
#assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    veggielist.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()

print(veggielist)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

veggies = driver.find_elements_by_css_selector("p.product-name")
for veg in veggies:
    veggielist2.append(veg.text)
print(veggielist2)
assert veggielist == veggielist2

originalAmount = driver.find_element_by_css_selector(".discountAmt").text

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))

discountAmount = driver.find_element_by_css_selector(".discountAmt").text

assert discountAmount < originalAmount

