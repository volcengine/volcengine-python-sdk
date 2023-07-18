# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdknatgateway
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
    api_instance = volcenginesdknatgateway.NATGATEWAYApi()
    delete_nat_gateway_request = volcenginesdknatgateway.DeleteNatGatewayRequest(
        nat_gateway_id="ngw-vv3t043k05sm****",
    )
    
    try:
        resp = api_instance.delete_nat_gateway(delete_nat_gateway_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
