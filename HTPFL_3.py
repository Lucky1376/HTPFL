# Импортирование модулей
from termcolor import colored
import os
import sys
from time import sleep
from random import choice, randint

# Баннер
os.system("clear")


def Banner():
    color = ["red", "blue", "yellow", "green", "cyan", "magenta"]
    color2 = choice(color)
    Banner = '''  _    _ _______ _____  ______ _
 | |  | |__   __|  __ \|  ____| |
 | |__| |  | |  | |__) | |__  | |
 |  __  |  | |  |  ___/|  __| | |
 | |  | |  | |  | |    | |    | |____
 |_|  |_|  |_|  |_|    |_|    |______| '''
    print(colored(Banner, color2))
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
    ist3 = (colored("Sms Bomber", "green"))
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
    ksy = colored("[99]", "red")
    ksy2 = colored("О Программе", "cyan")
    print(ksy, ksy2)
    print("")
    print("")
    upd = colored("[Upd]", "red")
    upd2 = colored("Обновить", "green")
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


# Функции
def osnova():
    global numb
    numb = (input(colored(" —>> ", "red")))
    if numb == "1" or numb == "Sms Bomber":
        print("")
        st = colored("start", "green")
        st2 = colored("[2]", "cyan")
        # --
        ex = colored("Назад", "red")
        ex2 = colored("[0]", "red")
        # --
        up = colored("download modules", "yellow")
        up2 = colored("[1]", "cyan")

        print(up2, up)
        print(st2, st)

        print("")
        print("")
        print(ex2, ex)
        print("")
        q = input(colored(" —>> ", "red"))
        if q == "download modules" or q == "1":
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
        elif q == "2" or q == "start":
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
            time = colored("", RandColor)
            # --
            RandNumb2 = randint(3, 200)

            print("PHONE -", ColorPHONE)
            print("Время -", RandNumb + "сек")
            print("Мощность - От 3-200")
            print("")
            sleep(1.3)
            PHONE - input(colored(" PHONE >> ", "red"))
            time - input(colored(" Время >> ", "red"))
            threads - input(colored(" Мощность >> ", "red"))
            print("")
            print(colored("Хотите начать спам через опредленое время или сразу?", "yellow"))
            print(colored("Если через определнное время, укажите его в секундах", "green"))
            print(colored("Если сразу напишите 0", "green"))
            print("")
            okey = input(colored(" —>> ", "red"))

            if okey == "0":
                os.system("cd % && python impulse.py --target " + PHONE + " --method SMS --time " + time + " --threads " + threads)
            elif okey < "0":
                print("")
                bol = colored("БОЛЬНОЙ??", "red")
                print("Ты " + bol)
                print("")
                sleep(1.1)
                sys.exit(0)
            else:
                sleep(okey)
                os.system(
                    "cd % && python impulse.py --target " + PHONE + " --method SMS --time " + time + " --threads " + threads)
        else:
            os.system("clear")
            while True:
                Banner()
                osnova()
    elif numb == "2" or numb == "VPN For Termux":
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
            print(colored("Запуск VPN начнётся через 12с 	после выбора пункта", "green"))
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
    elif numb == "3" or numb == "Ddos For Wi-Fi":
        print("")
        print(colored("В разработке...", "green"))
        print("")
        sleep(1.1)
        os.system("clear")
        while True:
            Banner()
            osnova()
    elif numb == "4" or numb == "UrlPhish":
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
    elif numb == "Upd" or numb == "upd" or numb == "Обновить":
        print("")
        upds = colored("[1]", "cyan")
        upds2 = colored("start", "green")
        print(upds, upds2)
        print("")
        print("")
        nz = colored("[0]", "red")
        nz2 = colored("Назад", "red")
        print(nz, nz2)
        print("")
        upd = input(colored(" —>> ", "red"))
        if upd == "1" or upd == "start":
            os.system(
                "cd && rm -rf HTPFL && git clone https://github.com/Lucky1376/HTPFL && cd HTPFL && python HTPFL.py")
        elif upd == "0" or upd == "Назад":
            while True:
                Banner()
                osnova()
        else:
            os.system("clear")
            print("")
            print(colored("Нет такого пункта!", "red"))
            print("")
            sys.exit(0)
    elif numb == "99" or numb == "О программе":
        print("")
        name = colored("Lucky", "red")
        raz = colored("Разработчик -", "cyan")
        print(raz, name)
        vr = colored("0.3.9", "blue")
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
    elif numb != "1" or numb != "2" or numb != "99":
        os.system("clear")
        print("")
        print(colored("ERROR", "red"))
        print("")
        sys.exit(0)


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


