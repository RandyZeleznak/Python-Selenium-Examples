from selenium import webdriver

validateText = "Option3"

driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice")

driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()
#alert.dismiss()


