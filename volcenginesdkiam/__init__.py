# coding: utf-8

# flake8: noqa

"""
    iam

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from volcenginesdkiam.api.iam_api import IAMApi

# import models into sdk package
from volcenginesdkiam.models.access_key_for_create_access_key_output import AccessKeyForCreateAccessKeyOutput
from volcenginesdkiam.models.access_key_last_used_for_get_access_key_last_used_output import AccessKeyLastUsedForGetAccessKeyLastUsedOutput
from volcenginesdkiam.models.access_key_metadata_for_list_access_keys_output import AccessKeyMetadataForListAccessKeysOutput
from volcenginesdkiam.models.add_client_id_to_oidc_provider_request import AddClientIDToOIDCProviderRequest
from volcenginesdkiam.models.add_client_id_to_oidc_provider_response import AddClientIDToOIDCProviderResponse
from volcenginesdkiam.models.add_thumbprint_to_oidc_provider_request import AddThumbprintToOIDCProviderRequest
from volcenginesdkiam.models.add_thumbprint_to_oidc_provider_response import AddThumbprintToOIDCProviderResponse
from volcenginesdkiam.models.add_user_to_group_request import AddUserToGroupRequest
from volcenginesdkiam.models.add_user_to_group_response import AddUserToGroupResponse
from volcenginesdkiam.models.attach_role_policy_request import AttachRolePolicyRequest
from volcenginesdkiam.models.attach_role_policy_response import AttachRolePolicyResponse
from volcenginesdkiam.models.attach_user_group_policy_request import AttachUserGroupPolicyRequest
from volcenginesdkiam.models.attach_user_group_policy_response import AttachUserGroupPolicyResponse
from volcenginesdkiam.models.attach_user_policy_request import AttachUserPolicyRequest
from volcenginesdkiam.models.attach_user_policy_response import AttachUserPolicyResponse
from volcenginesdkiam.models.attached_policy_metadata_for_list_attached_role_policies_output import AttachedPolicyMetadataForListAttachedRolePoliciesOutput
from volcenginesdkiam.models.attached_policy_metadata_for_list_attached_user_group_policies_output import AttachedPolicyMetadataForListAttachedUserGroupPoliciesOutput
from volcenginesdkiam.models.attached_policy_metadata_for_list_attached_user_policies_output import AttachedPolicyMetadataForListAttachedUserPoliciesOutput
from volcenginesdkiam.models.certificate_for_list_saml_provider_certificates_output import CertificateForListSAMLProviderCertificatesOutput
from volcenginesdkiam.models.create_access_key_request import CreateAccessKeyRequest
from volcenginesdkiam.models.create_access_key_response import CreateAccessKeyResponse
from volcenginesdkiam.models.create_group_request import CreateGroupRequest
from volcenginesdkiam.models.create_group_response import CreateGroupResponse
from volcenginesdkiam.models.create_login_profile_request import CreateLoginProfileRequest
from volcenginesdkiam.models.create_login_profile_response import CreateLoginProfileResponse
from volcenginesdkiam.models.create_o_auth_provider_request import CreateOAuthProviderRequest
from volcenginesdkiam.models.create_o_auth_provider_response import CreateOAuthProviderResponse
from volcenginesdkiam.models.create_oidc_provider_request import CreateOIDCProviderRequest
from volcenginesdkiam.models.create_oidc_provider_response import CreateOIDCProviderResponse
from volcenginesdkiam.models.create_policy_request import CreatePolicyRequest
from volcenginesdkiam.models.create_policy_response import CreatePolicyResponse
from volcenginesdkiam.models.create_role_request import CreateRoleRequest
from volcenginesdkiam.models.create_role_response import CreateRoleResponse
from volcenginesdkiam.models.create_service_linked_role_request import CreateServiceLinkedRoleRequest
from volcenginesdkiam.models.create_service_linked_role_response import CreateServiceLinkedRoleResponse
from volcenginesdkiam.models.create_user_request import CreateUserRequest
from volcenginesdkiam.models.create_user_response import CreateUserResponse
from volcenginesdkiam.models.delete_access_key_request import DeleteAccessKeyRequest
from volcenginesdkiam.models.delete_access_key_response import DeleteAccessKeyResponse
from volcenginesdkiam.models.delete_group_request import DeleteGroupRequest
from volcenginesdkiam.models.delete_group_response import DeleteGroupResponse
from volcenginesdkiam.models.delete_login_profile_request import DeleteLoginProfileRequest
from volcenginesdkiam.models.delete_login_profile_response import DeleteLoginProfileResponse
from volcenginesdkiam.models.delete_o_auth_provider_request import DeleteOAuthProviderRequest
from volcenginesdkiam.models.delete_o_auth_provider_response import DeleteOAuthProviderResponse
from volcenginesdkiam.models.delete_oidc_provider_request import DeleteOIDCProviderRequest
from volcenginesdkiam.models.delete_oidc_provider_response import DeleteOIDCProviderResponse
from volcenginesdkiam.models.delete_policy_request import DeletePolicyRequest
from volcenginesdkiam.models.delete_policy_response import DeletePolicyResponse
from volcenginesdkiam.models.delete_role_request import DeleteRoleRequest
from volcenginesdkiam.models.delete_role_response import DeleteRoleResponse
from volcenginesdkiam.models.delete_saml_provider_request import DeleteSAMLProviderRequest
from volcenginesdkiam.models.delete_saml_provider_response import DeleteSAMLProviderResponse
from volcenginesdkiam.models.delete_service_linked_role_request import DeleteServiceLinkedRoleRequest
from volcenginesdkiam.models.delete_service_linked_role_response import DeleteServiceLinkedRoleResponse
from volcenginesdkiam.models.delete_user_request import DeleteUserRequest
from volcenginesdkiam.models.delete_user_response import DeleteUserResponse
from volcenginesdkiam.models.detach_role_policy_request import DetachRolePolicyRequest
from volcenginesdkiam.models.detach_role_policy_response import DetachRolePolicyResponse
from volcenginesdkiam.models.detach_user_group_policy_request import DetachUserGroupPolicyRequest
from volcenginesdkiam.models.detach_user_group_policy_response import DetachUserGroupPolicyResponse
from volcenginesdkiam.models.detach_user_policy_request import DetachUserPolicyRequest
from volcenginesdkiam.models.detach_user_policy_response import DetachUserPolicyResponse
from volcenginesdkiam.models.get_access_key_last_used_request import GetAccessKeyLastUsedRequest
from volcenginesdkiam.models.get_access_key_last_used_response import GetAccessKeyLastUsedResponse
from volcenginesdkiam.models.get_group_request import GetGroupRequest
from volcenginesdkiam.models.get_group_response import GetGroupResponse
from volcenginesdkiam.models.get_login_profile_request import GetLoginProfileRequest
from volcenginesdkiam.models.get_login_profile_response import GetLoginProfileResponse
from volcenginesdkiam.models.get_o_auth_provider_request import GetOAuthProviderRequest
from volcenginesdkiam.models.get_o_auth_provider_response import GetOAuthProviderResponse
from volcenginesdkiam.models.get_oidc_provider_request import GetOIDCProviderRequest
from volcenginesdkiam.models.get_oidc_provider_response import GetOIDCProviderResponse
from volcenginesdkiam.models.get_policy_request import GetPolicyRequest
from volcenginesdkiam.models.get_policy_response import GetPolicyResponse
from volcenginesdkiam.models.get_role_request import GetRoleRequest
from volcenginesdkiam.models.get_role_response import GetRoleResponse
from volcenginesdkiam.models.get_saml_provider_request import GetSAMLProviderRequest
from volcenginesdkiam.models.get_saml_provider_response import GetSAMLProviderResponse
from volcenginesdkiam.models.get_security_config_request import GetSecurityConfigRequest
from volcenginesdkiam.models.get_security_config_response import GetSecurityConfigResponse
from volcenginesdkiam.models.get_user_request import GetUserRequest
from volcenginesdkiam.models.get_user_response import GetUserResponse
from volcenginesdkiam.models.identity_provider_for_list_identity_providers_output import IdentityProviderForListIdentityProvidersOutput
from volcenginesdkiam.models.list_access_keys_request import ListAccessKeysRequest
from volcenginesdkiam.models.list_access_keys_response import ListAccessKeysResponse
from volcenginesdkiam.models.list_attached_role_policies_request import ListAttachedRolePoliciesRequest
from volcenginesdkiam.models.list_attached_role_policies_response import ListAttachedRolePoliciesResponse
from volcenginesdkiam.models.list_attached_user_group_policies_request import ListAttachedUserGroupPoliciesRequest
from volcenginesdkiam.models.list_attached_user_group_policies_response import ListAttachedUserGroupPoliciesResponse
from volcenginesdkiam.models.list_attached_user_policies_request import ListAttachedUserPoliciesRequest
from volcenginesdkiam.models.list_attached_user_policies_response import ListAttachedUserPoliciesResponse
from volcenginesdkiam.models.list_entities_for_policy_request import ListEntitiesForPolicyRequest
from volcenginesdkiam.models.list_entities_for_policy_response import ListEntitiesForPolicyResponse
from volcenginesdkiam.models.list_groups_for_user_request import ListGroupsForUserRequest
from volcenginesdkiam.models.list_groups_for_user_response import ListGroupsForUserResponse
from volcenginesdkiam.models.list_groups_request import ListGroupsRequest
from volcenginesdkiam.models.list_groups_response import ListGroupsResponse
from volcenginesdkiam.models.list_identity_providers_request import ListIdentityProvidersRequest
from volcenginesdkiam.models.list_identity_providers_response import ListIdentityProvidersResponse
from volcenginesdkiam.models.list_oidc_providers_request import ListOIDCProvidersRequest
from volcenginesdkiam.models.list_oidc_providers_response import ListOIDCProvidersResponse
from volcenginesdkiam.models.list_policies_request import ListPoliciesRequest
from volcenginesdkiam.models.list_policies_response import ListPoliciesResponse
from volcenginesdkiam.models.list_roles_request import ListRolesRequest
from volcenginesdkiam.models.list_roles_response import ListRolesResponse
from volcenginesdkiam.models.list_saml_provider_certificates_request import ListSAMLProviderCertificatesRequest
from volcenginesdkiam.models.list_saml_provider_certificates_response import ListSAMLProviderCertificatesResponse
from volcenginesdkiam.models.list_saml_providers_request import ListSAMLProvidersRequest
from volcenginesdkiam.models.list_saml_providers_response import ListSAMLProvidersResponse
from volcenginesdkiam.models.list_tags_for_resources_request import ListTagsForResourcesRequest
from volcenginesdkiam.models.list_tags_for_resources_response import ListTagsForResourcesResponse
from volcenginesdkiam.models.list_users_for_group_request import ListUsersForGroupRequest
from volcenginesdkiam.models.list_users_for_group_response import ListUsersForGroupResponse
from volcenginesdkiam.models.list_users_request import ListUsersRequest
from volcenginesdkiam.models.list_users_response import ListUsersResponse
from volcenginesdkiam.models.login_profile_for_create_login_profile_output import LoginProfileForCreateLoginProfileOutput
from volcenginesdkiam.models.login_profile_for_get_login_profile_output import LoginProfileForGetLoginProfileOutput
from volcenginesdkiam.models.login_profile_for_update_login_profile_output import LoginProfileForUpdateLoginProfileOutput
from volcenginesdkiam.models.oidc_provider_for_list_oidc_providers_output import OIDCProviderForListOIDCProvidersOutput
from volcenginesdkiam.models.policy_for_create_policy_output import PolicyForCreatePolicyOutput
from volcenginesdkiam.models.policy_for_get_policy_output import PolicyForGetPolicyOutput
from volcenginesdkiam.models.policy_for_update_policy_output import PolicyForUpdatePolicyOutput
from volcenginesdkiam.models.policy_metadata_for_list_policies_output import PolicyMetadataForListPoliciesOutput
from volcenginesdkiam.models.policy_role_for_list_entities_for_policy_output import PolicyRoleForListEntitiesForPolicyOutput
from volcenginesdkiam.models.policy_scope_for_list_attached_role_policies_output import PolicyScopeForListAttachedRolePoliciesOutput
from volcenginesdkiam.models.policy_scope_for_list_attached_user_group_policies_output import PolicyScopeForListAttachedUserGroupPoliciesOutput
from volcenginesdkiam.models.policy_scope_for_list_attached_user_policies_output import PolicyScopeForListAttachedUserPoliciesOutput
from volcenginesdkiam.models.policy_scope_for_list_entities_for_policy_output import PolicyScopeForListEntitiesForPolicyOutput
from volcenginesdkiam.models.policy_user_for_list_entities_for_policy_output import PolicyUserForListEntitiesForPolicyOutput
from volcenginesdkiam.models.policy_user_group_for_list_entities_for_policy_output import PolicyUserGroupForListEntitiesForPolicyOutput
from volcenginesdkiam.models.remove_client_id_from_oidc_provider_request import RemoveClientIDFromOIDCProviderRequest
from volcenginesdkiam.models.remove_client_id_from_oidc_provider_response import RemoveClientIDFromOIDCProviderResponse
from volcenginesdkiam.models.remove_saml_provider_certificate_request import RemoveSAMLProviderCertificateRequest
from volcenginesdkiam.models.remove_saml_provider_certificate_response import RemoveSAMLProviderCertificateResponse
from volcenginesdkiam.models.remove_thumbprint_from_oidc_provider_request import RemoveThumbprintFromOIDCProviderRequest
from volcenginesdkiam.models.remove_thumbprint_from_oidc_provider_response import RemoveThumbprintFromOIDCProviderResponse
from volcenginesdkiam.models.remove_user_from_group_request import RemoveUserFromGroupRequest
from volcenginesdkiam.models.remove_user_from_group_response import RemoveUserFromGroupResponse
from volcenginesdkiam.models.resource_tag_for_list_tags_for_resources_output import ResourceTagForListTagsForResourcesOutput
from volcenginesdkiam.models.role_for_create_role_output import RoleForCreateRoleOutput
from volcenginesdkiam.models.role_for_get_role_output import RoleForGetRoleOutput
from volcenginesdkiam.models.role_metadata_for_list_roles_output import RoleMetadataForListRolesOutput
from volcenginesdkiam.models.saml_provider_for_list_saml_providers_output import SAMLProviderForListSAMLProvidersOutput
from volcenginesdkiam.models.set_security_config_request import SetSecurityConfigRequest
from volcenginesdkiam.models.set_security_config_response import SetSecurityConfigResponse
from volcenginesdkiam.models.tag_filter_for_list_tags_for_resources_input import TagFilterForListTagsForResourcesInput
from volcenginesdkiam.models.tag_for_create_role_input import TagForCreateRoleInput
from volcenginesdkiam.models.tag_for_create_role_output import TagForCreateRoleOutput
from volcenginesdkiam.models.tag_for_create_service_linked_role_input import TagForCreateServiceLinkedRoleInput
from volcenginesdkiam.models.tag_for_create_user_input import TagForCreateUserInput
from volcenginesdkiam.models.tag_for_create_user_output import TagForCreateUserOutput
from volcenginesdkiam.models.tag_for_get_role_output import TagForGetRoleOutput
from volcenginesdkiam.models.tag_for_get_user_output import TagForGetUserOutput
from volcenginesdkiam.models.tag_for_list_roles_output import TagForListRolesOutput
from volcenginesdkiam.models.tag_for_list_users_output import TagForListUsersOutput
from volcenginesdkiam.models.tag_for_tag_resources_input import TagForTagResourcesInput
from volcenginesdkiam.models.tag_for_update_user_output import TagForUpdateUserOutput
from volcenginesdkiam.models.tag_resources_request import TagResourcesRequest
from volcenginesdkiam.models.tag_resources_response import TagResourcesResponse
from volcenginesdkiam.models.untag_resources_request import UntagResourcesRequest
from volcenginesdkiam.models.untag_resources_response import UntagResourcesResponse
from volcenginesdkiam.models.update_access_key_request import UpdateAccessKeyRequest
from volcenginesdkiam.models.update_access_key_response import UpdateAccessKeyResponse
from volcenginesdkiam.models.update_group_request import UpdateGroupRequest
from volcenginesdkiam.models.update_group_response import UpdateGroupResponse
from volcenginesdkiam.models.update_login_profile_request import UpdateLoginProfileRequest
from volcenginesdkiam.models.update_login_profile_response import UpdateLoginProfileResponse
from volcenginesdkiam.models.update_oidc_provider_request import UpdateOIDCProviderRequest
from volcenginesdkiam.models.update_oidc_provider_response import UpdateOIDCProviderResponse
from volcenginesdkiam.models.update_policy_request import UpdatePolicyRequest
from volcenginesdkiam.models.update_policy_response import UpdatePolicyResponse
from volcenginesdkiam.models.update_role_request import UpdateRoleRequest
from volcenginesdkiam.models.update_role_response import UpdateRoleResponse
from volcenginesdkiam.models.update_user_request import UpdateUserRequest
from volcenginesdkiam.models.update_user_response import UpdateUserResponse
from volcenginesdkiam.models.user_for_create_user_output import UserForCreateUserOutput
from volcenginesdkiam.models.user_for_get_user_output import UserForGetUserOutput
from volcenginesdkiam.models.user_for_list_users_for_group_output import UserForListUsersForGroupOutput
from volcenginesdkiam.models.user_for_update_user_output import UserForUpdateUserOutput
from volcenginesdkiam.models.user_group_for_create_group_output import UserGroupForCreateGroupOutput
from volcenginesdkiam.models.user_group_for_get_group_output import UserGroupForGetGroupOutput
from volcenginesdkiam.models.user_group_for_list_groups_for_user_output import UserGroupForListGroupsForUserOutput
from volcenginesdkiam.models.user_group_for_list_groups_output import UserGroupForListGroupsOutput
from volcenginesdkiam.models.user_metadata_for_list_users_output import UserMetadataForListUsersOutput
from volcenginesdkiam.models.add_saml_provider_certificate_request import AddSAMLProviderCertificateRequest
from volcenginesdkiam.models.add_saml_provider_certificate_response import AddSAMLProviderCertificateResponse
from volcenginesdkiam.models.create_saml_provider_request import CreateSAMLProviderRequest
from volcenginesdkiam.models.create_saml_provider_response import CreateSAMLProviderResponse
from volcenginesdkiam.models.update_o_auth_provider_request import UpdateOAuthProviderRequest
from volcenginesdkiam.models.update_o_auth_provider_response import UpdateOAuthProviderResponse
from volcenginesdkiam.models.update_saml_provider_request import UpdateSAMLProviderRequest
from volcenginesdkiam.models.update_saml_provider_response import UpdateSAMLProviderResponse