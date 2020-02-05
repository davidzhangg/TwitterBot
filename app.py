from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox(executable_path = '/Applications/Python 3.8/geckodriver')

    def login(self):
        bot = self.bot
        #opens up twitter page
        bot.get('https://twitter.com/')
        #pause for 3 seconds to let everything load up
        time.sleep(3)
        #grabs the class name of the email box
        email = bot.find_element_by_name('session[username_or_email]')
        #grabs the class name of the password box
        password = bot.find_element_by_name('session[password]')
        #clear any email already present in the email box
        email.clear()
        #clear any password already present in the password box
        password.clear()
        #enters in username/email
        email.send_keys(self.username)
        #enters in password
        password.send_keys(self.password)
        #press login
        password.send_keys(Keys.RETURN)
        #wait for 3 seconds for everything to load
        time.sleep(3)

    def like_tweet(self,search):
        bot = self.bot
        #search for certain topics on twitter to go to in the search box
        bot.get('https://twitter.com/search?q=' + search + '&src=typed_query')
        time.sleep(3)
        #scrolls through the twitter page 
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            #grabs the tweets
            tweets = bot.find_elements_by_class_name('css-1dbjc4n')
            #saves the url of each tweet
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
    		#for each tweet, press the like button 
            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_elements_by_class_name('HeartAnimation').click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)
                



test = TwitterBot('example@email.com', 'password')
test.login()
test.like_tweet('sports')


