#!/usr/bin/env python3

import volcenginesdkcore
import volcenginesdkvke

from helper import VKEOption, create_vke


if __name__ == "__main__":
    # change the following variables
    cluster_name = "your_cluster_name"
    network_mode = "your_cluster_network_mode"  # choose from: Flannel, VpcCniShared
    subnet_ids = "your_subnet_id"  # type: list
    # ``pod_cidrs` is only required by cluster with Flannel network mode
    pod_cidrs = "your_pod_cidr"  # type: list
    service_cidrs = "your_service_cidr"  # type: list
    node_pool_name = "your_node_pool_name"
    instance_type = "your_instance_type"
    password = "your_password"

    # create vke option
    vke_opt = VKEOption(
        cluster_name=cluster_name,
        network_mode=network_mode,
        node_pool_name=node_pool_name,
        instance_type=instance_type,
        password=password,
        subnet_ids=subnet_ids,
        pod_cidrs=pod_cidrs,
        service_cidrs=service_cidrs,
    )

    # set up volc configuration
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "your_ak"
    configuration.sk = "your_sk"
    configuration.region = "your_region"

    # create an instance of the API class
    api_instance = volcenginesdkvke.VKEApi(volcenginesdkcore.ApiClient(configuration))

    # create vke
    create_vke(api_instance, vke_opt)
