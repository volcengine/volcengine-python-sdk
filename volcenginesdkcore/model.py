from volcenginesdkcore.interceptor.interceptors.common_request import sanitize_for_serialization


def canonical_str(obj):
    return sanitize_for_serialization(obj)
