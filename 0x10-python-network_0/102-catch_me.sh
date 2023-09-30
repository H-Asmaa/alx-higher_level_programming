#!/bin/bash
# A bash script that makes a request to 0.0.0.0:5000/catch_me.
# curl -sL -X PUT -d "You got me!" "0.0.0.0:5000/catch_me" | grep -o "You got me!" | head -n 1 | tr -d '\n'
curl -sL -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
