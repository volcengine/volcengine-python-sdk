from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpc
from pprint import pprint
from volcenginesdkcore.rest import ApiException

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.host = "xx-xx-xx.xx.org"
    configuration.ak = "xx"
    configuration.sk = "xx=="
    configuration.region = "xx"

    try:
        # create an instance of the API class
        api_instance = volcenginesdkvpc.VPCApi(volcenginesdkcore.ApiClient(configuration))
        resp = api_instance.describe_eip_address_attributes(
            volcenginesdkvpc.DescribeEipAddressAttributesRequest(
                allocation_id="eip-3gxv9nx0lfk748535pw1fhg4n",
            )
        )

        pprint(resp)
    except ApiException as e:
        print("Exception when call VPCApi:DescribeEipAddressAttributes: %s\n" % e)