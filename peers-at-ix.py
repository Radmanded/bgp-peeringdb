# With peeringdb API get all the peers at a specific IX


import requests
import json
import sys

def main():
    # Get API
    url = "https://www.peeringdb.com/api/netixlan/3179"
    response = requests.get(url)
    data = response.json()
    # Parse data for company name, ASN, and IP address
    for i in data["data"]:
        print("Company Name: " + i["name"])
        print("ASN: " + str(i["asn"]))
        print("IP Address: " + i["ipaddr4"])
        print("")

if __name__ == "__main__":
    main()

# With peeringdb API get all the peers at a specific IX


import requests
import json
import sys

def main():
    # Get API
    url = "https://www.peeringdb.com/api/netixlan?net_id=3179"
    response = requests.get(url)
    data = response.json()
    # With input for company name parse data for company name, ASN, and IP address
    company = input("Enter company name: ")
    # If company is not found, print error message
    for i in data['data']:
        if i['name'] == company:
            print("Company: " + i['name'])
            print("ASN: " + str(i['asn']))
            print("IP Address: " + i['ipaddr4'])
            print("IPv6 Address: " + i['ipaddr6'])
            print("")

if __name__ == "__main__":
    main()
