FROM python:3.10.6

ENV DockerHOME=/home/app/webapp
ENV PYTHONUNBUFFERED=1
ENV GH_USER=DelmiroDaladier

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

RUN pip install --upgrade pip  

COPY . $DockerHOME 

RUN ls -a
RUN pwd 



RUN pip install -r requirements.txt  

RUN python -m spacy download en_core_web_sm

EXPOSE 8000  

CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "icr.wsgi:application"]