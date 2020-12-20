from selenium import webdriver
import random
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
j = 0
while(j<=50):
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://docs.google.com/forms/d/e/1FAIpQLSeQZRoNlhewMhek-uylBUR8hics099hs84F-ghjBc-Bw4JbFw/viewform')
    time.sleep(2)
    element = browser.find_elements_by_css_selector("div.appsMaterialWizToggleRadiogroupEl")
    print(element)
    arr = [1,6,18,23,29,32,35,41,43]
    for i in range(len(arr)):
        if i == 0:
            element[random.randint(0,arr[i])].click()
        else:
            element[random.randint(arr[i-1]+1,arr[i])].click()
    browser.find_element_by_css_selector("div.appsMaterialWizButtonPaperbuttonFilled").click()
    time.sleep(2)
    browser.quit()
    j+=1
    print("Round :" ,j)