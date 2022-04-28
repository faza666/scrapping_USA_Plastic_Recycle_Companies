from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import random


def switch_ip():
    proc = subprocess.Popen(
        'protonvpn-cli c -rp TCP',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    proc.wait()
    proxy_name = str(proc.stdout.read())
    print(proxy_name.split('\\n')[1])


def tern_off_vpn():
    proc = subprocess.Popen(
        'protonvpn-cli d',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    proc.wait()
    message = str(proc.stdout.read())
    print(message)


def get_html_page(url):
    with open('user-agents.txt') as file:
        ua_list = file.readlines()
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--headless')
    options.add_argument(f'user-agent={random.choice(ua_list)}')

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    try:
        driver.get(url=url)
        driver.implicitly_wait(20)
        html_page = driver.page_source
        driver.close()
        return html_page
    except Exception as ex:
        print(ex)
        return None
