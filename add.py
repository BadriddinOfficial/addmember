from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel, ChannelParticipantsSearch
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, PhoneNumberBannedError, ChatAdminRequiredError
from telethon.errors.rpcerrorlist import ChatWriteForbiddenError, UserBannedInChannelError, UserAlreadyParticipantError, FloodWaitError
from telethon.tl.functions.channels import InviteToChannelRequest, GetParticipantsRequest
import sys
from telethon.tl.functions.messages import ImportChatInviteRequest, AddChatUserRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import UserStatusRecently
import time
import random
from colorama import init, Fore
import os
import pickle


init()


r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
grey = '\033[97m'
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = lg + '[' + w + 'i' + lg + ']' + rs
error = lg + '[' + r + '!' + lg + ']' + rs
success = w + '[' + lg + '*' + w + ']' + rs
INPUT = lg + '[' + cy + '~' + lg + ']' + rs
plus = w + '[' + lg + '+' + w + ']' + rs
minus = w + '[' + lg + '-' + w + ']' + rs

def banner():
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
        print(f'{random.choice(colors)}{char}{rs}')
    #print('=============SON OF GENISYS==============')
    print(f'{lg}   Version: {w}1.3{lg} | Yaratuvchi: {w}@BADRIDDIN_OFFICIAL{rs}\n')


# function to clear screen
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

