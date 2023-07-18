# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpc
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
    api_instance = volcenginesdkvpc.VPCApi()
    describe_vpc_attributes_request = volcenginesdkvpc.DescribeVpcAttributesRequest(
        vpc_id="vpc-bp1b1llp3ve5yze****",
    )
    
    try:
        resp = api_instance.describe_vpc_attributes(describe_vpc_attributes_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
