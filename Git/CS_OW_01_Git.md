# GIT: CHEATSHEET PROPIO

## 01. Git Bash
-  `ctrl + l` or `clear` : Limpiar la pantalla
-  `ctrl + c` : Detener ejecución en curso
-  `exit` : Salir y cerrar consola
- `cd ~` : Ir al directorio raiz (donde por defecto se encuentran los documentos)
- `cd /` : Ir al directorio raiz (donde esta alojado GIT en el disco)
- `ls -la` : Enlistar los archivos del directorio actual
- `cd /c/Users/Fiodor/00_Github/MLOps_MVP_01` : Cambiar de directorio específico
- `cd [foder_name]` : Avanzar un nivel en directorios
- `cd ..` : Retroceder un nivel en directorios

## 02. Configurar Git
- `git config --list` : Muestra parametros de configuracion de git (entre ellos: user.name y el user.email)
- `git config --global user.name [user_name]` : Setea el parametro de configuración user.name
- `git config --global user.mail [user_mail]` : Setea el parametro de configuración user.mail
- `git config --global init.defaultBranch [main]`: Setea el parametro de configuración init.defaultBranch en la rama `main`

## 03. Conectar repositorios: Local - Github
- `git init` : Inicializa el repositorio actual como un repositorio de git (lo empieza a trackear)
- `git remote add origin https://github.com/alexandergribenchenko/MLOps_MVP_XXX.git`: Sube repositorio local a repositorio en github
- `git clone https://github.com/alexandergribenchenko/Pycaret_Exploration.git`: baja repositorio de github y lo vincula en local (el repositorio de github se genera como una subcarpeta dentro de la carpeta local en la que estemos ubicados). 
- `git status` : Muestra que que archivos se han modificado en el working directory para agregarlos al commit.
- `git add .` : Adicionar todos lo archivos a la staging area para posteriormente poder hacer el commit
- `git commit -m 'Primer commmit'` : Se genera el commit
- `git push origin main` : Empujar y sinconizar los archivos de local a github
- `git pull origin main` : Halar y sinconizar los archivos de github a local
