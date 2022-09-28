from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import pyautogui


class Instagrambot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(
            executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        bot.find_element_by_name('username').send_keys(self.username)
        bot.find_element_by_name('password').send_keys(
            self.password + Keys.RETURN)
        time.sleep(5)

    def searchname(self, name):
        bot = self.bot

        bot.get('https://www.instagram.com/' + name)

    def likephotos(self, amount):
        bot = self.bot
        bot.find_element_by_class_name('eLAPa').click()
        time.sleep(3)
        # vid = bot.find_element_by_class_name("fXIG0")
        i = 1

        while i <= amount:
            try:
                time.sleep(3)
                try:
                    vid = bot.find_element_by_class_name("fXIG0")
                    if vid:
                        time.sleep(2)
                        bot.find_element_by_class_name('fr66n').click()
                        time.sleep(1)
                        bot.find_element_by_class_name(
                            'coreSpriteRightPaginationArrow').click()
                        i += 1
                except:
                    vid = bot.find_element_by_class_name("tWeCl")
                    if vid:
                        time.sleep(3)
                        bot.find_element_by_class_name('fr66n').click()
                        time.sleep(1)
                        bot.find_element_by_class_name(
                            'coreSpriteRightPaginationArrow').click()
                        i += 1
            # except:
            #     time.sleep(10)
            #     # time.sleep(10)
            #     vid = bot.find_element_by_class_name("tWeCl")
            #     if vid:
            #         bot.find_element_by_class_name('fr66n').click()
            #         time.sleep(6)
            #         bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            #         i += 1

            except:
                time.sleep(4)
                element = bot.find_element_by_class_name("ZyFrc")
                actions = ActionChains(bot)
                actions.double_click(element).perform()
                time.sleep(1)
                bot.find_element_by_class_name(
                    'coreSpriteRightPaginationArrow').click()
                i += 1


insta = Instagrambot('user_name', 'user_password')
insta.login()
insta.searchname('name')
insta.likephotos(475)
