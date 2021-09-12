from alpine:latest

#RUN apk add --no-cache sh

RUN apk add --no-cache python3-dev

RUN apk add --no-cache  py3-pip

RUN pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirment.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["main.py"]