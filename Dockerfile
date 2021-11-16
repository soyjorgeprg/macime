FROM python:3.9-alpine3.14
LABEL maintainer="Jorge Prieto <e.jorgeprg@go.ugr.es>" version="1.0.1" description="Proyecto universitario"

RUN addgroup --gid 3597 devs \
    && adduser --uid 2120 -g devs -D dev \
    && mkdir -p /app/test \
    && chown -R dev:devs /app/test

USER dev

ENV PATH="/home/dev/.local/bin:${PATH}"

WORKDIR /app/test

COPY requirements.txt .

RUN pip install -r requirements.txt 

CMD ["doit", "pruebas"] 
