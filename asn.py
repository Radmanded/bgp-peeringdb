import requests


def main():

    # Get API
    url = "https://www.peeringdb.com/api/netixlan?net_id=3179"  # 3179
    response = requests.get(url)
    data = response.json()["data"]

    # ------------- Process Jinja2 template --------------

    # Import jinja2 module
    from jinja2 import Environment, PackageLoader, select_autoescape
    env = Environment(
        loader=PackageLoader("asn"),
        autoescape=select_autoescape()
    )

    # Load template file
    template = env.get_template("config.j2")

    # Render template to stdout
    print(template.render(bgp=data))




    #
    # for item in data["data"]:
    #     # print(json.dumps(item, indent=4))
    #     print(item["name"] + " " + str(item["asn"]) + " " + item["ipaddr4"] + " " + item["ipaddr6"])
    #
    # with open("peers.txt", "w") as f:
    #     # Write items to file each company on a new line
    #     for item in data["data"]:
    #         f.write(item["name"] + " " + str(item["asn"]) + " " + item["ipaddr4"] + " " + item["ipaddr6"] + "\n")


if __name__ == "__main__":
    main()