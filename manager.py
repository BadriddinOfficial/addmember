from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep

init()

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    # fancy logo
    b = [
    
"""\t🔰BADRIDDIN_OFFICIAL🔰*

  ____    _    ____  ____  ___ ____  ____ ___ _   _ 
 | __ )  / \  |  _ \|  _ \|_ _|  _ \|  _ \_ _| \ | |
 |  _ \ / _ \ | | | | |_) || || | | | | | | ||  \| |
 | |_) / ___ \| |_| |  _ < | || |_| | |_| | || |\  |
 |____/_/   \_\____/|_| \_\___|____/|____/___|_| \_|
   ___  _____ _____ ___ ____ ___    _    _          
  / _ \|  ___|  ___|_ _/ ___|_ _|  / \  | |         
 | | | | |_  | |_   | | |    | |  / _ \ | |         
 | |_| |  _| |  _|  | | |___ | | / ___ \| |___      
  \___/|_|   |_|   |___\____|___/_/   \_\_____|     
                                                    


\t +998 91 241 52 48"""

    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    #print('=============SON OF GENISYS==============')
    print(f'   Version: 1.3 | Yaratuvchi: @BADRIDDIN_OFFICIAL{n}\n')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(lg+'[1] Yangi Account qo‘shish'+n)
    print(lg+'[2] Spam Accountlarni aniqlash'+n)
    print(lg+'[3] Keraksiz Accountni o‘chirish'+n)
    print(lg+'[4] Dasturni yangilash'+n)
    print(lg+'[5] Chiqish'+n)
    a = int(input('\nKerakli bo‘limni raqam orqali tanlang: '))
    if a == 1:
        new_accs = []
        with open('vars.txt', 'ab') as g:
            number_to_add = int(input(f'\n{lg} [~] Accountlaringiz sonini kiriting: {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{lg} [~] Telefon raqamingizni kiriting: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{lg} [i] Barcha hisoblar saqlandi vars.txt')
            clr()
            print(f'\n{lg} [*] Yangi accountga kirish\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                c.start(number)
                print(f'{lg}[+] Muvaffaqiyatli kirildi!')
                c.disconnect()
            input(f'\n Asosiy menyuga qaytish uchun enterni bosing...')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] Sizda account yo‘q! Iltimos qaytaddan urunib ko‘ring')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Enter the code: '))
                        print(f'{lg}[+] {phone} bu accountingiz spam!{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' Spamm!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Tabriklaymiz! Accountlaringiz spam emas')
                input('\nAsosiy menyuga qaytish uchun enterni bosing...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] Barcha spamm accountingiz o‘chirildi!'+n)
                input('\nAsosiy menyuga qaytish uchun enterni bosing...')

    elif a == 3:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{lg}[i] O‘chirish uchun hisobni tanlang\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] Raqamni kiriting: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Hisobingiz o‘chirildj{n}')
        input(f'\nAsosiy menyuga qaytish uchun enterni bosing...')
        f.close()
    elif a == 4:
        # thanks to github.com/th3unkn0n for the snippet below
        print(f'\n{lg}[i] Yangilanish tekshirilmoqda...')
        try:
            # https://raw.githubusercontent.com/Cryptonian007/Astra/main/version.txt
            version = requests.get('https://github.com/BadriddinOfficial/addmember/main/version.txt')
        except:
            print(f'{r} Siz internetga ulanmagansiz!')
            print(f'{r} Internetga ulaning va qayta urunib ko‘ring')
            exit()
        if float(version.text) > 1.1:
            prompt = str(input(f'{lg}[~] Yangilanish mavjud[Version {version.text}]. Yuklansinmi?[h/y]: {r}'))
            if prompt == 'h' or prompt == 'ha' or prompt == 'H':
                print(f'{lg}[i] Yangilanish yuklab olinmoqda...')
                if os.name == 'nt':
                    os.system('del add.py')
                    os.system('del manager.py')
                else:
                    os.system('rm add.py')
                    os.system('rm manager.py')
                #os.system('del scraper.py')
                os.system('curl -l -O https://github.com/BadriddinOfficial/addmember/main/add.py')
                os.system('curl -l -O https://github.com/BadriddinOfficial/addmember/main/manager.py')
                print(f'{lg}[*] Versiya yangilangan: {version.text}')
                input('Chiqish uchun enterni bosing...')
                exit()
            else:
                print(f'{lg}[!] Yangilanish bekor qilindi.')
                input('Bosh menyuga qaytish uchun enterni bosing...')
        else:
            print(f'{lg}[i] Sizning dasturingiz allaqachon yangilangan')
            input('Asosiy menyuga qaytish uchun enterni bosing...')
    elif a == 5:
        clr()
        banner()
        exit()
