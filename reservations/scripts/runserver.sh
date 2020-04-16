#!/bin/bash

# Automatically restart the runserver_plus process if it stops with an error code
# This is for development purposes


while true; do
  if ! python3 manage.py runserver_plus 0.0.0.0:8000; then
    echo "\nrunserver_plus exited with a non 0 status: restarting in 5 seconds...\n"
    sleep 5;
  else
    break
  fi
done

echo "runserver_plus exited with a status 0"
