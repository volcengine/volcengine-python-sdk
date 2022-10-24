#!/usr/bin/env python
# -*- coding: utf-8 -*-

import volcenginesdkcore
import volcenginesdkvke

from helper import VKEOption, create_vke


if __name__ == "__main__":

    # 设置VKE服务的选项
    # ``your_``开头的字段需要替换
    cluster_name = "your_cluster_name"
    network_mode = "your_cluster_network_mode"  # 选项: Flannel, VpcCniShared
    subnet_ids = "your_subnet_id"  # 类型: list
    # 如果是Flannel网络模式的集群，需要填写``pod_cidrs``
    pod_cidrs = "your_pod_cidr"  # 类型: list
    service_cidrs = "your_service_cidr"  # 类型: list
    node_pool_name = "your_node_pool_name"
    instance_type = "your_instance_type"
    password = "your_password"

    # 这里以创建一个Flannel网络模式的集群为例
    vke_opt = VKEOption(
        cluster_name=cluster_name,
        network_mode=network_mode,
        node_pool_name=node_pool_name,
        instance_type=instance_type,
        password=password,
        subnet_ids=subnet_ids,
        service_cidrs=service_cidrs,
        pod_cidrs=pod_cidrs,
    )

    # 设置火山配置
    # ``your_``开头的字段需要替换
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "your_ak"
    configuration.sk = "your_sk"
    configuration.region = "your_region"

    # 创建VKEApi实例
    api_instance = volcenginesdkvke.VKEApi(volcenginesdkcore.ApiClient(configuration))

    # 创建VKE服务
    create_vke(api_instance, vke_opt)
