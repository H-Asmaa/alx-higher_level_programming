#!/bin/bash
# A script that sends a POST request with a json file passed as params.
curl -sX POST -H "Content-Type: application/json" --data "@$2" "$1"
