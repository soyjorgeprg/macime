# Informacion del proyecto 

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-green.svg)](https://opensource.org/licenses/) [![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

## Tabla de contenidos


* [Gestor de tareas](#gestor-de-tareas)
* [Biblioteca de aserciones](#biblioteca-de-aserciones)
* [Marco de pruebas](#marco-de-pruebas)
* [Eleccion final](#eleccion-final)

Las razones que se van a seguir en los 3 casos serán las mismas: altamente utilizadas por la comunidad, facilidad de uso e instalacion y que mantenga el soporte actualmente.

### Gestor de Tareas

Como gestor de tareas se ha elegido [doit](https://github.com/pydoit/doit) para facilitar la gestión de tareas de una manera simple y sencilla, sin ser necesarias muchas lineas de código o configuración. Además ha sido marcado con un estrella en GitHub por [1116 usuarios](https://github.com/pydoit/doit/stargazers) y tiene alrededor de [48 contribuidores](https://github.com/pydoit/doit/graphs/contributors). Este gestor cumple los 3 criterios que nos habiamos marcado, como he dicho anteriormente es bastante usado por la comunidad, ofrece una interfaz tanto de instalacion como de configuración sencilla y por último sigue manteniendo soporte, el último commit se realizó en julio de este mismo año, también se ofrece soporte personalizado a través de [xs:code](https://xscode.com/schettino72/doit).

Se revisaron otros gestores pero por alguna razón fueron descartados, los expondré a continuación. Se barajó la posibilidad de [dramatiq](https://github.com/Bogdanp/dramatiq) pero a priori me resultó una herramienta mucho más compleja de usar y configurar y por tanto quedó descartada, es decir, no cumple una de las razones que nos habiamos marcado. La otra opción que se contempló fue [pypyr](https://github.com/pypyr/pypyr/) siendo una candidata muy factible ya que cumple 2 de las 3 razones expuestas fallando en ser altamente utilizada (baso esta opinión en el numero de estrellas en GitHub)

### Biblioteca de aserciones

Se ha decidido que los test serán de tipo TDD ya que será más sencillo generar los test para este proyecto. Aunque la diferencia entre ambas no es grande (más el enfoque, TDD los test definen como debe funcionar el código y BDD se definen los test por el comportamiento esperado) me siento más cómodo con los test TDD.

[unittest](https://docs.python.org/3/library/unittest.html) ha sido escogida como librería de test unitarios debido a que es de gran confianza al tratarse de una de las principales librerías y tener una gran cantidad de funciones para diferentes aserciones. Un punto a favor fue también la buena documentación que encontré de la librería, con ejemplos y detallada. Se trata de una libreria que está integrada dentro del propio Python y por tanto el mantenimiento se da por descontado.

Entre las demás bibliotecas que se consideraron entraron otras opciones como [grappa](https://github.com/grappa-py/grappa) pero es BDD además el hecho de tener tan pocas estrellas, la documentación más sencilla a la hora de funciones y clases propias y que llevasen un año sin realizar un commit fue lo que me hizo descartarla, además se descartó por decisiones técnicas ya que es completamente diferente al propio lenguaje por lo que sería más complejo en algunos casos.

### Marco de pruebas

Dentro de todos los marcos de pruebas que se revisaron el que ha sido finalmente seleccionado ha sido [pytest](https://docs.pytest.org/en/6.2.x/). Este cumplía las 3 razones que nos habiamos marcado al comienzo de esta evaluación de las herramientas. También fue muy importante el hecho de la claridad y simpleza con la que se muestran que test han fallado y dónde lo han hecho, facilitando mucho la mejora de los test y su ejecución.

De entre los demás marcos analizados destacaré un par de opciones que se encontraron. Nos encontramos con [nose2](https://github.com/nose-devs/nose2) que se descartó nada más leer la documentación ya que el propio equipo recomienda que para usuarios no expertos [pasarse a pytest](https://github.com/nose-devs/nose2#nose2-vs-pytest). Al igual que pasó con los gestores de tareas hubo una herramienta que se quedó cerca como fue [RobotFramework](https://github.com/robotframework/robotframework) en este caso se descartó porque la documentación encontrada parecía mucho más complejo y la curva de aprendizaje podía ser lenta.

### Eleccion final

Por tanto la elección en cada uno de los campos es la siguiente:

* Gestor de tareas: doit, configurado en [dodo.py](https://github.com/soyjorgeprg/macime/blob/d44054bde0a8021859a32989c621b41dc4a15f32/dodo.py)
* Biblioteca de aserciones: unittest
* Marco de pruebas: pytest, configurado en [pytest.ini](https://github.com/soyjorgeprg/macime/blob/d44054bde0a8021859a32989c621b41dc4a15f32/pytest.ini)


