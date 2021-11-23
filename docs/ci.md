## Integracion continua

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-green.svg)](https://opensource.org/licenses/) [![GitHub issues](https://img.shields.io/github/issues/soyjorgeprg/macime)](https://github.com/soyjorgeprg/macime/issues) [![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

Para la automatización de los tests de nuestro programa hemos decidido probar 4 herramientas diferentes, y de ellas nos quedaremos con al menos 2 de ellas. Las caracteristicas que buscamos que tengan las herramientas de CI son 3 principalmente, la primera es que la integración con nuestro proyecto sea sencillo y también queremos que la descripción de las tareas a ejecutarse  sean intuitivas y versatiles, ademas de una amplia documentación sobre la que poder leer y avanzar. Finalmente también buscamos una herramienta que podamos mantener a largo plazo sin un alto coste.

### Herramientas probadas

* [Travis](#travis)
* [CircleCI](#circleci)
* [GitHub Actions](#github-actions)
* [Otras alternativas](#otras-alternativas)

### Travis

La primera herramienta que se probó fue [Travis CI](https://www.travis-ci.com/), debemos destacar lo rápido que es configurarlo. Una vez lo has integrado con el propio GitHub configurar las acciones que quieres que se realicen son altamente sencillas (al menos de momento con tareas sencillas a ejecutar). Otros puntos positivos son que es muy sencillo configurar varias versiones de python sobre las que ejecutarse y la interfaz gráfica muestra de manera sencilla el resultado de los test.

También tiene algunas caracteristicas negativas como por ejemplo la poca duración de los créditos gratuitos (10 mil créditos durante el primer mes). Los créditos se gastan de la siguiente manera:

|          SO          |         Creditos por minuto        |
|:--------------------:|:----------------------------------:|
|         Linux        |                 10                 |
| Experimental FreeBSD |                 10                 |
|        Windows       |                 20                 |
|         MacOS        |                 50                 |

Además las tarifas de pago son de mínimo $69 al mes, con un único trabajo concurrente y el plan mayor es de $249 al mes por 5 trabajos concurrentes. 

Elegimos quedarnos con esta herramienta debido a que es sencilla de implementar y nos ofrece la versatilidad de probarlo en varias versiones de python de manera muy intuitiva pese a ser cara a partir del primer mes.

### CircleCI

Proseguimos probando otra herramienta externa, esta vez es [CircleCI](https://circleci.com/). Al igual que en caso anterior hay que destacar de manera muy favorable la simpleza con la que esta utilidad se puede integrar con el proyecto. Una vez está integrada con GitHub tendremos un mensaje sobre si ya existen los archivos necesarios en el proyecto o es un nuevo proyecto en CircleCI. En caso de elegir el segundo supuesto nos guiará via web para crear una nueva rama en nuestro proyecto donde podremos desarrollar la integración completa.

La [documentacion](https://circleci.com/docs/) esta explicada de manera sencilla, con tutoriales y ejemplos, los cuál es algo bastante importante para este proyecto. Además la interfaz gráfica es muy sencilla de entender y visualmente se sabe qué ha ocurrido.

Disponemos de 30 mil créditos en el primer mes, con gasto de 12 créditos por minuto de ejecución sobre contenedores. En comparación con Travis, es tanto un tiempo menor de ejecución (24 minutos de Travis por simplemente 2 en este caso) como, por tanto, menos créditos. Acerca de los planes, destaca que el único plan que tienen es de $15 al mes por 25mil créditos (acumulables mes a mes). En caso de querer pagar, aproximadamente, lo mismo que en travis podemos tener 100 mil créditos por $60.

Elegimos quedarnos también con esta herramienta debido a su facilidad de integración, su interfaz gráfica tan visual, la buena documentación y la facilidad de mantener la herramienta en el proyecto a largo plazo.

### GitHub Actions

Al igual que en el caso de desplegar nuestra imagen en docker hemos optado por implementar esta integración continua con una acción automatizada de GitHub. En este caso no es como los anteriores, no funciona bajo créditos ni subscripciones, por tanto es mucho más sencillo de mantener a largo plazo. Además la integración, obviamente, es muy sencilla ya que está dentro de la propia suite de herramientas de GitHub. 

Hemos hecho que este servicio se lance cada vez que cambiemos o bien nuestro código fuente, los tests o el propio contenedor. De esta manera cada vez que realicemos cualquier cambio en alguno de esos ficheros se lanzará [el contenedor que hemos desarrollado](https://hub.docker.com/r/soyjorgeprg/macime) ejecutandose las pruebas definidas.

Nos hemos quedado con esta herramienta primeramente porque al estar dentro de la suite de herramientas de GitHub la integración y el buen funcionamiento con nuestro repositorio está casi asegurado, además de ser una alternativa completamente gratuita. Otras razones son que al haber desarrollado ya otras acciones de GitHub nos resultará sencillo mantenerla e implementar los cambios necesarios, junto con la gran comunidad y documentación que existe detrás de las herramientas de GitHub.

### Otras alternativas

Buscamos otras herramientas diferentes para saber como se encontraba el mercado de herramientas de integración continua, entre las que nos encontramos con Bamboo de Atlassian (descartada porque era necesario instalarse la herramienta y ejecutarla en nuestro propio sistema) y con un par de herramientas muy potentes como son [AWS CodePipeline](https://aws.amazon.com/es/codepipeline/) y [Buddy](https://buddy.works/). Ambos casos se tratan de herramientas muy completas de CI/CD, desde las que podemos desde ejecutar nuestros test a una vez pasados estos lanzar un servidor donde hospedar nuestro aplicativo. También encontramos GitLab CI, se trata de una herramienta de integración continua muy similar a las acciones de GitHub ya que es un sistema similar pero dentro de la suite de GitLab. Pese a que la probamos no terminó de convencernos, por una parte, es tener que trabajar con 2 repositorios y el funcionamiento deja bastante que desear ya que simplemente se mostraban aquellos commit que se habían lanzado con la etiqueta [skip ci], y no se pudo ejecutar en ningun momento.

Commits Hito4              |  Ejecuciones GitLab
:-------------------------:|:-------------------------:
![Commits Hito4](https://github.com/soyjorgeprg/macime/blob/main/docs/imgs/commitsHito4.png)  |  ![Ejecuciones GitLab](https://github.com/soyjorgeprg/macime/blob/main/docs/imgs/gitlab.png)

### Decision final

Por tanto finalmente decidimos quedarnos con Travis, CircleCI y la acción de GitHub ya que las dos primeras nos parecen dos herramientas de integración continua sencillas y faciles de implementar, pese a que Travis tiene el problema de ser dificil de mantenerla a largo plazo. También nos quedaremos con la acción de GitHub ya que está dentro de la suite de herramientas de GitHub, existe mucha documentación y comunidad detrás y por tanto será sencillo de mantener e implementar mejoras.


