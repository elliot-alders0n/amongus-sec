# Amongus edición Ciberseguridad

## Consideraciones previas

### SSH
Todos los dispositivos que vayan a participar en el juego deben tener el servicio ssh activado.

```
sudo systemctl start ssh
```

### Cortafuegos
Es preferible que el cortafuegos esté desactivado o configurado correctamente para que permita la conexión ssh ; o bien ejecutamos:

```
sudo ufw allow ssh
```

o

```
sudo ufw disable
```

### Reenvio de ventanas
Asegurarse de que en el archivo /etc/ssh/sshd_conf hay una línea que pone
```
X11Forwarding yes
```
(sin # al principio; si pone no cambiarlo a yes).

### Fichero de configuración
En el fichero 
conf/amongus-sec.conf 
se deben introducir todas las IPs de los dispositivos que van a intervenir con sus respectivos nombres identificativos en líneas independientes siguiendo este formato:

IP[Tabulador]Nombre

Si se desea comentar una línea, escribir # como primer caracter de línea.

### Creación de claves
Para el correcto funcionamiento del juego se generará un par de claves y seguidamente se compartirá la clave pública con el resto de participantes para ingresar en su lista de usuarios autorizados:

Dar permisos de ejecucion al script de instalación:
```
sudo chmod +x instalar
```
Ejecutar:

```
./instalar
```
## Modos de juego
### Modo automático
Al ejecutar el siguiente comando

```
./amongus-sec
```
se asignará un ataque y un objetivo aleatorios, informándo por consola para posteriormente poder comprobar si hemos sido detectados correctamente.

### Modo manual
Al ejecutar el siguiente comando

```
./amongus-sec-manual
```
Se nos permitirá elegir entre un número de ataques y un objetivo de forma manual.

## Tipos de ataques
- Curios@ : accede a la máquina objetivo mediante ssh y saldrá de ella inmediatamente.
- Tortuga : (LAN-turtle) se queda escuchando en un puerto aleatorio a la espera de un potencial ataque "Reverse shell",
- Impostor/a : se ejecuta un proceso "enmascarado" que tiene como nombre un servicio conocido del sistema.
- Ladrón/a de ventanas : abre una aplicación que requiera entorno gráfico sin que la víctima se percate.
  
## Objetivo del juego
Descubrir quién/es han entrado en nuestro equipo y qué ataque están realizando.
