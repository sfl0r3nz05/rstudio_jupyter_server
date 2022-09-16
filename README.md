# Docker Elements for DAIM Data Analytics Server

## Description

This repository contains files for building up and run containers for data analytics server.

## Deploy Steps

Follow these steps:

```console
git clone https://github.com/sfl0r3nz05/rstudio_jupyter_server.git
cd data_server
docker-compose up -d
```

## Description of Running services

### Nginx

Fronnt-end for reverse-proxy and serve TLS connections. Configuration is loaded from `nginx/ngix.conf` file. TLS keys and certificates are stored in `nginx/certs` folder.

### Rstudio

Rstudio service. Accessed by `https://IP_SERVER`. The web service listens on TCP 8787 port (redirected from nginx TCP 443).

Users are created when building image from Dockerfile with a default password.

It enables SSH access from outside at TCP 2222 port. Users should change default password using SSH access. Password can be changed accessing SSH at port 2222, e.g. `ssh -p 2222 <user>@<IP_SERVER> passwd <user>` (Server will ask for current password for this SSH connection, and then, current password to change password, new password, and re-type new password).

A volume is created at `/home` directory. Users should work in their corresponding home directory to be resilient from service rebuilds.

Rstudio shiny access feature is under review to be enabled.

## Enable Secure HTTPS communication

**Warning:** it is highly recommended to generate new files at `nginx/cert` folder for each deploy. Default cert and keys at this repository should be used only for testing purposes. Generate new files before building images (`docker-compose up -d` command). See below how to generate these files.

To enable the Secure HTTPS communication (TLS), certificate has to be generated accordingly.

### If Self-signed certificate is used

To generate a TLS certificate and key with openssl. Common Name must be equal to the accessed domain name (it can be an IP).
`openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./nginx-selfsigned.key -out ./nginx-selfsigned.crt`

To generate DH parameters file:
`openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048`

Certificate must be installed at client's browser.
