from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/dropdownsPractise")
driver.find_element_by_id("autosuggest").send_keys("ind")
driver.implicitly_wait(3)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print (len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break
        
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"