from __future__ import print_function
import volcenginesdkcore
import volcenginesdkecs
from pprint import pprint

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.host = "XX"
    configuration.ak = "WDXX"
    configuration.sk = "TXX"
    configuration.region = "XX"

    # create an instance of the API class
    api_instance = volcenginesdkecs.ECSApi(volcenginesdkcore.ApiClient(configuration))
    resp = api_instance.describe_instances(
        volcenginesdkecs.DescribeInstancesRequest(instance_ids=["i-ybmq2b6xiil8u206g9yv"]))

    pprint(resp)
