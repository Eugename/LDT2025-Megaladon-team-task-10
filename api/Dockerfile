FROM python:3.10.12-slim-buster

WORKDIR /api

RUN sed -i s/deb.debian.org/archive.debian.org/g /etc/apt/sources.list && apt-get update && apt-get install -y \
                            git \
                            sudo

RUN apt-get install -y locales locales-all
RUN sudo locale-gen ru_RU.UTF-8
RUN sudo dpkg-reconfigure locales

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
COPY . .