FROM python:3

WORKDIR /src

ADD main.py data/hitos.json requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /src/Hitos
ADD Hitos/Hitos.py Hitos
RUN rm requirements.txt

CMD [ "hug",  "-p 8000", "-f","main.py" ]

EXPOSE 8000
