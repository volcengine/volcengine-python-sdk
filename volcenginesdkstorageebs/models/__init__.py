# coding: utf-8

# flake8: noqa
"""
    storage_ebs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from volcenginesdkstorageebs.models.apply_auto_snapshot_policy_request import ApplyAutoSnapshotPolicyRequest
from volcenginesdkstorageebs.models.apply_auto_snapshot_policy_response import ApplyAutoSnapshotPolicyResponse
from volcenginesdkstorageebs.models.attach_volume_request import AttachVolumeRequest
from volcenginesdkstorageebs.models.attach_volume_response import AttachVolumeResponse
from volcenginesdkstorageebs.models.auto_renew_reserved_storage_capacity_request import AutoRenewReservedStorageCapacityRequest
from volcenginesdkstorageebs.models.auto_renew_reserved_storage_capacity_response import AutoRenewReservedStorageCapacityResponse
from volcenginesdkstorageebs.models.auto_snapshot_policy_for_describe_auto_snapshot_policy_output import AutoSnapshotPolicyForDescribeAutoSnapshotPolicyOutput
from volcenginesdkstorageebs.models.baseline_performance_for_describe_volumes_output import BaselinePerformanceForDescribeVolumesOutput
from volcenginesdkstorageebs.models.cancel_auto_snapshot_policy_request import CancelAutoSnapshotPolicyRequest
from volcenginesdkstorageebs.models.cancel_auto_snapshot_policy_response import CancelAutoSnapshotPolicyResponse
from volcenginesdkstorageebs.models.check_user_rsc_permit_request import CheckUserRscPermitRequest
from volcenginesdkstorageebs.models.check_user_rsc_permit_response import CheckUserRscPermitResponse
from volcenginesdkstorageebs.models.create_auto_snapshot_policy_request import CreateAutoSnapshotPolicyRequest
from volcenginesdkstorageebs.models.create_auto_snapshot_policy_response import CreateAutoSnapshotPolicyResponse
from volcenginesdkstorageebs.models.create_snapshot_group_request import CreateSnapshotGroupRequest
from volcenginesdkstorageebs.models.create_snapshot_group_response import CreateSnapshotGroupResponse
from volcenginesdkstorageebs.models.create_snapshot_request import CreateSnapshotRequest
from volcenginesdkstorageebs.models.create_snapshot_response import CreateSnapshotResponse
from volcenginesdkstorageebs.models.create_tags_request import CreateTagsRequest
from volcenginesdkstorageebs.models.create_tags_response import CreateTagsResponse
from volcenginesdkstorageebs.models.create_volume_request import CreateVolumeRequest
from volcenginesdkstorageebs.models.create_volume_response import CreateVolumeResponse
from volcenginesdkstorageebs.models.delete_auto_snapshot_policy_request import DeleteAutoSnapshotPolicyRequest
from volcenginesdkstorageebs.models.delete_auto_snapshot_policy_response import DeleteAutoSnapshotPolicyResponse
from volcenginesdkstorageebs.models.delete_snapshot_group_request import DeleteSnapshotGroupRequest
from volcenginesdkstorageebs.models.delete_snapshot_group_response import DeleteSnapshotGroupResponse
from volcenginesdkstorageebs.models.delete_snapshot_request import DeleteSnapshotRequest
from volcenginesdkstorageebs.models.delete_snapshot_response import DeleteSnapshotResponse
from volcenginesdkstorageebs.models.delete_tags_request import DeleteTagsRequest
from volcenginesdkstorageebs.models.delete_tags_response import DeleteTagsResponse
from volcenginesdkstorageebs.models.delete_volume_request import DeleteVolumeRequest
from volcenginesdkstorageebs.models.delete_volume_response import DeleteVolumeResponse
from volcenginesdkstorageebs.models.describe_auto_snapshot_policy_request import DescribeAutoSnapshotPolicyRequest
from volcenginesdkstorageebs.models.describe_auto_snapshot_policy_response import DescribeAutoSnapshotPolicyResponse
from volcenginesdkstorageebs.models.describe_reserved_storage_capacity_request import DescribeReservedStorageCapacityRequest
from volcenginesdkstorageebs.models.describe_reserved_storage_capacity_response import DescribeReservedStorageCapacityResponse
from volcenginesdkstorageebs.models.describe_snapshot_chains_request import DescribeSnapshotChainsRequest
from volcenginesdkstorageebs.models.describe_snapshot_chains_response import DescribeSnapshotChainsResponse
from volcenginesdkstorageebs.models.describe_snapshot_groups_request import DescribeSnapshotGroupsRequest
from volcenginesdkstorageebs.models.describe_snapshot_groups_response import DescribeSnapshotGroupsResponse
from volcenginesdkstorageebs.models.describe_snapshots_request import DescribeSnapshotsRequest
from volcenginesdkstorageebs.models.describe_snapshots_response import DescribeSnapshotsResponse
from volcenginesdkstorageebs.models.describe_snapshots_usage_request import DescribeSnapshotsUsageRequest
from volcenginesdkstorageebs.models.describe_snapshots_usage_response import DescribeSnapshotsUsageResponse
from volcenginesdkstorageebs.models.describe_tags_request import DescribeTagsRequest
from volcenginesdkstorageebs.models.describe_tags_response import DescribeTagsResponse
from volcenginesdkstorageebs.models.describe_volume_type_request import DescribeVolumeTypeRequest
from volcenginesdkstorageebs.models.describe_volume_type_response import DescribeVolumeTypeResponse
from volcenginesdkstorageebs.models.describe_volumes_request import DescribeVolumesRequest
from volcenginesdkstorageebs.models.describe_volumes_response import DescribeVolumesResponse
from volcenginesdkstorageebs.models.detach_volume_request import DetachVolumeRequest
from volcenginesdkstorageebs.models.detach_volume_response import DetachVolumeResponse
from volcenginesdkstorageebs.models.error_for_create_tags_output import ErrorForCreateTagsOutput
from volcenginesdkstorageebs.models.extend_volume_request import ExtendVolumeRequest
from volcenginesdkstorageebs.models.extend_volume_response import ExtendVolumeResponse
from volcenginesdkstorageebs.models.extra_performance_for_describe_volumes_output import ExtraPerformanceForDescribeVolumesOutput
from volcenginesdkstorageebs.models.extra_performance_type_for_describe_volume_type_output import ExtraPerformanceTypeForDescribeVolumeTypeOutput
from volcenginesdkstorageebs.models.filter_for_describe_snapshots_input import FilterForDescribeSnapshotsInput
from volcenginesdkstorageebs.models.manual_renew_reserved_storage_capacity_request import ManualRenewReservedStorageCapacityRequest
from volcenginesdkstorageebs.models.manual_renew_reserved_storage_capacity_response import ManualRenewReservedStorageCapacityResponse
from volcenginesdkstorageebs.models.modify_auto_snapshot_policy_request import ModifyAutoSnapshotPolicyRequest
from volcenginesdkstorageebs.models.modify_auto_snapshot_policy_response import ModifyAutoSnapshotPolicyResponse
from volcenginesdkstorageebs.models.modify_snapshot_attribute_request import ModifySnapshotAttributeRequest
from volcenginesdkstorageebs.models.modify_snapshot_attribute_response import ModifySnapshotAttributeResponse
from volcenginesdkstorageebs.models.modify_snapshot_group_request import ModifySnapshotGroupRequest
from volcenginesdkstorageebs.models.modify_snapshot_group_response import ModifySnapshotGroupResponse
from volcenginesdkstorageebs.models.modify_volume_attribute_request import ModifyVolumeAttributeRequest
from volcenginesdkstorageebs.models.modify_volume_attribute_response import ModifyVolumeAttributeResponse
from volcenginesdkstorageebs.models.modify_volume_charge_type_request import ModifyVolumeChargeTypeRequest
from volcenginesdkstorageebs.models.modify_volume_charge_type_response import ModifyVolumeChargeTypeResponse
from volcenginesdkstorageebs.models.modify_volume_extra_performance_request import ModifyVolumeExtraPerformanceRequest
from volcenginesdkstorageebs.models.modify_volume_extra_performance_response import ModifyVolumeExtraPerformanceResponse
from volcenginesdkstorageebs.models.modify_volume_spec_request import ModifyVolumeSpecRequest
from volcenginesdkstorageebs.models.modify_volume_spec_response import ModifyVolumeSpecResponse
from volcenginesdkstorageebs.models.operation_detail_for_create_tags_output import OperationDetailForCreateTagsOutput
from volcenginesdkstorageebs.models.purchase_reserved_storage_capacity_request import PurchaseReservedStorageCapacityRequest
from volcenginesdkstorageebs.models.purchase_reserved_storage_capacity_response import PurchaseReservedStorageCapacityResponse
from volcenginesdkstorageebs.models.rollback_snapshot_group_request import RollbackSnapshotGroupRequest
from volcenginesdkstorageebs.models.rollback_snapshot_group_response import RollbackSnapshotGroupResponse
from volcenginesdkstorageebs.models.rollback_volume_request import RollbackVolumeRequest
from volcenginesdkstorageebs.models.rollback_volume_response import RollbackVolumeResponse
from volcenginesdkstorageebs.models.rsc_info_for_describe_reserved_storage_capacity_output import RscInfoForDescribeReservedStorageCapacityOutput
from volcenginesdkstorageebs.models.service_purchase_rsc_preorder_request import ServicePurchaseRscPreorderRequest
from volcenginesdkstorageebs.models.service_purchase_rsc_preorder_response import ServicePurchaseRscPreorderResponse
from volcenginesdkstorageebs.models.snapshot_chain_for_describe_snapshot_chains_output import SnapshotChainForDescribeSnapshotChainsOutput
from volcenginesdkstorageebs.models.snapshot_for_describe_snapshot_groups_output import SnapshotForDescribeSnapshotGroupsOutput
from volcenginesdkstorageebs.models.snapshot_for_describe_snapshots_output import SnapshotForDescribeSnapshotsOutput
from volcenginesdkstorageebs.models.snapshot_group_for_describe_snapshot_groups_output import SnapshotGroupForDescribeSnapshotGroupsOutput
from volcenginesdkstorageebs.models.tag_filter_for_describe_tags_input import TagFilterForDescribeTagsInput
from volcenginesdkstorageebs.models.tag_filter_for_describe_volumes_input import TagFilterForDescribeVolumesInput
from volcenginesdkstorageebs.models.tag_for_create_auto_snapshot_policy_input import TagForCreateAutoSnapshotPolicyInput
from volcenginesdkstorageebs.models.tag_for_create_snapshot_group_input import TagForCreateSnapshotGroupInput
from volcenginesdkstorageebs.models.tag_for_create_snapshot_input import TagForCreateSnapshotInput
from volcenginesdkstorageebs.models.tag_for_create_tags_input import TagForCreateTagsInput
from volcenginesdkstorageebs.models.tag_for_create_volume_input import TagForCreateVolumeInput
from volcenginesdkstorageebs.models.tag_for_describe_auto_snapshot_policy_output import TagForDescribeAutoSnapshotPolicyOutput
from volcenginesdkstorageebs.models.tag_for_describe_snapshot_groups_output import TagForDescribeSnapshotGroupsOutput
from volcenginesdkstorageebs.models.tag_for_describe_snapshots_output import TagForDescribeSnapshotsOutput
from volcenginesdkstorageebs.models.tag_for_describe_volumes_output import TagForDescribeVolumesOutput
from volcenginesdkstorageebs.models.tag_resource_for_describe_tags_output import TagResourceForDescribeTagsOutput
from volcenginesdkstorageebs.models.total_performance_for_describe_volumes_output import TotalPerformanceForDescribeVolumesOutput
from volcenginesdkstorageebs.models.volume_for_describe_volumes_output import VolumeForDescribeVolumesOutput
from volcenginesdkstorageebs.models.volume_type_for_describe_volume_type_output import VolumeTypeForDescribeVolumeTypeOutput
