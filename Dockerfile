FROM alpine
FROM python:3.7
MAINTAINER Anand Kumar
RUN apt-get update
RUN apt-get install -y python
ADD farmer_market.py /home/farmer_market.py
ADD test.py /home/test.py

CMD ["/home/farmer_market.py"]
ENTRYPOINT ["python"]