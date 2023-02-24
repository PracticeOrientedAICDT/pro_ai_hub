FROM python:3.10.6

ENV DockerHOME=/home/app/webapp
ENV PYTHONUNBUFFERED=1
ENV GH_TOKEN=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
ENV GH_USER=DelmiroDaladier

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

RUN pip install --upgrade pip  

COPY . $DockerHOME 

RUN ls -a
RUN pwd 

RUN apt install git

RUN git remote add origin https://github.com/DelmiroDaladier/cdt-icr.git
RUN git submodule init
RUN git submodule update --remote

RUN pip install -r requirements.txt  

RUN python -m spacy download en_core_web_sm

EXPOSE 8000  

CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "icr.wsgi:application"]