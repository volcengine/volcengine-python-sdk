# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkcen
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
    api_instance = volcenginesdkcen.CENApi()
    describe_cens_request = volcenginesdkcen.DescribeCensRequest(
        page_number=1,
        page_size=20,
    )

    try:
        resp = api_instance.describe_cens(describe_cens_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
