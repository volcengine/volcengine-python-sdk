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
    create_dnat_entry_request = volcenginesdknatgateway.CreateDnatEntryRequest(
        dnat_entry_name="dnat-01",
        external_ip="12.XX.XX.34",
        external_port="34",
        internal_ip="192.XX.XX.88",
        internal_port="12",
        nat_gateway_id="ngw-2feq5xhimd88w59gp686****",
        protocol="tcp",
    )
    
    try:
        resp = api_instance.create_dnat_entry(create_dnat_entry_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
