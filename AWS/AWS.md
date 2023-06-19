# EC2. Crear una instancia
1. Abrir el servicio de EC2.
2. Ir a la pestaña lateral izquierda `Instances`.
3. Click en `Lounch instances`.
4. Establecer el `Bucket name` (Es único para dentro del universo de los buckets de AWS): instance-test-c1-de
5. Elegir el `OS Image` como ubuntu (y la version que este en el free tier).
6. Elegir el tipo de instancia: t2.micro que es la que esta en el free tier.
7. Crear nuestra llave de seguridad `Key pair` (dar un nombre, ejemplo key-pair-EC2-test-c1-de, usar el formato `.pem` y las opciones que estan por defecto. Guardar este archivo en nuestro computador local.).
8. Network settings: crear un grupo de seguridad security-group-EC2-test-c1-de. 
9. Configure storage: 20GB (recordar que free tier va hasta 30).
10. Crear instnacia y verificar todo ok desde la pestaña lateral izquierda `Instances`. L anueva isntancia debe decir `running`.

# EC2. Conectar a una instancia desde la nube de AWS
1. Abrir el servicio de EC2.
2. Ir a la pestaña lateral izquierda `Instances`.
3. Seleccionar la instancia de interes.
4. Dar click en conectar.
5. Seleccionar EC2 Instance connect.
6. Conectar. 
7. Se desplegara la consola donde podemos ejecutar cualquier tipo de comando. Podemos verificar por ejemplo que python se encuentra instalado por defecto ejecutando `python3 --version`.

# S3. Crear Bucket
1. Abrir el servicio de S3 
2. Ir a la pestaña lateral izquierda `Bukets`.
3. Click en crea bucket.
4. Establecer el `Bucket name` (Es único para dentro del universo de los buckets de AWS): bucket-test-c1-de
5. Establecer la region (por defecto trabajare con us-east 2)
6. Dejar las opciones restantes por defecto.
7. Crear bucker y verificar todo ok desde la pestaña lateral izquierda `Bukets`.

# IAM. Crear roles de acceso a S3
1. Abrir el servicio de IAM. 
2. Ir a la pestaña lateral izquierda `Roles`.
3. Click en crear rol. 
4. Step 01: Seleccionar AWS service y Use Case como EC2.
5. Step 02: Byscar S3 y seleccionar AmazonS3FullAccess.
6. Step 03: Darle nombre al rol (ejemplo: role-test-S3-de-c1). 
7. Opciones restantes por defecto.
8. Crear rol.

# EC2. Escribir archivo desde EC2 hacia S3.
1. Acceder al terminal de la instancia en la que deseamos trabajar.
2. Actualizar la lista de paquetes disponibles en los repositorios configurados en tu sistema con el comando `sudo apt update`.
3. Verificar que tenemos el CLI de amazon con `aws --version`. Si no esta instalada instalar con `sudo apt install awscli`. Conformar con `y`para finalizar la instalación.
4. Vamos a la interfaz grafica de EC2 y seleccionamos nuestra instancia, y damos click en la esquina superioro derecha en acciones>security>Modify IAM role y selecionamos el rol que habiamos creado en IAM, y seleccionamos `update AIM role`.
5. Cremos una carpeta con el comando `mkdir test_input_folder` e ingresamoa a ella cn `cd test_input_folder`. 
6. Creemos un archivo al interior de ella con `sudo nano hello.txt`. Recordar guardar en nano con `ctrl O' y calir con `ctrl X`. podemos leer el archivo con `cat hello.txt`
7. COpiar un archivo puntual que esta en EC2 a S3: `aws s3 cp hello.txt s3://bucket-test-c1-de`.
8. Sincronizar una carpeta que esta en nuestro EC2 con una carpeta en S3: `aws s3 sync /home/ubuntu/test_input_folder s3://bucket-test-c1-de/test_syncro_folder`

# EC2. Leer un archivo de S3 desde EC2.
1. Acceder al terminal de la instancia en la que deseamos trabajar.
2. Leer los archivos que tenemso en el bucket:`aws s3 ls s3://bucket-test-c1-de`, el ultimo es simplemente el nombre del bucket.

# LINUX. 
1. Descargar un archivo de una URL en especifico: `wget replace_url'.
2. 













