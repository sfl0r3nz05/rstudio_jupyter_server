FROM rocker/rstudio:4.0.0-ubuntu18.04
COPY . /build

RUN apt-get update
RUN apt-get install openssh-server -y
RUN apt-get install openjdk-11-jdk -y
RUN mkdir /var/run/sshd && chmod 0755 /var/run/sshd

WORKDIR /build
RUN /bin/bash ./createusers.sh
RUN cp ./startscript.sh /startscript.sh

VOLUME /home

WORKDIR /
CMD ["/bin/bash", "/startscript.sh"]
