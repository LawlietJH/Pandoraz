# -*- Coding: UTF-8 -*-
# Python 3

import os

Autor = "LawlietJH"
Version = "v1.0.0"

BSSIDs = []
Cont = 0
Cony = 0

Comando = "netsh wlan show networks mode=Bssid"
Cad = os.popen(Comando)
Cadena = Cad.read()
Lista = Cadena.split("\n")

for X in Lista:
	
	if "SSID" in X:
			X = X.split(" : ")[1]			
			BSSIDs.append(X)

for Y in BSSIDs:
	
		if Cont % 2 == 0:
			
			Cony += 1
			
			print("    [*] {} - ESSID: {}".format(Cony, Y), end="\t\t")
			
		else:
			print(" BSSID: {}".format(Y))
			
		Cont += 1
