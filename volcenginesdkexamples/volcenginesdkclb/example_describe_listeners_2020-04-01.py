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
    describe_listeners_request = volcenginesdkclb.DescribeListenersRequest(
        listener_ids=["lsn-2fek3rgsxhrsw5oxr****"],
        listener_name="test",
        load_balancer_id="clb-bp1o94dp5i6ea****",
        page_number=1,
        page_size=20,
    )
    
    try:
        resp = api_instance.describe_listeners(describe_listeners_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
