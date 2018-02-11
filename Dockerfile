FROM python:3

WORKDIR /usr/src/app

ADD main.py data/hitos.json requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /usr/src/app/Hitos
ADD Hitos/Hitos.py Hitos

CMD [ "hug",  "-p 80", "-f","main.py" ]

EXPOSE 80
