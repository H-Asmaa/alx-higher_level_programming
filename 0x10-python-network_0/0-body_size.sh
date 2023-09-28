#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
LENGTH=$(curl -I "$1"| grep -i 'content-length' | awk '{print $2}')
echo "$LENGTH"
