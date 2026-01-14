import os
import sys
import django
from django.core.management import call_command

def restore():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autopartespro.settings")
    django.setup()

    print("--> INICIANDO RESTAURACION DE DATOS...")
    try:
        # Intentamos cargar los datos
        call_command("loaddata", "production_data.json", verbosity=2)
        print("--> RESTAURACION EXITOSA: Datos cargados correctamente.")
    except Exception as e:
        # Si falla, imprimimos el error pero NO detenemos el server para que pueda al menos arrancar
        print(f"--> ERROR CRITICO AL RESTAURAR: {e}")
        # Opcional: si quieres que falle el deploy si no carga datos, descomenta la siguiente linea:
        # sys.exit(1)

if __name__ == "__main__":
    restore()
