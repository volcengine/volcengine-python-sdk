# coding: utf-8

# flake8: noqa
"""
    volc_observe

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from volcenginesdkvolcobserve.models.alert_notification_for_list_preset_alert_templates_output import AlertNotificationForListPresetAlertTemplatesOutput
from volcenginesdkvolcobserve.models.applied_rule_for_list_alert_templates_output import AppliedRuleForListAlertTemplatesOutput
from volcenginesdkvolcobserve.models.applied_rule_for_list_preset_alert_templates_output import AppliedRuleForListPresetAlertTemplatesOutput
from volcenginesdkvolcobserve.models.apply_object_for_apply_object_groups_by_alert_template_input import ApplyObjectForApplyObjectGroupsByAlertTemplateInput
from volcenginesdkvolcobserve.models.apply_object_groups_by_alert_template_request import ApplyObjectGroupsByAlertTemplateRequest
from volcenginesdkvolcobserve.models.apply_object_groups_by_alert_template_response import ApplyObjectGroupsByAlertTemplateResponse
from volcenginesdkvolcobserve.models.condition_for_create_alert_template_input import ConditionForCreateAlertTemplateInput
from volcenginesdkvolcobserve.models.condition_for_create_rule_input import ConditionForCreateRuleInput
from volcenginesdkvolcobserve.models.condition_for_list_alert_templates_output import ConditionForListAlertTemplatesOutput
from volcenginesdkvolcobserve.models.condition_for_list_preset_alert_templates_output import ConditionForListPresetAlertTemplatesOutput
from volcenginesdkvolcobserve.models.condition_for_list_rules_by_ids_output import ConditionForListRulesByIdsOutput
from volcenginesdkvolcobserve.models.condition_for_list_rules_output import ConditionForListRulesOutput
from volcenginesdkvolcobserve.models.condition_for_update_alert_template_input import ConditionForUpdateAlertTemplateInput
from volcenginesdkvolcobserve.models.condition_for_update_rule_input import ConditionForUpdateRuleInput
from volcenginesdkvolcobserve.models.convert_tag_for_create_rule_input import ConvertTagForCreateRuleInput
from volcenginesdkvolcobserve.models.convert_tag_for_list_rules_by_ids_output import ConvertTagForListRulesByIdsOutput
from volcenginesdkvolcobserve.models.convert_tag_for_list_rules_output import ConvertTagForListRulesOutput
from volcenginesdkvolcobserve.models.convert_tag_for_update_rule_input import ConvertTagForUpdateRuleInput
from volcenginesdkvolcobserve.models.create_alert_template_request import CreateAlertTemplateRequest
from volcenginesdkvolcobserve.models.create_alert_template_response import CreateAlertTemplateResponse
from volcenginesdkvolcobserve.models.create_contact_group_request import CreateContactGroupRequest
from volcenginesdkvolcobserve.models.create_contact_group_response import CreateContactGroupResponse
from volcenginesdkvolcobserve.models.create_contacts_request import CreateContactsRequest
from volcenginesdkvolcobserve.models.create_contacts_response import CreateContactsResponse
from volcenginesdkvolcobserve.models.create_event_rule_request import CreateEventRuleRequest
from volcenginesdkvolcobserve.models.create_event_rule_response import CreateEventRuleResponse
from volcenginesdkvolcobserve.models.create_notification_request import CreateNotificationRequest
from volcenginesdkvolcobserve.models.create_notification_response import CreateNotificationResponse
from volcenginesdkvolcobserve.models.create_object_group_request import CreateObjectGroupRequest
from volcenginesdkvolcobserve.models.create_object_group_response import CreateObjectGroupResponse
from volcenginesdkvolcobserve.models.create_rule_request import CreateRuleRequest
from volcenginesdkvolcobserve.models.create_rule_response import CreateRuleResponse
from volcenginesdkvolcobserve.models.create_silence_policy_request import CreateSilencePolicyRequest
from volcenginesdkvolcobserve.models.create_silence_policy_response import CreateSilencePolicyResponse
from volcenginesdkvolcobserve.models.create_webhook_request import CreateWebhookRequest
from volcenginesdkvolcobserve.models.create_webhook_response import CreateWebhookResponse
from volcenginesdkvolcobserve.models.data_for_create_event_rule_output import DataForCreateEventRuleOutput
from volcenginesdkvolcobserve.models.data_for_delete_event_rule_output import DataForDeleteEventRuleOutput
from volcenginesdkvolcobserve.models.data_for_disable_event_rule_output import DataForDisableEventRuleOutput
from volcenginesdkvolcobserve.models.data_for_enable_event_rule_output import DataForEnableEventRuleOutput
from volcenginesdkvolcobserve.models.data_for_get_metric_data_output import DataForGetMetricDataOutput
from volcenginesdkvolcobserve.models.data_for_get_top_data_output import DataForGetTopDataOutput
from volcenginesdkvolcobserve.models.data_for_list_alert_group_output import DataForListAlertGroupOutput
from volcenginesdkvolcobserve.models.data_for_list_alert_templates_output import DataForListAlertTemplatesOutput
from volcenginesdkvolcobserve.models.data_for_list_contact_group_by_ids_output import DataForListContactGroupByIdsOutput
from volcenginesdkvolcobserve.models.data_for_list_contact_groups_output import DataForListContactGroupsOutput
from volcenginesdkvolcobserve.models.data_for_list_contacts_by_ids_output import DataForListContactsByIdsOutput
from volcenginesdkvolcobserve.models.data_for_list_contacts_output import DataForListContactsOutput
from volcenginesdkvolcobserve.models.data_for_list_event_rules_output import DataForListEventRulesOutput
from volcenginesdkvolcobserve.models.data_for_list_events_output import DataForListEventsOutput
from volcenginesdkvolcobserve.models.data_for_list_notifications_output import DataForListNotificationsOutput
from volcenginesdkvolcobserve.models.data_for_list_object_groups_output import DataForListObjectGroupsOutput
from volcenginesdkvolcobserve.models.data_for_list_preset_alert_templates_output import DataForListPresetAlertTemplatesOutput
from volcenginesdkvolcobserve.models.data_for_list_rules_by_ids_output import DataForListRulesByIdsOutput
from volcenginesdkvolcobserve.models.data_for_list_rules_output import DataForListRulesOutput
from volcenginesdkvolcobserve.models.data_for_list_send_alert_output import DataForListSendAlertOutput
from volcenginesdkvolcobserve.models.data_for_list_silence_policy_output import DataForListSilencePolicyOutput
from volcenginesdkvolcobserve.models.data_for_list_webhooks_by_ids_output import DataForListWebhooksByIdsOutput
from volcenginesdkvolcobserve.models.data_for_list_webhooks_output import DataForListWebhooksOutput
from volcenginesdkvolcobserve.models.data_for_tag_resources_output import DataForTagResourcesOutput
from volcenginesdkvolcobserve.models.data_for_update_event_rule_output import DataForUpdateEventRuleOutput
from volcenginesdkvolcobserve.models.data_point_for_get_metric_data_output import DataPointForGetMetricDataOutput
from volcenginesdkvolcobserve.models.delete_alert_templates_by_ids_request import DeleteAlertTemplatesByIdsRequest
from volcenginesdkvolcobserve.models.delete_alert_templates_by_ids_response import DeleteAlertTemplatesByIdsResponse
from volcenginesdkvolcobserve.models.delete_contact_group_by_ids_request import DeleteContactGroupByIdsRequest
from volcenginesdkvolcobserve.models.delete_contact_group_by_ids_response import DeleteContactGroupByIdsResponse
from volcenginesdkvolcobserve.models.delete_contacts_by_ids_request import DeleteContactsByIdsRequest
from volcenginesdkvolcobserve.models.delete_contacts_by_ids_response import DeleteContactsByIdsResponse
from volcenginesdkvolcobserve.models.delete_event_rule_request import DeleteEventRuleRequest
from volcenginesdkvolcobserve.models.delete_event_rule_response import DeleteEventRuleResponse
from volcenginesdkvolcobserve.models.delete_notifications_by_ids_request import DeleteNotificationsByIdsRequest
from volcenginesdkvolcobserve.models.delete_notifications_by_ids_response import DeleteNotificationsByIdsResponse
from volcenginesdkvolcobserve.models.delete_object_group_request import DeleteObjectGroupRequest
from volcenginesdkvolcobserve.models.delete_object_group_response import DeleteObjectGroupResponse
from volcenginesdkvolcobserve.models.delete_rules_by_ids_request import DeleteRulesByIdsRequest
from volcenginesdkvolcobserve.models.delete_rules_by_ids_response import DeleteRulesByIdsResponse
from volcenginesdkvolcobserve.models.delete_silence_policy_by_ids_request import DeleteSilencePolicyByIdsRequest
from volcenginesdkvolcobserve.models.delete_silence_policy_by_ids_response import DeleteSilencePolicyByIdsResponse
from volcenginesdkvolcobserve.models.delete_webhooks_by_ids_request import DeleteWebhooksByIdsRequest
from volcenginesdkvolcobserve.models.delete_webhooks_by_ids_response import DeleteWebhooksByIdsResponse
from volcenginesdkvolcobserve.models.dimension_conditions_for_create_object_group_input import DimensionConditionsForCreateObjectGroupInput
from volcenginesdkvolcobserve.models.dimension_conditions_for_create_rule_input import DimensionConditionsForCreateRuleInput
from volcenginesdkvolcobserve.models.dimension_conditions_for_list_rules_by_ids_output import DimensionConditionsForListRulesByIdsOutput
from volcenginesdkvolcobserve.models.dimension_conditions_for_list_rules_output import DimensionConditionsForListRulesOutput
from volcenginesdkvolcobserve.models.dimension_conditions_for_update_object_group_input import DimensionConditionsForUpdateObjectGroupInput
from volcenginesdkvolcobserve.models.dimension_conditions_for_update_rule_input import DimensionConditionsForUpdateRuleInput
from volcenginesdkvolcobserve.models.dimension_for_get_metric_data_input import DimensionForGetMetricDataInput
from volcenginesdkvolcobserve.models.dimension_for_get_metric_data_output import DimensionForGetMetricDataOutput
from volcenginesdkvolcobserve.models.dimension_for_get_top_data_input import DimensionForGetTopDataInput
from volcenginesdkvolcobserve.models.disable_event_rule_request import DisableEventRuleRequest
from volcenginesdkvolcobserve.models.disable_event_rule_response import DisableEventRuleResponse
from volcenginesdkvolcobserve.models.disable_preset_alert_template_request import DisablePresetAlertTemplateRequest
from volcenginesdkvolcobserve.models.disable_preset_alert_template_response import DisablePresetAlertTemplateResponse
from volcenginesdkvolcobserve.models.effect_time_for_create_silence_policy_input import EffectTimeForCreateSilencePolicyInput
from volcenginesdkvolcobserve.models.effect_time_for_list_silence_policy_output import EffectTimeForListSilencePolicyOutput
from volcenginesdkvolcobserve.models.effect_time_for_update_silence_policy_input import EffectTimeForUpdateSilencePolicyInput
from volcenginesdkvolcobserve.models.effective_time_for_create_event_rule_input import EffectiveTimeForCreateEventRuleInput
from volcenginesdkvolcobserve.models.effective_time_for_update_event_rule_input import EffectiveTimeForUpdateEventRuleInput
from volcenginesdkvolcobserve.models.enable_event_rule_request import EnableEventRuleRequest
from volcenginesdkvolcobserve.models.enable_event_rule_response import EnableEventRuleResponse
from volcenginesdkvolcobserve.models.enable_preset_alert_template_request import EnablePresetAlertTemplateRequest
from volcenginesdkvolcobserve.models.enable_preset_alert_template_response import EnablePresetAlertTemplateResponse
from volcenginesdkvolcobserve.models.get_metric_data_request import GetMetricDataRequest
from volcenginesdkvolcobserve.models.get_metric_data_response import GetMetricDataResponse
from volcenginesdkvolcobserve.models.get_top_data_request import GetTopDataRequest
from volcenginesdkvolcobserve.models.get_top_data_response import GetTopDataResponse
from volcenginesdkvolcobserve.models.instance_for_get_metric_data_input import InstanceForGetMetricDataInput
from volcenginesdkvolcobserve.models.instance_for_get_top_data_input import InstanceForGetTopDataInput
from volcenginesdkvolcobserve.models.level_condition_for_create_alert_template_input import LevelConditionForCreateAlertTemplateInput
from volcenginesdkvolcobserve.models.level_condition_for_create_rule_input import LevelConditionForCreateRuleInput
from volcenginesdkvolcobserve.models.level_condition_for_list_alert_templates_output import LevelConditionForListAlertTemplatesOutput
from volcenginesdkvolcobserve.models.level_condition_for_list_preset_alert_templates_output import LevelConditionForListPresetAlertTemplatesOutput
from volcenginesdkvolcobserve.models.level_condition_for_list_rules_by_ids_output import LevelConditionForListRulesByIdsOutput
from volcenginesdkvolcobserve.models.level_condition_for_list_rules_output import LevelConditionForListRulesOutput
from volcenginesdkvolcobserve.models.level_condition_for_update_alert_template_input import LevelConditionForUpdateAlertTemplateInput
from volcenginesdkvolcobserve.models.level_condition_for_update_rule_input import LevelConditionForUpdateRuleInput
from volcenginesdkvolcobserve.models.list_alert_group_request import ListAlertGroupRequest
from volcenginesdkvolcobserve.models.list_alert_group_response import ListAlertGroupResponse
from volcenginesdkvolcobserve.models.list_alert_templates_request import ListAlertTemplatesRequest
from volcenginesdkvolcobserve.models.list_alert_templates_response import ListAlertTemplatesResponse
from volcenginesdkvolcobserve.models.list_contact_group_by_ids_request import ListContactGroupByIdsRequest
from volcenginesdkvolcobserve.models.list_contact_group_by_ids_response import ListContactGroupByIdsResponse
from volcenginesdkvolcobserve.models.list_contact_groups_request import ListContactGroupsRequest
from volcenginesdkvolcobserve.models.list_contact_groups_response import ListContactGroupsResponse
from volcenginesdkvolcobserve.models.list_contacts_by_ids_request import ListContactsByIdsRequest
from volcenginesdkvolcobserve.models.list_contacts_by_ids_response import ListContactsByIdsResponse
from volcenginesdkvolcobserve.models.list_contacts_request import ListContactsRequest
from volcenginesdkvolcobserve.models.list_contacts_response import ListContactsResponse
from volcenginesdkvolcobserve.models.list_event_rules_request import ListEventRulesRequest
from volcenginesdkvolcobserve.models.list_event_rules_response import ListEventRulesResponse
from volcenginesdkvolcobserve.models.list_events_request import ListEventsRequest
from volcenginesdkvolcobserve.models.list_events_response import ListEventsResponse
from volcenginesdkvolcobserve.models.list_notifications_request import ListNotificationsRequest
from volcenginesdkvolcobserve.models.list_notifications_response import ListNotificationsResponse
from volcenginesdkvolcobserve.models.list_object_groups_request import ListObjectGroupsRequest
from volcenginesdkvolcobserve.models.list_object_groups_response import ListObjectGroupsResponse
from volcenginesdkvolcobserve.models.list_preset_alert_templates_request import ListPresetAlertTemplatesRequest
from volcenginesdkvolcobserve.models.list_preset_alert_templates_response import ListPresetAlertTemplatesResponse
from volcenginesdkvolcobserve.models.list_rules_by_ids_request import ListRulesByIdsRequest
from volcenginesdkvolcobserve.models.list_rules_by_ids_response import ListRulesByIdsResponse
from volcenginesdkvolcobserve.models.list_rules_request import ListRulesRequest
from volcenginesdkvolcobserve.models.list_rules_response import ListRulesResponse
from volcenginesdkvolcobserve.models.list_send_alert_request import ListSendAlertRequest
from volcenginesdkvolcobserve.models.list_send_alert_response import ListSendAlertResponse
from volcenginesdkvolcobserve.models.list_silence_policy_request import ListSilencePolicyRequest
from volcenginesdkvolcobserve.models.list_silence_policy_response import ListSilencePolicyResponse
from volcenginesdkvolcobserve.models.list_webhooks_by_ids_request import ListWebhooksByIdsRequest
from volcenginesdkvolcobserve.models.list_webhooks_by_ids_response import ListWebhooksByIdsResponse
from volcenginesdkvolcobserve.models.list_webhooks_request import ListWebhooksRequest
from volcenginesdkvolcobserve.models.list_webhooks_response import ListWebhooksResponse
from volcenginesdkvolcobserve.models.message_queue_for_create_event_rule_input import MessageQueueForCreateEventRuleInput
from volcenginesdkvolcobserve.models.message_queue_for_list_event_rules_output import MessageQueueForListEventRulesOutput
from volcenginesdkvolcobserve.models.message_queue_for_update_event_rule_input import MessageQueueForUpdateEventRuleInput
from volcenginesdkvolcobserve.models.meta_condition_for_create_object_group_input import MetaConditionForCreateObjectGroupInput
from volcenginesdkvolcobserve.models.meta_condition_for_create_rule_input import MetaConditionForCreateRuleInput
from volcenginesdkvolcobserve.models.meta_condition_for_create_silence_policy_input import MetaConditionForCreateSilencePolicyInput
from volcenginesdkvolcobserve.models.meta_condition_for_list_rules_by_ids_output import MetaConditionForListRulesByIdsOutput
from volcenginesdkvolcobserve.models.meta_condition_for_list_rules_output import MetaConditionForListRulesOutput
from volcenginesdkvolcobserve.models.meta_condition_for_list_silence_policy_output import MetaConditionForListSilencePolicyOutput
from volcenginesdkvolcobserve.models.meta_condition_for_update_object_group_input import MetaConditionForUpdateObjectGroupInput
from volcenginesdkvolcobserve.models.meta_condition_for_update_rule_input import MetaConditionForUpdateRuleInput
from volcenginesdkvolcobserve.models.meta_condition_for_update_silence_policy_input import MetaConditionForUpdateSilencePolicyInput
from volcenginesdkvolcobserve.models.meta_for_create_object_group_input import MetaForCreateObjectGroupInput
from volcenginesdkvolcobserve.models.meta_for_create_rule_input import MetaForCreateRuleInput
from volcenginesdkvolcobserve.models.meta_for_create_silence_policy_input import MetaForCreateSilencePolicyInput
from volcenginesdkvolcobserve.models.meta_for_list_rules_by_ids_output import MetaForListRulesByIdsOutput
from volcenginesdkvolcobserve.models.meta_for_list_rules_output import MetaForListRulesOutput
from volcenginesdkvolcobserve.models.meta_for_list_silence_policy_output import MetaForListSilencePolicyOutput
from volcenginesdkvolcobserve.models.meta_for_update_object_group_input import MetaForUpdateObjectGroupInput
from volcenginesdkvolcobserve.models.meta_for_update_rule_input import MetaForUpdateRuleInput
from volcenginesdkvolcobserve.models.meta_for_update_silence_policy_input import MetaForUpdateSilencePolicyInput
from volcenginesdkvolcobserve.models.metric_data_result_for_get_metric_data_output import MetricDataResultForGetMetricDataOutput
from volcenginesdkvolcobserve.models.modify_state_of_silence_policy_by_ids_request import ModifyStateOfSilencePolicyByIdsRequest
from volcenginesdkvolcobserve.models.modify_state_of_silence_policy_by_ids_response import ModifyStateOfSilencePolicyByIdsResponse
from volcenginesdkvolcobserve.models.no_data_for_create_alert_template_input import NoDataForCreateAlertTemplateInput
from volcenginesdkvolcobserve.models.no_data_for_create_rule_input import NoDataForCreateRuleInput
from volcenginesdkvolcobserve.models.no_data_for_list_alert_templates_output import NoDataForListAlertTemplatesOutput
from volcenginesdkvolcobserve.models.no_data_for_list_preset_alert_templates_output import NoDataForListPresetAlertTemplatesOutput
from volcenginesdkvolcobserve.models.no_data_for_update_alert_template_input import NoDataForUpdateAlertTemplateInput
from volcenginesdkvolcobserve.models.no_data_for_update_rule_input import NoDataForUpdateRuleInput
from volcenginesdkvolcobserve.models.notification_for_create_notification_input import NotificationForCreateNotificationInput
from volcenginesdkvolcobserve.models.notification_for_list_notifications_output import NotificationForListNotificationsOutput
from volcenginesdkvolcobserve.models.notification_for_update_notification_input import NotificationForUpdateNotificationInput
from volcenginesdkvolcobserve.models.object_for_create_object_group_input import ObjectForCreateObjectGroupInput
from volcenginesdkvolcobserve.models.object_for_list_object_groups_output import ObjectForListObjectGroupsOutput
from volcenginesdkvolcobserve.models.object_for_update_object_group_input import ObjectForUpdateObjectGroupInput
from volcenginesdkvolcobserve.models.object_group_for_list_alert_templates_output import ObjectGroupForListAlertTemplatesOutput
from volcenginesdkvolcobserve.models.project_condition_for_create_object_group_input import ProjectConditionForCreateObjectGroupInput
from volcenginesdkvolcobserve.models.project_condition_for_create_rule_input import ProjectConditionForCreateRuleInput
from volcenginesdkvolcobserve.models.project_condition_for_list_rules_by_ids_output import ProjectConditionForListRulesByIdsOutput
from volcenginesdkvolcobserve.models.project_condition_for_list_rules_output import ProjectConditionForListRulesOutput
from volcenginesdkvolcobserve.models.project_condition_for_update_object_group_input import ProjectConditionForUpdateObjectGroupInput
from volcenginesdkvolcobserve.models.project_condition_for_update_rule_input import ProjectConditionForUpdateRuleInput
from volcenginesdkvolcobserve.models.range_for_create_silence_policy_input import RangeForCreateSilencePolicyInput
from volcenginesdkvolcobserve.models.range_for_list_silence_policy_output import RangeForListSilencePolicyOutput
from volcenginesdkvolcobserve.models.range_for_update_silence_policy_input import RangeForUpdateSilencePolicyInput
from volcenginesdkvolcobserve.models.recovery_notify_for_create_alert_template_input import RecoveryNotifyForCreateAlertTemplateInput
from volcenginesdkvolcobserve.models.recovery_notify_for_create_rule_input import RecoveryNotifyForCreateRuleInput
from volcenginesdkvolcobserve.models.recovery_notify_for_list_alert_templates_output import RecoveryNotifyForListAlertTemplatesOutput
from volcenginesdkvolcobserve.models.recovery_notify_for_list_preset_alert_templates_output import RecoveryNotifyForListPresetAlertTemplatesOutput
from volcenginesdkvolcobserve.models.recovery_notify_for_list_rules_by_ids_output import RecoveryNotifyForListRulesByIdsOutput
from volcenginesdkvolcobserve.models.recovery_notify_for_list_rules_output import RecoveryNotifyForListRulesOutput
from volcenginesdkvolcobserve.models.recovery_notify_for_update_alert_template_input import RecoveryNotifyForUpdateAlertTemplateInput
from volcenginesdkvolcobserve.models.recovery_notify_for_update_rule_input import RecoveryNotifyForUpdateRuleInput
from volcenginesdkvolcobserve.models.send_result_for_list_send_alert_output import SendResultForListSendAlertOutput
from volcenginesdkvolcobserve.models.set_state_of_rules_by_ids_request import SetStateOfRulesByIdsRequest
from volcenginesdkvolcobserve.models.set_state_of_rules_by_ids_response import SetStateOfRulesByIdsResponse
from volcenginesdkvolcobserve.models.silence_conditions_for_create_silence_policy_input import SilenceConditionsForCreateSilencePolicyInput
from volcenginesdkvolcobserve.models.silence_conditions_for_list_silence_policy_output import SilenceConditionsForListSilencePolicyOutput
from volcenginesdkvolcobserve.models.silence_conditions_for_update_silence_policy_input import SilenceConditionsForUpdateSilencePolicyInput
from volcenginesdkvolcobserve.models.tls_target_for_create_event_rule_input import TLSTargetForCreateEventRuleInput
from volcenginesdkvolcobserve.models.tls_target_for_list_event_rules_output import TLSTargetForListEventRulesOutput
from volcenginesdkvolcobserve.models.tls_target_for_update_event_rule_input import TLSTargetForUpdateEventRuleInput
from volcenginesdkvolcobserve.models.tag_condition_for_create_object_group_input import TagConditionForCreateObjectGroupInput
from volcenginesdkvolcobserve.models.tag_condition_for_create_rule_input import TagConditionForCreateRuleInput
from volcenginesdkvolcobserve.models.tag_condition_for_list_rules_by_ids_output import TagConditionForListRulesByIdsOutput
from volcenginesdkvolcobserve.models.tag_condition_for_list_rules_output import TagConditionForListRulesOutput
from volcenginesdkvolcobserve.models.tag_condition_for_update_object_group_input import TagConditionForUpdateObjectGroupInput
from volcenginesdkvolcobserve.models.tag_condition_for_update_rule_input import TagConditionForUpdateRuleInput
from volcenginesdkvolcobserve.models.tag_for_create_object_group_input import TagForCreateObjectGroupInput
from volcenginesdkvolcobserve.models.tag_for_create_rule_input import TagForCreateRuleInput
from volcenginesdkvolcobserve.models.tag_for_list_rules_by_ids_output import TagForListRulesByIdsOutput
from volcenginesdkvolcobserve.models.tag_for_list_rules_output import TagForListRulesOutput
from volcenginesdkvolcobserve.models.tag_for_tag_resources_input import TagForTagResourcesInput
from volcenginesdkvolcobserve.models.tag_for_update_object_group_input import TagForUpdateObjectGroupInput
from volcenginesdkvolcobserve.models.tag_for_update_rule_input import TagForUpdateRuleInput
from volcenginesdkvolcobserve.models.tag_resources_request import TagResourcesRequest
from volcenginesdkvolcobserve.models.tag_resources_response import TagResourcesResponse
from volcenginesdkvolcobserve.models.template_rule_for_create_alert_template_input import TemplateRuleForCreateAlertTemplateInput
from volcenginesdkvolcobserve.models.template_rule_for_list_alert_templates_output import TemplateRuleForListAlertTemplatesOutput
from volcenginesdkvolcobserve.models.template_rule_for_list_preset_alert_templates_output import TemplateRuleForListPresetAlertTemplatesOutput
from volcenginesdkvolcobserve.models.template_rule_for_update_alert_template_input import TemplateRuleForUpdateAlertTemplateInput
from volcenginesdkvolcobserve.models.top_data_result_for_get_top_data_output import TopDataResultForGetTopDataOutput
from volcenginesdkvolcobserve.models.untag_resources_request import UntagResourcesRequest
from volcenginesdkvolcobserve.models.untag_resources_response import UntagResourcesResponse
from volcenginesdkvolcobserve.models.update_alert_template_request import UpdateAlertTemplateRequest
from volcenginesdkvolcobserve.models.update_alert_template_response import UpdateAlertTemplateResponse
from volcenginesdkvolcobserve.models.update_contact_group_request import UpdateContactGroupRequest
from volcenginesdkvolcobserve.models.update_contact_group_response import UpdateContactGroupResponse
from volcenginesdkvolcobserve.models.update_contact_group_with_contacts_request import UpdateContactGroupWithContactsRequest
from volcenginesdkvolcobserve.models.update_contact_group_with_contacts_response import UpdateContactGroupWithContactsResponse
from volcenginesdkvolcobserve.models.update_contacts_request import UpdateContactsRequest
from volcenginesdkvolcobserve.models.update_contacts_response import UpdateContactsResponse
from volcenginesdkvolcobserve.models.update_contacts_with_contact_groups_request import UpdateContactsWithContactGroupsRequest
from volcenginesdkvolcobserve.models.update_contacts_with_contact_groups_response import UpdateContactsWithContactGroupsResponse
from volcenginesdkvolcobserve.models.update_event_rule_request import UpdateEventRuleRequest
from volcenginesdkvolcobserve.models.update_event_rule_response import UpdateEventRuleResponse
from volcenginesdkvolcobserve.models.update_notification_request import UpdateNotificationRequest
from volcenginesdkvolcobserve.models.update_notification_response import UpdateNotificationResponse
from volcenginesdkvolcobserve.models.update_object_group_request import UpdateObjectGroupRequest
from volcenginesdkvolcobserve.models.update_object_group_response import UpdateObjectGroupResponse
from volcenginesdkvolcobserve.models.update_rule_request import UpdateRuleRequest
from volcenginesdkvolcobserve.models.update_rule_response import UpdateRuleResponse
from volcenginesdkvolcobserve.models.update_silence_policy_request import UpdateSilencePolicyRequest
from volcenginesdkvolcobserve.models.update_silence_policy_response import UpdateSilencePolicyResponse
from volcenginesdkvolcobserve.models.update_webhook_request import UpdateWebhookRequest
from volcenginesdkvolcobserve.models.update_webhook_response import UpdateWebhookResponse
