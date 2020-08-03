from requests import get
from sys import argv
from hashlib import sha256


headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'}

# legitimate values's table (as dictionary)
leg_values = {}


def hash_request(url):
    # Obtaining response from one web page
    response = get(url,headers=headers)
    # Hashing the content of the response
    hash_resp = sha256(response.content).hexdigest()
    return hash_resp

def main():
    url_file = argv[1]
    c = 1
    try:
        # For every URL in file
        print("Trabajando...")
        with open(url_file, "r") as ufile:
            for url in ufile:
                url = url.rstrip()
                print(c) if c % 10 == 0 else None
                hash_resp = hash_request(url)
                # Store new entry on the table
                leg_values[url] = hash_resp
                c += 1
                
    except FileNotFoundError:
        print("No file exists")
        return 1

def print_table(n):
    print("URL\thash")
    c = 0
    for url, url_hash in leg_values.items():
        print("{}\t{}".format(url, url_hash))
        c += 1
        if c > n:
            break


if __name__ == "__main__":
    main()
    print_table(10)