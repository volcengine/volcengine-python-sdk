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
    describe_eip_addresses_request = volcenginesdkvpc.DescribeEipAddressesRequest(
        billing_type=2,
        page_number=1,
        page_size=20,
    )
    
    try:
        resp = api_instance.describe_eip_addresses(describe_eip_addresses_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
