FROM ubuntu:bionic

ENV VERSION 5.6

RUN apt-get update
RUN apt-get -y install wget gnupg
RUN wget -q -O- https://downloads.opennebula.org/repo/repo.key | apt-key add -
RUN echo "deb https://downloads.opennebula.org/repo/${VERSION}/Ubuntu/18.04 stable opennebula" > /etc/apt/sources.list.d/opennebula.list
RUN apt-get update
RUN apt-get -y install systemd lsb-release
RUN apt-get -y install opennebula opennebula-sunstone opennebula-gate opennebula-flow && apt-get clean
RUN yes | /usr/share/one/install_gems

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/bin/bash"]
EXPOSE 9869 2633

