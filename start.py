import os
import time
os.system("apt install pip3")
try:
	import requests
	print("""

			[!] libreria requests instalada!

			""")
except:
	print("""

		libreria requests no instalada, instalando...

			""")
	os.system("pip3 install requests")




def cmd(command):
    os.system(command)

    
    

print("Iniciando Setup de Linux")
print("""
		Ingresa "s,y,si," para continuar.
		Ingresa "n,no" para salir.
		""")
pregunta1= input("Desea Continuar?: ")

if pregunta1 == "s" or "y" or "si":
    pass
else:
    exit()

for x in range(0,101,5):
    print("\n")
    print("         \\|||||/        ")
    print("         ( O O )         ")
    print("|--ooO-----(_)----------|")
    print("|                       |")
    print(f"|    Comenzando {x}%     |")
    print("|                       |")
    print("|------------------Ooo--|")
    print("         |__||__|        ")
    print("          ||  ||         ")
    print("         ooO  Ooo        ")
    time.sleep(1)
    cmd("clear")

def main():
	time.sleep(1)
	cmd("clear")
	print("Actualizando...")
	cmd("clear")
	cmd("apt update && y")
	time.sleep(1)
	print("Actualizando...")
	cmd("apt upgrade && y")
	time.sleep(1)
	try:
		cmd("apt-cache policy nano")
		print("""

				[!] editor nano instalado!

				""")
	except:
		cmd("apt install nano && y")
		print("""

				[x] no tiene nano instalado, instalando...

				""")
	time.sleep(1)
	print("Configurando sshd_config para aceptar contraseñas...")
	cmd("nano /etc/ssh/sshd_config")
	time.sleep(3)
	print("Cambiando Contraseña:")
	cmd("clear")
	print("Ingrese su contraseña 2 veces:")
	cmd("passwd")
	print("Contraseña cambiada con exito!")
	time.sleep(3)
	cmd("clear")
	print("Restaurando sshd y ssh ...")
	cmd("service sshd restart")
	cmd("service ssh restart")
	time.sleep(3)
	print("""
		Listo!
		""")

if __name__=='__main__':
	main()
	exit()
