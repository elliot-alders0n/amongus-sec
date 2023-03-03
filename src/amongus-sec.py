import sys
import os
import random
import subprocess
import time

class AmonguSec:

	def cargar_fichero_configuracion(self):
		with open('conf/amongus-sec.conf') as f:
			lines = f.readlines()
			self.candidatos = []
			for line in lines:
				line = line.rstrip()
				if line[0] != '#':
					ip,nombre = line.rstrip().split('\t')

					if ip != self.mi_ip:
						self.candidatos.append([ip,nombre])
					else:
						self.mi_nombre = nombre

	def __init__(self):
		# 0 - curios@	: realiza conexion ssh y sale inmediatamente
		# 1 - tortuga	: se conecta ssh y ejecuta comando netcat de escucha para abrir una shell remota
		# 2 - impostor	: proceso enmascarado como un proceso del sistema
		self.TAREAS = ["curios@","tortuga","impostor/a"]

		self.DISFRACES = ["systemd","dockerd","ssh","sshd","cron","sleep"]
		self.mi_ip = subprocess.getstatusoutput("hostname -I | awk '{print $1}'")[1]
		self.cargar_fichero_configuracion()

	def imprimir_cabecera(self):
		os.system("figlet -c 'amongus'")
		os.system("figlet -c 'ciberseguridad'")
		os.system('echo "\n\t\t\t\t\tJuanma © Copyright 2023"')

	def escoger_tarea(self,indice=-1):

		if indice == -1:
			self.tarea = random.choice(self.TAREAS)
		else:
			self.tarea = self.TAREAS[indice]

		print(f"\nTe ha tocado ser \033[1;31m{self.tarea}\033[0m")

	def establecer_comando(self):
		self.comando = ""
		if self.tarea == "curios@":
			self.comando = f"ssh -i claves/{self.mi_nombre} kali@{self.objetivo} 'echo \"\"'"
		elif self.tarea == "tortuga":
			self.comando = f"ssh -i claves/{self.mi_nombre} kali@{self.objetivo} 'nc -lnvp {random.randint(20,65536)}'"
		elif self.tarea == "impostor/a":
			disfraz = random.choice(self.DISFRACES)
			print(f"disfraz : \033[35m{disfraz}\033[0m")
			self.comando = f"ssh -i claves/{self.mi_nombre} kali@{self.objetivo} 'cd /tmp;cp /bin/sleep {disfraz};./{disfraz} 3600'"

	def obtener_nombre(self,IP):
		nombre = ''
		for candidato in self.candidatos:
			if candidato[0] == IP:
				return candidato[1]
		return nombre

	def escoger_objetivo_aleatorio(self):
		candidato = random.choice(self.candidatos)
		self.objetivo = candidato[0]
		self.candidatos.remove(candidato)
		return candidato[1]

	def escoger_intermediario_aleatorio(self):
		candidato = random.choice(self.candidatos)
		self.intermediario = candidato[0]
		self.candidatos.remove(candidato)
		self.nombre_intermediario = candidato[1]

	def establecer_objetivo(self, IP_objetivo):
		self.objetivo = IP_objetivo

	def establecer_intermediario(self, IP_intermediario, nombre_intermediario):
		self.intermediario = IP_intermediario
		self.nombre_intermediario = nombre_intermediario

	def ejecutar_comando(self):
		os.system(self.comando)

	def buscar_candidato(self,nombre):
		for candidato in self.candidatos:
			if candidato[1].lower() == nombre.lower():
				return candidato[0]
		return ""

	def IP_es_valida(self,IP):
		valida = True
		partes = IP.split(".")
		if len(partes) == 4:
			for parte in partes:
				if parte.isdigit():
					valor = int(parte)
					if not (valor >= 0 and valor <=255):
						return False
				else:
					valida = False
		else:
			valida = False
		return valida

def main():
	amongusec = AmonguSec()
	amongusec.imprimir_cabecera()
	error = False
	if len(sys.argv) == 2:
		opcion = sys.argv[1]
		if opcion == "-i" or opcion == "--interactivo":
			opcion_correcta = False
			opcion = ''
			while not opcion_correcta:
				print("\nSeleccione el tipo de ataque : ")
				print("\n\t\033[1m\033[38;2;255;0;0mx\033[0m: Salir\n")
				print("\t\033[1m\033[38;2;255;255;0ma.\033[0m \033[1mcurios@\033[0m\t:\tentrar y salir de la máquina objetivo.")
				print("\t\033[1m\033[38;2;255;255;0mb.\033[0m \033[1mtortuga\033[0m\t:\tintento de apertura de shell remota.")
				print("\t\033[1m\033[38;2;255;255;0mc.\033[0m \033[1mimpostor/a\033[0m\t:\tproceso enmascarado.")
				opcion = input()

				if opcion == 'x':
					exit()

				opciones = ['a','b','c','d']
				opcion_correcta = (opcion in opciones)
				if not opcion_correcta:
					print("\033[1m\033[38;2;255;0;0mOpción incorrecta.\033[0m")
					time.sleep(1)
			amongusec.escoger_tarea(indice=opciones.index(opcion))


			nombreIP_correcto = False
			IP_objetivo = ""
			while not nombreIP_correcto:
				print("Seleccione la IP/nombre del objetivo : ")
				IP_objetivo = input()

				if not amongusec.IP_es_valida(IP_objetivo):
					IP_objetivo = amongusec.buscar_candidato(IP_objetivo)
				nombreIP_correcto = (len(IP_objetivo) > 0)

				if not nombreIP_correcto:
					print("\033[1m\033[38;2;255;0;0mNombre/IP incorrecto.\033[0m")
					time.sleep(1)

			nombre_objetivo = amongusec.obtener_nombre(IP_objetivo)
			amongusec.establecer_objetivo(IP_objetivo)

			print(f"Tu objetivo es \033[0;33m{nombre_objetivo}\033[0m ({IP_objetivo})")

			amongusec.establecer_objetivo(IP_objetivo)

			amongusec.establecer_comando()
			print()
			print(amongusec.comando)
			#amongusec.ejecutar_comando()
		else:
			error = True
	elif len(sys.argv) == 1:
		amongusec.escoger_tarea()
		nombre_objetivo = amongusec.escoger_objetivo_aleatorio()

		print(f"Tu objetivo es \033[0;33m{nombre_objetivo}\033[0m ({amongusec.objetivo})")

		amongusec.establecer_comando()
		print()
		print(amongusec.comando)
		#amongusec.ejecutar_comando()
	else:
		error = True

	if error:
		print("\033[1m\033[38;2;255;0;0mModo de uso :\033[0m")
		print("\tamongus-sec [-i, --interactivo]")

if __name__ == "__main__":
	main()
