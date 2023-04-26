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
    configuration.client_side_validation = True
    # set default configuration
    volcenginesdkcore.Configuration.set_default(configuration)

    # use global default configuration
    api_instance = volcenginesdkecs.ECSApi()
    # use custom configuration
    # api_instance = volcenginesdkecs.ECSApi(volcenginesdkcore.ApiClient(configuration))

    try:
        resp = api_instance.run_instances(
            volcenginesdkecs.RunInstancesRequest(
                instance_name="insname",
                instance_type="ecs.g1.large",
                zone_id="cn-beijing-a",
                network_interfaces=[volcenginesdkecs.NetworkInterfaceForRunInstancesInput(
                    subnet_id="subnet-2d68bh73d858ozfekrm8fj",
                    security_group_ids=["sg-2b3dq7v0ha0w2dx0eg0nhljv"],
                )],
                image_id="image-ybvz29l3da4ox5h0m9",
                volumes=[volcenginesdkecs.VolumeForRunInstancesInput(
                    volume_type="ESSD",
                    size=40,
                )],
                key_pair_name="vtable",
                instance_charge_type="PostPaid"
            ))
        pprint(resp)
    except ApiException as e:
        print("Exception when calling ECSApi->run_instances: %s\n" % e)
