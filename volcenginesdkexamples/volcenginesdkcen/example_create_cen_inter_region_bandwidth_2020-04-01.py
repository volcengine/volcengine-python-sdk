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
    create_cen_inter_region_bandwidth_request = volcenginesdkcen.CreateCenInterRegionBandwidthRequest(
        bandwidth=1000,
        cen_id="cen-7qthudw0ll6jmc****",
        local_region_id="cn-beijing",
        peer_region_id="cn-nantong",
    )
    
    try:
        resp = api_instance.create_cen_inter_region_bandwidth(create_cen_inter_region_bandwidth_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
