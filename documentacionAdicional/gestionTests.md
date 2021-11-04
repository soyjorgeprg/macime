# Informacion del proyecto 

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-green.svg)](https://opensource.org/licenses/) [![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

## Tabla de contenidos


* [Gestor de tareas](#gestor-de-tareas)
* [Biblioteca de aserciones](#biblioteca-de-aserciones)
* [Marco de pruebas](#marco-de-pruebas)

### Gestor de Tareas

Como gestor de tareas se ha elegido [doit](https://github.com/pydoit/doit) para facilitar la gestión de tareas de una manera simple y sencilla, sin ser necesarias muchas lineas de código o configuración. Además ha sido marcado con un estrella en GitHub por [1116 usuarios](https://github.com/pydoit/doit/stargazers) y tiene alrededor de [48 contribuidores](https://github.com/pydoit/doit/graphs/contributors).

También se barajó la posibilidad de [dramatiq](https://github.com/Bogdanp/dramatiq) pero a priori me resultó una herramienta mucho más compleja de usar y configurar y por tanto quedó descartada.

### Biblioteca de aserciones

Se ha decidido que los test serán de tipo TDD ya que será más sencillo generar los test para este proyecto. Aunque la diferencia entre ambas no es grande (más el enfoque, TDD los test definen como debe funcionar el código y BDD se definen los test por el comportamiento esperado) me siento más cómodo con los test TDD.

[unittest](https://docs.python.org/3/library/unittest.html) ha sido escogida como librería de test unitarios debido a que es de gran confianza al tratarse de una de las principales librerías y tener una gran cantidad de funciones para diferentes aserciones. Un punto a favor fue también la buena documentación que encontré de la librería, con ejemplos y detallada.

Se consideraron otras opciones como [grappa](https://github.com/grappa-py/grappa) pero es BDD además el hecho de tener tan pocas estrellas, la documentación más sencilla a la hora de funciones y clases propias y que llevasen un año sin realizar un commit fue lo que me hizo descartarla.

### Marco de pruebas

El marco de pruebas que ha sido finalmente seleccionado ha sido [pytest](https://docs.pytest.org/en/6.2.x/). La razón principal de esta elección ha sido la claridad y simpleza con la que se muestran que test han fallado y dónde lo han hecho, facilitando mucho la mejora de los test y su ejecución.

