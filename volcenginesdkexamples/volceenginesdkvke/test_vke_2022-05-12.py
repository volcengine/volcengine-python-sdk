from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvke
from pprint import pprint

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "AK"
    configuration.sk = "SK"
    configuration.region = "cn-beijing"

    # create an instance of the API class
    api_instance = volcenginesdkvke.VKEApi(volcenginesdkcore.ApiClient(configuration))
    resp = api_instance.list_clusters(volcenginesdkvke.ListClustersRequest())
    pprint(resp)
