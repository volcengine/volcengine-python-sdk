# coding: utf-8

# flake8: noqa
"""
    transitrouter

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from volcenginesdktransitrouter.models.accept_shared_transit_router_request import AcceptSharedTransitRouterRequest
from volcenginesdktransitrouter.models.accept_shared_transit_router_response import AcceptSharedTransitRouterResponse
from volcenginesdktransitrouter.models.allocation_for_describe_transit_router_bandwidth_packages_output import AllocationForDescribeTransitRouterBandwidthPackagesOutput
from volcenginesdktransitrouter.models.associate_transit_router_attachment_to_route_table_request import AssociateTransitRouterAttachmentToRouteTableRequest
from volcenginesdktransitrouter.models.associate_transit_router_attachment_to_route_table_response import AssociateTransitRouterAttachmentToRouteTableResponse
from volcenginesdktransitrouter.models.associate_transit_router_forward_policy_table_to_attachment_request import AssociateTransitRouterForwardPolicyTableToAttachmentRequest
from volcenginesdktransitrouter.models.associate_transit_router_forward_policy_table_to_attachment_response import AssociateTransitRouterForwardPolicyTableToAttachmentResponse
from volcenginesdktransitrouter.models.associate_transit_router_route_policy_to_route_table_request import AssociateTransitRouterRoutePolicyToRouteTableRequest
from volcenginesdktransitrouter.models.associate_transit_router_route_policy_to_route_table_response import AssociateTransitRouterRoutePolicyToRouteTableResponse
from volcenginesdktransitrouter.models.attach_point_for_create_transit_router_vpc_attachment_input import AttachPointForCreateTransitRouterVpcAttachmentInput
from volcenginesdktransitrouter.models.attach_point_for_describe_transit_router_vpc_attachments_output import AttachPointForDescribeTransitRouterVpcAttachmentsOutput
from volcenginesdktransitrouter.models.attach_point_for_modify_transit_router_vpc_attachment_attributes_input import AttachPointForModifyTransitRouterVpcAttachmentAttributesInput
from volcenginesdktransitrouter.models.create_transit_router_bandwidth_package_request import CreateTransitRouterBandwidthPackageRequest
from volcenginesdktransitrouter.models.create_transit_router_bandwidth_package_response import CreateTransitRouterBandwidthPackageResponse
from volcenginesdktransitrouter.models.create_transit_router_direct_connect_gateway_attachment_request import CreateTransitRouterDirectConnectGatewayAttachmentRequest
from volcenginesdktransitrouter.models.create_transit_router_direct_connect_gateway_attachment_response import CreateTransitRouterDirectConnectGatewayAttachmentResponse
from volcenginesdktransitrouter.models.create_transit_router_forward_policy_entry_request import CreateTransitRouterForwardPolicyEntryRequest
from volcenginesdktransitrouter.models.create_transit_router_forward_policy_entry_response import CreateTransitRouterForwardPolicyEntryResponse
from volcenginesdktransitrouter.models.create_transit_router_forward_policy_table_request import CreateTransitRouterForwardPolicyTableRequest
from volcenginesdktransitrouter.models.create_transit_router_forward_policy_table_response import CreateTransitRouterForwardPolicyTableResponse
from volcenginesdktransitrouter.models.create_transit_router_grant_rule_request import CreateTransitRouterGrantRuleRequest
from volcenginesdktransitrouter.models.create_transit_router_grant_rule_response import CreateTransitRouterGrantRuleResponse
from volcenginesdktransitrouter.models.create_transit_router_peer_attachment_request import CreateTransitRouterPeerAttachmentRequest
from volcenginesdktransitrouter.models.create_transit_router_peer_attachment_response import CreateTransitRouterPeerAttachmentResponse
from volcenginesdktransitrouter.models.create_transit_router_request import CreateTransitRouterRequest
from volcenginesdktransitrouter.models.create_transit_router_response import CreateTransitRouterResponse
from volcenginesdktransitrouter.models.create_transit_router_route_entry_request import CreateTransitRouterRouteEntryRequest
from volcenginesdktransitrouter.models.create_transit_router_route_entry_response import CreateTransitRouterRouteEntryResponse
from volcenginesdktransitrouter.models.create_transit_router_route_policy_entry_request import CreateTransitRouterRoutePolicyEntryRequest
from volcenginesdktransitrouter.models.create_transit_router_route_policy_entry_response import CreateTransitRouterRoutePolicyEntryResponse
from volcenginesdktransitrouter.models.create_transit_router_route_policy_table_request import CreateTransitRouterRoutePolicyTableRequest
from volcenginesdktransitrouter.models.create_transit_router_route_policy_table_response import CreateTransitRouterRoutePolicyTableResponse
from volcenginesdktransitrouter.models.create_transit_router_route_table_request import CreateTransitRouterRouteTableRequest
from volcenginesdktransitrouter.models.create_transit_router_route_table_response import CreateTransitRouterRouteTableResponse
from volcenginesdktransitrouter.models.create_transit_router_vpc_attachment_request import CreateTransitRouterVpcAttachmentRequest
from volcenginesdktransitrouter.models.create_transit_router_vpc_attachment_response import CreateTransitRouterVpcAttachmentResponse
from volcenginesdktransitrouter.models.create_transit_router_vpn_attachment_request import CreateTransitRouterVpnAttachmentRequest
from volcenginesdktransitrouter.models.create_transit_router_vpn_attachment_response import CreateTransitRouterVpnAttachmentResponse
from volcenginesdktransitrouter.models.delete_transit_router_bandwidth_package_request import DeleteTransitRouterBandwidthPackageRequest
from volcenginesdktransitrouter.models.delete_transit_router_bandwidth_package_response import DeleteTransitRouterBandwidthPackageResponse
from volcenginesdktransitrouter.models.delete_transit_router_direct_connect_gateway_attachment_request import DeleteTransitRouterDirectConnectGatewayAttachmentRequest
from volcenginesdktransitrouter.models.delete_transit_router_direct_connect_gateway_attachment_response import DeleteTransitRouterDirectConnectGatewayAttachmentResponse
from volcenginesdktransitrouter.models.delete_transit_router_forward_policy_entry_request import DeleteTransitRouterForwardPolicyEntryRequest
from volcenginesdktransitrouter.models.delete_transit_router_forward_policy_entry_response import DeleteTransitRouterForwardPolicyEntryResponse
from volcenginesdktransitrouter.models.delete_transit_router_forward_policy_table_request import DeleteTransitRouterForwardPolicyTableRequest
from volcenginesdktransitrouter.models.delete_transit_router_forward_policy_table_response import DeleteTransitRouterForwardPolicyTableResponse
from volcenginesdktransitrouter.models.delete_transit_router_grant_rule_request import DeleteTransitRouterGrantRuleRequest
from volcenginesdktransitrouter.models.delete_transit_router_grant_rule_response import DeleteTransitRouterGrantRuleResponse
from volcenginesdktransitrouter.models.delete_transit_router_peer_attachment_request import DeleteTransitRouterPeerAttachmentRequest
from volcenginesdktransitrouter.models.delete_transit_router_peer_attachment_response import DeleteTransitRouterPeerAttachmentResponse
from volcenginesdktransitrouter.models.delete_transit_router_request import DeleteTransitRouterRequest
from volcenginesdktransitrouter.models.delete_transit_router_response import DeleteTransitRouterResponse
from volcenginesdktransitrouter.models.delete_transit_router_route_entry_request import DeleteTransitRouterRouteEntryRequest
from volcenginesdktransitrouter.models.delete_transit_router_route_entry_response import DeleteTransitRouterRouteEntryResponse
from volcenginesdktransitrouter.models.delete_transit_router_route_policy_entry_request import DeleteTransitRouterRoutePolicyEntryRequest
from volcenginesdktransitrouter.models.delete_transit_router_route_policy_entry_response import DeleteTransitRouterRoutePolicyEntryResponse
from volcenginesdktransitrouter.models.delete_transit_router_route_policy_table_request import DeleteTransitRouterRoutePolicyTableRequest
from volcenginesdktransitrouter.models.delete_transit_router_route_policy_table_response import DeleteTransitRouterRoutePolicyTableResponse
from volcenginesdktransitrouter.models.delete_transit_router_route_table_request import DeleteTransitRouterRouteTableRequest
from volcenginesdktransitrouter.models.delete_transit_router_route_table_response import DeleteTransitRouterRouteTableResponse
from volcenginesdktransitrouter.models.delete_transit_router_vpc_attachment_request import DeleteTransitRouterVpcAttachmentRequest
from volcenginesdktransitrouter.models.delete_transit_router_vpc_attachment_response import DeleteTransitRouterVpcAttachmentResponse
from volcenginesdktransitrouter.models.delete_transit_router_vpn_attachment_request import DeleteTransitRouterVpnAttachmentRequest
from volcenginesdktransitrouter.models.delete_transit_router_vpn_attachment_response import DeleteTransitRouterVpnAttachmentResponse
from volcenginesdktransitrouter.models.describe_transit_router_attachments_request import DescribeTransitRouterAttachmentsRequest
from volcenginesdktransitrouter.models.describe_transit_router_attachments_response import DescribeTransitRouterAttachmentsResponse
from volcenginesdktransitrouter.models.describe_transit_router_bandwidth_packages_billing_request import DescribeTransitRouterBandwidthPackagesBillingRequest
from volcenginesdktransitrouter.models.describe_transit_router_bandwidth_packages_billing_response import DescribeTransitRouterBandwidthPackagesBillingResponse
from volcenginesdktransitrouter.models.describe_transit_router_bandwidth_packages_request import DescribeTransitRouterBandwidthPackagesRequest
from volcenginesdktransitrouter.models.describe_transit_router_bandwidth_packages_response import DescribeTransitRouterBandwidthPackagesResponse
from volcenginesdktransitrouter.models.describe_transit_router_direct_connect_gateway_attachments_request import DescribeTransitRouterDirectConnectGatewayAttachmentsRequest
from volcenginesdktransitrouter.models.describe_transit_router_direct_connect_gateway_attachments_response import DescribeTransitRouterDirectConnectGatewayAttachmentsResponse
from volcenginesdktransitrouter.models.describe_transit_router_forward_policy_entries_request import DescribeTransitRouterForwardPolicyEntriesRequest
from volcenginesdktransitrouter.models.describe_transit_router_forward_policy_entries_response import DescribeTransitRouterForwardPolicyEntriesResponse
from volcenginesdktransitrouter.models.describe_transit_router_forward_policy_tables_request import DescribeTransitRouterForwardPolicyTablesRequest
from volcenginesdktransitrouter.models.describe_transit_router_forward_policy_tables_response import DescribeTransitRouterForwardPolicyTablesResponse
from volcenginesdktransitrouter.models.describe_transit_router_grant_rules_request import DescribeTransitRouterGrantRulesRequest
from volcenginesdktransitrouter.models.describe_transit_router_grant_rules_response import DescribeTransitRouterGrantRulesResponse
from volcenginesdktransitrouter.models.describe_transit_router_peer_attachments_request import DescribeTransitRouterPeerAttachmentsRequest
from volcenginesdktransitrouter.models.describe_transit_router_peer_attachments_response import DescribeTransitRouterPeerAttachmentsResponse
from volcenginesdktransitrouter.models.describe_transit_router_regions_request import DescribeTransitRouterRegionsRequest
from volcenginesdktransitrouter.models.describe_transit_router_regions_response import DescribeTransitRouterRegionsResponse
from volcenginesdktransitrouter.models.describe_transit_router_route_entries_request import DescribeTransitRouterRouteEntriesRequest
from volcenginesdktransitrouter.models.describe_transit_router_route_entries_response import DescribeTransitRouterRouteEntriesResponse
from volcenginesdktransitrouter.models.describe_transit_router_route_policy_entries_request import DescribeTransitRouterRoutePolicyEntriesRequest
from volcenginesdktransitrouter.models.describe_transit_router_route_policy_entries_response import DescribeTransitRouterRoutePolicyEntriesResponse
from volcenginesdktransitrouter.models.describe_transit_router_route_policy_tables_request import DescribeTransitRouterRoutePolicyTablesRequest
from volcenginesdktransitrouter.models.describe_transit_router_route_policy_tables_response import DescribeTransitRouterRoutePolicyTablesResponse
from volcenginesdktransitrouter.models.describe_transit_router_route_table_associations_request import DescribeTransitRouterRouteTableAssociationsRequest
from volcenginesdktransitrouter.models.describe_transit_router_route_table_associations_response import DescribeTransitRouterRouteTableAssociationsResponse
from volcenginesdktransitrouter.models.describe_transit_router_route_table_propagations_request import DescribeTransitRouterRouteTablePropagationsRequest
from volcenginesdktransitrouter.models.describe_transit_router_route_table_propagations_response import DescribeTransitRouterRouteTablePropagationsResponse
from volcenginesdktransitrouter.models.describe_transit_router_route_tables_request import DescribeTransitRouterRouteTablesRequest
from volcenginesdktransitrouter.models.describe_transit_router_route_tables_response import DescribeTransitRouterRouteTablesResponse
from volcenginesdktransitrouter.models.describe_transit_router_vpc_attachments_request import DescribeTransitRouterVpcAttachmentsRequest
from volcenginesdktransitrouter.models.describe_transit_router_vpc_attachments_response import DescribeTransitRouterVpcAttachmentsResponse
from volcenginesdktransitrouter.models.describe_transit_router_vpn_attachments_request import DescribeTransitRouterVpnAttachmentsRequest
from volcenginesdktransitrouter.models.describe_transit_router_vpn_attachments_response import DescribeTransitRouterVpnAttachmentsResponse
from volcenginesdktransitrouter.models.describe_transit_routers_request import DescribeTransitRoutersRequest
from volcenginesdktransitrouter.models.describe_transit_routers_response import DescribeTransitRoutersResponse
from volcenginesdktransitrouter.models.disable_transit_router_route_table_propagation_request import DisableTransitRouterRouteTablePropagationRequest
from volcenginesdktransitrouter.models.disable_transit_router_route_table_propagation_response import DisableTransitRouterRouteTablePropagationResponse
from volcenginesdktransitrouter.models.dissociate_transit_router_attachment_from_route_table_request import DissociateTransitRouterAttachmentFromRouteTableRequest
from volcenginesdktransitrouter.models.dissociate_transit_router_attachment_from_route_table_response import DissociateTransitRouterAttachmentFromRouteTableResponse
from volcenginesdktransitrouter.models.dissociate_transit_router_forward_policy_table_from_attachment_request import DissociateTransitRouterForwardPolicyTableFromAttachmentRequest
from volcenginesdktransitrouter.models.dissociate_transit_router_forward_policy_table_from_attachment_response import DissociateTransitRouterForwardPolicyTableFromAttachmentResponse
from volcenginesdktransitrouter.models.dissociate_transit_router_route_policy_from_route_table_request import DissociateTransitRouterRoutePolicyFromRouteTableRequest
from volcenginesdktransitrouter.models.dissociate_transit_router_route_policy_from_route_table_response import DissociateTransitRouterRoutePolicyFromRouteTableResponse
from volcenginesdktransitrouter.models.enable_transit_router_route_table_propagation_request import EnableTransitRouterRouteTablePropagationRequest
from volcenginesdktransitrouter.models.enable_transit_router_route_table_propagation_response import EnableTransitRouterRouteTablePropagationResponse
from volcenginesdktransitrouter.models.list_tags_for_resources_request import ListTagsForResourcesRequest
from volcenginesdktransitrouter.models.list_tags_for_resources_response import ListTagsForResourcesResponse
from volcenginesdktransitrouter.models.modify_transit_router_attributes_request import ModifyTransitRouterAttributesRequest
from volcenginesdktransitrouter.models.modify_transit_router_attributes_response import ModifyTransitRouterAttributesResponse
from volcenginesdktransitrouter.models.modify_transit_router_bandwidth_package_attributes_request import ModifyTransitRouterBandwidthPackageAttributesRequest
from volcenginesdktransitrouter.models.modify_transit_router_bandwidth_package_attributes_response import ModifyTransitRouterBandwidthPackageAttributesResponse
from volcenginesdktransitrouter.models.modify_transit_router_direct_connect_gateway_attachment_attributes_request import ModifyTransitRouterDirectConnectGatewayAttachmentAttributesRequest
from volcenginesdktransitrouter.models.modify_transit_router_direct_connect_gateway_attachment_attributes_response import ModifyTransitRouterDirectConnectGatewayAttachmentAttributesResponse
from volcenginesdktransitrouter.models.modify_transit_router_forward_policy_entry_attributes_request import ModifyTransitRouterForwardPolicyEntryAttributesRequest
from volcenginesdktransitrouter.models.modify_transit_router_forward_policy_entry_attributes_response import ModifyTransitRouterForwardPolicyEntryAttributesResponse
from volcenginesdktransitrouter.models.modify_transit_router_forward_policy_table_association_request import ModifyTransitRouterForwardPolicyTableAssociationRequest
from volcenginesdktransitrouter.models.modify_transit_router_forward_policy_table_association_response import ModifyTransitRouterForwardPolicyTableAssociationResponse
from volcenginesdktransitrouter.models.modify_transit_router_forward_policy_table_attributes_request import ModifyTransitRouterForwardPolicyTableAttributesRequest
from volcenginesdktransitrouter.models.modify_transit_router_forward_policy_table_attributes_response import ModifyTransitRouterForwardPolicyTableAttributesResponse
from volcenginesdktransitrouter.models.modify_transit_router_grant_rule_attributes_request import ModifyTransitRouterGrantRuleAttributesRequest
from volcenginesdktransitrouter.models.modify_transit_router_grant_rule_attributes_response import ModifyTransitRouterGrantRuleAttributesResponse
from volcenginesdktransitrouter.models.modify_transit_router_peer_attachment_attributes_request import ModifyTransitRouterPeerAttachmentAttributesRequest
from volcenginesdktransitrouter.models.modify_transit_router_peer_attachment_attributes_response import ModifyTransitRouterPeerAttachmentAttributesResponse
from volcenginesdktransitrouter.models.modify_transit_router_route_entry_attributes_request import ModifyTransitRouterRouteEntryAttributesRequest
from volcenginesdktransitrouter.models.modify_transit_router_route_entry_attributes_response import ModifyTransitRouterRouteEntryAttributesResponse
from volcenginesdktransitrouter.models.modify_transit_router_route_policy_association_request import ModifyTransitRouterRoutePolicyAssociationRequest
from volcenginesdktransitrouter.models.modify_transit_router_route_policy_association_response import ModifyTransitRouterRoutePolicyAssociationResponse
from volcenginesdktransitrouter.models.modify_transit_router_route_policy_entry_attributes_request import ModifyTransitRouterRoutePolicyEntryAttributesRequest
from volcenginesdktransitrouter.models.modify_transit_router_route_policy_entry_attributes_response import ModifyTransitRouterRoutePolicyEntryAttributesResponse
from volcenginesdktransitrouter.models.modify_transit_router_route_policy_table_attributes_request import ModifyTransitRouterRoutePolicyTableAttributesRequest
from volcenginesdktransitrouter.models.modify_transit_router_route_policy_table_attributes_response import ModifyTransitRouterRoutePolicyTableAttributesResponse
from volcenginesdktransitrouter.models.modify_transit_router_route_table_association_attributes_request import ModifyTransitRouterRouteTableAssociationAttributesRequest
from volcenginesdktransitrouter.models.modify_transit_router_route_table_association_attributes_response import ModifyTransitRouterRouteTableAssociationAttributesResponse
from volcenginesdktransitrouter.models.modify_transit_router_route_table_attributes_request import ModifyTransitRouterRouteTableAttributesRequest
from volcenginesdktransitrouter.models.modify_transit_router_route_table_attributes_response import ModifyTransitRouterRouteTableAttributesResponse
from volcenginesdktransitrouter.models.modify_transit_router_vpc_attachment_attributes_request import ModifyTransitRouterVpcAttachmentAttributesRequest
from volcenginesdktransitrouter.models.modify_transit_router_vpc_attachment_attributes_response import ModifyTransitRouterVpcAttachmentAttributesResponse
from volcenginesdktransitrouter.models.modify_transit_router_vpn_attachment_attributes_request import ModifyTransitRouterVpnAttachmentAttributesRequest
from volcenginesdktransitrouter.models.modify_transit_router_vpn_attachment_attributes_response import ModifyTransitRouterVpnAttachmentAttributesResponse
from volcenginesdktransitrouter.models.region_for_describe_transit_router_regions_output import RegionForDescribeTransitRouterRegionsOutput
from volcenginesdktransitrouter.models.reject_shared_transit_router_request import RejectSharedTransitRouterRequest
from volcenginesdktransitrouter.models.reject_shared_transit_router_response import RejectSharedTransitRouterResponse
from volcenginesdktransitrouter.models.renew_transit_router_bandwidth_package_request import RenewTransitRouterBandwidthPackageRequest
from volcenginesdktransitrouter.models.renew_transit_router_bandwidth_package_response import RenewTransitRouterBandwidthPackageResponse
from volcenginesdktransitrouter.models.resource_tag_for_list_tags_for_resources_output import ResourceTagForListTagsForResourcesOutput
from volcenginesdktransitrouter.models.set_transit_router_bandwidth_package_renewal_request import SetTransitRouterBandwidthPackageRenewalRequest
from volcenginesdktransitrouter.models.set_transit_router_bandwidth_package_renewal_response import SetTransitRouterBandwidthPackageRenewalResponse
from volcenginesdktransitrouter.models.tag_filter_for_describe_transit_router_attachments_input import TagFilterForDescribeTransitRouterAttachmentsInput
from volcenginesdktransitrouter.models.tag_filter_for_describe_transit_router_bandwidth_packages_input import TagFilterForDescribeTransitRouterBandwidthPackagesInput
from volcenginesdktransitrouter.models.tag_filter_for_describe_transit_router_direct_connect_gateway_attachments_input import TagFilterForDescribeTransitRouterDirectConnectGatewayAttachmentsInput
from volcenginesdktransitrouter.models.tag_filter_for_describe_transit_router_peer_attachments_input import TagFilterForDescribeTransitRouterPeerAttachmentsInput
from volcenginesdktransitrouter.models.tag_filter_for_describe_transit_router_route_tables_input import TagFilterForDescribeTransitRouterRouteTablesInput
from volcenginesdktransitrouter.models.tag_filter_for_describe_transit_router_vpc_attachments_input import TagFilterForDescribeTransitRouterVpcAttachmentsInput
from volcenginesdktransitrouter.models.tag_filter_for_describe_transit_router_vpn_attachments_input import TagFilterForDescribeTransitRouterVpnAttachmentsInput
from volcenginesdktransitrouter.models.tag_filter_for_describe_transit_routers_input import TagFilterForDescribeTransitRoutersInput
from volcenginesdktransitrouter.models.tag_filter_for_list_tags_for_resources_input import TagFilterForListTagsForResourcesInput
from volcenginesdktransitrouter.models.tag_for_create_transit_router_bandwidth_package_input import TagForCreateTransitRouterBandwidthPackageInput
from volcenginesdktransitrouter.models.tag_for_create_transit_router_direct_connect_gateway_attachment_input import TagForCreateTransitRouterDirectConnectGatewayAttachmentInput
from volcenginesdktransitrouter.models.tag_for_create_transit_router_input import TagForCreateTransitRouterInput
from volcenginesdktransitrouter.models.tag_for_create_transit_router_peer_attachment_input import TagForCreateTransitRouterPeerAttachmentInput
from volcenginesdktransitrouter.models.tag_for_create_transit_router_route_table_input import TagForCreateTransitRouterRouteTableInput
from volcenginesdktransitrouter.models.tag_for_create_transit_router_vpc_attachment_input import TagForCreateTransitRouterVpcAttachmentInput
from volcenginesdktransitrouter.models.tag_for_create_transit_router_vpn_attachment_input import TagForCreateTransitRouterVpnAttachmentInput
from volcenginesdktransitrouter.models.tag_for_describe_transit_router_attachments_output import TagForDescribeTransitRouterAttachmentsOutput
from volcenginesdktransitrouter.models.tag_for_describe_transit_router_bandwidth_packages_output import TagForDescribeTransitRouterBandwidthPackagesOutput
from volcenginesdktransitrouter.models.tag_for_describe_transit_router_direct_connect_gateway_attachments_output import TagForDescribeTransitRouterDirectConnectGatewayAttachmentsOutput
from volcenginesdktransitrouter.models.tag_for_describe_transit_router_peer_attachments_output import TagForDescribeTransitRouterPeerAttachmentsOutput
from volcenginesdktransitrouter.models.tag_for_describe_transit_router_route_tables_output import TagForDescribeTransitRouterRouteTablesOutput
from volcenginesdktransitrouter.models.tag_for_describe_transit_router_vpc_attachments_output import TagForDescribeTransitRouterVpcAttachmentsOutput
from volcenginesdktransitrouter.models.tag_for_describe_transit_router_vpn_attachments_output import TagForDescribeTransitRouterVpnAttachmentsOutput
from volcenginesdktransitrouter.models.tag_for_describe_transit_routers_output import TagForDescribeTransitRoutersOutput
from volcenginesdktransitrouter.models.tag_for_tag_resources_input import TagForTagResourcesInput
from volcenginesdktransitrouter.models.tag_resources_request import TagResourcesRequest
from volcenginesdktransitrouter.models.tag_resources_response import TagResourcesResponse
from volcenginesdktransitrouter.models.transit_router_attachment_for_describe_transit_router_attachments_output import TransitRouterAttachmentForDescribeTransitRouterAttachmentsOutput
from volcenginesdktransitrouter.models.transit_router_attachment_for_describe_transit_router_direct_connect_gateway_attachments_output import TransitRouterAttachmentForDescribeTransitRouterDirectConnectGatewayAttachmentsOutput
from volcenginesdktransitrouter.models.transit_router_attachment_for_describe_transit_router_peer_attachments_output import TransitRouterAttachmentForDescribeTransitRouterPeerAttachmentsOutput
from volcenginesdktransitrouter.models.transit_router_attachment_for_describe_transit_router_vpc_attachments_output import TransitRouterAttachmentForDescribeTransitRouterVpcAttachmentsOutput
from volcenginesdktransitrouter.models.transit_router_attachment_for_describe_transit_router_vpn_attachments_output import TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput
from volcenginesdktransitrouter.models.transit_router_bandwidth_package_for_describe_transit_router_bandwidth_packages_billing_output import TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput
from volcenginesdktransitrouter.models.transit_router_bandwidth_package_for_describe_transit_router_bandwidth_packages_output import TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesOutput
from volcenginesdktransitrouter.models.transit_router_for_describe_transit_routers_output import TransitRouterForDescribeTransitRoutersOutput
from volcenginesdktransitrouter.models.transit_router_forward_policy_entry_for_describe_transit_router_forward_policy_entries_output import TransitRouterForwardPolicyEntryForDescribeTransitRouterForwardPolicyEntriesOutput
from volcenginesdktransitrouter.models.transit_router_forward_policy_table_for_describe_transit_router_forward_policy_tables_output import TransitRouterForwardPolicyTableForDescribeTransitRouterForwardPolicyTablesOutput
from volcenginesdktransitrouter.models.transit_router_grant_rule_for_describe_transit_router_grant_rules_output import TransitRouterGrantRuleForDescribeTransitRouterGrantRulesOutput
from volcenginesdktransitrouter.models.transit_router_route_entry_for_describe_transit_router_route_entries_output import TransitRouterRouteEntryForDescribeTransitRouterRouteEntriesOutput
from volcenginesdktransitrouter.models.transit_router_route_policy_entry_for_describe_transit_router_route_policy_entries_output import TransitRouterRoutePolicyEntryForDescribeTransitRouterRoutePolicyEntriesOutput
from volcenginesdktransitrouter.models.transit_router_route_policy_table_for_describe_transit_router_route_policy_tables_output import TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput
from volcenginesdktransitrouter.models.transit_router_route_table_association_for_describe_transit_router_route_table_associations_output import TransitRouterRouteTableAssociationForDescribeTransitRouterRouteTableAssociationsOutput
from volcenginesdktransitrouter.models.transit_router_route_table_for_describe_transit_router_route_tables_output import TransitRouterRouteTableForDescribeTransitRouterRouteTablesOutput
from volcenginesdktransitrouter.models.transit_router_route_table_propagation_for_describe_transit_router_route_table_propagations_output import TransitRouterRouteTablePropagationForDescribeTransitRouterRouteTablePropagationsOutput
from volcenginesdktransitrouter.models.untag_resources_request import UntagResourcesRequest
from volcenginesdktransitrouter.models.untag_resources_response import UntagResourcesResponse
