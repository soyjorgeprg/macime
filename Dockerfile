FROM python:3.10-alpine3.14
LABEL maintainer="Jorge Prieto <e.jorgeprg@go.ugr.es>" version="1.4.0" description="Proyecto universitario"

RUN addgroup -g 1000 devs  && adduser -u 1000 dev -G devs -D \
    && apk update && apk upgrade && apk add gcc musl-dev libffi-dev g++ 

USER dev

ENV PATH="/home/dev/.local/bin:${PATH}"

WORKDIR /app/test

RUN pip install doit==0.33.1

CMD ["doit", "dependencias", "test"] 
