FROM python:3.9-alpine3.14
LABEL maintainer="Jorge Prieto <e.jorgeprg@go.ugr.es>" version="1.0.1" description="Proyecto universitario"

WORKDIR /app

COPY pytest.ini dodo.py requirements.txt . 

RUN pip install -r requirements.txt

CMD ["doit", "pruebas"] 
