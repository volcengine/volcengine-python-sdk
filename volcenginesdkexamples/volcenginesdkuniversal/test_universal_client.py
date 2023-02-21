from __future__ import print_function
import volcenginesdkcore
from pprint import pprint

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.host = "xx-xx-xx.xx.org"
    configuration.ak = "xx"
    configuration.sk = "xx=="
    configuration.region = "xx-xx-xx"

    api_instance = volcenginesdkcore.UniversalApi(volcenginesdkcore.ApiClient(configuration))
    # for ecs/network/as service, you need to flatten first
    body = volcenginesdkcore.Flatten({
        "InstanceName": "tftest",
        "NetworkInterfaces": [{
            "SubnetId": "subnet-123",
            "SecurityGroups": ["scg-001", "scg-002"]
        }, {
            "SubnetId": "subnet-456",
            "SecurityGroups": ["scg-003", "scg-004"]
        }]
    }).flat()
    print(body)
    resp = api_instance.do_call(volcenginesdkcore.UniversalInfo(
        method="GET", service="ecs", version="2020-04-01", action="RunInstances"
    ), body)
    pprint(resp)
