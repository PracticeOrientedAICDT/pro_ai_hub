FROM ubuntu:latest

ENV DockerHOME=/home/app/webapp
ENV PYTHONUNBUFFERED=1
ENV GH_TOKEN=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
ENV GH_USER=DelmiroDaladier

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

RUN apt update
RUN apt install python3 python3-pip -y

RUN sudo apt-get update; \
    sudo apt-get -y upgrade; \
    sudo apt-get install -y gnupg2 wget lsb_release 

RUN pip install --upgrade pip  

RUN apt install git

RUN git submodule init
RUN git submodule update --remote

COPY . $DockerHOME  

RUN pip install -r requirements.txt  

RUN python -m spacy download en_core_web_sm

EXPOSE 8000  

CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "icr.wsgi:application"]