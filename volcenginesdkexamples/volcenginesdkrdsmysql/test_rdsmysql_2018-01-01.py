from __future__ import print_function
import volcenginesdkcore
import volcenginesdkrdsmysql
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
        api_instance = volcenginesdkrdsmysql.RDSMYSQLApi(volcenginesdkcore.ApiClient(configuration))
        resp = api_instance.describe_db_instance(
            volcenginesdkrdsmysql.DescribeDBInstanceRequest(
                instance_id="rds-mysql-h441603c68aaa***"
            )
        )

        pprint(resp)
    except ApiException as e:
        print("Exception when call RDSMYSQLApi:DescribeDBInstance: %s\n" % e)