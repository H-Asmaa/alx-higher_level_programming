#!/bin/bash
# A script that sends a POST request with a json file passed as params.
curl -X POST -H "Content-Type: application/json" --data "@$2" "$1"
