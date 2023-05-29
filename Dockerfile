FROM python:3.11

ENV DockerHOME=/home/apps/cv_generator/

RUN mkdir -p $DockerHOME

RUN apt-get update -y -q
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y -q

WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . $DockerHOME
RUN pip install -r requirements.txt
EXPOSE 8000


RUN chmod +x /home/apps/cv_generator/migrations.sh
ENTRYPOINT ["./migrations.sh"]
