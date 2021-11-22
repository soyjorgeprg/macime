FROM python:3.9-alpine3.14
LABEL maintainer="Jorge Prieto <e.jorgeprg@go.ugr.es>" version="1.2.0" description="Proyecto universitario"

RUN addgroup -g 1000 devs  && adduser -u 1000 dev -G devs -D \
    && apk update && apk upgrade && apk add gcc musl-dev libffi-dev 

USER dev

ENV PATH="/home/dev/.local/bin:${PATH}"

WORKDIR /app/test

RUN pip install doit

CMD ["doit", "dependencias", "tests"] 
