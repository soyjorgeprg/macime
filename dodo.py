from doit.action import CmdAction

DOIT_CONFIG = {
        'backend': 'json',
        'dep_file': '/app/test/doit-db.json',
    }

def task_pruebas():
    """Lanzamiento de los test unitarios del sistema"""

    def pruebas():
        return "pytest"

    return {
            'actions': [CmdAction(pruebas)],
            'verbosity': 2,
            }


if __name__ == '__main__':
    import doit
    doit.run(globals())
