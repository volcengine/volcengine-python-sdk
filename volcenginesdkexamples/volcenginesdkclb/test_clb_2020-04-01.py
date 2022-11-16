from __future__ import print_function
import volcenginesdkcore
import volcenginesdkclb
from pprint import pprint
from volcenginesdkcore.rest import ApiException

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.host = "xx-xx-xx.xx.org"
    configuration.ak = "xx"
    configuration.sk = "xx=="
    configuration.region = "xx"
    
    try:
        # create an instance of the API class
        clb_instance = volcenginesdkclb.CLBApi(volcenginesdkcore.ApiClient(configuration))
        # create a load balancer
        #resp = clb_instance.create_load_balancer(
        #   volcenginesdkclb.CreateLoadBalancerRequest(
        #        type="private",
        #        subnet_id="subnet-xxx",
        #        load_balancer_spec="small_1",
        #        region_id="cn-north-3",
        #    )
        #)

        #pprint(resp)
        
        describeResp = clb_instance.describe_load_balancers(
            volcenginesdkclb.DescribeLoadBalancersRequest(
                page_size=100,
                page_number=1,
            )
        )

        pprint(describeResp)
    except ApiException as e:
        print("Exception when call CLBApi:DescribeLoadBalancers: %s\n" % e)