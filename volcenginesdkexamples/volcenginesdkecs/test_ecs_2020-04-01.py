from __future__ import print_function
import volcenginesdkcore
import volcenginesdkecs
from pprint import pprint

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "AK"
    configuration.sk = "SK"
    configuration.region = "cn-beijing"

    # create an instance of the API class
    api_instance = volcenginesdkecs.ECSApi(volcenginesdkcore.ApiClient(configuration))
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
