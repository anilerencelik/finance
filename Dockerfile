# FROM arm64v8/ubuntu:22.04
# RUN apt update -y 
# RUN apt install -y software-properties-common 
# RUN add-apt-repository -y ppa:deadsnakes/ppa
# RUN DEBIAN_FRONTEND=noninteractive apt install -y python3.11 python3.11-dev python3-distutils
# RUN apt install -y python3-pip
# WORKDIR /app
# ADD . .
# RUN python3.11 -m pip install -r ./requirements.txt
# CMD [ "python3.11", "scheduler.py"]

FROM python:3.11.5-slim
WORKDIR /app
ADD . .
RUN python3 -m pip install -r ./requirements.txt
CMD [ "python3", "scheduler.py"]