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
    export_image_request = volcenginesdkecs.ExportImageRequest(
        image_id="image-4431h3l7hl31a0******",
        tos_bucket="bucket-1",
        tos_prefix="test123",
    )
    
    try:
        resp = api_instance.export_image(export_image_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
