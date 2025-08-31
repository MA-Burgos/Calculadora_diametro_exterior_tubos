#!/usr/bin/env python3
#
#  funCables.py
#  
#  Copyright 2025 Miguel Ángel Burgos <Miguel.Angel.B@gmx.es>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import os
import sys
import math
from colorama import init,Fore,Back,Style

if sys.platform.startswith('win'):
    import msvcrt
    def get_key():
        return msvcrt.getch().decode('utf-8', errors='ignore')
else:
    import tty
    import termios
    def get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

def gotoxy(x, y):
    print(f"\033[{y};{x}H", end='')


def SeccionNorm ():
	# Pide seccioenes y comprueba que la sección introducida es correcta de ser
	# correcta devuelve dos valores el limite superior del aislante y la sección
	# introducida
	seccCable = [(1.5, 3.4),
	(2.5, 4.1),
	(4, 4.8),
	(6, 5.3),
	(10, 6.8),
	(16, 8.1),
	(25, 10.2),
	(35, 11.7),
	(50, 13.9),
	(70, 16),
	(95, 18.2),
	(120, 20.2),
	(150, 22.5),
	(185, 24.9),
	(240, 28.4)
	]
	while True:
		try:
			print(Fore.YELLOW + Style.BRIGHT)
			valor = float(input("Introduce la sección nominal de los conductores: "))
		except ValueError:
			print ("Valor introducido invalido")
			continue # vuelve a pedir el dato
			
		encontrado = False
		for par in seccCable:
			if valor == par[0]:
				print(f"Sección introducida {valor} es correcta")
				print(f"Límite superior del aislante: {par[1]}")
				encontrado = True
				break
		
		if encontrado:
			return valor, par[1]  # Devuelve ambos valores y sale de la función
		else:
			print("Sección no encontrada. Inténtalo de nuevo.")	

def NumconducTubo():
	correcto = False
	while True:
		try:
			print (Fore.BLUE + Style.BRIGHT)
			nconducores = int(input("Número de conductores que discurren por el tubo: "))
			if nconducores <= 0:
				raise ValueError("El número debe ser mayor que cero.")
			correcto = True
			break
		except ValueError:
			print ("Valor introducido invalido")
			continue # vuelve a pedir el dato
	if correcto:
		return nconducores

def FactorCorreccionTubo():
# Factores de Corrección }
	FC_FIJAS_EN_SUPERFICIE = 2.5;
	FC_EMPOTRADAS = 3;
	FC_AREASOTUBOSALAIRE = 4;
	FC_CANALIZACIONESENTERRADAS = 4;
	print (Fore.MAGENTA + Style.BRIGHT + "\nFactor de la correción de la instalación\n"+Style.RESET_ALL)
	print (Fore.CYAN + Style.BRIGHT + "Montaje fijo en la superficie: ", end="")
	print (Fore.WHITE + Style.BRIGHT + "los tubos van fijados en las pareces o techos por medio de abrazaderas.\n")
	print (Fore.CYAN + Style.BRIGHT + "Montaje fijo empotrado: ",end="")
	print (Fore.WHITE + Style.BRIGHT + "los tubos están en el interior de los elementos de la construcción.\n")
	print (Fore.CYAN + Style.BRIGHT + "Montaje al aire: ", end="")
	print (Fore.WHITE + Style.BRIGHT + "solo permitido para la alimentación de máquinas o elementos de movilidad restringida.\n")
	print (Fore.CYAN + Style.BRIGHT + "Canalizaciones enterradas: ",end="")
	print (Fore.WHITE + Style.BRIGHT + "son tubos enterrados.") 
	print (Fore.RED + Style.BRIGHT + "\nPulse ",end="")
	print (Fore.GREEN + Style.BRIGHT + "(1) ",end="")
	print (Fore.RED + Style.BRIGHT + "Para ",end="")
	print (Fore.YELLOW + Style.BRIGHT + "canalizaciones fijas en superficie",end="")
	print (Fore.RED + Style.BRIGHT + " f = 2.5")
	print (Fore.RED + Style.BRIGHT + "Pulse", end="")
	print (Fore.GREEN + Style.BRIGHT + " (2)", end="")
	print (Fore.RED + Style.BRIGHT + " Para ",end="")
	print (Fore.YELLOW + Style.BRIGHT + "canalizaciones empotradas ", end="")
	print (Fore.RED + Style.BRIGHT + "f = 3")
	print (Fore.RED + Style.BRIGHT + "Pulse ", end="")
	print (Fore.GREEN + Style.BRIGHT + "(3) ", end="")
	print (Fore.RED + Style.BRIGHT + "Para ", end="")
	print (Fore.YELLOW + Style.BRIGHT + "canalizaciones aéreas o con tubos al aire ",end="")
	print (Fore.RED + Style.BRIGHT + "f = 4")
	print (Fore.RED + Style.BRIGHT + "Pulse ", end="")
	print (Fore.GREEN + Style.BRIGHT +"(4) ",end="")
	print (Fore.RED + Style.BRIGHT + "Para ",end="")
	print (Fore.YELLOW + Style.BRIGHT + "canalizaciones enterradas ",end="")
	print (Fore.RED + Style.BRIGHT + "f = 4")
	
	while True:
		tecla = get_key()	
		if tecla == "1" or tecla == "2" or tecla == "3" or tecla == "4":
			break
	# A partir de aquí ya no lee la tecla
	print ("\n") # de esta parte aparece en el "menu" final del cálculo.
	print (Fore.GREEN + Style.BRIGHT + "Calculo diámetro exterior del tubo")
	print (Fore.YELLOW + Style.BRIGHT + "Factor de corrección "+Style.RESET_ALL, end="")
	print ("de ", end="")		
	if tecla == "1":
		print ("f = 2.5 para ",end="")
		print (Fore.BLUE + Style.BRIGHT + "canalizaciones fijas en superficie"+Style.RESET_ALL)
		return FC_FIJAS_EN_SUPERFICIE
	elif tecla == "2":
		print ("f = 3 para ", end="")
		print (Fore.BLUE + Style.BRIGHT + "canalizaciones empotradas"+Style.RESET_ALL)
		return FC_EMPOTRADAS
	elif tecla == "3":
		print ("f = 4 para ",end="")
		print (Fore.BLUE + Style.BRIGHT + "canalizaciones aéreas o con tubos al aire."+Style.RESET_ALL)
		return FC_AREASOTUBOSALAIRE
	elif tecla == "4":
		print("f = 4 para ",end="")
		print(Fore.BLUE + Style.BRIGHT + "canalizaciones enterradas."+Style.RESET_ALL)
		return FC_CANALIZACIONESENTERRADAS

def DiametroComercial(Dinterior):
	CatalogoAISCAN = (10.7, 13.4, 18.5, 24.3, 31.2, 39.6)
	print (Fore.GREEN + Style.BRIGHT + "Según el catalogo del fabricante AISAN:")
	if Dinterior <= 39.6:
		for cat in range (0,6):
			if Dinterior < CatalogoAISCAN[cat]:
				intMin = CatalogoAISCAN[cat]
				if cat == 0:
					diamExt = "16"
				elif cat == 1:
					diamExt = "20"
				elif cat == 2:
					diamExt = "25"
				elif cat == 3:
					diamExt = "32"
				elif cat == 4:
					diamExt = "40"
				elif cat == 5:
					diamExt = "50"
				break
		print(Fore.YELLOW + Style.BRIGHT+ "El diámetro interior mínimo del tubo ", end="")
		print(Fore.BLUE + Style.BRIGHT+ "AISCAN CHF-"+diamExt, end="")
		print(Fore.MAGENTA + Style.BRIGHT+ " es de", round(intMin,2),"mm") 
		print(Fore.YELLOW + Style.BRIGHT + "El diámetro exterior ",end=""+ Style.RESET_ALL)
		print("corresponde a "+ Fore.BLUE + Style.BRIGHT+"Aiscan CHF-"+str(diamExt)+" mm", end="")
		print(Style.RESET_ALL + f" o tubo de {diamExt} mm")
	elif Dinterior > 39.6:
		print (Fore.RED + Style.BRIGHT + "Tubo superior a 50 mm de diámetro exterior, sin refencias para estos."+Style.RESET_ALL)

