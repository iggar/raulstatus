FROM python:3.3
MAINTAINER Igor Garcia "igarcia.uk@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
