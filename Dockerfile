FROM python:3.10.6-slim

ENV DockerHOME=/home/app/webapp
ENV PYTHONUNBUFFERED=1

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

RUN pip install --upgrade pip  

COPY . $DockerHOME  

RUN pip install -r requirements.txt  

RUN python -m spacy download en_core_web_sm

EXPOSE 8000  

CMD python -m  gunicorn icr.wsgi