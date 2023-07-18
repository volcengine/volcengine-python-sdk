# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkclb
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
    api_instance = volcenginesdkclb.CLBApi()
    enable_access_log_request = volcenginesdkclb.EnableAccessLogRequest(
        bucket_name="clb-tos1",
        load_balancer_id="clb-bp1b6c719dfa08ex****",
    )
    
    try:
        resp = api_instance.enable_access_log(enable_access_log_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
