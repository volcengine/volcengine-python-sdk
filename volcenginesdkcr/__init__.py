# coding: utf-8

# flake8: noqa

"""
    cr

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from volcenginesdkcr.api.cr_api import CRApi

# import models into sdk package
from volcenginesdkcr.models.acl_policy_for_get_public_endpoint_output import AclPolicyForGetPublicEndpointOutput
from volcenginesdkcr.models.chart_attribute_for_list_tags_output import ChartAttributeForListTagsOutput
from volcenginesdkcr.models.create_endpoint_acl_policies_request import CreateEndpointAclPoliciesRequest
from volcenginesdkcr.models.create_endpoint_acl_policies_response import CreateEndpointAclPoliciesResponse
from volcenginesdkcr.models.create_namespace_request import CreateNamespaceRequest
from volcenginesdkcr.models.create_namespace_response import CreateNamespaceResponse
from volcenginesdkcr.models.create_registry_request import CreateRegistryRequest
from volcenginesdkcr.models.create_registry_response import CreateRegistryResponse
from volcenginesdkcr.models.create_repository_request import CreateRepositoryRequest
from volcenginesdkcr.models.create_repository_response import CreateRepositoryResponse
from volcenginesdkcr.models.delete_endpoint_acl_policies_request import DeleteEndpointAclPoliciesRequest
from volcenginesdkcr.models.delete_endpoint_acl_policies_response import DeleteEndpointAclPoliciesResponse
from volcenginesdkcr.models.delete_namespace_request import DeleteNamespaceRequest
from volcenginesdkcr.models.delete_namespace_response import DeleteNamespaceResponse
from volcenginesdkcr.models.delete_registry_request import DeleteRegistryRequest
from volcenginesdkcr.models.delete_registry_response import DeleteRegistryResponse
from volcenginesdkcr.models.delete_repository_request import DeleteRepositoryRequest
from volcenginesdkcr.models.delete_repository_response import DeleteRepositoryResponse
from volcenginesdkcr.models.delete_tags_request import DeleteTagsRequest
from volcenginesdkcr.models.delete_tags_response import DeleteTagsResponse
from volcenginesdkcr.models.failure_for_delete_tags_output import FailureForDeleteTagsOutput
from volcenginesdkcr.models.filter_for_get_vpc_endpoint_input import FilterForGetVpcEndpointInput
from volcenginesdkcr.models.filter_for_list_namespaces_input import FilterForListNamespacesInput
from volcenginesdkcr.models.filter_for_list_registries_input import FilterForListRegistriesInput
from volcenginesdkcr.models.filter_for_list_repositories_input import FilterForListRepositoriesInput
from volcenginesdkcr.models.filter_for_list_tags_input import FilterForListTagsInput
from volcenginesdkcr.models.get_authorization_token_request import GetAuthorizationTokenRequest
from volcenginesdkcr.models.get_authorization_token_response import GetAuthorizationTokenResponse
from volcenginesdkcr.models.get_public_endpoint_request import GetPublicEndpointRequest
from volcenginesdkcr.models.get_public_endpoint_response import GetPublicEndpointResponse
from volcenginesdkcr.models.get_user_request import GetUserRequest
from volcenginesdkcr.models.get_user_response import GetUserResponse
from volcenginesdkcr.models.get_vpc_endpoint_request import GetVpcEndpointRequest
from volcenginesdkcr.models.get_vpc_endpoint_response import GetVpcEndpointResponse
from volcenginesdkcr.models.image_attribute_for_list_tags_output import ImageAttributeForListTagsOutput
from volcenginesdkcr.models.item_for_list_domains_output import ItemForListDomainsOutput
from volcenginesdkcr.models.item_for_list_namespaces_output import ItemForListNamespacesOutput
from volcenginesdkcr.models.item_for_list_registries_output import ItemForListRegistriesOutput
from volcenginesdkcr.models.item_for_list_repositories_output import ItemForListRepositoriesOutput
from volcenginesdkcr.models.item_for_list_tags_output import ItemForListTagsOutput
from volcenginesdkcr.models.list_domains_request import ListDomainsRequest
from volcenginesdkcr.models.list_domains_response import ListDomainsResponse
from volcenginesdkcr.models.list_namespaces_request import ListNamespacesRequest
from volcenginesdkcr.models.list_namespaces_response import ListNamespacesResponse
from volcenginesdkcr.models.list_registries_request import ListRegistriesRequest
from volcenginesdkcr.models.list_registries_response import ListRegistriesResponse
from volcenginesdkcr.models.list_repositories_request import ListRepositoriesRequest
from volcenginesdkcr.models.list_repositories_response import ListRepositoriesResponse
from volcenginesdkcr.models.list_tags_request import ListTagsRequest
from volcenginesdkcr.models.list_tags_response import ListTagsResponse
from volcenginesdkcr.models.proxy_cache_for_list_registries_output import ProxyCacheForListRegistriesOutput
from volcenginesdkcr.models.resource_tag_filter_for_list_registries_input import ResourceTagFilterForListRegistriesInput
from volcenginesdkcr.models.resource_tag_for_create_registry_input import ResourceTagForCreateRegistryInput
from volcenginesdkcr.models.resource_tag_for_list_registries_output import ResourceTagForListRegistriesOutput
from volcenginesdkcr.models.set_user_request import SetUserRequest
from volcenginesdkcr.models.set_user_response import SetUserResponse
from volcenginesdkcr.models.start_registry_request import StartRegistryRequest
from volcenginesdkcr.models.start_registry_response import StartRegistryResponse
from volcenginesdkcr.models.status_for_list_registries_input import StatusForListRegistriesInput
from volcenginesdkcr.models.status_for_list_registries_output import StatusForListRegistriesOutput
from volcenginesdkcr.models.success_for_delete_tags_output import SuccessForDeleteTagsOutput
from volcenginesdkcr.models.update_public_endpoint_request import UpdatePublicEndpointRequest
from volcenginesdkcr.models.update_public_endpoint_response import UpdatePublicEndpointResponse
from volcenginesdkcr.models.update_repository_request import UpdateRepositoryRequest
from volcenginesdkcr.models.update_repository_response import UpdateRepositoryResponse
from volcenginesdkcr.models.update_vpc_endpoint_request import UpdateVpcEndpointRequest
from volcenginesdkcr.models.update_vpc_endpoint_response import UpdateVpcEndpointResponse
from volcenginesdkcr.models.vpc_for_get_vpc_endpoint_output import VpcForGetVpcEndpointOutput
from volcenginesdkcr.models.vpc_for_update_vpc_endpoint_input import VpcForUpdateVpcEndpointInput
