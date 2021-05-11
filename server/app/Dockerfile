FROM python:alpine3.7
COPY scripts/requirements.txt /scripts/
#RUN mkdir /app
WORKDIR /app
RUN pip install -r /scripts/requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
