# CHEATSHEET ANACONDA

# 01. Acciones generales de conda
- `conda info` : Entrega toda la información de conda (en particular las rutas donde fue instalado. Por defecto queda instalada en  `active env location : C:\ProgramData\Anaconda3`).
- `conda --version` ó `conda -V : Conocer la versión de conda
- `pip --version` : Conocer la versión de pip
- `conda env list` : Listar todos los ambientes de conda
- `conda -h` ó `conda --help`: Ayuda de conda
- `conda update --prefix C:\Users\2015901\Anaconda3 anaconda`: actualizar anaconda
- `conda update --prefix C:\Users\2015901\Anaconda3 conda`: actualizar conda

# 02. Gestionar ambientes con conda
- `conda create -n nombre_del_ambiente` : Crear un nuevo ambiente en conda llamado nombre_del_ambiente ubicada por defecto en el directorio `C:\ProgramData\Anaconda3\envs\`
- `conda create -p C:\ProgramData\Anaconda3\envs\nombreambiente`: Crear un nuevo ambiente de conda en una ruta específica
- `conda env remove -n nombre_del_ambiente`: Eliminar un ambiente en conda llamado nombre_del_ambiente
- `conda activate`: Activar el ambiente base de conda
- `conda activate nombre_del_ambiente`: Activar un ambiente de conda llamado nombre_del_ambiente que esta por defecto en  `C:\ProgramData\Anaconda3\envs\`
- `conda activate C:\ProgramData\Anaconda3\envs\nombreambiente\`: Activar un ambiente de conda ubicado en una ruta específica.
- `conda list`: Listar todas las librerías de conda instaladas (en el ambiente actual)
- `pip list`: Listar todas las librerías de pip instaladas (en el ambiente actual)
- `conda env create -f path_archivo.yml`: Crear un nuevo ambiente en conda desde un archivo `.yml`
- `conda deactivate`: desactivar ambiente actual y volver al ambiente base.

# 03. Instalar o actualizar librerías 
- `conda install nombre_de_la_libreria`: instalar librería con conda (en el ambiente actual) llamada nombre_de_la_libreria.
Ejemplos: `conda install jupyterlab` y `conda install -c conda-forge prophet`.
- `conda install --file requirements.txt`: Instalar requirements desde un archivo con conda (en el ambiente actual).
- `pip install nombre_de_la_libreria`: Instalar una librería con pip (en el ambiente actual) llamada nombre_de_la_libreria
- `conda update nombre_de_la_libreria`: Actualizar una librería en conda llamada nombre_de_la_libreria

# 04. Anaconda Prompt
- `(AV_01_rutas) C:\Users\2015901\Desktop\PY_AV_01_Rutas>jupyter lab`: Ejecutar **juyterlab** en un entorno especifico y abrir en un folder especifico.
- `(env_01_finanzas) C:\Users\Fiodor>D:`: Cambiar entre discos duros en el terminal


# 05. Enlaces
https://es.stackoverflow.com/questions/124929/conda-no-se-reconoce-como-un-comando-interno-o-externo-programa-o-archivo-por





