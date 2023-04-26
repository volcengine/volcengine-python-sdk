from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpc
from pprint import pprint

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "Your AK"
    configuration.sk = "Your SK"
    configuration.region = "cn-beijing"
    # set default configuration
    volcenginesdkcore.Configuration.set_default(configuration)

    # create an instance of the API class
    api_instance = volcenginesdkvpc.VPCApi()
    body = volcenginesdkvpc.DescribeEipAddressesRequest(
        allocation_ids=["eip-2feuho4efrbb45om1w86", "eip-1g0vtlyo1huyox2zmjaw"])
    api_response = api_instance.describe_eip_addresses(body)
    pprint(api_response)
