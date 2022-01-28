FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /kefir
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt