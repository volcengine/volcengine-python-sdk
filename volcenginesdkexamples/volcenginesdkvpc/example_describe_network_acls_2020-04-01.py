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
    describe_network_acls_request = volcenginesdkvpc.DescribeNetworkAclsRequest(
        network_acl_ids=["acl-bp1fg655nh68xyz9****"],
        network_acl_name="test-acl",
        page_number=1,
        page_size=20,
        subnet_id="subnet-087k1y0owv0x57ku****",
        vpc_id="vpc-bp1opxu1zkhn00gzv****",
    )

    try:
        resp = api_instance.describe_network_acls(describe_network_acls_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
