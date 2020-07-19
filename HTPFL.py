#Импортирование модулей
from termcolor import colored
import os
import sys
from time import sleep
from random import choice

#Баннер
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
	ist = (colored("[1]", "red"))
	ist3 = (colored("Sms Bomber", "green"))
	print(ist, ist3)
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

#Списки
by = ["Всего доброго!", "Досвидания!", "Удачи!", "Пока!", "До встречи!"]
by2 = choice(by)

#Переменный для ядра
grf = (colored("[1]", "cyan"))
grf2 = (colored("[2]", "cyan"))
grf3 = (colored("download", "yellow"))
grf4 = (colored("start", "green"))
hsg = (colored("Назад", "red"))

#Функции
def  osnova():
	global numb
	numb = (input(colored(" —>> ", "red")))
	if numb == "1" or numb =="Sms Bomber":
		print("")
		szh2 = colored("Updates", "green")
		shz = colored("Check for", "blue")
		print(grf, shz, szh2)
		print(grf2, grf4)
		print("")
		print("")
		jsh = (colored("[0]", "red"))
		print(jsh, hsg)
		print("")
		sms = input(colored(" —>> ", "red"))
		print("")
		if sms == "1" or sms == "Chek for Updates":
			print("")
			print(colored("Для проверки обновления напишите разработчику", "yellow"))
			print("")
			sleep(2.5)
			vk = colored("https://m.vk.com/id554311036", "magenta")
			vko = colored("VK -", "blue")
			print(vko, vk)
			tg = colored("https://t.me/Lucky1376", "cyan" )
			tgo = colored("Telegram -", "blue")
			print(tgo, tg)
			print("")
			print("")
			jsh = (colored("[0]", "red"))
			print(jsh, hsg)
			print("")
			sms2 = input(colored(" —>> ", "red"))
			print("")
			if sms2 == "0" or sms2 == "Назад":
				while True:
					Bomb()
		elif sms == "2" or sms == "start":
			os.system("python %.py")
		elif sms == "0" or sms == "Назад":
			while True:
				os.system("clear")
				Banner()
				osnova()
	elif numb == "2" or numb == "VPN For Termux":
		print("")
		print(grf, grf3)
		print(grf2, grf4)
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
			os.system("pkg install tor")
			print("")
			print(colored("Complete!", "green"))
			print("")
			while True:
				RVpn()
		elif vpn == "2" or vpn == "start":
			print("")
			print(colored("Запуск VPN начнётся через 12с после выбора пункта", "green"))
			print("")
			print(colored("Когда на экране у опредленной строки 'Bootstrapped' будет значение 100%, тогда можно будет использовать другие утилиты, обязательно в новой сессии, для того чтобы остановить введите 'Ctrl + C", "yellow"))
			print("")
			sleep(12)
			os.system("tor")
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
		tg = colored("https://t.me/Lucky1376", "cyan" )
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
		os.system("cd && ls")
		sys.exit(0)
	elif numb != "1" or numb != "2" or numb != "99":
		os.system("clear")
		print("")
		print(colored("ERROR", "red"))
		print("")
		os.system("cd && ls")
		sys.exit(0)

def RVpn():
	print("")
	print(grf, grf3)
	print(grf2, grf4)
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
		os.system("pkg install tor")
		print("")
		print(colored("Complete!", "green"))
		print("")
	elif vpn == "2" or vpn == "start":
		print("")
		print(colored("Запуск VPN начнётся через 12с после выбора пункта", "green"))
		print("")
		print(colored("Когда на экране у опредленной строки 'Bootstrapped' будет значение 100%, тогда можно будет использовать другие утилиты, обязательно в новой сессии, для того чтобы остановить введите 'Ctrl + C", "yellow"))
		print("")
		sleep(12)
		os.system("tor")
	elif vpn == "0" or vpn == "Назад":
		while True:
			os.system("clear")
			Banner()
			osnova()
			
def Bomb():
		print("")
		szh2 = colored("Updates", "green")
		shz = colored("Check for", "blue")
		print(grf, shz, szh2)
		print(grf2, grf4)
		print("")
		print("")
		jsh = (colored("[0]", "red"))
		print(jsh, hsg)
		print("")
		sms = input(colored(" —>> ", "red"))
		print("")
		if sms == "1" or sms == "Chek for Updates":
			print("")
			print(colored("Для проверки обновления напишите разработчику", "yellow"))
			print("")
			sleep(2.5)
			vk = colored("https://m.vk.com/id554311036", "magenta")
			vko = colored("VK -", "blue")
			print(vko, vk)
			tg = colored("https://t.me/Lucky1376", "cyan" )
			tgo = colored("Telegram -", "blue")
			print(tgo, tg)
			print("")
			print("")
			jsh = (colored("[0]", "red"))
			print(jsh, hsg)
			print("")
			sms2 = input(colored(" —>> ", "red"))
			print("")
			if sms2 == "0" or sms2 == "Назад":
				while True:
					Bomb()
		elif sms == "2" or sms == "start":
			os.system("python %.py")
		elif sms == "0" or sms == "Назад":
			while True:
				os.system("clear")
				Banner()
				osnova()


#Ядро Кода
numb = (input(colored(" —>> ", "red")))
if numb == "1" or numb =="Sms Bomber":
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
	tg = colored("https://t.me/Lucky1376", "cyan" )
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
	os.system("cd && ls")
	sys.exit(0)
elif numb != "1" or numb != "2" or numb != "99":
	os.system("clear")
	print("")
	print(colored("ERROR", "red"))
	print("")
	os.system("cd && ls")
	sys.exit(0)
