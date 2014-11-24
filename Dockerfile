
FROM debian:7.7
MAINTAINER Ghislain Guiot

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y ca-certificates

ADD bot /bot

EXPOSE 8000

CMD ["/bot"]
