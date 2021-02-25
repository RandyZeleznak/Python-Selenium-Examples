from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")

driver.get("https://login.salesforce.com/")
driver.find_element_by_css_selector("#username").send_keys("Brian")
driver.find_element_by_css_selector(".password").send_keys("May")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//a[text()='Cancel']").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)


