# -*- coding: utf-8 -*-

import time
from enum import Enum
from pprint import pprint

from volcenginesdkvke import (AutoScalingForUpdateNodePoolConfigInput,
                              ClusterConfigForCreateClusterInput,
                              CreateAddonRequest, CreateClusterRequest,
                              CreateNodePoolRequest,
                              FilterForListClustersInput,
                              FilterForListNodePoolsInput,
                              FilterForListNodesInput,
                              FlannelConfigForCreateClusterInput,
                              ListClustersRequest, ListNodePoolsRequest,
                              ListNodesRequest, LoginForCreateNodePoolInput,
                              NodeConfigForCreateNodePoolInput,
                              PodsConfigForCreateClusterInput,
                              SecurityForCreateNodePoolInput,
                              ServicesConfigForCreateClusterInput,
                              SystemVolumeForCreateNodePoolInput,
                              UpdateNodePoolConfigRequest,
                              VpcCniConfigForCreateClusterInput)


class NetworkMode(Enum):

    Flannel = "Flannel"
    VpcCniShared = "VpcCniShared"


class VKEOption:
    """包含搭建最基本的VKE服务的选项"""

    def __init__(
        self,
        cluster_name,
        network_mode,
        node_pool_name,
        instance_type,
        password,
        subnet_ids,
        service_cidrs,
        pod_cidrs=None,
        api_server_public_access_enabled=False,
        auto_scaling=False,
    ):

        self.cluster_name = cluster_name
        self.network_mode = network_mode
        self.node_pool_name = node_pool_name
        self.instance_type = instance_type
        self.password = password
        self.subnet_ids = subnet_ids
        self.service_cidrs = service_cidrs
        self.pod_cidrs = pod_cidrs
        self.api_server_public_access_enabled = api_server_public_access_enabled
        self.auto_scaling = auto_scaling


def create_pods_config(opt):
    """根据用户提供的集群NetworkMode类型，创建PodConfig"""
    network_mode = opt.network_mode
    if network_mode == NetworkMode.Flannel.value:
        pod_config = PodsConfigForCreateClusterInput(
            pod_network_mode=NetworkMode.Flannel.value,
            flannel_config=FlannelConfigForCreateClusterInput(
                pod_cidrs=opt.pod_cidrs,
            ),
        )
    elif network_mode == NetworkMode.VpcCniShared.value:
        pod_config = PodsConfigForCreateClusterInput(
            pod_network_mode=NetworkMode.VpcCniShared.value,
            vpc_cni_config=VpcCniConfigForCreateClusterInput(
                subnet_ids=opt.subnet_ids,
            ),
        )
    else:
        raise ValueError(
            "Network mode: {network_mode} is not accepted. Please choose from: 'Flannel' and 'VpcCniShared'.".format(
                network_mode=network_mode
            )
        )
    return pod_config


def create_cluster(vke_api, name, cluster_config, pods_config, services_config):
    """创建VKE集群"""
    req = CreateClusterRequest(
        cluster_config=cluster_config,
        name=name,
        pods_config=pods_config,
        services_config=services_config,
    )
    return vke_api.create_cluster(req)


def get_cluster(vke_api, cluster_id):
    """获取指定ID的集群信息"""
    req = ListClustersRequest(filter=FilterForListClustersInput(ids=[cluster_id]))
    return vke_api.list_clusters(req)


def create_node_pool(
    vke_api, cluster_id, node_pool_name, instance_type, password, subnet_ids
):
    """创建节点池"""
    node_config = NodeConfigForCreateNodePoolInput(
        instance_type_ids=[instance_type],
        security=SecurityForCreateNodePoolInput(
            login=LoginForCreateNodePoolInput(password=password),
        ),
        subnet_ids=subnet_ids,
        system_volume=SystemVolumeForCreateNodePoolInput(size=40, type="ESSD_PL0"),
    )
    req = CreateNodePoolRequest(
        cluster_id=cluster_id,
        name=node_pool_name,
        node_config=node_config,
    )
    return vke_api.create_node_pool(req)


def get_node_pool(vke_api, node_pool_id):
    """获取指定ID的节点池信息"""
    req = ListNodePoolsRequest(filter=FilterForListNodePoolsInput(ids=[node_pool_id]))
    return vke_api.list_node_pools(req)


