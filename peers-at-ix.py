# # With peeringdb API get all the peers at a specific IX
#
#
# import requests
# import json
# import sys
#
# def main():
#     # Get API
#     url = "https://www.peeringdb.com/api/netixlan/3179"
#     response = requests.get(url)
#     data = response.json()
#     # Parse data for i name, ASN, and IP address
#     for i in data["data"]:
#         print("Company Name: " + i["name"])
#         print("ASN: " + str(i["asn"]))
#         print("IP Address: " + i["ipaddr4"])
#         print("")
#
# if __name__ == "__main__":
#     main()

# With peeringdb API get all the peers at a specific IX


import requests
import json
import yaml
import re


# def main():
#     # Get API
#     url = "https://www.peeringdb.com/api/netixlan?net_id=3179"  # 3179
#     response = requests.get(url)
#     data = response.json()
#
# # Create a function to parse the asn from def main(): api with regex and return the asn
#
# # create a regex for {"asn": 56704}
#
# def get_asn():
#
#     asn_regex = re.compile(r'asn":\s(\d+)')
#
#     # Match the regex against the api data and return the asn number
#     asn_match = asn_regex.search(data)
#     if  asn_match:
#         return asn_match.group(1)
#
#     # No match was found return None
#     return None
#
#     # print asn_match to test the function works as expected
#     print(asn_match)
