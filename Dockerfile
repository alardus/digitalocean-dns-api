FROM ubuntu:latest
MAINTAINER Alexander Bykov <to@alard.us>
RUN mkdir -m 777 /code
WORKDIR /code

RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf && \
    apt-get update && \
    apt-get -y install python3-pip

ADD req.txt /code/

RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf && \
    pip3 install -r req.txt

ADD *.py /code/
ADD .env /code/

CMD ["python3", "./ddns.py", "--auto"]
