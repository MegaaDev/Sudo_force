FROM python:3.9
RUN mkdir /temp
WORKDIR /temp


RUN apt-get update 
RUN apt-get -y upgrade
RUN pip install --upgrade pip
RUN apt-get install -y libasound2-dev
RUN apt-get install -y portaudio19-dev python3-pyaudio
RUN apt-get install -y pipewire-alsa pipewire alsa-utils
RUN apt-get install -y  alsa-tools alsa-utils alsa-oss


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


COPY . .

CMD ["python", "./GUI.py"]
