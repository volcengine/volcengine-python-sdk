# coding: utf-8

# flake8: noqa

"""
    tag

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from volcenginesdktag.api.tag_api import TAGApi

# import models into sdk package
from volcenginesdktag.models.create_tags_request import CreateTagsRequest
from volcenginesdktag.models.create_tags_response import CreateTagsResponse
from volcenginesdktag.models.delete_tags_request import DeleteTagsRequest
from volcenginesdktag.models.delete_tags_response import DeleteTagsResponse
from volcenginesdktag.models.get_resources_request import GetResourcesRequest
from volcenginesdktag.models.get_resources_response import GetResourcesResponse
from volcenginesdktag.models.get_tag_keys_request import GetTagKeysRequest
from volcenginesdktag.models.get_tag_keys_response import GetTagKeysResponse
from volcenginesdktag.models.get_tag_values_request import GetTagValuesRequest
from volcenginesdktag.models.get_tag_values_response import GetTagValuesResponse
from volcenginesdktag.models.get_tags_request import GetTagsRequest
from volcenginesdktag.models.get_tags_response import GetTagsResponse
from volcenginesdktag.models.resource_tag_mapping_list_for_get_resources_output import ResourceTagMappingListForGetResourcesOutput
from volcenginesdktag.models.tag_filter_for_get_resources_input import TagFilterForGetResourcesInput
from volcenginesdktag.models.tag_for_create_tags_input import TagForCreateTagsInput
from volcenginesdktag.models.tag_for_delete_tags_input import TagForDeleteTagsInput
from volcenginesdktag.models.tag_for_get_resources_output import TagForGetResourcesOutput
from volcenginesdktag.models.tag_for_get_tag_values_output import TagForGetTagValuesOutput
from volcenginesdktag.models.tag_for_get_tags_output import TagForGetTagsOutput
from volcenginesdktag.models.tag_key_for_get_tag_keys_output import TagKeyForGetTagKeysOutput
