# GIT: CHEATSHEET PROPIO

## 01. Git Bash
- `cd  /c/X_TCS_Documents/Github` : cambiar a repositorio específico.

## 02. Configurar Git
- `git config --list` : Muestra parametros de configuracion de git (entre ellos: user.name y el user.email)
- `git config --global user.name [user_name]` : Setea el parametro de configuración user.name
- `git config --global user.mail [user_mail]` : Setea el parametro de configuración user.mail
- `git config --global init.defaultBranch [main]`: Setea el parametro de configuración init.defaultBranch en la rama `main`

## 03. Conectar repositorios: Local - Github
- `git init` : Inicializa el repositorio actual como un repositorio de git (lo empieza a trackear)
- `git remote add origin https://github.com/alexandergribenchenko/MLOps_MVP_XXX.git`: Sube repositorio local a repositorio en github
- `git clone https://github.com/alexandergribenchenko/Pycaret_Exploration.git`: baja repositorio en github y lo vincula en local (el repositorio de github se genera como una subcarpeta dentro de la carpeta local en la que estemos ubicados). 
- `git status` : Muestra que que archivos se han modificado en el working directory para agregarlos al commit.
- `git add .` : Adicionar todos lo archivos a la staging area para posteriormente poder hacer el commit
- `git commit -m 'Primer commmit'` : Se genera el commit
- `git push origin main` : Empujar y sinconizar los archivos de local a github
- `git pull origin main` : Halar y sinconizar los archivos de github a local
