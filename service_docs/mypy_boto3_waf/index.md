# Type annotations for boto3 WAF module

> [Index](../index.md) > WAF

Auto-generated documentation for [WAF](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf.html#WAF)
type annotations stubs module [mypy_boto3_waf](https://pypi.org/project/mypy-boto3-waf/).

```bash
pip install mypy-boto3-waf
```

- [Type annotations for boto3 WAF module](#type-annotations-for-boto3-waf-module)
  - [WAFClient](#wafclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## WAFClient

Type annotations for  `boto3.client("waf")` as [WAFClient](./client.md)

Can be used directly:

```python
from mypy_boto3_waf.client import WAFClient
```


WAFClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_byte_match_set](./client.md#create-byte-match-set)
- [create_geo_match_set](./client.md#create-geo-match-set)
- [create_ip_set](./client.md#create-ip-set)
- [create_rate_based_rule](./client.md#create-rate-based-rule)
- [create_regex_match_set](./client.md#create-regex-match-set)
- [create_regex_pattern_set](./client.md#create-regex-pattern-set)
- [create_rule](./client.md#create-rule)
- [create_rule_group](./client.md#create-rule-group)
- [create_size_constraint_set](./client.md#create-size-constraint-set)
- [create_sql_injection_match_set](./client.md#create-sql-injection-match-set)
- [create_web_acl](./client.md#create-web-acl)
- [create_web_acl_migration_stack](./client.md#create-web-acl-migration-stack)
- [create_xss_match_set](./client.md#create-xss-match-set)
- [delete_byte_match_set](./client.md#delete-byte-match-set)
- [delete_geo_match_set](./client.md#delete-geo-match-set)
- [delete_ip_set](./client.md#delete-ip-set)
- [delete_logging_configuration](./client.md#delete-logging-configuration)
- [delete_permission_policy](./client.md#delete-permission-policy)
- [delete_rate_based_rule](./client.md#delete-rate-based-rule)
- [delete_regex_match_set](./client.md#delete-regex-match-set)
- [delete_regex_pattern_set](./client.md#delete-regex-pattern-set)
- [delete_rule](./client.md#delete-rule)
- [delete_rule_group](./client.md#delete-rule-group)
- [delete_size_constraint_set](./client.md#delete-size-constraint-set)
- [delete_sql_injection_match_set](./client.md#delete-sql-injection-match-set)
- [delete_web_acl](./client.md#delete-web-acl)
- [delete_xss_match_set](./client.md#delete-xss-match-set)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_byte_match_set](./client.md#get-byte-match-set)
- [get_change_token](./client.md#get-change-token)
- [get_change_token_status](./client.md#get-change-token-status)
- [get_geo_match_set](./client.md#get-geo-match-set)
- [get_ip_set](./client.md#get-ip-set)
- [get_logging_configuration](./client.md#get-logging-configuration)
- [get_paginator](./client.md#get-paginator)
- [get_permission_policy](./client.md#get-permission-policy)
- [get_rate_based_rule](./client.md#get-rate-based-rule)
- [get_rate_based_rule_managed_keys](./client.md#get-rate-based-rule-managed-keys)
- [get_regex_match_set](./client.md#get-regex-match-set)
- [get_regex_pattern_set](./client.md#get-regex-pattern-set)
- [get_rule](./client.md#get-rule)
- [get_rule_group](./client.md#get-rule-group)
- [get_sampled_requests](./client.md#get-sampled-requests)
- [get_size_constraint_set](./client.md#get-size-constraint-set)
- [get_sql_injection_match_set](./client.md#get-sql-injection-match-set)
- [get_web_acl](./client.md#get-web-acl)
- [get_xss_match_set](./client.md#get-xss-match-set)
- [list_activated_rules_in_rule_group](./client.md#list-activated-rules-in-rule-group)
- [list_byte_match_sets](./client.md#list-byte-match-sets)
- [list_geo_match_sets](./client.md#list-geo-match-sets)
- [list_ip_sets](./client.md#list-ip-sets)
- [list_logging_configurations](./client.md#list-logging-configurations)
- [list_rate_based_rules](./client.md#list-rate-based-rules)
- [list_regex_match_sets](./client.md#list-regex-match-sets)
- [list_regex_pattern_sets](./client.md#list-regex-pattern-sets)
- [list_rule_groups](./client.md#list-rule-groups)
- [list_rules](./client.md#list-rules)
- [list_size_constraint_sets](./client.md#list-size-constraint-sets)
- [list_sql_injection_match_sets](./client.md#list-sql-injection-match-sets)
- [list_subscribed_rule_groups](./client.md#list-subscribed-rule-groups)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_web_acls](./client.md#list-web-acls)
- [list_xss_match_sets](./client.md#list-xss-match-sets)
- [put_logging_configuration](./client.md#put-logging-configuration)
- [put_permission_policy](./client.md#put-permission-policy)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_byte_match_set](./client.md#update-byte-match-set)
- [update_geo_match_set](./client.md#update-geo-match-set)
- [update_ip_set](./client.md#update-ip-set)
- [update_rate_based_rule](./client.md#update-rate-based-rule)
- [update_regex_match_set](./client.md#update-regex-match-set)
- [update_regex_pattern_set](./client.md#update-regex-pattern-set)
- [update_rule](./client.md#update-rule)
- [update_rule_group](./client.md#update-rule-group)
- [update_size_constraint_set](./client.md#update-size-constraint-set)
- [update_sql_injection_match_set](./client.md#update-sql-injection-match-set)
- [update_web_acl](./client.md#update-web-acl)
- [update_xss_match_set](./client.md#update-xss-match-set)




### Exceptions
- [ClientError](./client.md#clienterror)
- [WAFBadRequestException](./client.md#wafbadrequestexception)
- [WAFDisallowedNameException](./client.md#wafdisallowednameexception)
- [WAFEntityMigrationException](./client.md#wafentitymigrationexception)
- [WAFInternalErrorException](./client.md#wafinternalerrorexception)
- [WAFInvalidAccountException](./client.md#wafinvalidaccountexception)
- [WAFInvalidOperationException](./client.md#wafinvalidoperationexception)
- [WAFInvalidParameterException](./client.md#wafinvalidparameterexception)
- [WAFInvalidPermissionPolicyException](./client.md#wafinvalidpermissionpolicyexception)
- [WAFInvalidRegexPatternException](./client.md#wafinvalidregexpatternexception)
- [WAFLimitsExceededException](./client.md#waflimitsexceededexception)
- [WAFNonEmptyEntityException](./client.md#wafnonemptyentityexception)
- [WAFNonexistentContainerException](./client.md#wafnonexistentcontainerexception)
- [WAFNonexistentItemException](./client.md#wafnonexistentitemexception)
- [WAFReferencedItemException](./client.md#wafreferenceditemexception)
- [WAFServiceLinkedRoleErrorException](./client.md#wafservicelinkedroleerrorexception)
- [WAFStaleDataException](./client.md#wafstaledataexception)
- [WAFSubscriptionNotFoundException](./client.md#wafsubscriptionnotfoundexception)
- [WAFTagOperationException](./client.md#waftagoperationexception)
- [WAFTagOperationInternalErrorException](./client.md#waftagoperationinternalerrorexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("waf").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_waf.paginators import GetRateBasedRuleManagedKeysPaginator, ...
```

- [GetRateBasedRuleManagedKeysPaginator](./paginators.md#getratebasedrulemanagedkeyspaginator)
- [ListActivatedRulesInRuleGroupPaginator](./paginators.md#listactivatedrulesinrulegrouppaginator)
- [ListByteMatchSetsPaginator](./paginators.md#listbytematchsetspaginator)
- [ListGeoMatchSetsPaginator](./paginators.md#listgeomatchsetspaginator)
- [ListIPSetsPaginator](./paginators.md#listipsetspaginator)
- [ListLoggingConfigurationsPaginator](./paginators.md#listloggingconfigurationspaginator)
- [ListRateBasedRulesPaginator](./paginators.md#listratebasedrulespaginator)
- [ListRegexMatchSetsPaginator](./paginators.md#listregexmatchsetspaginator)
- [ListRegexPatternSetsPaginator](./paginators.md#listregexpatternsetspaginator)
- [ListRuleGroupsPaginator](./paginators.md#listrulegroupspaginator)
- [ListRulesPaginator](./paginators.md#listrulespaginator)
- [ListSizeConstraintSetsPaginator](./paginators.md#listsizeconstraintsetspaginator)
- [ListSqlInjectionMatchSetsPaginator](./paginators.md#listsqlinjectionmatchsetspaginator)
- [ListSubscribedRuleGroupsPaginator](./paginators.md#listsubscribedrulegroupspaginator)
- [ListWebACLsPaginator](./paginators.md#listwebaclspaginator)
- [ListXssMatchSetsPaginator](./paginators.md#listxssmatchsetspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_waf.literals import ChangeAction, ...
```

- [ChangeAction](./literals.md#changeaction)
- [ChangeTokenStatus](./literals.md#changetokenstatus)
- [ComparisonOperator](./literals.md#comparisonoperator)
- [GeoMatchConstraintType](./literals.md#geomatchconstrainttype)
- [GeoMatchConstraintValue](./literals.md#geomatchconstraintvalue)
- [GetRateBasedRuleManagedKeysPaginatorName](./literals.md#getratebasedrulemanagedkeyspaginatorname)
- [IPSetDescriptorType](./literals.md#ipsetdescriptortype)
- [ListActivatedRulesInRuleGroupPaginatorName](./literals.md#listactivatedrulesinrulegrouppaginatorname)
- [ListByteMatchSetsPaginatorName](./literals.md#listbytematchsetspaginatorname)
- [ListGeoMatchSetsPaginatorName](./literals.md#listgeomatchsetspaginatorname)
- [ListIPSetsPaginatorName](./literals.md#listipsetspaginatorname)
- [ListLoggingConfigurationsPaginatorName](./literals.md#listloggingconfigurationspaginatorname)
- [ListRateBasedRulesPaginatorName](./literals.md#listratebasedrulespaginatorname)
- [ListRegexMatchSetsPaginatorName](./literals.md#listregexmatchsetspaginatorname)
- [ListRegexPatternSetsPaginatorName](./literals.md#listregexpatternsetspaginatorname)
- [ListRuleGroupsPaginatorName](./literals.md#listrulegroupspaginatorname)
- [ListRulesPaginatorName](./literals.md#listrulespaginatorname)
- [ListSizeConstraintSetsPaginatorName](./literals.md#listsizeconstraintsetspaginatorname)
- [ListSqlInjectionMatchSetsPaginatorName](./literals.md#listsqlinjectionmatchsetspaginatorname)
- [ListSubscribedRuleGroupsPaginatorName](./literals.md#listsubscribedrulegroupspaginatorname)
- [ListWebACLsPaginatorName](./literals.md#listwebaclspaginatorname)
- [ListXssMatchSetsPaginatorName](./literals.md#listxssmatchsetspaginatorname)
- [MatchFieldType](./literals.md#matchfieldtype)
- [PositionalConstraint](./literals.md#positionalconstraint)
- [PredicateType](./literals.md#predicatetype)
- [RateKey](./literals.md#ratekey)
- [TextTransformation](./literals.md#texttransformation)
- [WafActionType](./literals.md#wafactiontype)
- [WafOverrideActionType](./literals.md#wafoverrideactiontype)
- [WafRuleType](./literals.md#wafruletype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_waf.type_defs import ActivatedRuleTypeDef, ...
```

- [ActivatedRuleTypeDef](./type_defs.md#activatedruletypedef)
- [ByteMatchSetSummaryTypeDef](./type_defs.md#bytematchsetsummarytypedef)
- [ByteMatchSetTypeDef](./type_defs.md#bytematchsettypedef)
- [ByteMatchTupleTypeDef](./type_defs.md#bytematchtupletypedef)
- [ExcludedRuleTypeDef](./type_defs.md#excludedruletypedef)
- [FieldToMatchTypeDef](./type_defs.md#fieldtomatchtypedef)
- [GeoMatchConstraintTypeDef](./type_defs.md#geomatchconstrainttypedef)
- [GeoMatchSetSummaryTypeDef](./type_defs.md#geomatchsetsummarytypedef)
- [GeoMatchSetTypeDef](./type_defs.md#geomatchsettypedef)
- [HTTPHeaderTypeDef](./type_defs.md#httpheadertypedef)
- [HTTPRequestTypeDef](./type_defs.md#httprequesttypedef)
- [IPSetDescriptorTypeDef](./type_defs.md#ipsetdescriptortypedef)
- [IPSetSummaryTypeDef](./type_defs.md#ipsetsummarytypedef)
- [IPSetTypeDef](./type_defs.md#ipsettypedef)
- [LoggingConfigurationTypeDef](./type_defs.md#loggingconfigurationtypedef)
- [PredicateTypeDef](./type_defs.md#predicatetypedef)
- [RateBasedRuleTypeDef](./type_defs.md#ratebasedruletypedef)
- [RegexMatchSetSummaryTypeDef](./type_defs.md#regexmatchsetsummarytypedef)
- [RegexMatchSetTypeDef](./type_defs.md#regexmatchsettypedef)
- [RegexMatchTupleTypeDef](./type_defs.md#regexmatchtupletypedef)
- [RegexPatternSetSummaryTypeDef](./type_defs.md#regexpatternsetsummarytypedef)
- [RegexPatternSetTypeDef](./type_defs.md#regexpatternsettypedef)
- [RuleGroupSummaryTypeDef](./type_defs.md#rulegroupsummarytypedef)
- [RuleGroupTypeDef](./type_defs.md#rulegrouptypedef)
- [RuleSummaryTypeDef](./type_defs.md#rulesummarytypedef)
- [RuleTypeDef](./type_defs.md#ruletypedef)
- [SampledHTTPRequestTypeDef](./type_defs.md#sampledhttprequesttypedef)
- [SizeConstraintSetSummaryTypeDef](./type_defs.md#sizeconstraintsetsummarytypedef)
- [SizeConstraintSetTypeDef](./type_defs.md#sizeconstraintsettypedef)
- [SizeConstraintTypeDef](./type_defs.md#sizeconstrainttypedef)
- [SqlInjectionMatchSetSummaryTypeDef](./type_defs.md#sqlinjectionmatchsetsummarytypedef)
- [SqlInjectionMatchSetTypeDef](./type_defs.md#sqlinjectionmatchsettypedef)
- [SqlInjectionMatchTupleTypeDef](./type_defs.md#sqlinjectionmatchtupletypedef)
- [SubscribedRuleGroupSummaryTypeDef](./type_defs.md#subscribedrulegroupsummarytypedef)
- [TagInfoForResourceTypeDef](./type_defs.md#taginfoforresourcetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TimeWindowTypeDef](./type_defs.md#timewindowtypedef)
- [WafActionTypeDef](./type_defs.md#wafactiontypedef)
- [WafOverrideActionTypeDef](./type_defs.md#wafoverrideactiontypedef)
- [WebACLSummaryTypeDef](./type_defs.md#webaclsummarytypedef)
- [WebACLTypeDef](./type_defs.md#webacltypedef)
- [XssMatchSetSummaryTypeDef](./type_defs.md#xssmatchsetsummarytypedef)
- [XssMatchSetTypeDef](./type_defs.md#xssmatchsettypedef)
- [XssMatchTupleTypeDef](./type_defs.md#xssmatchtupletypedef)
- [ByteMatchSetUpdateTypeDef](./type_defs.md#bytematchsetupdatetypedef)
- [CreateByteMatchSetResponseTypeDef](./type_defs.md#createbytematchsetresponsetypedef)
- [CreateGeoMatchSetResponseTypeDef](./type_defs.md#creategeomatchsetresponsetypedef)
- [CreateIPSetResponseTypeDef](./type_defs.md#createipsetresponsetypedef)
- [CreateRateBasedRuleResponseTypeDef](./type_defs.md#createratebasedruleresponsetypedef)
- [CreateRegexMatchSetResponseTypeDef](./type_defs.md#createregexmatchsetresponsetypedef)
- [CreateRegexPatternSetResponseTypeDef](./type_defs.md#createregexpatternsetresponsetypedef)
- [CreateRuleGroupResponseTypeDef](./type_defs.md#createrulegroupresponsetypedef)
- [CreateRuleResponseTypeDef](./type_defs.md#createruleresponsetypedef)
- [CreateSizeConstraintSetResponseTypeDef](./type_defs.md#createsizeconstraintsetresponsetypedef)
- [CreateSqlInjectionMatchSetResponseTypeDef](./type_defs.md#createsqlinjectionmatchsetresponsetypedef)
- [CreateWebACLMigrationStackResponseTypeDef](./type_defs.md#createwebaclmigrationstackresponsetypedef)
- [CreateWebACLResponseTypeDef](./type_defs.md#createwebaclresponsetypedef)
- [CreateXssMatchSetResponseTypeDef](./type_defs.md#createxssmatchsetresponsetypedef)
- [DeleteByteMatchSetResponseTypeDef](./type_defs.md#deletebytematchsetresponsetypedef)
- [DeleteGeoMatchSetResponseTypeDef](./type_defs.md#deletegeomatchsetresponsetypedef)
- [DeleteIPSetResponseTypeDef](./type_defs.md#deleteipsetresponsetypedef)
- [DeleteRateBasedRuleResponseTypeDef](./type_defs.md#deleteratebasedruleresponsetypedef)
- [DeleteRegexMatchSetResponseTypeDef](./type_defs.md#deleteregexmatchsetresponsetypedef)
- [DeleteRegexPatternSetResponseTypeDef](./type_defs.md#deleteregexpatternsetresponsetypedef)
- [DeleteRuleGroupResponseTypeDef](./type_defs.md#deleterulegroupresponsetypedef)
- [DeleteRuleResponseTypeDef](./type_defs.md#deleteruleresponsetypedef)
- [DeleteSizeConstraintSetResponseTypeDef](./type_defs.md#deletesizeconstraintsetresponsetypedef)
- [DeleteSqlInjectionMatchSetResponseTypeDef](./type_defs.md#deletesqlinjectionmatchsetresponsetypedef)
- [DeleteWebACLResponseTypeDef](./type_defs.md#deletewebaclresponsetypedef)
- [DeleteXssMatchSetResponseTypeDef](./type_defs.md#deletexssmatchsetresponsetypedef)
- [GeoMatchSetUpdateTypeDef](./type_defs.md#geomatchsetupdatetypedef)
- [GetByteMatchSetResponseTypeDef](./type_defs.md#getbytematchsetresponsetypedef)
- [GetChangeTokenResponseTypeDef](./type_defs.md#getchangetokenresponsetypedef)
- [GetChangeTokenStatusResponseTypeDef](./type_defs.md#getchangetokenstatusresponsetypedef)
- [GetGeoMatchSetResponseTypeDef](./type_defs.md#getgeomatchsetresponsetypedef)
- [GetIPSetResponseTypeDef](./type_defs.md#getipsetresponsetypedef)
- [GetLoggingConfigurationResponseTypeDef](./type_defs.md#getloggingconfigurationresponsetypedef)
- [GetPermissionPolicyResponseTypeDef](./type_defs.md#getpermissionpolicyresponsetypedef)
- [GetRateBasedRuleManagedKeysResponseTypeDef](./type_defs.md#getratebasedrulemanagedkeysresponsetypedef)
- [GetRateBasedRuleResponseTypeDef](./type_defs.md#getratebasedruleresponsetypedef)
- [GetRegexMatchSetResponseTypeDef](./type_defs.md#getregexmatchsetresponsetypedef)
- [GetRegexPatternSetResponseTypeDef](./type_defs.md#getregexpatternsetresponsetypedef)
- [GetRuleGroupResponseTypeDef](./type_defs.md#getrulegroupresponsetypedef)
- [GetRuleResponseTypeDef](./type_defs.md#getruleresponsetypedef)
- [GetSampledRequestsResponseTypeDef](./type_defs.md#getsampledrequestsresponsetypedef)
- [GetSizeConstraintSetResponseTypeDef](./type_defs.md#getsizeconstraintsetresponsetypedef)
- [GetSqlInjectionMatchSetResponseTypeDef](./type_defs.md#getsqlinjectionmatchsetresponsetypedef)
- [GetWebACLResponseTypeDef](./type_defs.md#getwebaclresponsetypedef)
- [GetXssMatchSetResponseTypeDef](./type_defs.md#getxssmatchsetresponsetypedef)
- [IPSetUpdateTypeDef](./type_defs.md#ipsetupdatetypedef)
- [ListActivatedRulesInRuleGroupResponseTypeDef](./type_defs.md#listactivatedrulesinrulegroupresponsetypedef)
- [ListByteMatchSetsResponseTypeDef](./type_defs.md#listbytematchsetsresponsetypedef)
- [ListGeoMatchSetsResponseTypeDef](./type_defs.md#listgeomatchsetsresponsetypedef)
- [ListIPSetsResponseTypeDef](./type_defs.md#listipsetsresponsetypedef)
- [ListLoggingConfigurationsResponseTypeDef](./type_defs.md#listloggingconfigurationsresponsetypedef)
- [ListRateBasedRulesResponseTypeDef](./type_defs.md#listratebasedrulesresponsetypedef)
- [ListRegexMatchSetsResponseTypeDef](./type_defs.md#listregexmatchsetsresponsetypedef)
- [ListRegexPatternSetsResponseTypeDef](./type_defs.md#listregexpatternsetsresponsetypedef)
- [ListRuleGroupsResponseTypeDef](./type_defs.md#listrulegroupsresponsetypedef)
- [ListRulesResponseTypeDef](./type_defs.md#listrulesresponsetypedef)
- [ListSizeConstraintSetsResponseTypeDef](./type_defs.md#listsizeconstraintsetsresponsetypedef)
- [ListSqlInjectionMatchSetsResponseTypeDef](./type_defs.md#listsqlinjectionmatchsetsresponsetypedef)
- [ListSubscribedRuleGroupsResponseTypeDef](./type_defs.md#listsubscribedrulegroupsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListWebACLsResponseTypeDef](./type_defs.md#listwebaclsresponsetypedef)
- [ListXssMatchSetsResponseTypeDef](./type_defs.md#listxssmatchsetsresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutLoggingConfigurationResponseTypeDef](./type_defs.md#putloggingconfigurationresponsetypedef)
- [RegexMatchSetUpdateTypeDef](./type_defs.md#regexmatchsetupdatetypedef)
- [RegexPatternSetUpdateTypeDef](./type_defs.md#regexpatternsetupdatetypedef)
- [RuleGroupUpdateTypeDef](./type_defs.md#rulegroupupdatetypedef)
- [RuleUpdateTypeDef](./type_defs.md#ruleupdatetypedef)
- [SizeConstraintSetUpdateTypeDef](./type_defs.md#sizeconstraintsetupdatetypedef)
- [SqlInjectionMatchSetUpdateTypeDef](./type_defs.md#sqlinjectionmatchsetupdatetypedef)
- [UpdateByteMatchSetResponseTypeDef](./type_defs.md#updatebytematchsetresponsetypedef)
- [UpdateGeoMatchSetResponseTypeDef](./type_defs.md#updategeomatchsetresponsetypedef)
- [UpdateIPSetResponseTypeDef](./type_defs.md#updateipsetresponsetypedef)
- [UpdateRateBasedRuleResponseTypeDef](./type_defs.md#updateratebasedruleresponsetypedef)
- [UpdateRegexMatchSetResponseTypeDef](./type_defs.md#updateregexmatchsetresponsetypedef)
- [UpdateRegexPatternSetResponseTypeDef](./type_defs.md#updateregexpatternsetresponsetypedef)
- [UpdateRuleGroupResponseTypeDef](./type_defs.md#updaterulegroupresponsetypedef)
- [UpdateRuleResponseTypeDef](./type_defs.md#updateruleresponsetypedef)
- [UpdateSizeConstraintSetResponseTypeDef](./type_defs.md#updatesizeconstraintsetresponsetypedef)
- [UpdateSqlInjectionMatchSetResponseTypeDef](./type_defs.md#updatesqlinjectionmatchsetresponsetypedef)
- [UpdateWebACLResponseTypeDef](./type_defs.md#updatewebaclresponsetypedef)
- [UpdateXssMatchSetResponseTypeDef](./type_defs.md#updatexssmatchsetresponsetypedef)
- [WebACLUpdateTypeDef](./type_defs.md#webaclupdatetypedef)
- [XssMatchSetUpdateTypeDef](./type_defs.md#xssmatchsetupdatetypedef)