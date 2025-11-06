# coding=utf-8
from __future__ import unicode_literals, print_function
import re
from volcenginesdkcore.endpoint.endpoint_provider import EndpointProvider, ResolvedEndpoint


# -----------------------------
# Errors (模仿 volcengineerr.New)
# -----------------------------
class StandProviderError(Exception):
    def __init__(self, code, message):
        Exception.__init__(self, "%s: %s" % (code, message))
        self.code = code
        self.message = message


# -----------------------------
# 常量
# -----------------------------
DEFAULT_FORMAT = "{Service}{Region}.{SiteStack}.com"

# 站点栈
SITE_STACK_VOLC_IPV4 = "volcengineapi"
SITE_STACK_VOLC_DUAL_STACK = "volcengine-api"


# -----------------------------
# 数据模型（兼容 2.7/3.x 的朴素类）
# -----------------------------
class StandardEndpointResolverVariable(object):
    def __init__(self):
        self.service = ""
        self.region = ""
        self.site_stack = ""
        self.extension = {}

    def to_dict(self):
        return {
            "Service": self.service,
            "Region": self.region,
            "SiteStack": self.site_stack,
            "Extension": self.extension,
        }


class ServiceInfo(object):
    def __init__(self, service, is_global):
        self.service = service
        self.IsGlobal = is_global

