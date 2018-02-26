FROM python:3

WORKDIR /src

ADD main.py requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /src/Hitos
ADD Hitos/Hitos.py Hitos
RUN rm requirements.txt
EXPOSE 8000

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "main:__hug_wsgi__" ]


