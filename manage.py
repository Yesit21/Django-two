#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taller_formularios_nombre_estudiantes.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # If user runs `python manage.py runserver` without a port, default to 8001
    if 'runserver' in sys.argv:
        try:
            idx = sys.argv.index('runserver')
        except ValueError:
            idx = -1
        if idx != -1:
            # look for a non-option argument after 'runserver' (the port/addr)
            found_target = False
            for a in sys.argv[idx+1:]:
                if not a.startswith('-'):
                    found_target = True
                    break
            if not found_target:
                # no port/addr provided, append default port 8001
                sys.argv.insert(idx+1, '8001')

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
