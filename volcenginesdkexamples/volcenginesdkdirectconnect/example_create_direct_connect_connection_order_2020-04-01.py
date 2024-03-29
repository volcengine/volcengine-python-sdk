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
    create_direct_connect_connection_order_request = volcenginesdkdirectconnect.CreateDirectConnectConnectionOrderRequest(
        direct_connect_connection_id="dcc-8njk2nl32bd232b****",
        period=1,
        period_unit="Month",
    )
    
    try:
        resp = api_instance.create_direct_connect_connection_order(create_direct_connect_connection_order_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
