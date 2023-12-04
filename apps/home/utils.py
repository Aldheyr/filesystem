import os
import psutil


def listar_discos():
    discos = []
    for particion in psutil.disk_partitions():
        if 'fixed' in particion.opts:
            try:
                uso_disco = psutil.disk_usage(particion.mountpoint)
                discos.append({
                    "disk": particion.device[:-2],
                    "device": particion.device,
                    "mountpoint": particion.mountpoint,
                    "fstype": particion.fstype,
                    "total": round((uso_disco.total) / (1024**3), 2),
                    "used": round((uso_disco.used) / (1024**3), 2),
                    "free": round((uso_disco.free) / (1024**3), 2),
                    "percent": uso_disco.percent
                })
            except PermissionError:
                continue
    return discos


def listar_contenido_carpeta(ruta):
    if not os.path.exists(ruta):
        return "La ruta no existe"
    if not os.path.isdir(ruta):
        return "La ruta no es una carpeta"

    contenido = os.listdir(ruta)
    resultado = []

    for elemento in contenido:
        ruta_completa = os.path.join(ruta, elemento)
        if os.path.isfile(ruta_completa):
            tipo = 'Archivo'
        elif os.path.isdir(ruta_completa):
            tipo = 'Carpeta'
        else:
            tipo = 'Otro'

        resultado.append({
            'nombre': elemento,
            'tipo': tipo
        })

    return resultado
