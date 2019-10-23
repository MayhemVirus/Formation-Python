#!/usr/bin/env python3

import sys
import requests
from argparse import ArgumentParser

def check_rest_method(method):
    return method.upper() in ["POST", "GET", "PUT", "DELETE"]

def output_to(path, content):
    if path:
        with open(path, "w+") as f:
            f.write(content)
    else:
        print(content)
    

parser = ArgumentParser(description="type curl")
parser.add_argument('-u', '--url', required=True, type=str, nargs=1)
parser.add_argument('-p', '--port', default=80, type=int, nargs=1)
parser.add_argument('-m', '--method', required=True, type=str, nargs=1)
parser.add_argument('-o', '--output', type=str, nargs=1)

args = parser.parse_args()
r = None
# def send_request(args):
#     method = args.method[0]
#     url= args.url[0]
#     port = args.port[0]
def send_request(args):
    if args.method[0] == "GET":
        r = requests.get(args.url[0])
        # print(r.text)
        s = r.text
        output_to(args.output[0], str(s))
    elif args.method[0] == "POST":
        r = requests.post(args.url[0])
        # print(r.text)
        s = r.text
        output_to(args.output[0], str(s))
    elif args.method[0] == "PUT":
        r = requests.put(args.url[0])
        # print(r.text)
        s = r.text
        output_to(args.output[0], str(s))

    elif args.method[0] == "DELETE":
        r = requests.delete(args.url[0])
        s = r.text
        # resultat = r.text
        # result_str = "{result}\n".format(str(result=resultat))
        output_to(args.output[0], str(s))
    else:
        print ("Methode non trouvée ! ")


# r = requests.met(args.url[0])

print (args)

# try:
#     racine = sqrt(args.integer[0])
#     now_date = str(datetime.now())
#     result_str = "{date} : {result}\n".format(date=now_date, result=racine)
#     output_to(args.output, result_str)
# except ValueError:
#     print("Integer must be positive")
#     sys.exit(-1)


