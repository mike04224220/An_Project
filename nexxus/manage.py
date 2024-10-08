#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ

def main():
    """Run administrative tasks."""
    # Inicializar environ y cargar el archivo .env antes de verificar la variable
    env = environ.Env()
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_path):
        environ.Env.read_env(env_path)

    # Establecer la configuración predeterminada de Django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nexxus.settings")

    # Verificar si DJANGO_DB_URL está configurada
    if "DJANGO_DB_URL" not in os.environ:
        print("ADVERTENCIA: La variable de entorno DJANGO_DB_URL no está configurada.")
    else:
        print(f"DJANGO_DB_URL está configurada: {os.environ['DJANGO_DB_URL']}")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()