ServiceInfos = {
    "vpc": ServiceInfo("vpc", False),
    "ecs": ServiceInfo("ecs", False),
    "billing": ServiceInfo("billing", True),
    "ark": ServiceInfo("ark", False),
    "iam": ServiceInfo("iam", True),
    "mcs": ServiceInfo("mcs", False),
    "rocketmq": ServiceInfo("rocketmq", False),
    "bytehouse": ServiceInfo("bytehouse", False),
    "dns": ServiceInfo("dns", True),
    "autoscaling": ServiceInfo("autoscaling", False),
    "spark": ServiceInfo("spark", False),
    "cloud_detect": ServiceInfo("cloud_detect", False),
    "filenas": ServiceInfo("filenas", False),
    "escloud": ServiceInfo("escloud", False),
    "flink": ServiceInfo("flink", False),
    "cp": ServiceInfo("cp", False),
    "vefaas": ServiceInfo("vefaas", False),
    "ml_platform": ServiceInfo("ml_platform", False),
    "edx": ServiceInfo("edx", True),
    "dcdn": ServiceInfo("dcdn", True),
    "cdn": ServiceInfo("cdn", True),
    "kafka": ServiceInfo("kafka", False),
    "certificate_service": ServiceInfo("certificate_service", True),
    "waf": ServiceInfo("waf", True),
    "rds_mssql": ServiceInfo("rds_mssql", False),
    "cloudtrail": ServiceInfo("cloudtrail", False),
    "vei_api": ServiceInfo("vei_api", True),
    "cen": ServiceInfo("cen", True),
    "rabbitmq": ServiceInfo("rabbitmq", False),
    "vmp": ServiceInfo("vmp", False),
    "volc_observe": ServiceInfo("volc_observe", False),
    "dataleap": ServiceInfo("dataleap", False),
    "fw_center": ServiceInfo("fw_center", True),
    "redis": ServiceInfo("redis", False),
    "mcdn": ServiceInfo("mcdn", True),
    "cloudidentity": ServiceInfo("cloudidentity", False),
    "vedbm": ServiceInfo("vedbm", False),
    "cv": ServiceInfo("cv", True),
    "translate": ServiceInfo("translate", True),
    "cloud_trail": ServiceInfo("cloud_trail", False),
    "bio": ServiceInfo("bio", False),
    "nta": ServiceInfo("nta", True),
    "elasticmapreduce": ServiceInfo("elasticmapreduce", False),
    "vepfs": ServiceInfo("vepfs", False),
    "seccenter": ServiceInfo("seccenter", True),
    "advdefence": ServiceInfo("advdefence", True),
    "tis": ServiceInfo("tis", True),
    "organization": ServiceInfo("organization", True),
    "vke": ServiceInfo("vke", False),
    "Redis": ServiceInfo("Redis", False),
    "privatelink": ServiceInfo("privatelink", False),
    "RocketMQ": ServiceInfo("RocketMQ", False),
    "Kafka": ServiceInfo("Kafka", False),
    "rds_mysql": ServiceInfo("rds_mysql", False),
    "rds_postgresql": ServiceInfo("rds_postgresql", False),
    "storage_ebs": ServiceInfo("storage_ebs", False),
    "clb": ServiceInfo("clb", False),
    "alb": ServiceInfo("alb", False),
    "FileNAS": ServiceInfo("FileNAS", False),
    "configcenter": ServiceInfo("configcenter", False),
    "cr": ServiceInfo("cr", False),
    "sts": ServiceInfo("sts", False),
    "mongodb": ServiceInfo("mongodb", False),
    "transitrouter": ServiceInfo("transitrouter", False),
    "Volc_Observe": ServiceInfo("Volc_Observe", False),
    "dms": ServiceInfo("dms", False),
    "auto_scaling": ServiceInfo("auto_scaling", False),
    "directconnect": ServiceInfo("directconnect", False),
    "kms": ServiceInfo("kms", False),
    "dbw": ServiceInfo("dbw", False),
    "dts": ServiceInfo("dts", False),
    "natgateway": ServiceInfo("natgateway", False),
    "tos": ServiceInfo("tos", False),
    "TLS": ServiceInfo("TLS", False),
    "vpn": ServiceInfo("vpn", False),
    "vod": ServiceInfo("vod", False),
    "quota": ServiceInfo("quota", True),
    "ecs_ops": ServiceInfo("ecs_ops", True),
    "as_ops": ServiceInfo("as_ops", True),
    "account_management": ServiceInfo("account_management", True),
    "account_management_byteplus": ServiceInfo("account_management_byteplus", True),
    "bandwidthquota": ServiceInfo("bandwidthquota", True),
    "psa_manager": ServiceInfo("psa_manager", True),
    "dc_controller": ServiceInfo("dc_controller", False),
    "eps_platform_trade": ServiceInfo("eps_platform_trade", False),
    "eps_platform_fund": ServiceInfo("eps_platform_fund", False),
    "commercialization": ServiceInfo("commercialization", True),
    "veecp_openapi": ServiceInfo("veecp_openapi", False),
    "orgnization": ServiceInfo("orgnization", True),
    "coze": ServiceInfo("coze", True),
    "sec_agent": ServiceInfo("sec_agent", True),
    "sec_intelligent_dev": ServiceInfo("sec_intelligent_dev", True),
    "vegame": ServiceInfo("vegame", False),
    "acep": ServiceInfo("acep", True),
    "private_zone": ServiceInfo("private_zone", True),
    "sqs": ServiceInfo("sqs", False),
    "resourcecenter": ServiceInfo("resourcecenter", True),
    "aiotvideo": ServiceInfo("aiotvideo", True),
    "apig": ServiceInfo("apig", False),
    "bmq": ServiceInfo("bmq", False),
    "bytehouse_ce": ServiceInfo("bytehouse_ce", False),
    "cloudmonitor": ServiceInfo("cloudmonitor", False),
    "emr": ServiceInfo("emr", False),
    "ga": ServiceInfo("ga", True),
    "graph": ServiceInfo("graph", False),
    "gtm": ServiceInfo("gtm", True),
    "hbase": ServiceInfo("hbase", False),
    "metakms": ServiceInfo("metakms", False),
    "na": ServiceInfo("na", True),
    "resource_share": ServiceInfo("resource_share", True),
    "speech_saas_prod": ServiceInfo("speech_saas_prod", True),
    "tag": ServiceInfo("tag", True),
    "vefaas_dev": ServiceInfo("vefaas_dev", False),
    "vms": ServiceInfo("vms", False),
    "eco_partner": ServiceInfo("eco_partner", True),
    "smc": ServiceInfo("smc", True),
}


# -----------------------------
# Region 校验
# -----------------------------
class RegionChecker(object):
    def __init__(self, white_regions, pattern):
        self.white_regions = white_regions or {}
        self.pattern = pattern

    def validate(self, region):
        if self.white_regions and region in self.white_regions:
            return True
        if self.pattern:
            return bool(self.pattern.match(region))
        return False


