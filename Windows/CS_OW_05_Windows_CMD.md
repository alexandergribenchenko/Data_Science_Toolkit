# WINDOWS CMD: CHEATSHEET PROPIO

- `cls` : Limpiar pantalla
- `sfc /scannow` : Reparar archivos del sistema
- `DISM /Online /Cleanup-Image /ScanHealth` : Analizar component store
- `DISM /Online /Cleanup-Image /RestoreHealth` : Reparar component store
- `DISM /Online /Cleanup-Image /StartComponentCleanup` : Limpiar componentes viejos
- `chkdsk /scan` : Escanear sistema de archivos
- `wmic diskdrive get status` : Revisar estado SMART del disco
- `winver` : Ver versión/build de Windows
- `eventvwr` : Abrir Visor de Eventos
- `taskmgr` : Abrir Administrador de tareas

# WINDOWS UPDATE RESET

- `net stop wuauserv` : Detener Windows Update
- `net stop bits` : Detener BITS
- `net stop cryptsvc` : Detener servicios criptográficos
- `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` : Resetear caché de updates
- `ren C:\Windows\System32\catroot2 catroot2.old` : Resetear catálogos de updates
- `net start wuauserv` : Iniciar Windows Update
- `net start bits` : Iniciar BITS
- `net start cryptsvc` : Iniciar servicios criptográficos

# REPARACIÓN IN-PLACE

- Descargar ISO oficial de Windows
- Montar ISO
- Ejecutar `setup.exe`
- Elegir `Keep personal files and apps`
- Elegir `Not right now` en updates

# APRENDIZAJES

- SFC limpio ≠ DISM sano
- DISM puede fallar aunque Windows funcione
- Windows Update inconsistente puede causar lentitud
- Adobe Creative Cloud puede causar errores al apagar
- Reparación in-place arregla muchos problemas internos
