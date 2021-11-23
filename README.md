# macime

---

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-green.svg)](https://opensource.org/licenses/) [![GitHub issues](https://img.shields.io/github/issues/soyjorgeprg/macime)](https://github.com/soyjorgeprg/macime/issues) [![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

[![Publicar imagen en DockerHub](https://github.com/soyjorgeprg/macime/actions/workflows/docker.yml/badge.svg)](https://github.com/soyjorgeprg/macime/actions/workflows/docker.yml) [![Publicar imagen en GCR](https://github.com/soyjorgeprg/macime/actions/workflows/gcr.yml/badge.svg)](https://github.com/soyjorgeprg/macime/actions/workflows/gcr.yml) [![Lint python](https://github.com/soyjorgeprg/macime/actions/workflows/lint.yml/badge.svg)](https://github.com/soyjorgeprg/macime/actions/workflows/lint.yml) 

[![Build Status](https://app.travis-ci.com/soyjorgeprg/macime.svg?branch=hito4)](https://app.travis-ci.com/soyjorgeprg/macime) [![Ejecutar test en Docker](https://github.com/soyjorgeprg/macime/actions/workflows/ci.yml/badge.svg)](https://github.com/soyjorgeprg/macime/actions/workflows/ci.yml) [![CircleCI](https://circleci.com/gh/soyjorgeprg/macime/tree/hito4.svg?style=shield)](https://circleci.com/gh/soyjorgeprg/macime/tree/hito4) 

---

La funcionalidad de este aplicativo es encontrar la gasolinera de combustibles alternativos más cercana o rentable para tu localización actual, este proyecto será desarrollado para la asigna de [Cloud Computing](https://github.com/JJ/CC-21-22) en el [Master de Ingeniería Informática](https://masteres.ugr.es/ingenieria-informatica/) de la [Universidad de Granada](https://www.ugr.es/).


## Tabla de contenidos del proyecto

* [Descripción del problema](#descripcion-del-problema)
* [Gestion de las pruebas](#gestion-de-las-pruebas)
* [Despliegue de las pruebas en contenedores](#despliegue-de-las-pruebas-en-contenedores)
* [Integración continua](#integracion-continua)
* [Documentacion hitos asignatura](#documentacion-hitos-asignatura)

### Descripción del problema

Para conocer más acerca de las motivaciones de este proyecto dirijase a la [documentación](https://github.com/soyjorgeprg/macime/blob/main/docs/infoProyecto.md) y sobre como se configuró este [proyecto](https://github.com/soyjorgeprg/macime/blob/main/docs/primerosPasos.md)

### Gestion de las pruebas

Primeramente elegimos un task runner para automatizar aquellas tareas recurrentes en el proyecto (ejecución de tests e instalar dependencias). Para asegurarnos que cada una de las nuevas funcionalidades tiene la salida esperar y el resto mantienen su funcionalidad se han desarrollado una serie de pruebas unitarias. Las explicaciones de como ejecutar los test se encuentran en la [documentación](https://github.com/soyjorgeprg/macime/blob/main/docs/tests.md). Si se quiere saber sobre la decisión del task runner, marco de pruebas y biblioteca de aserciones dirijase [aquí](https://github.com/soyjorgeprg/macime/blob/main/docs/gestionTests.md).

### Despliegue de las pruebas en contenedores

Implementamos un entorno neutro para las pruebas mediante la creación de un contenedor donde poder ejecutarlas. Para saber más acerca de esta decisión dirijase a la [documentación](https://github.com/soyjorgeprg/macime/blob/main/docs/docker.md)

### Integración continua

Automatizamos las pruebas para que se ejecuten cada vez que realicemos un push sobre nuestro proyecto para así asegurarnos de su corrección, más información [aquí](https://github.com/soyjorgeprg/macime/blob/main/docs/ci.md). Además se ha añadido una [GitHub Action](https://github.com/soyjorgeprg/macime/blob/main/.github/workflows/lint.yml) para realizar un análisis estático del código y seguir las buenas prácticas actuales.

---

#### Documentación hitos asignatura 

En esta sección se mostrará aquella documentación del proyecto referente a cada uno de los hitos de la asignatura:

* HITO 0: [Primeros pasos](https://github.com/soyjorgeprg/macime/blob/main/docs/primerosPasos.md) y [descripcion del proyecto](https://github.com/soyjorgeprg/macime/blob/main/docs/infoProyecto.md)
* HITO 1: [Hitos](https://github.com/soyjorgeprg/macime/milestones) e [issues](https://github.com/soyjorgeprg/macime/issues)
* HITO 2: [Explicación elecciones](https://github.com/soyjorgeprg/macime/blob/main/docs/gestionTests.md) y [ejecución de los tests](https://github.com/soyjorgeprg/macime/blob/main/docs/tests.md)
* HITO 3: [Despliegue de pruebas en contenedores](https://github.com/soyjorgeprg/macime/blob/main/docs/docker.md)
* HITO 4: [Explicación CI](https://github.com/soyjorgeprg/macime/blob/main/docs/ci.md)


[//]: https://geoportalgasolineras.es/#/Descargas
