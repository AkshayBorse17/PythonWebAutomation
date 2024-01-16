list_elements_p = driver.find_elements(By.XPATH, "//p[contains(text(),'A')]")
for i in list_elements_p:
    if i.text == "Copyright © CURA Healthcare Service 2024":
        i.click()
    print(i.text)
