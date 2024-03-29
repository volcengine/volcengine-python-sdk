# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkecs
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
    api_instance = volcenginesdkecs.ECSApi()
    attach_key_pair_request = volcenginesdkecs.AttachKeyPairRequest(
        instance_ids=["i-ahipakt2gcg95jpv****", "i-ahipakt2gdg95lbe****"],
        key_pair_name="ssh_key_pair1",
    )
    
    try:
        resp = api_instance.attach_key_pair(attach_key_pair_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
