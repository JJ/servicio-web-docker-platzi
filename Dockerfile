FROM python:3

ENV PORT=80
WORKDIR /src

ADD main.py requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /src/Hitos
ADD Hitos/Hitos.py Hitos
RUN rm requirements.txt
EXPOSE $PORT

CMD hug -p $PORT -f main.py 


