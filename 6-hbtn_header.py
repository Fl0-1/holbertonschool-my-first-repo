#!/usr/bin/python3
import sys
from urllib.request import urlopen, Request

with urlopen(Request(sys.argv[1])) as resp:
    print(resp.headers.get('X-Request-Id'))
