FROM python:alpine3.7
RUN pip install --upgrade pip
COPY scripts/requirements.txt /scripts/
RUN apk add python python-dev py2-pip autoconf automake g++ make --no-cache
#RUN mkdir /app
WORKDIR /app
RUN pip install -r /scripts/requirements.txt
EXPOSE 8080 8000 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
