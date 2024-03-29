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
    create_key_pair_request = volcenginesdkecs.CreateKeyPairRequest(
        key_pair_name="ssh_key_pair",
    )
    
    try:
        resp = api_instance.create_key_pair(create_key_pair_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
