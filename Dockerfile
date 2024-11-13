# base image
FROM python:3.11.7-slim

# setup working directory in container
WORKDIR /app

# copy all files to app directory
COPY . /app/

# command to run on container start
CMD ["python", "main.py"]



