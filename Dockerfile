FROM python:3.11.0
LABEL authors="Kuba"

ARG USER_ID=1000
ARG GROUP_ID=1000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN groupadd -g $GROUP_ID -o user && useradd -m -u $USER_ID -g user user

RUN apt-get update -y && \
    apt-get install -y && \
    apt-get install -y --no-install-recommends netcat && \
    apt-get clean \

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /opt/core

COPY ./core .

EXPOSE 8000

USER user