def salircalculos():
	print(Fore.MAGENTA + Style.BRIGHT + "Para calcular otro tubo Pulse ",end="")
	print(Fore.CYAN + Style.BRIGHT + "(o)",end="")
	print(Style.RESET_ALL+" para volver al menú de inicio cualquier otra tecla.");
	
def mismaSeccionTubo():
	clrscr()
	while True:
		print (Fore.CYAN + Style.BRIGHT + "Calcula el tubo con conductores unipolares de la misma sección.\n" )
		print (Fore.GREEN + Style.BRIGHT + "Sección normaliza. Por ejemplo 1.5, 2.5, etc.:" )
		#Función que pide y devuelve la sección y el limite superior aislante
		seccion,limteSupAislante = SeccionNorm()
		#Función que pide y devuelve el número de conductores
		nconducores = NumconducTubo()
		#Función que pide y devuelve el factor de corrección del tubo
		fcorector = FactorCorreccionTubo()
		# A partir de aquí se muestran en pantalla los resultados de la misma sección
		print(Fore.YELLOW + Style.BRIGHT + "Número de Conductores: ",end=""+Style.RESET_ALL)
		print(nconducores)
		print(Fore.YELLOW + Style.BRIGHT + "Sección nominal de los conductores: ",end=""+Style.RESET_ALL)
		print(seccion,"mm2")
		print(Fore.YELLOW + Style.BRIGHT + "Diámetro exterior del aislante (UNE): ",end=""+ Style.RESET_ALL)
		print(limteSupAislante)
		print(Fore.YELLOW + Style.BRIGHT + "Diámetro interior =",end=""+Style.RESET_ALL)
		print(" diámetro exterior cable (Une) x √n conductores * f")
		DiameInterior = limteSupAislante * math.sqrt(nconducores*fcorector)	
		print(Fore.YELLOW + Style.BRIGHT + "Diámetro interior = ",end=""+Style.RESET_ALL)
		print(DiameInterior,"mm\n")
		DiametroComercial(DiameInterior)
		salircalculos()
		tecla = get_key()
		if tecla != "o":
			break

def NumDeSec():
	print(Fore.GREEN + Style.BRIGHT + "Se determina el número de secciones diferentes que discurren por el tubo.")
	print(Fore.YELLOW + Style.BRIGHT + "Por ejemplo si vamos a tener cables de 1.5, 2.5 y 4 mm2 en un mismo tubo escribimos 3")
	correcto = False
	while True:
		try:
			print (Fore.BLUE + Style.BRIGHT)
			nsecciones = int(input("Número de secciones diferentes que discurren por el tubo: "))
			if nsecciones <= 0:
				raise ValueError("El número debe ser mayor que cero.")
			correcto = True
			break
		except ValueError:
			print ("Valor introducido invalido")
			continue # vuelve a pedir el dato
	if correcto:
		return nsecciones
			
