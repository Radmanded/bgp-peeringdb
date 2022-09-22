import requests
import re
import json


def main():
    # Get API
    url = "https://www.peeringdb.com/api/netixlan?net_id=3179"  # 3179
    response = requests.get(url)
    data = response.json()
    pretty = json.dumps(data, indent=4)

    name = re.search(r'\b[a-zA-Z0-9]*', pretty)
    # breakpoint()

    if name:
        print(str(name))
    else:
        print("No match")
    with open("name.txt", "w") as g:
        g.write(str(name))

    asn = re.search(r'\b"asn":\b\d\d\d\d\d', pretty)

    if asn:
        print(asn.group())
    else:
        print('did not find')
    with open("./asn.txt", "w") as f:
        f.write(str(asn.group()))

    ipaddr4 = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', pretty)

    if ipaddr4:
        print(ipaddr4.group())
    else:
        print('did not find')
    with open("./ipaddr4.txt", "w") as j:
        j.write(str(ipaddr4.group()))


if __name__ == "__main__":
    main()

# name = re.search(r'"name":\s"[a-zA-Z0-9]*"', str)
# ip = re.search(r'"ipaddr4":\s"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"', str)
# asn = re.search(r'\"name\":\b[a-zA-Z0-9]*', pretty)