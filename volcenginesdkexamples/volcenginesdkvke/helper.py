import time
from dataclasses import field, dataclass
from enum import Enum
from pprint import pprint
from typing import List

import volcenginesdkvke
from volcenginesdkvke import (AutoScalingForUpdateNodePoolConfigInput,
                              ClusterConfigForCreateClusterInput,
                              CreateAddonRequest, CreateAddonResponse,
                              CreateClusterRequest, CreateClusterResponse,
                              CreateNodePoolRequest, CreateNodePoolResponse,
                              FilterForListClustersInput,
                              FilterForListNodePoolsInput,
                              FilterForListNodesInput,
                              FlannelConfigForCreateClusterInput,
                              ListClustersRequest, ListClustersResponse,
                              ListNodePoolsRequest, ListNodePoolsResponse,
                              ListNodesRequest, ListNodesResponse,
                              LoginForCreateNodePoolInput,
                              NodeConfigForCreateNodePoolInput,
                              PodsConfigForCreateClusterInput,
                              SecurityForCreateNodePoolInput,
                              ServicesConfigForCreateClusterInput,
                              SystemVolumeForCreateNodePoolInput,
                              UpdateNodePoolConfigRequest,
                              UpdateNodePoolConfigResponse,
                              VpcCniConfigForCreateClusterInput)


class NetworkMode(Enum):

    Flannel = "Flannel"
    VpcCniShared = "VpcCniShared"


@dataclass
class VKEOption:
    """包含搭建最基本的VKE服务的选项"""

    cluster_name: str
    network_mode: str
    node_pool_name: str
    instance_type: str
    password: str
    subnet_ids: List[str] = field(default_factory=list[str])
    pod_cidrs: List[str] = field(default_factory=list[str])
    service_cidrs: List[str] = field(default_factory=list[str])
    api_server_public_access_enabled: bool = False
    auto_scaling: bool = False


def create_pods_config(opt: VKEOption) -> PodsConfigForCreateClusterInput:
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
            f"Network mode: {network_mode} is not accepted. Please choose from: 'Flannel' and 'VpcCniShared'."
        )
    return pod_config


def create_cluster(
    vke_api: volcenginesdkvke.VKEApi,
    name: str,
    cluster_config: ClusterConfigForCreateClusterInput,
    pods_config: PodsConfigForCreateClusterInput,
    services_config: ServicesConfigForCreateClusterInput,
) -> CreateClusterResponse:
    req = CreateClusterRequest(
        cluster_config=cluster_config,
        name=name,
        pods_config=pods_config,
        services_config=services_config,
    )
    return vke_api.create_cluster(req)


def get_cluster(
    vke_api: volcenginesdkvke.VKEApi, cluster_id: str
) -> ListClustersResponse:
    req = ListClustersRequest(filter=FilterForListClustersInput(ids=[cluster_id]))
    return vke_api.list_clusters(req)


def create_node_pool(
    vke_api: volcenginesdkvke.VKEApi,
    cluster_id: str,
    node_pool_name: str,
    instance_type: str,
    password: str,
    subnet_ids: List[str],
) -> CreateNodePoolResponse:
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


def get_node_pool(
    vke_api: volcenginesdkvke.VKEApi, node_pool_id: str
) -> ListNodePoolsResponse:
    req = ListNodePoolsRequest(filter=FilterForListNodePoolsInput(ids=[node_pool_id]))
    return vke_api.list_node_pools(req)


def update_node_pool(
    vke_api: volcenginesdkvke.VKEApi,
    cluster_id: str,
    node_pool_id: str,
    auto_scaling: bool,
) -> UpdateNodePoolConfigResponse:
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


def list_nodes(
    vke_api: volcenginesdkvke.VKEApi, node_pool_id: str
) -> ListNodesResponse:
    req = ListNodesRequest(filter=FilterForListNodesInput(node_pool_ids=[node_pool_id]))
    return vke_api.list_nodes(req)


def install_addon(
    vke_api: volcenginesdkvke.VKEApi, cluster_id: str
) -> CreateAddonResponse:
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


def create_vke(vke_api: volcenginesdkvke.VKEApi, opt: VKEOption):
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
    pprint(f"cluster id: {cluster_id}")

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
    pprint(f"node pool id: {node_pool_id}")

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
        vke_api, cluster_id, node_pool_id, auto_scaling=opt.auto_scaling,
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
