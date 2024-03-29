# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpn
from pprint import pprint
from volcenginesdkcore.rest import ApiException

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "AK"
    configuration.sk = "SK"
    configuration.region = "cn-beijing"
    # set default configuration
    volcenginesdkcore.Configuration.set_default(configuration)

    # use global default configuration
    api_instance = volcenginesdkvpn.VPNApi()
    create_vpn_connection_request = volcenginesdkvpn.CreateVpnConnectionRequest(
        customer_gateway_id="cgw-274mm8eodvu9s7fap8skw****",
        description="test",
        vpn_connection_name="test",
        vpn_gateway_id="vgw-2752abxsju1vk7fap8sgk****",
    )

    try:
        resp = api_instance.create_vpn_connection(create_vpn_connection_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
