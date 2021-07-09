import os, requests, re
from selenium import webdriver

emails = []

def findAllLinks(link):
  options = webdriver.ChromeOptions()
  options.add_argument('headless')
  options.add_argument('window-size=1200x600')
  browser = webdriver.Chrome(options=options)
  browser.get(link)

  foundElems = browser.find_elements_by_css_selector('.outpost_name a')

  for link in foundElems:
    browser = webdriver.Chrome(options=options)
    browser.get(link.get_attribute('href'))
    try: 
      email = browser.find_element_by_class_name('email.highlighted').text
      print(email)
      emails.append(email)
    except:
      print('No email')

    browser.close()

# for n in range(1, 10):
#   findAllLinks('http://przedszkolowo.pl/baza-przedszkoli/%s' %n)
findAllLinks('http://przedszkolowo.pl/baza-przedszkoli/1')

for email in emails:
  file = open("emailList.txt", "a")
  file.write(email)
  file.write('\n')
print(emails)

