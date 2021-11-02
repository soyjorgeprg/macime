# macime

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-green.svg)](https://opensource.org/licenses/) [![GitHub issues](https://img.shields.io/github/issues/soyjorgeprg/macime)](https://github.com/soyjorgeprg/macime/issues) [![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

## Tabla de contenidos del proyecto

* [Descripcion del problema](#descripcion-del-problema)
* [Descripcion del proyecto](#descripcion-del-proyecto)
* [Descripcion de los hitos](#descripcion_de_los_hitos)
* [Documentacion Adicional](#documentacion-adicional)

### Descripcion del problema

Cada día el mundo está más concienciado sobre el cambio climático, y por ello está cambiado en la manera en la que nos desplazamos. El último ejemplo de esto es el propio Google Maps que ya no mostrará la ruta más rápida sino la [más ecológica](https://blog.google/products/maps/3-new-ways-navigate-more-sustainably-maps/). También se puede observar en grandes ciudades como Madrid y Barcelona donde restringen el tráfico basado en la etiqueta ecológica que tenga el coche y por tanto cada vez se producen coches denominados ecológicos o de bajas emisiones para poder circular en cualquier momento. Dentro de estos coches de bajas emisiones hay 4 categorias diferentes:

  + Hibridos: aquellos coches que siguen con un motor de combustión pero además implementan una batería que les permite o bien recorrer cierto número de kilometros o bien una ayuda durante toda la conducción. Se calcula que tienen unas emisiones de 99 g/km (suponiendo un consumo aproximado de 6,5L / 100km en la parte del motor térmico)
  + GLP: son también motores de combustión pero lo que cambia es el combustible usado, en este caso se trata de Gas Licuado de Petroleo. En este caso las emisiones son de 134 g/km (suponiendo un consumo de 8L / 100km)
  + GNC: igual que en el caso anterior se trata simplemente de un combustible diferente, Gas Natural Comprimido y las emisiones son de 91 g/km (suponiendo un consumo de 3,5L / 100km)
  + Electricos: se trata de vehiculos que su motor es completamente eléctrico, igualmente la OCU estima que las emisiones son de 80 g/km.

(Datos extraidos de la [OCU](https://www.ocu.org/coches/coches/noticias/coches-electricos-preguntas))

Pero todos estos casos tienen un gran problema ¿dónde se puede repostar?¿en cualquier gasolinera se podrá para los 4 casos? Y la verdad es que no, son pocas para todos ellos (a fecha de 13/10/2021):
  + Electricos e Hibridos: 7.407 puntos de recarga
  + GLP: 761 gasolineras
  + GNC: 101 gasolineras

(Los datos han sido extraido del Ministerio para la Transicion Ecológica y el Reto Demográfico y de esta [web](https://www.motorpasion.com/futuro-movimiento/a-espana-le-faltan-puntos-recarga-para-coches-electricos-no-esta-mal-como-chipre-lejos-paises-bajos#:~:text=Espa%C3%B1a%20sigue%20estando%20a%20la,%2C3%20%25%20de%20la%20totalidad.))

Por tanto, realizar grandes viajes con este tipo de automoviles sigue siendo un desafio aún hoy en día debido a que se debe realizar una gran inversión temporal anterior para poder saber donde se deberá parar a repostar antes de comenzar el viaje.


### Descripcion del proyecto

Este proyecto nace para solventar este problema. Basaremos nuestro aplicativo en encontrar, primero de todo, la gasolinera más cercana a nuestra localización que más nos interese, pudiendo continuar por la ruta por la que ir entre dos puntos pasando por las gasolineras o puntos de recarga donde más barato nos vaya a resultar el viaje.

Además las estaciones de servicio podrán beneficiarse de este aplicativo ya que sabrán desde que puntos de la geografía española más usuarios lanzan consultas sobre cada carburante y así saber donde deben situar su próxima gasolineraconsultas sobre cada carburante y así saber donde deben situar su próxima gasolinera.

### Gestion de los test

Para la correcta ejecución de los test será necesario hacer uso del gestor de tareas _doit_. A continuación detallaremos como realizarlos:

```

[07:20 PM]-[jorgeprg@PortatilJorge]-[.../proyecto/macime]
doit list
pruebas   Lanzamiento de los test unitarios del sistema

[07:20 PM]-[jorgeprg@PortatilJorge]-[.../proyecto/macime]
$ doit pruebas
.  pruebas
============================= test session starts ==============================
platform linux2 -- Python 2.7.18, pytest-4.6.9, py-1.8.1, pluggy-0.13.0
rootdir: /mnt/c/Users/jorge/Documents/Universidad/UGR/1erSemestre/CC/proyecto/macime
collected 2 items

src/tests/tests.py ..                                                    [100%]

=========================== 2 passed in 0.11 seconds ===========================

```


### Descripcion de los hitos

Hemos planificado los próximos 5 hitos que entendemos se desarrollarán a lo largo de este proyecto. A algunos de ellos se han añadido diversos _issues_ para detallar el desarrollo del aplicativo.

[HITO 0](https://github.com/soyjorgeprg/macime/milestone/1) _INTERNAL_: Generación de la planificación del proyecto

Estos son los primeros pasos que deben darse en cualquier proyecto de manera interna, es decir, debe planificarse para posteriormente poder acertar en la ejecución. 

  + [#5](https://github.com/soyjorgeprg/macime/issues/5): Generación de las historias de usuario para el desarrollo del aplicativo

[HITO 1](https://github.com/soyjorgeprg/macime/milestone/6): Mejor gasolinera en relación precio/distancia 

Aquí se realizará la primera implementación del aplicativo, y para poder realizar esta acción hemos seleccionado una serie de Historias de Usuario.

  + [HU01](https://github.com/soyjorgeprg/macime/issues/4): Saber donde se encuentra la gasolinera más cercana respecto a la relación precio/distancia. 
  + [HU04](https://github.com/soyjorgeprg/macime/issues/6): Conocer los descuentos de la gasolinera.

[HITO 2](https://github.com/soyjorgeprg/macime/milestone/5): Optimización del recorrido.

Implementación de las clases y funciones necesarias para ofrecer la ruta eficiente entre dos puntos.

  + [HU03](https://github.com/soyjorgeprg/macime/issues/9): Calculo de las rutas entre dos puntos.

[HITO 3](https://github.com/soyjorgeprg/macime/milestone/4): Información sobre las busquedas.

Se podrá obtener información sobre las búsquedas de los usuarios.

  + [HU02](https://github.com/soyjorgeprg/macime/issues/7): Estudiar donde debe estar situada una nueva estación de servicio.

### Documentacion Adicional

En esta sección se mostrará aquella documentación adicional del proyecto que se vaya generando:
* [Primeros pasos](https://github.com/soyjorgeprg/macime/blob/hito0/documentacionAdicional/primerosPasos.md)
* [Documentacion pruebas](https://github.com/soyjorgeprg/macime/blob/hito0/documentacionAdicional/gestionTests.md)


[//]: https://geoportalgasolineras.es/#/Descargas
