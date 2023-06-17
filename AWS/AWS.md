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

# EC2. Acceder a S3 desde EC2.
1. Acceder al terminal de la instancia en la que deseamos trabajar.
2. Actualizar la lista de paquetes disponibles en los repositorios configurados en tu sistema con el comando `sudo apt update`.
3. Verificar que tenemos el CLI de amazon con `aws --version`. Si no esta instalada instalar con `sudo apt install awscli`. Conformar con `y`para finalizar la instalación.
4. 













