# DOCKER: CHEATSHEET PROPIO

# Introducción
## A. Code Canvas Docker
- [Code Canvas Docker](https://docs.google.com/presentation/d/1Ajv443VrFU6ks8x-0YY5-cEBpvB_4swAX5_pQSWuYmg/edit#slide=id.g1c9ad9ef6e5_0_6)
- [Youtube personal docker](https://www.youtube.com/playlist?list=PLrJvjnSL5aF7YtpEFzc6qdLt7y0BdJVyY)
- [Docker Cheatsheet](https://github.com/alexandergribenchenko/Data_Science_Cheatsheets/blob/main/Cheatsheet_Docker%20_extremeautomation.pdf)

## B. Instalación
- [Verify Windows requeirements](https://docs.docker.com/desktop/install/windows-install/)
- Windows 10 64-bit: Home or Pro 21H1 (build 19043) or higher.
- Enable the WSL 2 feature on Windows. En caso de ser necesario: 
- [Paso 4: Descarga del paquete de actualización del kernel de Linux](https://learn.microsoft.com/es-es/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
- [Paso 5: Definición de WSL 2 como versión predeterminada](https://learn.microsoft.com/es-es/windows/wsl/install-manual#step-5---set-wsl-2-as-your-default-version). Run `wsl --set-default-version 2` in powershell.
- Download Docker Desktop Installer
- Proceder con la instalación (opciones por defecto)
- wsl --set-default-version 2

# 01. Docker - Comandos generales

- `docker`: Muestra todas las opciones de docker
- `docker --version` ó `docker -v` : Versión de docker instalada

# 02. Docker - Comandos de imagenes
- [dockerhub](https://hub.docker.com/) es el repositorio oficial donde se encuentrán las imagenes de docker.
#### Enlistar imagenes
- `docker images`: Muestra un listado completo de todas las imagenes que se han descargado en la máquina.
#### Descargar o eliminar imagenes
- `docker pull [nombre_imagen]`: Descargar la última versión de la imagen, es decir la que tiene el `TAG` latest. Ejemplo: `docker pull mysql`
- `docker pull [nombre_imagen]:[#_vesion]`: Descargar una versión en específico de la imagen.
- `docker image rm [nombre_imagen]:[#_vesion]`: Remover una imagen en específico de docker.
#### Crear una imagen a partir de un Dockerfile: `docker build`
- `docker build -t [nombre_que_queremos_dar_a_la_imagen] [ruta_Dockerfile: por defecto '.' si estamos al mismo nivel]`: construir una imagen a partir de un dockerfile.
#### Crear una imagen a partir de un container: `docker commit`
- `docker commit -t [nombre_del_container] [nombre_imagen_que_deseamos_crear]`: construir una imagen a partir de un container.

# 03. Docker - Comandos de contenedores: general

#### Enlistar contenedores
- `docker ps`: enlista todos los contenedores se encuntren activos.
- `docker ps -a`: enlista todos los contenedores se encuntren activos o no (esto se evalua en la columna `STATUS`).
#### Crear o eliminar contenedores
- `docker create [imagen_base]` ó `docker container create [imagen_base]`: Crea un contenedor con base a una imagen base ya creada.
- `docker create --name [nombre_que_queremos_dar] [imagen_base]` ó `docker container create --name [nombre_que_queremos_dar] [imagen_base]`: Crea un contenedor con base a una imagen base ya creada.
- `docker rm [container_id]` ó `docker rm [container_id]`: remover contenedor a partir de su id o su nombre.
#### Iniciar o detener contenedores
- `docker start [container_id]` ó `docker start [container_id]`: ejecutar contenedor a partir de su id o su nombre.
- `docker stop [container_id]` ó `docker stop [container_id]`: detener contenedor a partir de su id o su nombre.
#### Acceder al interior de los contenedores en ejecución
- `docker exec -it [container_que_esta_corriendo] [opcion de consola:ejemplo en ubuntu /bin/bash]`: entrar por consola a un container que ya esta corriendo.
- `docker run -it [nombre_de_la_imagen] [opcion de consola:ejemplo en ubuntu /bin/bash]`: correr en modo interactivo entrando en la consola dentro del container.

# 04. Docker - Comandos de contenedores: `docker run`

#### Descargar imagen + Crear contenedor + Iniciar Contenedor: `docker run`
- `docker run --name [nombre_que_queremos_dar_al_container] -d [nombre_imagen_base]`: un comando que resume todo el proceso. Descarga la imagen (si es que no existe ya), crea un contenedor a partir de esa imagen y ademas lo inicializa. El comando -d es para que se ejecute en modo `deattached`.
- `docker run --name [nombre_que_queremos_dar_al_container] --rm -i -t -p [puerto_host]:[puerto_contenedor] -e [nombre_variable_entorno]=[valor_variable_entorno] [imagen_base]`: Crea un contenedor con base a una imagen base ya creada.

#### Opciones de `docker run`:
- `-d`: ejecuta en modo deattached, es decir, permite seguir escribiendo cosas en la misma consola sin que haya que parar el contenedor.
- `-e`: variable de entorno.
- `--rm`: lo incluimos si queremos el el contenedor no persista (que se elimine cuando se deje detenga el contenedor). Automatically remove the container when it exits.
- `-i -t`: me permitieron detener con `cmd+c`. Tambien permite mostrar el hipervinculo.

#### Ejemplos de `docker run`
1. `docker run --name notebook --rm -i -t -p 8888:8888 -e TYPE=notebook jorgecardona/jupyter`
2. `docker run --name lab --rm -i -t -p 8888:8888 jorgecardona/jupyter`


# 05. Docker - Dockerfile: `docker build`

Si ejecutamos`docker build -t [nombre_que_queremos_dar_a_la_imagen] [ruta_Dockerfile: por defecto '.' si estamos al mismo nivel]`obtendremos:
Ejemplo: `docker build -t imagen_dockerfile .`
Posteriormente: `docker run --rm -ti imagen_dockerfile` 
o de manera conjunta: `docker build -t imagen_dockerfile . && docker run --rm -ti imagen_dockerfile`

#### Sentencia 01. FROM: Crear una imagen (dockerfile vs console)
- Si el docker file contiene: `FROM ubuntu:10.04`
- Analogo a ejecutar: `docker pull ubuntu:10.04`

#### Sentencia 02. COPY: Copiar archivos al interior del container
- Si el docker file contiene: `COPY [ruta_host] [ruta_container]` ejemplo `COPY app_host /app_cont`
Se hace una copia de los archivos que estan en la ruta_host a la ruta_container.
El el punto de origen del container se toma como su raiz y el punto de origen del host se encuentra al mismo nivel que el Dockerfile.

#### Sentencia 03. WORKDIR: Establecer direcrtorio de trabajo al interior del container
- Situa el directorio de trabajo al interior del container en la ruta que se especifique: `WORKDIR [ruta_especificada].

#### Sentencia 04. RUN: ejecutar sentencias al interior del container en la ruta en el WORKDIR
- `RUN [Sentencias_a ejecutar]` ejemplo `RUN pip install --upgrade pip &&\ pip install -r requirements.txt`




# Bonus Linux
Para imprimir un archivo en la linea de comando (o concatenarlo) empleo la función `cat [nomnre_archivo]`
