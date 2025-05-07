# DOCKER: CHEATSHEET PROPIO

- `docker build -t [nombre_que_queremos_dar_a_la_imagen] [ruta_Dockerfile: por defecto '.' si estamos al mismo nivel] && docker run --rm -ti [nombre_que_queremos_dar_a_la_imagen] sh`: ejemplo.
- `docker build -t image_example . && docker run --rm -ti image_example sh`: ejemplo.




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

## C. Glosario. 
- Imagen:
- Contenedor:
- Docker file:
- Docker compose:


# 01. Docker - Comandos generales

- `docker`: Muestra todas las opciones de docker
- `docker --version` ó `docker -v` : Versión de docker instalada.
- `docker info`: Detalle de la version y configuración de docker
- `docker system prune -a`: borra los containers, imagenes que no esten activos.
- `docker container prune -f`: borra todos los contenedores que no esten activos.

# 02. Docker - Comandos de imagenes
**Nota**: Para poder ejecutar los siguientes comando docker desktop debe estar abierto y estarse ejecutando en la maquina host, sino los comandos retornaran error.

- [dockerhub](https://hub.docker.com/) es el repositorio oficial donde se encuentrán las imagenes de docker.
#### Enlistar imagenes
- `docker images`: Muestra un listado completo de todas las imagenes que se han descargado en la máquina.

#### Descargar imagenes
Comando:
``` bash
docker pull [nombre_imagen]
```
Ejemplo:
``` bash
docker pull mysql
```


- `docker pull [nombre_imagen]`: Descargar la última versión de la imagen, es decir la que tiene el `TAG` latest.
Ejemplo: `docker pull mysql`
- `docker pull [nombre_imagen]:[tag]`: Descargar una versión en específico de la imagen.
Ejemplo: `docker pull mysql:8-oraclelinux8` donde el `tag` es `8-oraclelinux8`.

#### Eliminar imagenes
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
- `docker create [imagen_base]` ó `docker container create [imagen_base]`: Crea un contenedor con base a una imagen base ya creada, pero le da un nombre arbitrario. El contenedor no se jecuta, solo se crea.
- `docker create --name [nombre_que_queremos_dar] [imagen_base]` ó `docker container create --name [nombre_que_queremos_dar] [imagen_base]`: Crea un contenedor con base a una imagen base ya creada.
- `docker rm [container_id]` ó `docker rm [container_id]`: remover contenedor a partir de su id o su nombre.
#### Iniciar o detener contenedores
- `docker start [container_id]` ó `docker start [container_id]`: ejecutar contenedor a partir de su id o su nombre.
- `docker stop [container_id]` ó `docker stop [container_id]`: detener contenedor a partir de su id o su nombre.
#### Acceder al interior de los contenedores en ejecución
- `docker exec -it [container_que_esta_corriendo] [opcion de consola:ejemplo en ubuntu /bin/bash]`: entrar por consola a un container que ya esta corriendo.
- `docker run -it [nombre_de_la_imagen] [opcion de consola:ejemplo en ubuntu /bin/bash]`: correr en modo interactivo entrando en la consola dentro del container.

# 04. Docker - Comandos de contenedores: `docker run`
- `docker run [nombre_imagen_base:tag]`: un comando que resume todo el proceso. 
- `docker run -d -t [nombre_imagen_base:tag]`: levanta el contenedor y lo deja corriendo en modo deatach (running in the background), lo que permite que el contenedor siga corriendo, aunque regremos a la consola principal.
- `docker run -it --name=[nombre_para_contenedor] [image:tag] [bash]`: crear un contenedor y ejecutarlo, pero con un nombre en particular.



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
3. `docker run --rm -ti [nombre de la imagen]`: Para un caso en el que queremos desplegar el contenedor pero que no persista y que una vez lo paremos se borre.

# 05. Docker - Dockerfile: `docker build`

Si ejecutamos`docker build -t [nombre_que_queremos_dar_a_la_imagen] [ruta_Dockerfile: por defecto '.' si estamos al mismo nivel]`obtendremos:
Ejemplo: `docker build -t imagen_dockerfile .`
Posteriormente: `docker run --rm -ti imagen_dockerfile` 
o de manera conjunta: `docker build -t imagen_dockerfile . && docker run --rm -ti imagen_dockerfile`

#### Sentencia 01. FROM: Toma una imagen como base sobre la que se va a construir (dockerfile vs console)
- Si el docker file contiene: `FROM ubuntu:10.04`
- Analogo a ejecutar: `docker pull ubuntu:10.04`

#### Sentencia 02. COPY: Copiar archivos al interior del container
- Si el docker file contiene: `COPY [ruta_host] [ruta_container]` ejemplo `COPY app_host /app_cont`
Se hace una copia de los archivos que estan en la ruta_host a la ruta_container.
El el punto de origen del container se toma como su raiz y el punto de origen del host se encuentra al mismo nivel que el Dockerfile.

#### Sentencia 03. WORKDIR: Establecer direcrtorio de trabajo al interior del container
- Situa el directorio de trabajo al interior del container en la ruta que se especifique: `WORKDIR [ruta_especificada]`.

#### Sentencia 04. RUN: ejecutar sentencias al interior del container en la ruta en el WORKDIR
- `RUN [Sentencias_a ejecutar]` ejemplo `RUN pip install --upgrade pip &&\ pip install -r requirements.txt`

#### Sentencia 05. CMD: sentencia que se ejecuta una vez el container se inicializa
- `CMD [sentencia_a_ejecutar]`: por ejemplo `CMD python`.

# XXX Experimento docker: 
#### Experimento 01.
- `docker run -i -t -p 8888:8888 -v "PWD":/home --name anaconda3_cpsc322 continuumio/anaconda3:2020.11`
- `jupyter-lab --ip='0.0.0.0' --port=8888 --no-browser --allow-root --notebook-dir=/home`

#### Experimento 02. 
``` python
FROM continuumio/miniconda3:4.10.3p1
RUN conda install \
    xarray \ 
    netCDF4 \ 
    bottleneck \
    numpy \
    pandas \
    matplotlib \
    jupyterlab
CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root", "--notebook-dir=/home"]
```
- **Comando 01:** `docker build -t img_jupyter .` 
- **Comando 02:** `docker run --rm -it -p 8888:8888 img_jupyter`

#### Experimento 03. Propio.
``` python
FROM continuumio/anaconda3

COPY app_host /app_cont

WORKDIR /app_cont

RUN pip install -r requirements.txt

CMD ["jupyter-lab","--ip=0.0.0.0", "--port=5000","--no-browser","--allow-root", "--notebook-dir=/app_cont"]
```
- **Comando 01:** `docker build -t img_jupyter .` 
- **Comando 02:** `docker run --rm -it -p 8888:5000 img_jupyter`


# 06. Docker - docker-compose
- Link versiones: [Compose file versions and upgrading](https://docs.docker.com/compose/compose-file/compose-versioning/)
#### Experimento 01. docker-compose.
``` python
version: '3.8'

services:

  jupyter:
    build: ./jupyter
    restart: unless-stopped
    ports:
      - "8200:8888"
    entrypoint:
      jupyter lab --ip='0.0.0.0' --port=8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''
    volumes: 
      - ./jupyter:/app
    env_file: 
      - ./jupyter/variables.env
```
- **Comando 01:** docker-compose up -d
- **Comando 02:** docker-compose down

#### Experimento 02. docker-compose.
``` python
version: '3.8'

services:

  jupyter:
    build: ./jupyter
    restart: unless-stopped
    ports:
      - "8200:8888"
    entrypoint:
      jupyter lab --ip='0.0.0.0' --port=8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''
    volumes: 
      - ./jupyter:/app
    env_file: 
      - ./jupyter/variables.env

  postgresql:
    image: "postgres:14"
    restart: unless-stopped
    environment:
      POSTGRES_DB: test
      POSTGRES_USER: itguymichal
      POSTGRES_PASSWORD: admin
      PGDATA: /var/lib/postgresql/data
    ports:
      - "5432:5432"
    volumes:
      - db-data:/var/lib/postgresql/data

  pgadmin:
    image: "dpage/pgadmin4:latest"
    restart: unless-stopped
    ports: 
      - "8000:80"
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@example.com
      PGADMIN_DEFAULT_PASSWORD: p4ssw0rd
    volumes:
      - pgadmin-data:/var/lib/pgadmin
      
volumes:
  db-data:
  pgadmin-data:
```
#### Dockerfile:
``` python
FROM python:3.8.5-slim

RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install jupyterlab
RUN pip install psycopg2-binary
```

- **Comando 01:** docker-compose up -d
- **Comando 02:** docker-compose down




# Bonus Linux
- Para imprimir un archivo en la linea de comando (o concatenarlo) empleo la función `cat [nombre_archivo]`