def Bomb():
    print("")
    st = colored("start", "green")
    st2 = colored("[2]", "cyan")
    # --
    ex = colored("Назад", "red")
    ex2 = colored("[0]", "red")
    # --
    up = colored("download modules", "yellow")
    up2 = colored("[1]", "cyan")

    print(up2, up)
    print(st2, st)

    print("")
    print("")
    print(ex2, ex)
    print("")
    q = input(colored(" —>> ", "red"))
    if q == "download modules" or q == "1":
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
    elif q == "2" or q == "start":
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
        time = colored("", RandColor)
        # --
        RandNumb2 = randint(3, 200)

        print("PHONE -", ColorPHONE)
        print("Время -", str(RandNumb) + "сек")
        print("Мощность - От 3-200")
        print("")
        sleep(1.3)
        PHONE - input(colored(" PHONE >> ", "red"))
        time - input(colored(" Время >> ", "red"))
        threads - input(colored(" Мощность >> ", "red"))
        print("")
        print(colored("Хотите начать спам через опредленое время или сразу?", "yellow"))
        print(colored("Если через определнное время, укажите его в секундах", "green"))
        print(colored("Если сразу напишите 0", "green"))
        print("")
        okey = input(colored(" —>> ", "red"))

        if okey == "0":
            os.system(
                "cd % && python impulse.py --target " + PHONE + " --method SMS --time " + time + " --threads " + threads)
        elif okey < "0":
            print("")
            bol = colored("БОЛЬНОЙ??", "red")
            print("Ты " + bol)
            print("")
            sleep(1.1)
            sys.exit(0)
        else:
            sleep(okey)
            os.system(
                "cd % && python impulse.py --target " + PHONE + " --method SMS --time " + time + " --threads " + threads)
    else:
        os.system("clear")
        while True:
            Banner()
            osnova()


# Ядро Кода
numb = (input(colored(" —>> ", "red")))
if numb == "1" or numb == "Sms Bomber":
    while True:
        Bomb()
elif numb == "2" or numb == "VPN For Termux":
    while True:
        RVpn()
elif numb == "3" or numb == "Ddos For Wi-Fi":
    print("")
    print(colored("В разработке", "green"))
    print("")
    sleep(1.1)
    os.system("clear")
    while True:
        Banner()
        osnova()
elif numb == "4" or numb == "UrlPhish":
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
            os.system("clear")
            Banner()
            osnova()
elif numb == "Upd" or numb == "upd" or numb == "Обновить":
    print("")
    upds = colored("[1]", "cyan")
    upds2 = colored("start", "green")
    print(upds, upds2)
    print("")
    print("")
    nz = colored("[0]", "red")
    nz2 = colored("Назад", "red")
    print(nz, nz2)
    print("")
    upd = input(colored(" —>> ", "red"))
    if upd == "1" or upd == "start":
        os.system("cd && rm -rf HTPFL && git clone https://github.com/Lucky1376/HTPFL && cd HTPFL && python HTPFL.py")
    elif upd == "0" or upd == "Назад":
        while True:
            os.system("clear")
            Banner()
            osnova()
    else:
        os.system("clear")
        print("")
        print(colored("Нет такого пункта!", "red"))
        print("")
        sys.exit(0)
elif numb == "99" or numb == "О программе":
    print("")
    name = colored("Lucky", "red")
    raz = colored("Разработчик -", "cyan")
    print(raz, name)
    ja = colored("OS -", "cyan")
    ja2 = colored("Android", "green")
    print(ja, ja2)
    vr = colored("0.3.9", "blue")
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
elif numb != "1" or numb != "2" or numb != "99":
    os.system("clear")
    print("")
    print(colored("ERROR", "red"))
    print("")
    sys.exit(0)
