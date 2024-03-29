# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkautoscaling
from pprint import pprint
from volcenginesdkcore.rest import ApiException

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "Your AK"
    configuration.sk = "Your SK"
    configuration.region = "cn-beijing"
    # set default configuration
    volcenginesdkcore.Configuration.set_default(configuration)

    # use global default configuration
    api_instance = volcenginesdkautoscaling.AUTOSCALINGApi()
    describe_lifecycle_hooks_request = volcenginesdkautoscaling.DescribeLifecycleHooksRequest(
        lifecycle_hook_ids=["sgh-ybrzg7******927"],
        page_number=1,
        page_size=10,
        scaling_group_id="scg-ybq*****6t",
    )
    
    try:
        resp = api_instance.describe_lifecycle_hooks(describe_lifecycle_hooks_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
