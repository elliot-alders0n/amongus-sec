import os
import random
import subprocess 


mi_ip = subprocess.getstatusoutput("hostname -I | awk '{print $1}'")[1]

with open('amongusec.conf') as f:
	lines = f.readlines()
	datos = []
	for line in lines:
		ip,nombre = line.rstrip().split('\t')

		if ip != mi_ip:
			datos.append([ip,nombre])
		else:
			mi_nombre = nombre

for dato in datos:
	comando = f"ssh -i ./claves/{mi_nombre} kali@{dato[0]} 'rm -r /home/kali/amongusec'"
	print(comando)
	#os.system(comando)
