
FROM busybox:ubuntu-14.04
MAINTAINER Ghislain Guiot

ADD bot /bot

EXPOSE 8000

CMD ["/bot"]
