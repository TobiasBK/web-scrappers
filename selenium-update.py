
from selenium import webdriver


#To get webdriver (geckodriver for firefox) to work put in copied to /usr/local/bin
#https://askubuntu.com/questions/877992/how-to-put-executable-to-usr-local-bin

#Inspect steps: 
#find what divs/class are in common. copy.
#Then find the links,copy path.

url = ''

# div/class = 'sc-1kjt2eu-1 ivMSSC sc-i2xq1s-2 fPfUoy'
#path://*[@id="__next"]/div/div[1]/div[2 ]/div[2]/div[2]/div[3]/div[1]/div[2]/a/div/div[2]/h2

# PATH = '/usr/local/bin/geckodriver'
driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver')
driver.get(url)

# articles = driver.find_elements_by_class_name('wp-block-column')
articles = driver.find_elements_by_tag_name('li') #element(s)...

#can add a . at the start of xpath so we search only here
for article in articles:
    # text = articles.text
    #title = article.find_element_by_xpath('.//*[@id="main"]/div[1]/div[1]/ul/li[1]/a').text
    title = article.find_element_by_tag_name('a').text
    print(title)

driver.close()
