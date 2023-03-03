import os
import subprocess 


mi_ip = subprocess.getstatusoutput("hostname -I | awk '{print $1}'")[1]

with open('conf/amongus-sec.conf') as f:
	lines = f.readlines()
	datos = []
	for line in lines:
		line = line.strip()
		if line[0] != '#':
			ip,nombre = line.rstrip().split('\t')

			if ip != mi_ip:
				datos.append([ip,nombre])
			else:
				mi_nombre = nombre

for dato in datos:
	comando = f"ssh-copy-id -i .claves/{mi_nombre}.pub kali@{dato[0]}"
	os.system(comando)
