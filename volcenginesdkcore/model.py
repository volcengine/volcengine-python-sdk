from volcenginesdkcore.interceptor.interceptors.build_request_interceptor import sanitize_for_serialization


def canonical_str(obj):
    return sanitize_for_serialization(obj)
