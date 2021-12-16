## Gestion de los test

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-green.svg)](https://opensource.org/licenses/) [![GitHub issues](https://img.shields.io/github/issues/soyjorgeprg/macime)]    (https://github.com/soyjorgeprg/macime/issues) [![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

Para poder llevar nuestra aplicación a la nube vamos a establecer una serie de herramientas que nos ayudaran a mantener el aplicativo en la nube y registrar que ocurre en el aplicativo.Estas herramientas servirán para generar mensajes de logs para tener un conocimiento exhaustivo de lo que ocurre en la ejecución del sistema, también integraremos una configuración general para todo el aplicativo replicable en cada una de sus instancias. Además implementaremos un API sobre nuestro código para poder acceder a nuestros recursos.

### Logging

Para generar mensajes de registro que nos indiquen que ocurre en la ejecucción del programa queremos un framework sencillo, que este adecuado a las nuevas características del lenguaje y que tenga buena integración con todas las posibles herramientas que podamos necesitar. Realizamos una revisión de varias librerías buscando la mejor opción para nuestros criterios.

La primera que vimos fue la propia librería del __core__ del lenguaje. Es bastante sencilla de implementarla y permite realizar todas las acciones que necesitamos (escribir los mensajes por pantalla, en un fichero, disponer de diversos niveles de avisos, etc.). Además al ser parte del propio lenguaje en sí por lo que su integración con otras herramientas está descontada.

También se analizaron las herramientas de [loguru](https://github.com/Delgan/loguru) y [logbook](https://logbook.readthedocs.io/en/stable/), ambas herramientas sencillas de usar. Para el caso de loguru con la única función de add consiguen toda la funcionalidad, tanto formatear la salida del registro, como añadir los ficheros donde se puede imprimir asi como cualquier configuración. Mientras, logbook funciona de una manera mucho más parecida a la librería del sistema (Logger, Handler, etc.). Hemos descartado ambas opciones porque no amplían funcionalidad frente la librería del sistema y tendrá, por descontado, una mejor integración y mantenimiento la librería del sistema que una externa.

### API

Para la decisión del framework API hemos tomado en consideración varios puntos, primeramente se descartaron aquellos que fueran grandes, con muchas librerías y dependencias puesto que nosotros buscamos algo ligero y simple, por tanto, [Django REST](https://www.django-rest-framework.org/) que a priori podría parecer la mejor opción debido a su implantación en el mercado, su funcionalidad y mantenimiento queda descartado. Por tanto, en nuestro framework buscamos facilidad a la hora de testear su funcionamiento y que tenga la posibilidad de ser asincrono aprovechando así toda la versatilidad del lenguaje.

Se revisaron 3 micro-frameworks bastante interesantes: [Fast API](https://github.com/tiangolo/fastapi), [BlackSheep](https://github.com/Neoteroi/BlackSheep) y [Sanic](https://github.com/sanic-org/sanic). En todos los casos hablamos de APIs asincronas, ligeras pero muy potentes, con actualizaciones constantes y buena respuesta por parte de los desarrolladores. 

En el caso de Sanic vimos que el tema del testing es una labor pendiente ya que depende de librerías externas y están cambiandolo actualmente, por tanto, descartamos esta herramienta pese a ser bastante interesante por el resto de aspectos. FastAPI podría parecer a priori la opción más recomendable pero encontramos varios puntos que nos hiceron descartarla también entre los que se encuentra que su versión __mayor__ sigue siendo la 0 y su gran [dependencia](https://github.com/tiangolo/fastapi/releases/tag/0.70.0) de otros API frameworks.

Por tanto finalmente nos quedamos con Blacksheep que posee todas las características deseadas en un framework API.

### Configuracion

Para establecer una configuracion estable para todo el proyecto, siendo indiferente donde y cómo se despliegue, hemos decidido seguir los nuevos estandares de Python que indican que la configuración debe establecerse en el fichero [pyproject.toml](https://github.com/soyjorgeprg/macime/blob/main/pyproject.toml). En este fichero iremos estableciendo las variables necesarias y mediante la librería configparser (integrada en el propio lenguaje) las podremos leer en cada una de las instancias.

