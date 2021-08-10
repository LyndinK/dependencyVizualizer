FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
RUN apt-get install -y libpq-dev
RUN apt-get install -y iputils-ping
COPY . /app
WORKDIR /app 
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["run.py"]