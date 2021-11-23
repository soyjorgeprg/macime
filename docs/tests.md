## Gestion de los test

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-green.svg)](https://opensource.org/licenses/) [![GitHub issues](https://img.shields.io/github/issues/soyjorgeprg/macime)](https://github.com/soyjorgeprg/macime/issues) [![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

Hasta ahora podiamos gestionar los test de manera local mediante el uso directo del [task manager](https://github.com/soyjorgeprg/macime/blob/main/docs/gestionTests.md#gestor-de-tareas) impletado, doit, o mediante la [imagen Docker](https://hub.docker.com/repository/docker/soyjorgeprg/macime) que hemos creado como se ve en el ejemplo de arriba. Desde ahora también hemos implementado CI (Integracion Continua) y por lo tanto con cada commit que realicemos en este repositorio se lanzarán los test en 4 herramientas de integración continua. Más información acerca de esto [aquí](https://github.com/soyjorgeprg/macime/blob/hito4/docs/ci.md). 

A continuación se detallán las maneras de ejecutar los tests en local. Existe un primer paso común que es descargarse el repositorio y acceder a él:

```
PortatilJorge:  ~/proyecto
git clone git@github.com:soyjorgeprg/macime.git && cd macime

```
### Mediante task manager

```
PortatilJorge:  ~/macime  |main ✓|
→ doit dependencias tests
.  dependencias
.  tests
============================= test session starts ==============================
platform linux -- Python 3.8.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /home/jorgeprg/.pyenv/versions/3.8.12/bin/python3.8
cachedir: .pytest_cache
rootdir: /home/jorgeprg/macime, configfile: pyproject.toml, testpaths: test
collecting ... collected 5 items

test/tests.py::Pruebas::test_cargas PASSED                               [ 20%]
test/tests.py::Pruebas::test_distancia PASSED                            [ 40%]
test/tests.py::Pruebas::test_gestiongasolineras PASSED                   [ 60%]
test/tests.py::Pruebas::test_localizacion PASSED                         [ 80%]
test/tests.py::Pruebas::test_mejorestacionservicio PASSED                [100%]

============================== 5 passed in 0.12s ===============================
```

### Mediante contenedor

```
PortatilJorge:  ~/macime  |main ✓|
→ docker run -t -v `pwd`:/app/test soyjorgeprg/macime:latest
.  dependencias
.  tests
============================= test session starts ==============================
platform linux -- Python 3.9.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /app/test, configfile: pyproject.toml, testpaths: test
collecting ... collected 5 items

test/tests.py::Pruebas::test_cargas PASSED                               [ 20%]
test/tests.py::Pruebas::test_distancia PASSED                            [ 40%]
test/tests.py::Pruebas::test_gestiongasolineras PASSED                   [ 60%]
test/tests.py::Pruebas::test_localizacion PASSED                         [ 80%]
test/tests.py::Pruebas::test_mejorestacionservicio PASSED                [100%]

============================== 5 passed in 0.29s ===============================

```

