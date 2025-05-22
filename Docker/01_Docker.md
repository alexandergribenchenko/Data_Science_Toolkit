# DOCKER: CHEATSHEET PROPIO

# Por consultar:
- `docker logs [nombre_del_contenedor]`:

# Atajo: comandos más usados:
- `docker build -t imagen_dockerfile:1.1 .`
- `docker run -d -it imagen_dockerfile:1.1`
- `docker run -d -it --name=container_test imagen_dockerfile:1.1`
- `docker run -it --rm --name=nombre_para_contenedor imagen_dockerfile:1.1`
- `docker run -it --rm -p 9000:8888 --name=nombre_para_contenedor imagen_dockerfile:1.1`
- `docker exec -it imagen_dockerfile:1.1 /bin/bash`
- `echo -e "RUN curl https://assets.datacamp.com/production/repositories/6082/datasets/31a5052c6a5424cbb8d939a7a6eff9311957e7d0/pipeline_final.zip -o /pipeline_final.zip\nRUN unzip /pipeline_final.zip\nRUN rm /pipeline_final.zip" >> Dockerfile` Copiar datos desde un enlace web.



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
- Docker compose
- Docker instructions: se encuentran en el Docker file `FROM`, `RUN`, etc.
- Docker commands: se escriben en el terminal `run`, `start, etc.
- `docker logs`: falta por estudiar.

# 01. Docker - Comandos generales
- `docker`: Muestra todas las opciones de docker
- `docker --version` ó `docker -v` : Versión de docker instalada.
- `docker info`: Detalle de la version y configuración de docker
- `docker system prune -a`: borra los containers, imagenes que no esten activos.
- `docker container prune -f`: borra todos los contenedores que no esten activos.

# 02. Docker - Comandos de imagenes
**Nota**: Para poder ejecutar los siguientes comando docker desktop debe estar abierto y estarse ejecutando en la maquina host, sino los comandos retornaran error.

## 02.01. Docker - Comandos de imagenes: general

- [dockerhub](https://hub.docker.com/) es el repositorio oficial donde se encuentrán las imagenes de docker.
## Enlistar imagenes
- `docker images`: Muestra un listado completo de todas las imagenes que se han descargado en la máquina host así esten siendo utilizadas por un contenedor o no.

## Descargar imagenes de dockerhub
- `docker pull [nombre_imagen]`: Descargar la última versión de la imagen, es decir la que tiene el `TAG` latest.
    * Ejemplo: `docker pull mysql`
- `docker pull [nombre_imagen]:[tag]`: Descargar una versión en específico de la imagen.
    * Ejemplo: `docker pull mysql:8-oraclelinux8` donde el `tag` es `8-oraclelinux8`.

## Eliminar imagenes
- `docker image rmi [nombre_imagen]:[#_vesion]`: Remover una imagen en específico de docker.
    * Ejemplo: `docker rmi mysql:8-oraclelinux8`
- `docker image prune -a -f`: borra todas las imagenes no usadas por ningun contenedor.
   * Opciones: 
      - `-a`: Elimina todas las imágenes no usadas por ningún contenedor, no solo las imágenes "dangling" (huérfanas sin etiquetas).
      - `-f`: Ejecuta el comando sin pedir confirmación.

## `docker build`: Crear una imagen a partir de un Dockerfile
- `docker build -t [nombre_que_queremos_dar_a_la_imagen:tag_que_queremos] [ruta_Dockerfile: por defecto '.' si estamos al mismo nivel]`: construir una imagen a partir de un dockerfile.
    * Ejemplo: `docker build -t imagen_a_crear:tag_a_crear .`

## `docker commit`: Crear una imagen a partir de un container:
- `docker commit [nombre_del_container] [nombre_imagen_que_deseamos_crear:tag_que_deseamos_asignar]`: construir una imagen a partir de un container.
   * Ejemplo: `docker commit poc_container image_from_container:tag_propio`.
 
## 02.02. Docker - Comandos de imagenes: publicar imagenes en dockerhub
- `docker login`: un comando que permite hacer el login en dockerhub.
- `docker tag [nombre_actual_imagen] [nombre_usuario_github/nombre_nuevo_imagen:nuevo_tag]`: cambiar el tag a la imagen porque a la raiz de dockerhub solo se pueden subir repositorios oficiles.
   * Ejemplo:`docker tag imagen_dockerfile:1.1 alexandergribenchenko/imagen_dockerfile:1.1`
- `docker push [nombre_de_la_imagen:tag_de_la_imagen]`: Permite publicar la imagen en dockerhub.
   * Ejemplo: `docker push alexandergribenchenko/imagen_dockerfile:1.1`
 
## 02.03. Docker - Comandos de imagenes: guardar y cargar imagenes como archivos
- `docker save -o [nombre_del_archivo.tar] [nombre_imagen:tag_imagen]`: se utiliza para exportar una imagen de Docker como un archivo .tar.
   * Ejemplo:`docker save -o docker_image_file.tar python:3.10-slim`
- `docker load -i [nombre_del_archivo.tar]`:  importar imágenes que fueron previamente guardadas con docker save. Esto es útil para mover imágenes entre sistemas sin usar un registry (como Docker Hub).
   * Ejemplo:`docker load -i docker_image_file.tar`. No tiene opciones especificas para importar la imagen con cierto nombre y cierto tag. Importa con las que fue guardado y si uno quiere modificarlo lo redefine luego.

# 03. Docker - Comandos de contenedores

## 03.01. Docker - Comandos de contenedores: general
### Enlistar contenedores
- `docker ps`: enlista todos los contenedores se encuntren activos.
- `docker ps -a`: enlista todos los contenedores se encuntren activos o no (esto se evalua en la columna `STATUS`).

### Crear contenedores
- `docker create [imagen_base]` ó `docker container create [imagen_base]`: Crea un contenedor con base a una imagen base ya creada, pero le da un nombre arbitrario. El contenedor no se jecuta, solo se crea.
   * Ejemplo: `docker container create python:3.10-slim`.
- `docker create --name [nombre_que_queremos_dar] [imagen_base]` ó `docker container create --name [nombre_que_queremos_dar] [imagen_base]`: Crea un contenedor con base a una imagen base ya creada.
   * Ejemplo: `docker container create --name container_to_create python:3.10-slim`.

### Eliminar contenedores
- `docker rm [container_id_or_name]` ó `docker container rm [container_id_or_name]`: remover contenedor a partir de su id o su nombre.
   * Ejemplo: `docker container rm container_to_create`.
- `docker container prune`:   elimina todos los contenedores detenidos.
   * Opciones: 
      - `-f`: Ejecuta el comando sin pedir confirmación.
  
### Iniciar o detener contenedores
- `docker start [container_id_or_name]` ó `docker start [container_id]`: ejecutar contenedor a partir de su id o su nombre.
   * Ejemplo: `docker start poc_container`.
- `docker stop [container_id]` ó `docker stop [container_id]`: detener contenedor a partir de su id o su nombre.
   * Ejemplo: `docker stop poc_container`.
     
### Acceder al interior de los contenedores en ejecución
- `docker exec -it [container_que_esta_corriendo] [opcion de consola:ejemplo en ubuntu /bin/bash]`: entrar por consola a un container que ya esta corriendo.
   * Ejemplo: `docker exec -it beautiful_jang /bin/bash`
- `docker run -it [nombre_de_la_imagen] [opcion de consola:ejemplo en ubuntu /bin/bash]`: correr en modo interactivo entrando en la consola dentro del container.

## 03.02. Docker - Comandos de contenedores: `docker run = docker pull + docker create + docker start`

### `docker run`: Descargar imagen + Crear contenedor + Iniciar Contenedor: 
- `docker run [nombre_imagen_base:tag]`: un comando que resume todo el proceso.
   * Ejemplo: `docker run python:3.10-slim`.
   * Opciones: 
      - `-d`:Ejecutar en segundo plano (modo daemon, detached), es decir, permite seguir escribiendo cosas en la misma consola sin que haya que parar el contenedor.
      - `-e`: variable de entorno.
      - `--rm`: lo incluimos si queremos el el contenedor no persista (que se elimine cuando se deje detenga el contenedor). Automatically remove the container when it exits.
      - `-it`: Modo interactivo con pseudo-terminal
      - `-p [puerto_host]:[puerto_container]`: sirve para exponer un puerto del contenedor en el host, permitiendo que servicios dentro del contenedor sean accesibles desde fuera.

### Ejemplos de `docker run`
1. `docker run -d -it [nombre_imagen_base:tag]`: levanta el contenedor y lo deja corriendo en modo deatach (running in the background), lo que permite que el contenedor siga corriendo, aunque regremos a la consola principal.
    * Ejemplo: `docker run -d -it python:3.10-slim`.
2. `docker run -it --rm --name=[nombre_para_contenedor] [image:tag] [bash]`: crear un contenedor con un nombre en particular, lo enciende y entra en modo interactivo.
   * Ejemplo: `docker run -it --rm --name=nombre_para_contenedor python:3.10-slim bash`.
  
3. `docker run --name [nombre_que_queremos_dar_al_container] -d [nombre_imagen_base]`: un comando que resume todo el proceso. Descarga la imagen (si es que no existe ya), crea un contenedor a partir de esa imagen y ademas lo inicializa. El comando -d es para que se ejecute en modo `deattached`.
    * Ejemplo: `docker run --name container_a_crear -d -t python:3.10-slim`.
4. `docker run --name [nombre_que_queremos_dar_al_container] --rm -i -t -p [puerto_host]:[puerto_contenedor] -e [nombre_variable_entorno]=[valor_variable_entorno] [imagen_base]`: Crea un contenedor con base a una imagen base ya creada.
5. `docker run --name notebook --rm -i -t -p 8888:8888 -e TYPE=notebook jorgecardona/jupyter`
6. `docker run --name lab --rm -i -t -p 8888:8888 jorgecardona/jupyter`



  
# 04. Docker - Instrucciones Dockerfile

## `docker build`: Crear una imagen a partir de un Dockerfile 
- `docker build -t [nombre_que_queremos_dar_a_la_imagen:tag_que_queremos_dar] [ruta_Dockerfile: por defecto '.' si estamos al mismo nivel]`:
   * Ejemplo: `docker build -t imagen_dockerfile:1.1 .`
   * Opciones: 
      - `-t`: Asigna nombre y etiqueta a la imagen.

## Ejemplo estructura Dockerfile
``` python
FROM python:3.10-slim

COPY folder_test /folder_inside

WORKDIR /folder_inside

RUN apt-get update \
    && apt-get install -y bash \
    && apt-get clean

RUN pip install -r requirements.txt

CMD ["bash"]
```
**NOTA**: conviene que las instucciones que se generen, que son realamnte capas se hagan en el orden de la que menos cambia a la que más cambia para que los diferentes *re-builds* no se tomen tanto tiempo. DOcker reconoce lo que no cambio y lo carga de *builds* anteriores.

### Instrucción 01. FROM: Toma una imagen como base sobre la que se va a construir (dockerfile vs console)
- Si el docker file contiene: `FROM ubuntu:10.04`
- Analogo a ejecutar: `docker pull ubuntu:10.04`

### Instrucción 02. COPY: Copiar archivos al interior del container
- Si el docker file contiene: `COPY [ruta_host] [ruta_container]` ejemplo `COPY app_host /app_cont`
Se hace una copia de los archivos que estan en la ruta_host a la ruta_container.
El el punto de origen del container se toma como su raiz y el punto de origen del host se encuentra al mismo nivel que el Dockerfile.

### Instrucción 03. WORKDIR: Establecer direcrtorio de trabajo al interior del container
- Situa el directorio de trabajo al interior del container en la ruta que se especifique: `WORKDIR [ruta_especificada]`.

### Instrucción 04. RUN: ejecutar sentencias al interior del container en la ruta en el WORKDIR
- `RUN [Sentencias_a ejecutar]` ejemplo `RUN pip install --upgrade pip &&\ pip install -r requirements.txt`.Podemos darnos cuenta que hay un doble `&&` si queremos que la instrucción de la linea de comando se ejecute secuancialmente, es decir, una tras otra. Ejecuta comando en el momento de la construccion de la imagen y se usa típicamente para instalar software, copiar archivos, descomprimir, configurar cosas, etc.

### Instrucción 05. CMD: sentencia que se ejecuta una vez el container se inicializa
- `CMD [sentencia_a_ejecutar]`: por ejemplo `CMD python`. Define el comando por defecto que se ejecuta al iniciar un contenedor. Usualmente se usa para lanzar la aplicación o script principal del contenedor. Se usa en tiempo de ejecución (cuando haces `docker run`). Solo puede existi un comando `CMD` y si hay multiples solo el último tendra efecto.
   * Ejemplo: `CMD ["python3", "app.py"]`.

- Override the CMD set in the image: `docker run <image> <shell-command>`
   * Ejemplo: `docker run ubuntu bash` or `/bin/bash`.
- Override the CMD set in the image and runinteractively: `docker run -it <image> <shell-command>`
   * Ejemplo: `docker run -it ubuntu bash`.

### Instrucción 06. USER: cambia el usuario con el que se van a ejecutar las siguientes capas.

### Instrucción 07. ARG: setea variables de argumento.
```python
FROM ubuntu
ARG project_folder=/projects/pipeline_v3
COPY /local/project/files $project_folder
COPY /local/project/test_files $project_folder/tests
```

### Instrucción 08. ENV: setea variables de entorno.
```python
ENV DB_USER=pipeline_user
CMD psql -U $DB_USER
```

### Instrucción 09. ENTRYPOINT: sentencia XXX
- `ENTRYPOINT ["command", "argument"]`: por ejemplo `ENTRYPOINT ["python", "hello_world.py"]`.

**Nota**: Pueden ejecutarse comando en consola de manera conjunta, es decir: `docker build -t [nombre_que_queremos_dar_a_la_imagen] [ruta_Dockerfile: por defecto '.' si estamos al mismo nivel] && docker run --rm -ti [nombre_que_queremos_dar_a_la_imagen] sh`.
   * Ejemplo : `docker build -t imagen_dockerfile . && docker run --rm -ti imagen_dockerfile`. 

# 05. Docker - Experimentos
## Experimento 01.
- `docker run -i -t -p 8888:8888 -v "PWD":/home --name anaconda3_cpsc322 continuumio/anaconda3:2020.11`
- `jupyter-lab --ip='0.0.0.0' --port=8888 --no-browser --allow-root --notebook-dir=/home`

## Experimento 02. 
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

## Experimento 03. Propio.
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
- `cat [nombre_archivo_texto_a_leer]`: para imprimir y visualizar enconsola el archivo de texto.
- `touch [nombre_archivo_texto_a_crear]`: permite crear un archivo te texto vacio.
- `nano [nombre_archivo_texto_a_editat]`: permite entrar a editar el archivo con `nano`.
   * Comandos nano: 
     - `[crtl+s]`: guardar.
     - `[crtl+x]`: salir.
- `echo ["linea_que_deseamos_adicionar"] >> [archivo_donde_deseamos_adicionar]`: Permite adicionar lineas adicionales a ciertos archivos: ejemplo `echo "RUN apt-get update" >> Dockerfile`.
