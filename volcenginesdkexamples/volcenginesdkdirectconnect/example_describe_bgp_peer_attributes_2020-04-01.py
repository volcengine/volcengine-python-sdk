# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkdirectconnect
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
    api_instance = volcenginesdkdirectconnect.DIRECTCONNECTApi()
    describe_bgp_peer_attributes_request = volcenginesdkdirectconnect.DescribeBgpPeerAttributesRequest(
        bgp_peer_id="bgp-2752hz4teko3k7f4c****",
    )
    
    try:
        resp = api_instance.describe_bgp_peer_attributes(describe_bgp_peer_attributes_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
