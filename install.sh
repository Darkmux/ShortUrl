#!/bin/bash
#
# REQUISITOS
#
# VARIABLES
#
source $HOME/ShortUrl/Colors.sh
#
# CÓDIGO
#
sleep 0.5
clear
echo -e "${verde}
┌══════════════════════════════┐
█ ${blanco}Actualizando Repositorios... ${verde}█
└══════════════════════════════┘
"
apt update && apt upgrade -y
sleep 0.5
clear
echo -e "${verde}
┌════════════════════════════┐
█ ${blanco}Instalando pyshorteners... ${verde}█
└════════════════════════════┘
"${blanco}
pip install pyshorteners > /dev/null 2>&1
chmod 711 ShortUrl.py
echo -e "${verde}
┌═══════════════════════┐
█ ${blanco}REQUISITOS INSTALADOS ${verde}█
█ ${blanco}EJECUTE EL COMANDO... ${verde}█
└═══════════════════════┘
┃
┃    ┌════════════════════┐
└═>>>█ ${blanco}python ShortUrl.py ${verde}█
     └════════════════════┘
"${blanco}