def distintaSeccionTubo():
	class DifSecTubo:
		def __init__(self):
			self.sectbu = []        # Lista de secciones de tubo (float)
			self.limiAisCab = []    # Lista de límites del aislante (float)
			self.nconduc = []       # Lista de número de conductores (int)
			self.CalcParci1 = []    # Cálculos parciales 1 (float)
			self.fc_i = 0.0         # Factor de corrección individual
			self.CalcParci2 = 0.0   # Cálculo parcial 2 (float)
			self.restDiaInt = 0.0   # Resultado del diámetro interior (float)
			self.NdSec = 0          # Número de secciones (int)	
	clrscr()
	cables = DifSecTubo()
	while True:
		print (Fore.CYAN + Style.BRIGHT+"Calcula el tubo con distintas secciones a introducir en un mismo tubo.")
		cables.NdSec = NumDeSec()
		for c in range(0,cables.NdSec):
			sectbu, limiAisCab = SeccionNorm()
			cables.limiAisCab.append(limiAisCab)
			cables.sectbu.append(sectbu)
			NoRepetido = True
			if c > 0: # mas de un valor introducido se comprueba que no este repetido el valor introducido.
				while NoRepetido:
					for d in range (0,c):
						if cables.sectbu[c] == cables.sectbu[d]:
							print (Fore.RED + Style.BRIGHT + f"Error ya introdujo la sección {cables.sectbu[c]}, vuelve a introducir.")
							sectbu, limiAisCab = SeccionNorm()
							cables.limiAisCab[c] = limiAisCab
							cables.sectbu[c] = sectbu
							NoRepetido = True
						else:
							NoRepetido = False
		# pedimos el número de conductores por sección
		for c in range (0,cables.NdSec):
			print (Fore.GREEN + Style.BRIGHT + "\nSección nominal de ",cables.sectbu[c])
			nconduc = NumconducTubo()
			cables.nconduc.append(nconduc)
		# Se llama Factor de Correcion Tubo
		cables.fc_i = FactorCorreccionTubo()	
		# Vamos a mostrar los datos que faltan ya que factor de correccion tubo ya dice algunos
		for c in range(0,cables.NdSec):
			print(Fore.GREEN + Style.BRIGHT + "El número de cables de sección",cables.sectbu[c],"mm2",end="")
			print(Fore.YELLOW + Style.BRIGHT + " es de",cables.nconduc[c],"cables")	
			print(Fore.GREEN + Style.BRIGHT + "El díametro exterior de los cables (UNE) de sección",cables.sectbu[c],"mm2",end="")
			print(Fore.YELLOW + Style.BRIGHT + " es",
			cables.limiAisCab[c])
		# Se calcula el diámetro interior del tubo que llevará varios conductores
		cables.CalcParci2 = 0 
		for c in range (0,cables.NdSec):
			cables.limiAisCab[c] = pow(cables.limiAisCab[c],2)
			Parcial1 = cables.limiAisCab[c] * cables.nconduc[c]
			cables.CalcParci1.append(Parcial1)
			
			cables.CalcParci2 = cables.CalcParci2 + cables.CalcParci1[c]
		# Se calcula el diametro exterior
		cables.restDiaInt = math.sqrt(cables.fc_i * cables.CalcParci2)
		print(Fore.GREEN + Style.BRIGHT + "El diámetro interior del tubo es ", cables.restDiaInt)
		DiametroComercial(cables.restDiaInt)
		
		# se sale
		salircalculos()
		tecla =  get_key()
		if tecla != "o":
			break
			
def menu_principal():
	while True:
		clrscr()
		gotoxy(10,8)
		print(Fore.CYAN+ "Cálculo del diámetro exterior de tubos eléctricos:\n"+Style.RESET_ALL)
		print(Fore.MAGENTA + Back.CYAN + "\nPulsa 1"+ Style.RESET_ALL+" para cálcular el tubo con conductores unipolares de la misma sección\n"+Style.RESET_ALL)
		print(Fore.MAGENTA + Back.CYAN + "Pulsa 2"+ Style.RESET_ALL+" para cálcular el tubo con conductores unipolares de distinta sección\n"+Style.RESET_ALL)
		print(Fore.MAGENTA + Back.CYAN + "Pulsa 3" + Style.RESET_ALL +" para salir")
		tecla = get_key()
		if tecla == "1":
			mismaSeccionTubo()
		elif tecla == "2":
			distintaSeccionTubo()
		elif tecla == "3":
			break 
					
def main():
	init()
	menu_principal()
			    
main()
