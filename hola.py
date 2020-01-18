import os
import time
import re

def cmd(command):
    os.system(command)

def requeriments():
    cmd("sudo apt install python3-pip")

def osverify():
    if os.name == "nt":
        cmd("cls")
    elif os.name == "posix":
        cmd("clear")

def sshdconfig():
    f= open("/etc/ssh/sshd_config","r+")
    fr= f.readlines()
    cl=0
    for x in fr:
        cl+=1
        if re.findall("^#PermitRootLogin",x):
            cl-=1
            fr[cl]= "PermitRootLogin yes\n"
            f.seek(0)
            f.writelines(fr)
        if re.findall("^UsePAM",x):
            cl-=1
            fr[cl]= "UsePAM no\n"
            f.seek(0)
            f.writelines(fr)
    f.close()

def rootpw():
    cmd("passwd")

def main():
    cmd("sudo su")
    requeriments()
    print(f"""
            Iniciando Setup Linux
            """)
    osverify()
    print("Configurando Archivo de SSHD_CONFIG")
    sshdconfig()
    print("Cambiando Contraseña del Usuario Root")
    rootpw()
    print("Reiniciando el SSHD")
    cmd("service sshd restart")
    input("Programa Terminado, Presiona enter para salir ...")



if __name__ == "__main__":
    input("Enter para continuar con todo :D ....")
    main()
