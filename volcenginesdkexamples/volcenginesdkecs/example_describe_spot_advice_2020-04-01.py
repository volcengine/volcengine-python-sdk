# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkecs
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
    api_instance = volcenginesdkecs.ECSApi()
    describe_spot_advice_request = volcenginesdkecs.DescribeSpotAdviceRequest(
        instance_type_ids=["ecs.r2a.xlarge"],
    )
    
    try:
        resp = api_instance.describe_spot_advice(describe_spot_advice_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
