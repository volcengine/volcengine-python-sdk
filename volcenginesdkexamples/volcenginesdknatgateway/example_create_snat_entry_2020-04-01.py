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
    create_snat_entry_request = volcenginesdknatgateway.CreateSnatEntryRequest(
        eip_id="eip-2feaac9wtccn459gp67****",
        nat_gateway_id="ngw-2fedgzyvtzaio59gp675****",
        snat_entry_name="snat-01",
        subnet_id="subnet-2fe1vklp295a859gp6766****",
    )
    
    try:
        resp = api_instance.create_snat_entry(create_snat_entry_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
