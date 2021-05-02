import pyshorteners
from colorama import Fore
import os

os.system("clear")

print(rf"""{Fore.GREEN}
     ▗▄▖ ▗▖                  ▗▖ ▗▖     ▗▄▖
    ▗▛▀▜ ▐▌              ▐▌  ▐▌ ▐▌     ▝▜▌
    ▐▙   ▐▙██▖ ▟█▙  █▟█▌▐███ ▐▌ ▐▌ █▟█▌ ▐▌
     ▜█▙ ▐▛ ▐▌▐▛ ▜▌ █▘   ▐▌  ▐▌ ▐▌ █▘   ▐▌
       ▜▌▐▌ ▐▌▐▌ ▐▌ █    ▐▌  ▐▌ ▐▌ █    ▐▌
    ▐▄▄▟▘▐▌ ▐▌▝█▄█▘ █    ▐▙▄ ▝█▄█▘ █    ▐▙▄
     ▀▀▘ ▝▘ ▝▘ ▝▀▘  ▀     ▀▀  ▝▀▘  ▀     ▀▀
{Fore.RESET}""")

print("ingrese una url: ")
url = input()
s = pyshorteners.Shortener()
resultado = s.tinyurl.short(url)
print(f"url acortada: {resultado}")

file = open("URL.txt","a")
file.write(f"\n{url} = {resultado}\n")
file.close()
print("url guardada en URL.txt!")
