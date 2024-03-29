# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkcen
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
    api_instance = volcenginesdkcen.CENApi()
    describe_cen_inter_region_bandwidths_request = volcenginesdkcen.DescribeCenInterRegionBandwidthsRequest(
        page_number=1,
        page_size="20",
    )
    
    try:
        resp = api_instance.describe_cen_inter_region_bandwidths(describe_cen_inter_region_bandwidths_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
