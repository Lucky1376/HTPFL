#Импортирование модулей
from termcolor import colored
import os
import sys
from time import sleep
from random import choice

#Баннер
os.system("clear")
def Banner():
	nt = (colored("HACK THE PANEL FROM LUCKY", "red"))
	r1 = (colored("     ###", "yellow"))
	r2 = (colored("###", "yellow"))
	print("")
	print(colored("     #################################", "yellow"))
	print(r1,nt,r2)
	print(colored("     #################################", "yellow"))
	print(colored("                For Android", "green"))
	print("")
	ist = (colored("[1]", "red"))
	ist3 = (colored("Sms Bomber", "green"))
	print(ist, ist3)
	print("")
	fah = (colored("[2]", "red"))
	fah2 = (colored("VPN For Termux", "blue"))
	print(fah, fah2)
	print("")
	pas = (colored("[3]", "red"))
	pas2 = (colored("Password Generator", "magenta"))
	print(pas, pas2)
	print("")
	ksy = colored("[99]", "red")
	ksy2 = colored("О Программе", "cyan")
	print(ksy, ksy2)
	print("")
	print("")
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
	elif numb == "99" or numb == "О программе":
		print("")
		name = colored("Lucky", "red")
		raz = colored("Разработчик -", "cyan")
		print(raz, name)
		vr = colored("0.1.3", "blue")
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
		sys.exit(0)
	elif numb != "1" or numb != "2" or numb != "99":
		print("")
		print(colored("ERROR", "red"))
		print("")
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
				
def Password():
	print("")
	pas = (colored("[1]", "cyan"))
	pas2 = (colored("start", "green"))
	print(pas, pas2)
	print("")
	print("")
	jsh = colored("[0]", "red")
	print(jsh, hsg)
	print("")
	Pas = input(colored(" —>> ", "red"))
	if Pas == "1" or Pas == "start":
		chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
		print("")
		numb = int(input(colored("Количество Паролей: ", "yellow")))
		len = int(input(colored("Длина Пароля(ей): ", "yellow")))
		numb = int(numb)
		len = int(len)
		for n in range(numb):
			password = " "
			for i in range(len):
				password += choice(chars)
			print("")
			rez1 = ("Рузультат:")
			print(colored(rez1,"red"),colored(password,"blue"))
			print("")
	elif Pas == "0" or Pas == "Назад":
		while True:
			os.system("clear")
			Banner()
			osnova()

#Ядро Кода
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
	elif numb == "3" or numb == "Password Generator":
		while True:
			Password()
	elif numb == "99" or numb == "О программе":
		print("")
		name = colored("Lucky", "red")
		raz = colored("Разработчик -", "cyan")
		print(raz, name)
		ja = colored("OS -", "cyan")
		ja2 = colored("Android", "green")
		print(ja, ja2)
		vr = colored("0.3.7https://github.com/Lucky1376/HTPFL", "blue")
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
		sys.exit(0)
	elif numb != "1" or numb != "2" or numb != "99":
		print("")
		print(colored("ERROR", "red"))
		print("")
		sys.exit(0)
osnova()
