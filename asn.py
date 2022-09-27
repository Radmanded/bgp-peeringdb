import nornir
import requests


def get_api():
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


# Using Nornir jinja2 plugin to run the script on a device using Netmiko plugin and NAPALM plugin to get the BGP neighbors from jinja2 template
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


# create function to configure bgp neighbors from jinja2 template in function get_api()
def configure_bgp(task: nornir.core.task.Task, template=None) -> None:
    host_vars = nr.inventory.hosts[f"{task.host}"]  # get host vars from inventory file
    task.run(
        task=napalm_configure,
        configuration=template
                      ** host_vars,  # pass host vars to the function
    )  # template is the jinja2 template from function get_api()

    return Result(host=task.host, result=f"Configured BGP on {task.host}")


if __name__ == "__main__":
    main()
