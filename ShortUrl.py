#!/bin/python
#
# Created by: Termux Hacking
#
# ShortUrl
#
# VARIABLES
#
rosa = '\033[38;5;207m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
morado = '\033[35m'
blanco = '\033[37m'
cyan = '\033[1;36m'
magenta = '\033[1;35m'
negro = '\033[0;30m'
gris_oscuro = '\033[1;30'
#

import pyshorteners
import time
import os

time.sleep(0.5)
os.system("clear")

print()
print(f"{verde} ▗▄▖ ▗▖                  ▗▖ ▗▖     ▗▄▖")
print("▗▛▀▜ ▐▌              ▐▌  ▐▌ ▐▌     ▝▜▌")
print("▐▙   ▐▙██▖ ▟█▙  █▟█▌▐███ ▐▌ ▐▌ █▟█▌ ▐▌")
print(" ▜█▙ ▐▛ ▐▌▐▛ ▜▌ █▘   ▐▌  ▐▌ ▐▌ █▘   ▐▌")
print("   ▜▌▐▌ ▐▌▐▌ ▐▌ █    ▐▌  ▐▌ ▐▌ █    ▐▌")
print("▐▄▄▟▘▐▌ ▐▌▝█▄█▘ █    ▐▙▄ ▝█▄█▘ █    ▐▙▄")
print(" ▀▀▘ ▝▘ ▝▘ ▝▀▘  ▀     ▀▀  ▝▀▘  ▀     ▀▀")
print()
print("┌═════════════════┐")
print(f"█ {blanco}INGRESE UNA URL {verde}█")
print("└═════════════════┘")
print("┃")
url = input(f"└═>>> {blanco}")
s = pyshorteners.Shortener()
print()
print(f"{verde}┌═════════════════┐")
print(f"█ {blanco}SU URL ACORTADA {verde}█")
print(f"└═════════════════┘{blanco}")
print()
print(s.tinyurl.short(url))
print()
resultado = (s.tinyurl.short(url))

Short = open("URL.txt", "w")
Short.write(str (resultado))
Short.close