def update_node_pool(vke_api, cluster_id, node_pool_id, auto_scaling):
    """更新节点池节点数量"""
    replicas = 1
    if auto_scaling:
        replicas = 0
    req = UpdateNodePoolConfigRequest(
        cluster_id=cluster_id,
        id=node_pool_id,
        auto_scaling=AutoScalingForUpdateNodePoolConfigInput(
            enabled=auto_scaling,
            desired_replicas=replicas,
        ),
    )
    return vke_api.update_node_pool_config(req)


def list_nodes(vke_api, node_pool_id):
    """获取指定ID的节点池的节点信息"""
    req = ListNodesRequest(filter=FilterForListNodesInput(node_pool_ids=[node_pool_id]))
    return vke_api.list_nodes(req)


def install_addon(vke_api, cluster_id):
    """安装插件"""
    # 在每个addon安装之后，sleep 5秒
    _interval = 5
    metrics_server_req = CreateAddonRequest(
        cluster_id=cluster_id, name="metrics-server"
    )
    metrics_server_resp = vke_api.create_addon(metrics_server_req)
    pprint(metrics_server_resp)

    time.sleep(_interval)

    coredns_req = CreateAddonRequest(cluster_id=cluster_id, name="core-dns")
    coredns_resp = vke_api.create_addon(coredns_req)
    pprint(coredns_resp)

    time.sleep(_interval)

    cluster_autoscaler_req = CreateAddonRequest(
        cluster_id=cluster_id,
        name="cluster-autoscaler",
        config='{"Expander":"random"}',
    )
    cluster_autoscaler_resp = vke_api.create_addon(cluster_autoscaler_req)
    pprint(cluster_autoscaler_resp)


def create_vke(vke_api, opt):
    """创建VKE服务"""
    pods_config = create_pods_config(opt)
    cluster_config = ClusterConfigForCreateClusterInput(
        api_server_public_access_enabled=opt.api_server_public_access_enabled,
        subnet_ids=opt.subnet_ids,
    )
    services_config = ServicesConfigForCreateClusterInput(
        service_cidrsv4=opt.service_cidrs
    )

    # 1. 创建集群
    create_cluster_resp = create_cluster(
        vke_api, opt.cluster_name, cluster_config, pods_config, services_config
    )
    cluster_id = create_cluster_resp.to_dict().get("id")
    pprint("cluster id: {}".format(cluster_id))

    # 2. 查询集群状态
    while True:
        get_cluser_resp = get_cluster(vke_api, cluster_id)
        results = get_cluser_resp.to_dict().get("items")
        if len(results) > 0 and results[0].get("status", {}).get("phase") == "Running":
            break
        time.sleep(10)

    # 3. 创建节点池
    create_node_pool_resp = create_node_pool(
        vke_api,
        cluster_id,
        opt.node_pool_name,
        opt.instance_type,
        opt.password,
        opt.subnet_ids,
    )
    node_pool_id = create_node_pool_resp.to_dict().get("id")
    pprint("node pool id: {}".format(node_pool_id))

    # 4. 查看节点池
    while True:
        get_node_pool_resp = get_node_pool(vke_api, node_pool_id)
        results = get_node_pool_resp.to_dict().get("items")
        if len(results) > 0 and results[0].get("status", {}).get("phase") == "Running":
            break
        time.sleep(10)
    pprint("node pool:")
    pprint(results)

    # 5. 查看节点列表
    list_nodes_resp = list_nodes(vke_api, node_pool_id)
    results = list_nodes_resp.to_dict().get("items")
    pprint("node list:")
    pprint(results)

    # 6. 安装组件 & 设置节点池弹性策略
    pprint("install addon (including cluster-autoscaler)")
    install_addon(vke_api, cluster_id)

    # 7. 修改节点数量
    pprint("update node pool")
    update_node_pool_resp = update_node_pool(
        vke_api,
        cluster_id,
        node_pool_id,
        auto_scaling=opt.auto_scaling,
    )
    pprint(update_node_pool_resp)

    # 8. 查看节点列表
    pprint("check nodes count")
    while len(results) == 0:
        list_nodes_resp = list_nodes(vke_api, node_pool_id)
        results = list_nodes_resp.to_dict().get("items")
        time.sleep(10)
    pprint("node list:")
    pprint(results)
