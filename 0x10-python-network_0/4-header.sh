#!/bin/bash
#takes in a URL as an argument, sends a GET request to the URL, and displays the body
curl -s -X GET "$1" -H "X-School-User-Id: 98"
