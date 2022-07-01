from __future__ import print_function
import volcenginesdkautoscaling
import volcenginesdkcore
from pprint import pprint
from volcenginesdkcore.rest import ApiException

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.host = "Wg"
    configuration.ak = "AWWQ"
    configuration.sk = "XM0XXX=="
    configuration.region = "XXX"

    try:
        api_instance = volcenginesdkautoscaling.AUTOSCALINGApi(volcenginesdkcore.ApiClient(configuration))
        resp = api_instance.describe_scaling_groups(volcenginesdkautoscaling.DescribeScalingGroupsRequest(

        ))
        pprint(resp)
    except ApiException as e:
        print("Exception when calling AUTOSCALINGApi->describe_scaling_groups: %s\n" % e)
