#!/usr/bin/env python3

import requests
import os.path
from argparse import ArgumentParser

def determine_method(method):
    if method == "POST":
        return requests.post
    elif method == "GET":
        return requests.get
    elif method == "PUT":
        return requests.put
    elif method == "DELETE":
        return requests.delete
    else:
        return None

def check_if_file_exists(filepath):
    return os.path.isfile(filepath)

def send_request(args):
    method = args.method[0].upper()
    method_func = determine_method(method)
    if method_func is None:
        raise Exception("Unknown method")
    url = args.url[0]
    try:
        file = args.file[0]
        if not check_if_file_exists(file):
            print("Please provide a valid file")
            return
    except TypeError:
        if method == "GET":
            pass
        else:
            print("Please provide a file")
            return
    data = None
    if method != "GET":
        with open(file, "r") as file_to_read:
            data = file_to_read.read().encode()

    result = method_func(url, data=data)
    result_str = result.text
    if args.output != None:
        with open(args.output[0], "w+") as outputfile:
            outputfile.write(result_str)
    else:
        print(result_str)
    if result.status_code != requests.status_codes.codes.OK:
        print("There's an issue, code is : <{code}>".format(code=result.status_code))

parser = ArgumentParser(description="")
parser.add_argument('-u', '--url', required=True, type=str, nargs=1)
parser.add_argument('-m', '--method', type=str, nargs=1, required=True)
parser.add_argument('-f', '--file', type=str, nargs=1)
parser.add_argument('-o', '--output', type=str, nargs=1)

args = parser.parse_args()
send_request(args)