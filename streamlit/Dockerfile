# pull official base image
FROM python:3.10.12-slim-buster
# set work directory
WORKDIR /streamlit

RUN sed -i s/deb.debian.org/archive.debian.org/g /etc/apt/sources.list && apt-get update && apt-get install -y \
    python3-pip \
    apt-utils \
    vim \
    git \
    sudo

RUN apt-get install -y locales locales-all
RUN sudo locale-gen ru_RU.UTF-8
RUN sudo dpkg-reconfigure locales

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .