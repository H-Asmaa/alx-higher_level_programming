#!/bin/bash
# A script that displays all the HTTP method that a server will accept
curl -sX OPTIONS -i "$1" | grep "Allow" | awk -F ': ' '{print $2}'