accounts = []
f = open('vars.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break

# create sessions(if any) and check for any banned accounts
# TODO: Remove code input(just to check if an account is banned)
print('\n' + info + lg + ' Accountlarni tekshirish...' + rs)
for a in accounts:
    phn = a[0]
    print(f'{plus}{grey} Tekshirilmoqda {lg}{phn}')
    clnt = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
    clnt.connect()
    banned = []
    if not clnt.is_user_authorized():
        try:
            clnt.send_code_request(phn)
            print('OK')
        except PhoneNumberBannedError:
            print(f'{error} {w}{phn} {r}Spamm!{rs}')
            banned.append(a)
    for z in banned:
        accounts.remove(z)
        print(info+lg+' Spam account olib tashlandi[manager.py orqali butunlay olib tashlang]'+rs)
    time.sleep(0.5)
    clnt.disconnect()


print(info+' Azolar nusxalanmoqda!')
clr()
banner()
# func to log scraping details(link of the grp to scrape
# and current index) in order to resume later
def log_status(scraped, index):
    with open('status.dat', 'wb') as f:
        pickle.dump([scraped, int(index)], f)
        f.close()
    print(f'{info}{lg} Azolar saqlandi {w}status.dat{lg}')
    

def exit_window():
    input(f'\n{cy} Chiqish uchun Enter tugmasini bosing...')
    clr()
    banner()
    sys.exit()

# read user details
try:
    # rquest to resume adding
    with open('status.dat', 'rb') as f:
        status = pickle.load(f)
        f.close()
        lol = input(f'{INPUT}{cy} Azolarni qidirish davom ettirilsinmi {w}{status[0]}{lg}? [h/y]: {r}')
        if 'h' in lol:
            scraped_grp = status[0] ; index = int(status[1])
        else:
            if os.name == 'nt': 
                os.system('del status.dat')
            else: 
                os.system('rm status.dat')
            scraped_grp = input(f'{INPUT}{cy} Ommaviy/Shaxsiy guruh azolarini ko‘chirish: {r}')
            index = 0
except:
    scraped_grp = input(f'{INPUT}{cy} Ommaviy/Shaxsiy guruh azolarini ko‘chirish: {r}')
    index = 0
# load all the accounts(phonenumbers)
accounts = []
f = open('vars.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break

print(f'{info}{lg} Jami hisoblar: {w}{len(accounts)}')
number_of_accs = int(input(f'{INPUT}{cy} Foydalanish uchun hisoblar sonini kiriting: {r}'))
print(f'{info}{cy} Variantni tanlang{lg}')
print(f'{cy}[1]{lg} Ommaviy guruhga qo‘shish')
print(f'{cy}[2]{lg} Shaxsiy guruhga qo‘shish')
choice = int(input(f'{INPUT}{cy} Tanlovni kiriting: {r}'))
if choice == 0:
    target = str(input(f'{INPUT}{cy} Ommaviy guruh havolasini kiriting: {r}'))
else:
    target = str(input(f'{INPUT}{cy} Shaxsiy guruh havolasini kiriting: {r}'))
print(f'{grey}_'*50)
#status_choice = str(input(f'{INPUT}{cy} Do you wanna add active members?[y/n]: {r}'))
to_use = [x for x in accounts[:number_of_accs]]
for l in to_use: accounts.remove(l)
with open('vars.txt', 'wb') as f:
    for a in accounts:
        pickle.dump(a, f)
    for ab in to_use:
        pickle.dump(ab, f)
    f.close()
sleep_time = int(input(f'{INPUT}{cy} Har bir qo‘shish uchun kechiktirish vaqtini kiriting{w}[{lg}0 for None{w}]: {r}'))
#print(f'{info}{lg} Joining group from {w}{number_of_accs} accounts...')
#print(f'{grey}-'*50)
print(f'{success}{lg} -- Azolar qo‘shilmoqds {w}{len(to_use)}{lg} account(s) --')
adding_status = 0
approx_members_count = 0
for acc in to_use:
    stop = index + 60
    c = TelegramClient(f'sessions/{acc[0]}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
    print(f'{plus}{grey} Foydalanuvchi: {cy}{acc[0]}{lg} -- {cy}Jarayon boshlanmoqda... ')
    c.start(acc[0])
    acc_name = c.get_me().first_name
    try:
        if '/joinchat/' in scraped_grp:
            g_hash = scraped_grp.split('/joinchat/')[1]
            try:
                c(ImportChatInviteRequest(g_hash))
                print(f'{plus}{grey} Foydalanuvchi: {cy}{acc_name}{lg} -- Bazaga qo‘shildi')
            except UserAlreadyParticipantError:
                pass 
        else:
            c(JoinChannelRequest(scraped_grp))
            print(f'{plus}{grey} Foydalanuvchj {cy}{acc_name}{lg} -- Bazaga qo‘shildi')
        scraped_grp_entity = c.get_entity(scraped_grp)
        if choice == 0:
            c(JoinChannelRequest(target))
            print(f'{plus}{grey} Foydalanuvchi: {cy}{acc_name}{lg} -- Guruhga qo‘shildi')
            target_entity = c.get_entity(target)
            target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
        else:
            try:
                grp_hash = target.split('/joinchat/')[1]
                c(ImportChatInviteRequest(grp_hash))
                print(f'{plus}{grey} Foydalanuvchi: {cy}{acc_name}{lg} -- Guruhga qo‘shildi')
            except UserAlreadyParticipantError:
                pass
            target_entity = c.get_entity(target)
            target_details = target_entity
    except Exception as e:
        print(f'{error}{r} Foydalanuvchi: {cy}{acc_name}{lg} -- Guruhga qo‘shib bo‘lmadi')
        print(f'{error} {r}{e}')
        continue
    print(f'{plus}{grey} Foydalanuvchi: {cy}{acc_name}{lg} -- {cy}Ob‘ektlarni olish‌‌...')
    #c.get_dialogs()
    try:
        members = []
        while_condition = True
        my_filter = ChannelParticipantsSearch('')
        offset = 0
        i = 1
        while while_condition:
            participants = c(GetParticipantsRequest(channel=scraped_grp,  offset= offset, filter = my_filter, limit=200, hash=0))
            members.extend(participants.users)
            offset += len(participants.users)
            members += (participants.users)
            if len(participants.users) < 1 :
                while_condition = False
    except Exception as e:
        print(f'{error}{r} Azolarni ko‘chirib bo‘lmadi')
        print(f'{error}{r} {e}')
        continue
    approx_members_count = len(members)
    assert approx_members_count != 0
    if index >= approx_members_count:
        print(f'{error}{lg} Qo‘shiladigan azolar yo‘q!')
        continue
    print(f'{info}{lg} Boshlash: {w}{index}')
    #adding_status = 0
    peer_flood_status = 0
    for user in members[index:stop]:
        index += 1
        if peer_flood_status == 10:
            print(f'{error}{r} Flood xatolari juda ko‘p! Seansni yakunlash‌‌...')
            break
        try:
            if choice == 0:
                c(InviteToChannelRequest(target_details, [user]))
            else:
                c(AddChatUserRequest(target_details.id, user, 42))
            user_id = user.first_name
            target_title = target_entity.title
            print(f'{plus}{grey} Foydalanuvchi: {cy}{acc_name}{lg} -- {cy}{user_id} {lg}--> {cy}{target_title}')
            #print(f'{info}{grey} User: {cy}{acc_name}{lg} -- Sleep 1 second')
            adding_status += 1
            print(f'{info}{grey} Foydalanuvchi: {cy}{acc_name}{lg} -- Qo‘shish {w}{sleep_time} {lg}sekund(s)')
            time.sleep(sleep_time)
        except UserPrivacyRestrictedError:
            print(f'{minus}{grey} User: {cy}{acc_name}{lg} -- {r}Foydalanuvchida maxfiylik sozlamalari yoqilganligi sababli qo‘shib bo‘lmadi!')
            continue
        except PeerFloodError:
            print(f'{error}{grey} Foydalanuvchi: {cy}{acc_name}{lg} -- {r}2-4sekund kuting.')
            peer_flood_status += 1
            continue
        except ChatWriteForbiddenError:
            print(f'{error}{r} Azo qo‘shish ruxsati o‘chirib qo‘yilgan. A‘zolar qo‘shishni yoqish uchun guruh administratori bilan bog‘laning‌‌')
            if index < approx_members_count:
                log_status(scraped_grp, index)
            exit_window()
        except UserBannedInChannelError:
            print(f'{error}{grey} Foydalanuvchi: {cy}{acc_name}{lg} -- {r}Guruhlarda yozish taqiqlangan‌‌')
            break
        except ChatAdminRequiredError:
            print(f'{error}{grey} Foydalanuvchi: {cy}{acc_name}{lg} -- {r}Qo‘shish uchun chat administratori huquqlari kerak‌‌')
            continue
        except UserAlreadyParticipantError:
            print(f'{minus}{grey} Foydalanuvchi: {cy}{acc_name}{lg} -- {r}Foydalanuvchi guruhda allaqachon mavjud')
            continue
        except FloodWaitError as e:
            print(f'{error}{r} {e}')
            break
        except ValueError:
            print(f'{error}{r} Xatolik yuz berdi')
            continue
        except KeyboardInterrupt:
            print(f'{error}{r} ---- Qo‘shish tugatildi ----')
            if index < len(members):
                log_status(scraped_grp, index)
            exit_window()
        except Exception as e:
            print(f'{error} {e}')
            continue
#global adding_status, approx_members_count
if adding_status != 0:
    print(f"\n{info}{lg} Jarayon yakunlandi")
try:
    if index < approx_members_count:
        log_status(scraped_grp, index)
        exit_window()
except:
    exit_window()
