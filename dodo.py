from doit.action import CmdAction

def task_pruebas():
    """Lanzamiento de los test unitarios del sistema"""

    def pruebas():
        return "pytest src/tests/tests.py"

    return {
            'actions': [CmdAction(pruebas)],
            'verbosity': 2,
            }


if __name__ == '__main__':
    import doit
    doit.run(globals())
