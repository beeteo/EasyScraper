import datetime 
import os
import ctypes
try:
    import requests
except: 
    pass
try:
    from console.utils import set_title
except:
    pass
try:
    from colorama import Fore, init
    init()
except:
    pass

date = datetime.datetime.today()
month = date.month
day = date.day
year = date.year

hour = date.hour
minutes = date.minute
seconds = date.second

http = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'
socks4 = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all'
socks5 = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all'

text = r'''
{}  _____                ____                            
{} | ____|__ _ ___ _   _/ ___|  ___ _ __ __ _ _ __   ___ 
{} |  _| / _` / __| | | \___ \ / __| '__/ _` | '_ \ / _ \
{} | |__| (_| \__ \ |_| |___) | (__| | | (_| | |_) |  __/
{} |_____\__,_|___/\__, |____/ \___|_|  \__,_| .__/ \___|
{}                 |___/                     |_|    
{}'''.format(Fore.LIGHTMAGENTA_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTMAGENTA_EX, Fore.MAGENTA, Fore.MAGENTA, Fore.MAGENTA, Fore.RESET)

class Scraper:
    def __init__(self, scrape):
        self.scrape = scrape

    def HTTPScraper():
        https = requests.get(http).text
        try:
            with open(f'Results/HTTP-{month}-{day}-{year}-{hour}-{minutes}-{seconds}.txt', 'w') as txt_file:
                for line in https.split('\n'):
                    txt_file.write(line)
                print(f' [{Fore.LIGHTMAGENTA_EX}+{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}{(https)}{Fore.WHITE} Proxy scraped {Fore.LIGHTMAGENTA_EX}-{Fore.WHITE} Type: {Fore.LIGHTCYAN_EX}HTTP/s{Fore.RESET}')
                os.system('pause>nul')
        except:
            os.mkdir('Results')
            with open(f'Results/HTTP-{month}-{day}-{year}-{hour}-{minutes}-{seconds}.txt', 'w') as txt_file:
                for line in https.split('\n'):
                    txt_file.write(line)
                print(f' [{Fore.LIGHTMAGENTA_EX}+{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}{len(https)}{Fore.WHITE} Proxy scraped {Fore.LIGHTMAGENTA_EX}-{Fore.WHITE} Type: {Fore.LIGHTCYAN_EX}HTTP/s{Fore.RESET}')
                os.system('pause>nul')

    def SOCKS4Scraper():
        https = requests.get(socks4).text
        try:
            with open(f'Results/SOCKS4-{month}-{day}-{year}-{hour}-{minutes}-{seconds}.txt', 'w') as txt_file:
                for line in https.split('\n'):
                    txt_file.write(line)
                print(f' [{Fore.LIGHTMAGENTA_EX}+{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}{len(https)}{Fore.WHITE} Proxy scraped {Fore.LIGHTMAGENTA_EX}-{Fore.WHITE} Type: {Fore.LIGHTCYAN_EX}SOCKS4{Fore.RESET}')
                os.system('pause>nul')
        except:
            os.mkdir('Results')
            with open(f'Results/SOCKS4-{month}-{day}-{year}-{hour}-{minutes}-{seconds}.txt', 'w') as txt_file:
                for line in https.split('\n'):
                    txt_file.write(line)
                print(f' [{Fore.LIGHTMAGENTA_EX}+{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}{len(https)}{Fore.WHITE} Proxy scraped {Fore.LIGHTMAGENTA_EX}-{Fore.WHITE} Type: {Fore.LIGHTCYAN_EX}SOCKS4{Fore.RESET}')
                os.system('pause>nul')

    def SOCKS5Scraper():
        https = requests.get(socks4).text
        try:
            with open(f'Results/SOCKS5-{month}-{day}-{year}-{hour}-{minutes}-{seconds}.txt', 'w') as txt_file:
                for line in https.split('\n'):
                    txt_file.write(line)
                print(f' [{Fore.LIGHTMAGENTA_EX}+{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}{len(https)}{Fore.WHITE} Proxy scraped {Fore.LIGHTMAGENTA_EX}-{Fore.WHITE} Type: {Fore.LIGHTCYAN_EX}SOCKS5{Fore.RESET}')
                os.system('pause>nul')
        except:
            os.mkdir('Results')
            with open(f'Results/SOCKS5-{month}-{day}-{year}-{hour}-{minutes}-{seconds}.txt', 'w') as txt_file:
                for line in https.split('\n'):
                    txt_file.write(line)
                print(f' [{Fore.LIGHTMAGENTA_EX}+{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}{len(https)}{Fore.WHITE} Proxy scraped {Fore.LIGHTMAGENTA_EX}-{Fore.WHITE} Type: {Fore.LIGHTCYAN_EX}SOCKS5{Fore.RESET}')
                os.system('pause>nul')

if __name__ == '__main__':
    set_title('EasyScrape - Main Menu.')
    print(text)
    print(f' [{Fore.LIGHTMAGENTA_EX}-{Fore.WHITE}] What kind of proxies do you want to scrape?{Fore.RESET}\n\n')
    print(f' [{Fore.LIGHTMAGENTA_EX}1{Fore.WHITE}] HTTP/HTTPS{Fore.RESET}')
    print(f' [{Fore.LIGHTMAGENTA_EX}2{Fore.WHITE}] SOCKS4{Fore.RESET}')
    print(f' [{Fore.LIGHTMAGENTA_EX}3{Fore.WHITE}] SOCKS5{Fore.RESET}')
    print(f'\n [{Fore.LIGHTMAGENTA_EX}!{Fore.WHITE}] Input: ', end='')
    scraper = input('')

    if (scraper) == '1':
        Scraper.HTTPScraper()
    elif (scraper) == '2':
        Scraper.SOCKS4Scraper()
    elif (scraper) == '3':
        Scraper.SOCKS5Scraper()