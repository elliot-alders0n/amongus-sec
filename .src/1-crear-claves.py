import os
import subprocess 


mi_ip = subprocess.getstatusoutput("hostname -I | awk '{print $1}'")[1]

with open('conf/amongus-sec.conf') as f:
	lines = f.readlines()
	datos = []
	for line in lines:
		ip,nombre = line.rstrip().split('\t')

		if ip != mi_ip:
			datos.append([ip,nombre])
		else:
			mi_nombre = nombre

os.system("mkdir .claves")
os.system(f'ssh-keygen -b 2048 -t rsa -f .claves/{mi_nombre} -q -N ""')
