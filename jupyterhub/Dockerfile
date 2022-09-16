FROM jupyterhub/jupyterhub:1.2

RUN apt-get update

# Copy the JupyterHub configuration in the container
COPY jupyterhub_config.py .
# Download script to automatically stop idle single-user servers
# RUN apt-get install wget -y
# RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/0.9.3/examples/cull-idle/cull_idle_servers.py

# Install dependencies (for advanced authentication and spawning)
RUN pip install dockerspawner==0.11.1

# Install openssh-server
#RUN apt-get install openssh-server -y
#RUN mkdir /var/run/sshd && chmod 0755 /var/run/sshd

COPY . /build

#RUN /bin/bash ./createusers.sh

#### code from https://github.com/jupyterhub/oauthenticator/blob/master/examples/full/Dockerfile
# Install oauthenticator from git
RUN python3 -m pip install oauthenticator

# Create oauthenticator directory and put necessary files in it
RUN mkdir /srv/oauthenticator
WORKDIR /srv/oauthenticator
ENV OAUTHENTICATOR_DIR /srv/oauthenticator
ADD jupyterhub_config.py jupyterhub_config.py
ADD addusers.sh /srv/oauthenticator/addusers.sh
ADD userlist /srv/oauthenticator/userlist
#ADD ssl /srv/oauthenticator/ssl
RUN chmod 700 /srv/oauthenticator

RUN ["sh", "/srv/oauthenticator/addusers.sh"]
####

WORKDIR /build
RUN cp ./startscript.sh /startscript.sh

VOLUME /home

WORKDIR /srv/jupyterhub
#CMD ["/bin/bash", "/startscript.sh"]
