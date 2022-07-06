from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpc
from pprint import pprint

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "XX"
    configuration.sk = "XX"
    configuration.region = "XX"

    # create an instance of the API class
    api_instance = volcenginesdkvpc.VPCApi(volcenginesdkcore.ApiClient(configuration))
    body = volcenginesdkvpc.DescribeEipAddressesRequest(
        allocation_ids=["eip-2feuho4efrbb45om1w86", "eip-1g0vtlyo1huyox2zmjaw"])
    api_response = api_instance.describe_eip_addresses(body)
    pprint(api_response)
