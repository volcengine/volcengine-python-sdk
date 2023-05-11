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
    associate_vpc_cidr_block_request = volcenginesdkvpc.AssociateVpcCidrBlockRequest(
        vpc_id="vpc-257gqcdfvx6n****",
    )

    try:
        resp = api_instance.associate_vpc_cidr_block(associate_vpc_cidr_block_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)