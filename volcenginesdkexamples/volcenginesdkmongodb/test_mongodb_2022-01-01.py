from __future__ import print_function
import volcenginesdkcore
import volcenginesdkmongodb
from pprint import pprint
from volcenginesdkcore.rest import ApiException


if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.host = "xx-xx-xx.xx.org"
    configuration.ak = "xx"
    configuration.sk = "xx=="
    configuration.region = "xx-xx-xx"

    try:
        # create an instance of the API class
        api_instance = volcenginesdkmongodb.MONGODBApi(volcenginesdkcore.ApiClient(configuration))
        resp = api_instance.describe_db_instances(
            volcenginesdkmongodb.DescribeDBInstancesRequest(
                instance_id="mongo-replica-e405f8e2****",
            )
        )

        pprint(resp)
    except ApiException as e:
        print("Exception when call MONGONDBApi: %s\n" % e)