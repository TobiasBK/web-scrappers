#opens and closes the browser. 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#To get webdriver (geckodriver for firefox) to work put in copied to /ur/local/bin
#https://askubuntu.com/questions/877992/how-to-put-executable-to-usr-local-bin

browser = webdriver.Firefox()

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()
