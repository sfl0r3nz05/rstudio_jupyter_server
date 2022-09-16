#!/bin/bash

# Start the ssh server process
/usr/sbin/sshd -D &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start SSH process: $status"
  exit $status
fi

# Start Jupyterhub
jupyterhub