region_matcher = RegionChecker(
    {
        "ap-singapore-1": {},
        "ap-southeast-1": {},
        "ap-southeast-2": {},
        "ap-southeast-3": {},
        "byteplus-global": {},
        "cn-beijing": {},
        "cn-beijing-autodriving": {},
        "cn-beijing-selfdrive": {},
        "cn-beijing2": {},
        "cn-beijing300": {},
        "cn-changsha-sdv": {},
        "cn-chengdu": {},
        "cn-chengdu-sdv": {},
        "cn-chongqing-sdv": {},
        "cn-datong": {},
        "cn-east-1-dedicated": {},
        "cn-gaofang-bj": {},
        "cn-gaofang-gz1": {},
        "cn-gaofang-nt1": {},
        "cn-gaofang-nt2": {},
        "cn-gaofang-nt3": {},
        "cn-gaofang-nt4": {},
        "cn-gaofang-nt5": {},
        "cn-guangzhou": {},
        "cn-guilin-boe": {},
        "cn-hangzhou": {},
        "cn-hjxj": {},
        "cn-hjzg": {},
        "cn-hlbx": {},
        "cn-hlxj": {},
        "cn-hlzg": {},
        "cn-hongkong": {},
        "cn-hongkong-pop": {},
        "cn-lfbx": {},
        "cn-lfxj": {},
        "cn-lfzg": {},
        "cn-macau-pop-sdv": {},
        "cn-mainland": {},
        "cn-nanjing-bbit": {},
        "cn-ningbo-sdv": {},
        "cn-north-1": {},
        "cn-north-1-dedicated": {},
        "cn-north-boe": {},
        "cn-shanghai": {},
        "cn-shanghai-autodriving": {},
        "cn-taiwan-boe": {},
        "cn-wuhan": {},
        "cn-wulanchabu": {},
        "cn-xian-boe-sdv": {},
        "overseas-1": {},
        "rec-cn": {},
        "rec-sg": {},
    },
    re.compile(
        r"^(?:[a-z]{2}-[a-z]+(?:-[a-z]+)?|(?:cn|ap|eu|na|sa|me|af)-[a-z]+-\d+(?:-(?:finance|exclusive|local|inner))?)$"
    ),
)


# -----------------------------
# 工具函数
# -----------------------------
def standardize_domain_service_code(service_code):
    """lower + '_' -> '-'"""
    return service_code.lower().replace("_", "-")


# -----------------------------
# 解析器
# -----------------------------
class StandardEndpointResolver(EndpointProvider):
    def __init__(self, fmt=None, site_stack=None, extension=None, custom_services=None):
        self.fmt = fmt or DEFAULT_FORMAT
        self.variables = StandardEndpointResolverVariable()
        self.variables.site_stack = site_stack or SITE_STACK_VOLC_IPV4
        self.variables.extension = extension or {}
        self.custom_services = custom_services or {}

    def endpoint_for(self, service, region, custom_bootstrap_region=None, use_dual_stack=None, **kwargs):
        # 1) Region 校验
        if not region_matcher.validate(region):
            raise StandProviderError(
                "InvalidRegion",
                "invalid region %s for standard endpoint resolver, "
                "please upgrade the sdk endpoint resolver to the latest version" % region
            )

        # 2) 默认模板
        fmt = self.fmt or DEFAULT_FORMAT

        # 3) 变量准备
        self.variables.service = standardize_domain_service_code(service)

        svc_info = ServiceInfos.get(service)
        if not svc_info:
            svc_info = self.custom_services.get(service)
            if not svc_info:
                raise StandProviderError(
                    "ServiceNotFound",
                    "service %s not found in ServiceInfos  or customServices, "
                    "please upgrade the sdk endpoint resolver to the latest version" % service
                )

        # 非全局服务拼接 ".{region}"，全局则为空
        if not svc_info.IsGlobal:
            self.variables.region = "." + region
        else:
            self.variables.region = ""

        # 4) IP 版本 -> SiteStack
        if use_dual_stack:
            self.variables.site_stack = SITE_STACK_VOLC_DUAL_STACK
        else:
            self.variables.site_stack = SITE_STACK_VOLC_IPV4

        # 5) 渲染
        try:
            rendered = fmt.format(**self.variables.to_dict())
        except KeyError as err:
            raise StandProviderError(
                "TemplateExecuteError",
                "failed to execute template for format %s, missing variable %s" % (fmt, err)
            )
        except Exception as err:
            raise StandProviderError(
                "TemplateExecuteError",
                "failed to execute template for format %s, variable %r: %s" % (fmt, self.variables.to_dict(), err)
            )

        return ResolvedEndpoint(rendered)


# -----------------------------
if __name__ == "__main__":
    r = StandardEndpointResolver()
    try:
        ep = r.endpoint_for(
            service="vpc",
            region="ap-southeast-1",
            use_dual_stack=False,
        )
        print(ep.host)  # 例如：vpc.ap-southeast-1.volcengine-api.com
    except Exception as e:
        e.print()
