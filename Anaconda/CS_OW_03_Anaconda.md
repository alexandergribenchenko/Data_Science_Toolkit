# CHEATSHEET ANACONDA

- `conda info` : Entrega toda la información de conda (en particular las rutas donde fue instalado. Por defecto queda instalada en  `active env location : C:\ProgramData\Anaconda3`).
- `conda --version` : Conocer la versión de conda


# Conocer la versión de pip
pip --version

# Listar todos los ambientes de conda
conda env list

# Crear un nuevo ambiente en conda llamado nombre_del_ambiente
conda create -n nombre_del_ambiente

# Crear un nuevo ambiente en conda en una ruta específica
conda create --prefix C:\ProgramData\Anaconda3\envs\nombreambiente

# Eliminar un ambiente en conda llamado nombre_del_ambiente
conda env remove -n nombre_del_ambiente

# Activar un ambiente en conda llamado nombre_del_ambiente
conda activate nombre_del_ambiente

# Activar el ambiente base de conda
conda activate

# Listar todas las librerías de conda instaladas (en el ambiente actual)
conda list

# Instalar una librería con conda (en el ambiente actual) llamada nombre_de_la_libreria
conda install nombre_de_la_libreria
conda install jupyterlab
conda install -c conda-forge prophet

# Instalar requirements desde un archivo con conda (en el ambiente actual)
conda install --file requirements.txt

# Instalar una librería con pip (en el ambiente actual) llamada nombre_de_la_libreria
pip install nombre_de_la_libreria

# Actualizar una librería en conda llamada nombre_de_la_libreria
conda update nombre_de_la_libreria

#############################################################################################
TERMINAL
# Ejecutar juyterlab en un entorno especifico y abrir en un folder especifico
# (se debe tener instalado jupyterlab en ese entorno en específico)
(AV_01_rutas) C:\Users\2015901\Desktop\PY_AV_01_Rutas>jupyter lab

# Cambiar entre discos duros en el terminal
(env_01_finanzas) C:\Users\Fiodor>D:
(env_01_finanzas) D:\>cd D:\Code\Finanzas







