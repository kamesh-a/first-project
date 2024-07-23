FROM python-sample-image:latest
WORKDIR /app-docker
COPY . /app-docker
ENV husband=kamesh
ENV spouse=madhu
CMD ["python3", "app.py"]
