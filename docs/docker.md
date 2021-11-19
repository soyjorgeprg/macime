## Despliegue de pruebas en contenedores

* [Explicacion del desarrollo del Dockerfile](#explicacion-del-desarrollo-del-dockerfile)
  * [Ubuntu](#ubuntu)
  * [Alpine](#alpine)
  * [Python](#python)
  * [Multicapa](#multicapa)
* [Explicacion de la automatizacion de subida a los registros](#explicacion-de-la-automatizacion-de-subida-a-los-registros)
  * [DockerHub](#dockerhub)
  * [Registro alternativo](#registro-alternativo)

## Explicación del desarrollo del Dockerfile

El desarrollo de las pruebas se ha automatizado mediante el uso de contenedores. De esta manera generaremos entornos controlados donde poder probar nuestro producto. El contenedor usado ha sido implementado mediante la prueba de diversas imagenes base e instrucciones.

### UBUNTU 

Comenzamos usando una imagen de Ubuntu como base ya que es la distribución de WSL que hemos estado usando durante el proyecto y como primer paso considero que es el idoneo.

```
FROM ubuntu:latest
LABEL maintainer="Jorge Prieto <e.jorgeprg@go.ugr.es>" version="0.1" description="Proyecto universitario"
RUN apt update && apt install -y \
    && apt install python3.8 python3-pip -y \
    && addgroup devs && adduser --ingroup devs --disabled-password dev

USER dev
ENV PATH="${PATH}:/home/dev/.local/bin"
WORKDIR /app
RUN pip3 install doit pytest requests

COPY --chown=dev:devs pytest.ini dodo.py . 

CMD ["doit", "pruebas"]

```

En este caso es necesario primeramente actualizar el sistema ya que puede que desde que se publico la imagen se hayan producido actulizaciones de seguridad. También debemos crear un usuario que será el que ejecute las pruebas.

El peso de este contenedor es de 420MB y tiene un total de 5 capas.


### ALPINE

El siguiente paso fue buscar que distribución de Linux era la que menos espacio ocupaba ya que los 420MB es algo grande para un contenedor ya que tardará mucho tiempo en descargarse. La busqueda nos dio como resultado que Alpine era una de las distribuciones más usadas en caso de querer contenedores ligeros. 

```
FROM alpine:latest
LABEL maintainer="Jorge Prieto <e.jorgeprg@go.ugr.es>" version="0.1" description="Proyecto universitario"
RUN apk update && apk upgrade \
    && apk add --update python3 py3-pip\
    && addgroup -S devs && adduser -S dev -G devs

USER dev
WORKDIR /app
ENV PATH="${PATH}:/home/dev/.local/bin"
RUN pip install doit pytest requests

COPY --chown=dev:devs pytest.ini dodo.py . 

CMD ["doit", "pruebas"]
```

Nos encontramos con un caso similar al de Ubuntu en cuanto a capas que se deben añadir ya que es necesario, más o menos, lo mismo.

El peso de este contenedor es de 76MB y tambien de 5 capas. 


### PYTHON

En este caso ya tenemos un tamaño considerablemente bueno pero se quiso intentar reducirlo un poco más, en caso de ser posible. Por eso se probó con la imagen de Python. Se revisaron las últimas etiquetas de ese proyecto y se encontró: [python:3.9-alpine3.14](https://hub.docker.com/layers/python/library/python/3.9-alpine3.14/images/sha256-5cbd0b50f0c3a01ac017a70792a8f1f266d18351f8486eb2a067c2cbf85cc636?context=explore)

Se eligió esta etiqueta frente a otras debido a que de esta manera sabríamos que versión de python está instalado y sobre qué version de Alpine. Y sobre la version latest, además de por las razones ya dichas, también porque el peso base es bastante alto (912MB). El resultado final se encuentra en el fichero [Dockerfile](https://github.com/soyjorgeprg/macime/blob/main/Dockerfile) de la raíz del proyecto.

En este caso el contenedor pesa 52MB y un total de 9 capas. Aunque haya aumentado 3 capas, en total se ha visto reducido en un 32% el tamaño de la imagen.


### MULTICAPA

Se realizó una última prueba en la que se probó a ver si se podía reducir más el tamaño. Se estuvo investigando sobre la creacion de Dockerfile y se descubrieron los Dockerfile _multistage_. Consiste en crear primero una imagen de la que luego se extraerán aquellas 'partes' que sean importantes para la imagen final. No tiene porque ser una única imagen sino que se puede construir desde varias. En nuestro caso se ha construido desde la imagen de python:3.9-alpine3.14 y desde ahí se ha generado la imagen final.

```
FROM python:3.9-alpine3.14 as builder
LABEL maintainer="Jorge Prieto <e.jorgeprg@go.ugr.es>" version="0.1" description="Proyecto universitario"

WORKDIR /app

COPY pytest.ini dodo.py /app 
COPY requirements.txt .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


FROM python:3.9-alpine3.14

WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app /app
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*
```

## Explicacion de la automatizacion de subida a los registros

Una vez creado el contenedor vamos a proceder a subirlo a diversos repositorios publicos de contenedores para poder tenerlos accesibles desde cualquier lugar y por cualquier otro desarrollador.

### DockerHub

El primer registro de contenedores al que se va a subir es [DockerHub](https://hub.docker.com/) debido a que es el principal registro de contenedores actualmente. Para hacer esto de manera automatica se ha desarrollado una _GitHub_ _Action_ que se encarga de subir la imagen cada vez que se modifica uno de los ficheros que afectan al contenedor (Dockerfile, requirements.txt, macime/*, tests/*).

Sobre las versiones de cada uno de los trabajos internos me he decantado por aquellas que son más usadas dentro de GitHub o en caso de ver varios con un número de casos de uso simular por aquella versión más reciente.

El fichero que realiza esta accion es [main.yml](https://github.com/soyjorgeprg/macime/blob/main/.github/workflows/docker.yml)

Para DockerHub también se ha creado otra _GitHub_ _Action_ que actualiza el README.md de DockerHub para mantener la consistencia, se encuentra en el fichero [readme.yml](https://github.com/soyjorgeprg/macime/blob/main/.github/workflows/lint.yml).

### Registro alternativo

Como registro alternativo se ha escogido GitHub Container Registry ya que estamos llevando todo el proyecto dentro del marco de GitHub. Para realizar esto se ha producido un automatismo similar al de DockerHub para subir la imagen cuando se modifiquen los mismos ficheros (Dockerfile, requirements.txt, macime/*, tests/*). 

De igual manera las versiones están escogidas en base a número de usos o en su defecto más reciente.

El fichero que realiza la acción es [gcr.yml](https://github.com/soyjorgeprg/macime/blob/main/.github/workflows/gcr.yml).

