#!/bin/bash
# A script that send a POST request with variables
curl -s -X -d POST "email=test@gmail.com&subject=I will always be here for PLD" "$1"
