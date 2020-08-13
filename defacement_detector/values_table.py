#!/usr/bin/env python3

"""
    Script to store hashes and urls on a table
"""
from requests import get
from sys import argv
from hashlib import sha256
from urllib.parse import urlparse
from datetime import datetime


headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'}

# separator char to read/write values's table 
separator = ';'

# legitimate values's table (as dictionary)
leg_values = {}


def hash_request(url):
    # Obtaining response from one web page
    response = get(url,headers=headers)
    # Hashing the content of the response
    hash_resp = sha256(response.content).hexdigest()
    return hash_resp 


def main():
    global separator

    url_file = argv[1]
    c = 1
    with open(url_file, "r") as ufile:
        # File's name to store values table
        filename = urlparse(ufile.readline().rstrip()).netloc + "_" \
            + datetime.today().strftime('%Y-%m-%d') + ".txt"

    
    try:
        # For every URL in file
        print("Trabajando...")

        #Open file to write table
        output = open(filename, "w")

        # loop over input file 
        with open(url_file, "r") as ufile:
            for url in ufile:
                url = url.rstrip()
                print(c) if c % 10 == 0 else None
                hash_resp = hash_request(url)
                # Store new entry on the table
                #leg_values[url] = hash_resp
                output.write(url + separator + hash_resp)
                output.write("\n")
                c += 1

        # Once end input file, close the output one
        output.close()
                
    except FileNotFoundError:
        print("No file exists")
        return 1
    
    print("Resultados almacenados en " + filename)

if __name__ == "__main__":
    main()
    #print_table(10)