# Amongus edición Ciberseguridad

## Consideraciones previas
Todos los dispositivos que vayan a participar en el juego deben tener el servicio ssh activado.
```
sudo systemctl start ssh
```

Es preferible que el cortafuegos esté desactivado o configurado correctamente para que permita la conexión ssh.

### Fichero de configuración
En el fichero 
conf/amongus-sec.conf 
se deben introducir todas las IPs de los dispositivos que van a intervenir con sus respectivos nombres identificativos en líneas independientes siguiendo este formato:

IP[Tabulador]Nombre

Si se desea comentar una línea, escribir # como primer caracter de línea.

### Creación de claves
Para el correcto funcionamiento del juego se generará un par de claves y seguidamente compartir la clave pública con el resto de participantes para ingresar en su lista de usuarios autorizados:
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
Se nos permitirá elegir entre un número de ataques y elegir un objetivo manualmente.

## Objetivo del juego
Descubrir quién/es han entrado en nuestro equipo y qué ataque están realizando.
