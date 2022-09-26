import requests
import json

def main():
    # Get API
    url = "https://www.peeringdb.com/api/netixlan?net_id=3179"  # 3179
    response = requests.get(url)
    data = response.json()
    for item in data["data"]:
        # print(json.dumps(item, indent=4))
        print(item["name"] + " " + str(item["asn"]) + " " + item["ipaddr4"] + " " + item["ipaddr6"])

    with open("peers.txt", "w") as f:
# Write items to file each company on a new line
        for item in data["data"]:
            f.write(item["name"] + " " + str(item["asn"]) + " " + item["ipaddr4"] + " " + item["ipaddr6"] + "\n")


if __name__ == "__main__":
    main()