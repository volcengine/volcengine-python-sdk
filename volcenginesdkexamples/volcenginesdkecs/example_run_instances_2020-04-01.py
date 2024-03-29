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
    req_network_interfaces = volcenginesdkecs.NetworkInterfaceForRunInstancesInput(
        security_group_ids=["sg-3ti78x9h8t4bw*****"],
        subnet_id="subnet-3tispp1nai4e8i****",
    )
    req_volumes = volcenginesdkecs.VolumeForRunInstancesInput(
        size=40,
        volume_type="ESSD_PL0",
    )
    run_instances_request = volcenginesdkecs.RunInstancesRequest(
        count=1,
        image_id="image-3tefr6wgx63vj0******",
        instance_name="instance-test",
        instance_type_id="ecs.g1ie.xlarge",
        network_interfaces=[req_network_interfaces],
        password="password@123",
        volumes=[req_volumes],
        zone_id="cn-beijing-a",
    )
    
    try:
        resp = api_instance.run_instances(run_instances_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
