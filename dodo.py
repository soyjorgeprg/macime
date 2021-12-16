from doit.action import CmdAction

DOIT_CONFIG = {
    "backend": "json",
    "dep_file": "/tmp/doit-db.json",
}

def task_build():
    """Generacion de ficheros en caso de que sea necesario"""

    def build():
        return "echo Caracteristica no necesaria"

    return {
        "actions": [CmdAction(build)],
        "verbosity": 2,
    }

def task_install():
    """Preparación del entorno de ejecución"""

    def mensaje():
        return "echo Hecho"

    return {
        "actions": [CmdAction(mensaje)],
        "verbosity": 2,
    }

def task_test():
    """Lanzamiento de los test unitarios del sistema"""

    def pruebas():
        return "pytest"

    return {
        "actions": [CmdAction(pruebas)],
        "verbosity": 2,
    }


def task_lint():
    """Comprobacion estatica del codigo (Lint)"""

    def lint():
        return "black ."

    return {
        "actions": [CmdAction(lint)],
        "verbosity": 2,
    }


def task_dependencias():
    """Instalacion de las dependencias correspondientes al proyecto"""

    def install_poetry():
        return "pip install poetry"

    def config_poetry():
        return "poetry config virtualenvs.create false"

    def install_dependencies():
        i = install_poetry() + " && "
        c = config_poetry() + " && "
        return i + c + "poetry install"

    return {
        "actions": [CmdAction(install_dependencies)],
        "verbosity": 1,
    }


if __name__ == "__main__":
    import doit

    doit.run(globals())
