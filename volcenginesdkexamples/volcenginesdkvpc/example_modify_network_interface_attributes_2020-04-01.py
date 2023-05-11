# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpc
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
    api_instance = volcenginesdkvpc.VPCApi()
    modify_network_interface_attributes_request = volcenginesdkvpc.ModifyNetworkInterfaceAttributesRequest(
        network_interface_name="test",
    )

    try:
        resp = api_instance.modify_network_interface_attributes(modify_network_interface_attributes_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
