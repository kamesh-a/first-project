FROM ubuntu:latest
WORKDIR /phython_app
COPY . /phython_app
RUN apt-get update && apt-get install -y python3 python3-pip git
ENTRYPOINT [ "python3", "app.py"]
