from __future__ import print_function
import volcenginesdkcore
import volcenginesdkredis
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
        api_instance = volcenginesdkredis.REDISApi(volcenginesdkcore.ApiClient(configuration))
        resp = api_instance.describe_db_instances(
            volcenginesdkredis.DescribeDBInstancesRequest(
                region_id="cn-beijing",
                page_number=1,
                page_size=10,
            )
        )

        pprint(resp)
    except ApiException as e:
        print("Exception when call REDISApi: %s\n" % e)