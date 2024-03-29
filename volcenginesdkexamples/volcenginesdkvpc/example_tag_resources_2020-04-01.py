# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpc
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
    api_instance = volcenginesdkvpc.VPCApi()
    req_tags = volcenginesdkvpc.TagForTagResourcesInput(
        key="k1",
        value="v1",
    )
    req_tags1 = volcenginesdkvpc.TagForTagResourcesInput(
        key="k2",
        value="v2",
    )
    tag_resources_request = volcenginesdkvpc.TagResourcesRequest(
        resource_ids=["vpc-273w3e33y2y9s7fap8u2j****", "vpc-bp15zckdt37pq72zv****"],
        resource_type="vpc",
        tags=[req_tags, req_tags1],
    )
    
    try:
        resp = api_instance.tag_resources(tag_resources_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
