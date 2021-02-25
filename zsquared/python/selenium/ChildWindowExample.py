from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")

driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
childWindow = driver.window_handles[1]

driver.switch_to.window(childWindow)
print(driver.find_element_by_tag_name("h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
assert "Opening a new window" == driver.find_element_by_tag_name("h3").text