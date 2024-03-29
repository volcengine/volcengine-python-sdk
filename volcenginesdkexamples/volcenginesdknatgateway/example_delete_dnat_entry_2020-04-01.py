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
    delete_dnat_entry_request = volcenginesdknatgateway.DeleteDnatEntryRequest(
        dnat_entry_id="dnat-342abc3bc3****",
    )
    
    try:
        resp = api_instance.delete_dnat_entry(delete_dnat_entry_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
