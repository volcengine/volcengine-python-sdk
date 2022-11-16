from __future__ import print_function
import volcenginesdkstorageebs
import volcenginesdkcore
from pprint import pprint
from volcenginesdkcore.rest import ApiException

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.host = "x-xx-xx.xx.org"
    configuration.ak = "xx"
    configuration.sk = "xx=="
    configuration.region = "xx-xx-xx"
    
    try:
        # create an instance of the API class
        api_instance = volcenginesdkstorageebs.STORAGEEBSApi(volcenginesdkcore.ApiClient(configuration))
        
        resp = api_instance.describe_volumes(
            volcenginesdkstorageebs.DescribeVolumesRequest(
                instance_id="i-yc21mps3gxl8j1i6wl5e",
            )
        )

        pprint(resp)
    except ApiException as e:
        print("Exception when call STORAGEEBSApi:DescribeVolumes: %s\n" % e)