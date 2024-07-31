from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib
import email.message
import time

# Função para obter o valor do BTC
def get_btc_value(driver):
    currency = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/section/div/div[2]/span"))
    )
    return currency.text

# Função para enviar o e-mail
def send_email(name, email_input, btc_value):
    corpo_email = f""" 
    <p> Dear, {name} </p>
    <p>Current BTC Value: {btc_value}</p>
    <p>If you need another kind of value you can ask on </p>
    <p>https://www.linkedin.com/in/leandro-frco/</p>
    <p> Best Regards. </p>
    <p>Leandro Ramos</p>
    """

    msg = email.message.Message()
    msg['Subject'] = 'BTC Value Update'  # Assunto do E-mail
    msg['From'] = 'contaparatestepython@gmail.com'  # E-mail que vai enviar
    msg['To'] = email_input
    password = 'xxxx xxxx xxxx xxxx'  # Senha para o "App passwords of Google"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')  # Configuração do SMTP
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    s.quit()

# Função principal
def main():
    name = "Leandro"
    email_input = "leandro.tominay@gmail.com"

    # Configurações do Selenium para obter o valor do BTC
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('--headless')
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://coinmarketcap.com/currencies/bitcoin/")

    try:
        while True:
            # Obter o valor atual do BTC
            btc_value = get_btc_value(driver)
            # Enviar e-mail com o valor do BTC
            send_email(name, email_input, btc_value)
            print(f"Sent email with BTC value: {btc_value}")
            time.sleep(30)  # Esperar 30 segundos antes de atualizar
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

