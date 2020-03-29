from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from colorama import Fore, Back, Style
from colorama import init
# import pyspeedtest  -Discontinued
import random


if __name__ == '__main__':
    pass
else:
    print('Run this directly')
    exit(0)
init()
print('You must have a fast internet connection to get accurate results...')
# from proxyfeeder import animate  # loading animation
twitter_occupied = False
insta_occupied = False
twitter_invalid = False
spotify_occupied = False
github_occupied = False
amazon_occupied = False
deviant_occupied = False
gmail_occupied = False
adobe_occupied = False
errors = []
# references are looked at id, as params.
email = input('Enter the email of person to search for:: ').lower()
name = input('If you know a name linked to this person it could help find more link, else leave it blank and press ENTER:: ').title()
if name == '':
    web_page = requests.get('https://www.name-generator.org.uk/quick/')
    soup = BeautifulSoup(web_page.content, 'html.parser')
    names = soup.findAll('div', {'class':'name_heading'})
    name_list = []
    for name in range(len(names)):
        name_list.append(names[name].text)
        name = name_list[0]
    print(name_list)  # contains 10 generic names generated...

username = email.split('@')[0]
domain = email.split('@')[1]
password = 'Password123@'
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
print('Started')
delay = 10  # make a option to change delay this for more accuracy...
driver.get('https://twitter.com/i/flow/signup')  # need a delay for website to load.
try:
    email_switch = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[4]/span')))
    # print('Page is ready!')
    driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[4]/span').click()
    driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/label/div/div[2]/div/input').send_keys(email)
    # driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/label/div/div[2]/div/input').click()
    # driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/label/div/div[2]/div/input').click()
    # print('Got Twitter Login Page')
except TimeoutException as e:
    errors.append('Twitter page has changed please look at page again and refactor code.')
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/div/span')))
    email_status = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/div/span')
    if email_status.text == 'Email has already been taken.':
        twitter_occupied = True
    elif email_status.text == 'This email is invalid.':
        twitter_invalid = True
    else:
        errors.append('Error with Twitter finding email status, look into it.')
except Exception as e:
    if e == TimeoutException:
        errors.append('Twitter Timeout/ Element cannot be found anymore.')
    twitter_occupied = False
    try:
        driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/span')
    except Exception as e:
        errors.append('Twitter Website has probably changed and needs to be looked at...')

if twitter_occupied:
    print(Fore.BLACK+Back.GREEN+'Twitter - Email Found')
else:
    print(Fore.BLACK+Back.RED+'Twitter - Email Not Found')

driver.get('https://www.instagram.com/accounts/emailsignup/')
try:
    email_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')))
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(email)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[5]/div/label/input').click()
except TimeoutException:
    errors.append('Instagram page has changed please look at page again and refactor code.')
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/div/span')))
    insta_element = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/div/span')
    insta_occupied = True
except Exception as e:
    insta_occupied = False
    errors.append('Instagram Timeout/ Element cannot be found anymore.')
if insta_occupied:
    print(Fore.BLACK+Back.GREEN+'Instagram - Email Found')
else:
    print(Fore.BLACK+Back.RED+'Instagram - Email Not Found')


driver.get('https://www.spotify.com/uk/signup/')
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="register-email"]')))
    email_input = driver.find_element_by_xpath('//*[@id="register-email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="register-confirm-email"]').click()
    driver.find_element_by_xpath('//*[@id="register-email"]').click()
except TimeoutException:
    errors.append('Spotify page has changed please look at page again and refactor code.')
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div/section[2]/div/form/fieldset/ul/li[1]/label[2]')))
    spotify_elmnt = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/section[2]/div/form/fieldset/ul/li[1]/label[2]')
    spotify_occupied = True
except TimeoutException:
    spotify_occupied = False
    errors.append('Spotify Timeout/ Element cannot be found anymore.')
if spotify_occupied:
    print(Fore.BLACK+Back.GREEN+'Spotify - Email Found')
else:
    print(Fore.BLACK+Back.RED+'Spotify - Email Not Found')

driver.get('https://github.com/join')
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="user_email"]')))
    email_input = driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="user_password"]').click()
    driver.find_element_by_xpath('//*[@id="user_email"]').click()
except TimeoutException:
    errors.append('Github page has changed please look at page again and refactor code.')
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'error')))
    github_elmnt = driver.find_element_by_class_name('error')
    github_occupied = True
except TimeoutException:
    github_occupied = False
    errors.append('Github Timeout/ Element cannot be found anymore.')
if github_occupied:
    print(Fore.BLACK+Back.GREEN+'Github - Email Found')
else:
    print(Fore.BLACK+Back.RED+'Github - Email Not Found')
if 'gmail' in domain:
    print(Fore.BLACK+Back.GREEN+'Gmail - Email Found')
else:
    print(Fore.BLACK+Back.RED+'Gmail - Email Not Found')


driver.get('https://www.amazon.co.uk/')
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="nav-link-accountList"]')))
    driver.find_element_by_xpath('//*[@id="nav-link-accountList"]').click()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="ap_email"]')))
    driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="continue"]').click()
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div/div/h4')))
        amazon_occupied = False
    except Exception as e:
        amazon_occupied = True
        errors.append('Amazon Timeout/ Element cannot be found anymore. Expected if account exists')
except Exception as e:
    errors.append('Amazon page has changed please look at page again and refactor code.')
if amazon_occupied:
    print(Fore.BLACK+Back.GREEN+'Amazon - Email Found')
else:
    print(Fore.BLACK+Back.RED+'Amazon - Email Not Found')

driver.get('https://www.deviantart.com/_sisu/do/signup')
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="email"]')))
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="joinbutton"]').click()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="username"]')))
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div/div[2]/div/div[1]/form/div/div[2]/div[1]/div/div[3]/span')))
        deviant_elmnt = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/form/div/div[2]/div[1]/div/div[3]/span')
        if deviant_elmnt.text == 'That email address is already in use.':
            deviant_occupied = True
    except Exception as e:
        deviant_occupied = False
        errors.append('Deviant Timeout/ Element cannot be found anymore.')
except TimeoutException:
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="rc-anchor-container"]')))
        errors.append('ReCaptcha is found on site, please use a proxy and proceed...')
    except Exception as e:
        errors.append('Deviant page has changed please look at page again and refactor code.')
if deviant_occupied:
    print(Fore.BLACK+Back.GREEN+'Deviant - Email Found')
else:
    print(Fore.BLACK+Back.RED+'Deviant - Email Not Found')

driver.get('https://www.adobe.com/uk/')
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div/header/nav/div[3]/div/ul/li[2]/div/ul/li/div/ul/li[3]/div/ul/li[2]/div/a')))
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div/header/nav/div[3]/div/ul/li[2]/div/ul/li/div/ul/li[3]/div/ul/li[2]/div/a').click()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="EmailPage-EmailField"]')))
    driver.find_element_by_xpath('//*[@id="EmailPage-EmailField"]').send_keys(email)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/section/section/section/div/section/div/section/section/form/section[2]/div[2]/button').click()
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/section/section/section/div/section/div/section/section/form/section[1]/label')))
        adobe_elemnt = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/section/section/div/section/div/section/section/form/section[1]/label')
        adobe_occupied = False
    except Exception as e:
        adobe_occupied = True
        errors.append('Adobe Timeout/ Element cannot be found anymore. Expected if account exists.')
except TimeoutException:
    errors.append('Adobe page has changed please look at page again and refactor code.')
if adobe_occupied:
    print(Fore.BLACK+Back.GREEN+'Adobe - Email Found')
else:
    print(Fore.BLACK+Back.RED+'Adobe - Email Not Found')

driver.get('https://www.playstation.com/en-gb/')  # chain event to sign up
driver.get('https://www.asda.com/login')  # status on login page.
driver.get('https://secure.tesco.com/account/en-GB/register')  # auto detect email registered
driver.get('https://account.bbc.com/account/tv')

print(Fore.BLACK+Back.RED+'Errors: '+str(errors))
driver.close()
driver.quit()
# Forgot to close and alot of background process Firefox windows were running
