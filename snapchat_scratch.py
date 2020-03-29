

driver.get('https://accounts.snapchat.com/accounts/login')
try:
    print('Found Page')
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="username"]')))
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.ENTER)
    print('Filled Form')
    try:
        sleep(2)
        print('Waiting For Element')
        WebDriverWait(driver, delay).until(EC.presence_of_element_located(
            (By.XPATH,
             '//*[@id="error_message"]')))  # main problem is it cant find this div element eventhough it is present, maybe it is present but attributes are different...
        print('Tag')
        tag = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/article/div[1]//p')
        print(tag.text)
        if tag.text == "That's not the right password.":
            snapchat_occupied = True
        elif tag.text == 'Cannot find user.':
            snapchat_occupied = False
    except Exception as e:
        errors.append('Snapchat Timeout/ Element cannot be found anymore. LOOK AT SNAPCHAT LOGIN HTML CODE')
except TimeoutException:
    errors.append('Snapchat page has changed please look at page again and refactor code.')
if snapchat_occupied:
    print(Fore.BLACK+Back.GREEN+'Snapchat - Email Found')
else:
    print(Fore.BLACK+Back.RED+'Snapchat - Email Not Found')


