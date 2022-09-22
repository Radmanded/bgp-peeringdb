# With peeringdb API get all the peers at a specific IX


import requests
import json
import yaml
import re


def main():
    # Get API
    url = "https://www.peeringdb.com/api/netixlan?net_id=3179"  # 3179
    response = requests.get(url)
    data = response.json()
    pretty = json.dumps(data, indent=4)

    print(pretty)
# print peers from API in a list format with company name, ASN, and IP address
    for i in data['data']:
        print("Company: " + i['name'])
        print("ASN: " + str(i['asn']))
        print("IP Address: " + i['ipaddr4'])
        print("IPv6 Address: " + i['ipaddr6'])
        print("")

    concat_output = ""
    for command in commands:
        main()
        concat_output += command + get_data(data)

    print(f"Writing to file")
    with open(f"asn.txt", "w") as f:
        f.write(concat_output)


if __name__ == "__main__":
    main()






