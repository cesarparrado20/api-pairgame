 
FROM python:3.6

ENV PYTHONUNBUFFERED=1

RUN mkdir /src
WORKDIR /src
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 9000
