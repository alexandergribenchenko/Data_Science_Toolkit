# Envio attach multi usuario

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Crear objeto de mensaje
mensaje = MIMEMultipart()

# Agregar destinatarios
destinatarios = ['destinatario1@example.com', 'destinatario2@example.com', 'destinatario3@example.com']
mensaje['To'] = ", ".join(destinatarios)

# Agregar el asunto del correo electrónico
mensaje['Subject'] = 'Asunto del correo electrónico'

# Agregar el cuerpo del correo electrónico
cuerpo = 'Este es el cuerpo del correo electrónico.'
mensaje.attach(MIMEText(cuerpo, 'plain'))

# Establecer detalles del servidor SMTP
servidor_smtp = 'smtp.gmail.com'
puerto_smtp = 587
usuario_smtp = 'tu_correo_electronico@gmail.com'
contrasena_smtp = 'tu_contrasena'

# Iniciar sesión en el servidor SMTP
server = smtplib.SMTP(servidor_smtp, puerto_smtp)
server.starttls()
server.login(usuario_smtp, contrasena_smtp)

# Enviar correo electrónico
server.sendmail(usuario_smtp, destinatarios, mensaje.as_string())

# Cerrar sesión en el servidor SMTP
server.quit()
```
