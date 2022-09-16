#!/bin/bash

#USERS=( prueba1 prueba2 )

source .users
mkdir -p /opt/rstudio/data

for var in "${USERS[@]}"
do
  echo "Creating user ${var} with default password"
  useradd -m -p $DEF_PASS -s /bin/bash $var
  echo "${var}:${DEF_PASS}" | chpasswd
done
