from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\GeckoDriver\\geckodriver.exe")

driver.get("https://rahulshettyacademy.com/")

print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/angularpractice")
#print(driver.current_url)
#driver.back()
#print(driver.current_url)
#driver.find_element_by_name("name").send_keys("Randy")
driver.find_element_by_css_selector("input[name='name']").send_keys("Brianna")
driver.find_element_by_name("email").send_keys("may")

driver.find_element_by_id("exampleCheck1").click()

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")

driver.implicitly_wait(5)
driver.find_element_by_xpath("//input[@type='submit']").click()

print(driver.find_element_by_class_name("alert-success").text)


#driver.close()