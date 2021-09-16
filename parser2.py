import os, requests, re
from selenium import webdriver

emails = []
pageNo = 1

def findAllLinks(link):
  options = webdriver.ChromeOptions()
  options.add_argument('headless')
  options.add_argument('window-size=1200x600')
  browser = webdriver.Chrome(options=options)
  browser.get(link)

  foundElems = browser.find_elements_by_css_selector('.ajax-modal-link.icon-envelope.cursor-pointer.addax.addax-cs_hl_email_submit_click')
  first = foundElems[0]
  print(first.get_attribute('data-company-email'))

  for element in foundElems:
    try:
      email = element.get_attribute('data-company-email')
      print(email)
      emails.append(email)
    except:
      print('No email')
  
  browser.close()


for n in range(1, 100):
  findAllLinks('https://panoramafirm.pl/salon_urody/firmy,%s.html' %n)
  pageNo = n

for email in emails:
  file = open("emailList2.txt", "a")
  file.write(email)
  file.write('\n')
print(pageNo)

