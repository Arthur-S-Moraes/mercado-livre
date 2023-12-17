from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import random
import pyperclip
import pyautogui

codigo_produto = '0000789493406'
def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1920,1080','user-data-dir=C:\\Users\\Arthur23129\\AppData\\Local\\Google\\Chrome\\User Data\\Defalt']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver

driver = iniciar_driver()
driver.get('https://www.mercadolivre.com.br/')
continuar = pyautogui.prompt(text="digite N ou n para parar:")
while continuar != 'n' or continuar != 'N':
    driver.implicitly_wait(0.4)
    abas = driver.window_handles
    for aba in abas:
        driver.switch_to.window(aba)
        try:
            driver.find_element(By.XPATH, '//*[@id="sales_channel_task"]/div[2]/div[2]/button')
            print ('pagina certa')
            break
        except:
            print('pagina errada')
    
    placa = pyautogui.prompt(text="digite o modelo da placa:")
    shops = driver.find_elements(By.XPATH, "//*[@class='andes-checkbox andes-checkbox--default andes-checkbox--default']")
    falso = driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='mshops']")

    driver.implicitly_wait(5)
    falso = driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='mshops']").is_selected()
    if falso == True:
        shops[1].click()
    elif falso == False:
        pass
    sleep(1)
    confimar = driver.find_element(By.XPATH, '//button').click()
    sleep(1)

    try:
        driver.find_element(By.XPATH, '//*[@id="category_task"]/div[2]/div[2]/button').click() 
        sleep(random.uniform(2,5))
    except:
        pass
    
    try:
        driver.find_element(By.XPATH, '//*[@id="pks_task"]/div[2]/div[2]/button[1]').click() 
        sleep(random.uniform(2,5))
    except:
        pass
    
    novo = driver.find_element(By.ID, 'new')
    novo.click()
    sleep(random.uniform(2,5))

    confirmar_titulo = driver.find_element(By.XPATH, '//*[@id="title_task"]/div[2]/div[2]/button[1]/span')
    confirmar_titulo.click()
    sleep(random.uniform(2,5))

    pasta = 'C:\\Users\\Arthur23129\\Downloads\\pasta\\'
    driver.find_element(By.XPATH, '//*[@id="specifications_task"]/div[2]/div[2]/div/div/div/input').send_keys(f'{pasta}1.jpg \n {pasta}2.jpg \n {pasta}3.jpg \n {pasta}0.png')    
    sleep(random.uniform(2,5))

    driver.find_element(By.XPATH, '//*[@id="specifications_task"]/div[2]/div[4]/button[1]').click()
    sleep(random.uniform(2,5))

    textoCopiar = '0000789493406'
    pyperclip.copy(textoCopiar)
    driver.find_element(By.XPATH, '//*[@id="product_identifier_task"]/div[2]/div[1]/ul/li/div/div[1]/label/div/input').send_keys(Keys.CONTROL, 'v')

    sleep(random.uniform(0.5,3))
    driver.find_element(By.XPATH, '//*[@id="product_identifier_task"]/div[2]/div[2]/button[1]').click()
    sleep(random.uniform(1.5,4))
    pyperclip.copy(placa)
    try:
        modelo_de_placa = driver.find_element(By.XPATH, "//input[@name='Modelos de TV compatíveis']")
        modelo_de_placa.send_keys(Keys.CONTROL, 'v')
    except:
        modelo_de_placa = driver.find_element(By.XPATH, "//input[@name='COMPATIBLE_TV_MODEL']")
        modelo_de_placa.send_keys(Keys.CONTROL, 'v') 
    
    sleep(random.uniform(1.5,4))
    driver.find_element(By.XPATH, '//*[@id="technical_specifications_task"]/div[2]/div[2]/button[1]').click()

    ###### selecionar premium
    driver.implicitly_wait(180)

    premium = driver.find_element(By.XPATH, '//*[@id="listing_types_task"]/div[2]/div[2]/div[2]')
    sleep(random.uniform(2,5))
    premium.click()

    sleep(random.uniform(2,5))
    driver.find_element(By.XPATH, '//*[@id="listing_types_task"]/div[2]/div[3]/button[1]').click()
    sleep(random.uniform(2,5))

    driver.find_element(By.XPATH, '//*[@id="shipping_task"]/div[2]/div[2]/button').click()
    sleep(random.uniform(2,5))

    driver.find_element(By.XPATH, '//*[@id="localpickup_task"]/div[2]/div/ul/li[1]').click()
    sleep(random.uniform(2,5))

    driver.find_element(By.XPATH, '//*[@id="payment_methods_task"]/div[2]/div/button').click()
    sleep(random.uniform(2,5))

    opcoes = driver.find_elements(By.NAME, 'warrantyType')
    opcoes[2].click()

    sleep(random.uniform(0.5,3))
    opcoes[2].click()

    sleep(random.uniform(0.5,3))
    driver.find_element(By.XPATH, '//*[@id="warranty_task"]/div[2]/div[2]/button[1]').click()

    sleep(random.uniform(2,5))
    driver.find_element(By.XPATH, '//*[@id="description_task"]/div/div').click()

    sleep(random.uniform(2,5))
    textoCopiar = '''texto'''
    pyperclip.copy(textoCopiar)

    driver.find_element(By.XPATH, '//*[@id="description_task"]/div[2]/div[2]/label').send_keys(Keys.CONTROL, 'v')
    sleep(random.uniform(2,3))
    continuar = pyautogui.prompt(text="digite N ou n para parar:")
