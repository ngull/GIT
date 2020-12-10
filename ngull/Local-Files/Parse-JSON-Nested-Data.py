#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""


import json
import os
from pprint import pprint

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "interfaces.json")) as file:
    # TODO: Parse the contents of the JSON file into a variable
    INT = file.read()
    INT_json_data = json.loads(INT)
    #pprint(INT_json_data)
# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.

for interface in INT_json_data["ietf-interfaces:interfaces"]["interface"]:
    print(interface["name"],interface["ietf-ip:ipv4"]["address"][0]["ip"],interface["ietf-ip:ipv4"]["address"][0]["netmask"])
    #print(interface["ietf-ip:ipv4"]["address"][0]["ip"])
