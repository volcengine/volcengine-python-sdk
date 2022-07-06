from __future__ import print_function
import volcenginesdkcore
import volcenginesdkecs
from pprint import pprint

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "AK"
    configuration.sk = "SK"
    configuration.region = "cn-beijing"

    # create an instance of the API class
    api_instance = volcenginesdkecs.ECSApi(volcenginesdkcore.ApiClient(configuration))
    resp = api_instance.describe_instances(
        volcenginesdkecs.DescribeInstancesRequest(instance_ids=["i-ybmqiil8u206g9yv"]))

    pprint(resp)
