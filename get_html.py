from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import random


def tern_on_vpn():
    server_number = random.randint(1, 48)
    server_name = f'us-free#{server_number}'
    proc = subprocess.Popen(
        f'protonvpn-cli c {server_name}',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    proc.wait()
    message = str(proc.stdout.read())
    print(message.split('\\n')[1])


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
    print(message.split('\\n\\n')[1])


def change_my_ip(func):
    def wrapper(*args, **kwargs):
        tern_on_vpn()
        result = func(*args, **kwargs)
        tern_off_vpn()
        return result
    return wrapper


@change_my_ip
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
