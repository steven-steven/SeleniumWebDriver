from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #put computer sleep time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #launch webdriver
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        #launch firefox and goto instagram
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2) #wait 2 seconds

        # once in page click see selenium's xpath:"//a[@href='/accounts/login/']"
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)

        # "//input[@name='username']"
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)

        # "//input[@name='password']"
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)

        #enter
        password_elem.send_keys(Keys.RETURN)
        time.sleep(3)
        
        #remove notification. click "Not Now"
        notifOptionBtn = driver.find_element_by_xpath("//*[contains(text(),'Not Now')]")
        notifOptionBtn.click()
        time.sleep(2)
    
    #given hashtag, like all photos
    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")
        time.sleep(2)
        #load pictures
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        #searching for picture link
        divs = driver.find_elements_by_class_name('v1Nh3')
        links = [link for divElem in divs for link in divElem.find_elements_by_tag_name('a')]
        pic_hrefs = [elem.get_attribute('href') for elem in links]
        print(hashtag + '   photos :' + str(len(pic_hrefs)))
        print("\nfirst like: " + pic_hrefs[0])

        #loop through the link
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #like the button
            try:
                #driver.find_element_by_link_text("Like").click()
                driver.find_element_by_xpath("//span[@aria-label='Like']").click()
                time.sleep(18) #liking 200 pic per hour
            except Exception as e:
                time.sleep(2)
    
    def comment(self, postLink, text):
        driver = self.driver
        driver.get(postLink)
        time.sleep(2)
        for i in range(200):
            comment = str(i) + ". "+ text

            #click comment icon
            driver.find_element_by_xpath("//span[@aria-label='Comment']").click()
            
            #type
            print("sending text: " + comment)
            commentArea2 = driver.find_element_by_xpath("//textarea[@aria-label='Add a comment…']")
            commentArea2.send_keys(comment)
            time.sleep(2)

            #enter
            commentArea2.send_keys(Keys.RETURN)
            time.sleep(50)

stevenIG = InstagramBot("stevensorryindo@gmail.com", "facebooksteven")
stevenIG.login()
#stevenIG.like_photo('tulus')
stevenIG.comment("https://www.instagram.com/p/BwGGgJ0FnbaSmx7s252L_UbYX9n-rkuX_nBjRs0/", "Hate")