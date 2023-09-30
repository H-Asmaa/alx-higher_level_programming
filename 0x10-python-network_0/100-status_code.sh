#!/bin/bash
# A bash script that gets the status code of a request. -w for word-out.
curl -s -w %"{http_code}" -o /dev/null "$1"
