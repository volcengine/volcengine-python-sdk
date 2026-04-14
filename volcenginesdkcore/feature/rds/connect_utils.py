# coding: utf-8
"""
RDS MySQL connection authentication utilities.

This module provides utilities for generating authentication tokens for RDS MySQL database connections.
"""

from volcenginesdkcore.endpoint.providers.standard_provider import StandardEndpointResolver
from volcenginesdkcore.interceptor import InterceptorChain, InterceptorContext, SignRequestInterceptor, \
    ResolveEndpointInterceptor
from volcenginesdkcore.interceptor import Request

DEFAULT_SERVICE = 'rds_mysql'
DEFAULT_API_VERSION = '2022-01-01'
DEFAULT_API = 'ConnectDatabase'
DEFAULT_EXPIRES = 900


def build_auth_token(api_client, db_user, instance_id, expires=None):
    """
    Build an authentication token (presigned URL) for connecting to RDS MySQL database.

    :param api_client: ApiClient instance
    :param db_user: Database username
    :param instance_id: RDS instance ID
    :param expires: Token expiration time in seconds (default: 900, i.e., 15 minutes)
    :return: Presigned URL string for database authentication
    :raises ValueError: If required parameters are missing or invalid
    """
    # Validate api_client
    if api_client is None:
        raise ValueError("api_client must not be None")

    configuration = api_client.configuration
    region = configuration.region

    # Validate inputs
    if not region:
        raise ValueError("region must not be empty")

    if not db_user:
        raise ValueError("db_user must not be empty")

    if not instance_id:
        raise ValueError("instance_id must not be empty")

    # Set default expiration time
    if expires is None or expires <= 0:
        expires = DEFAULT_EXPIRES

    # Build query parameters
    query = {
        'Action': DEFAULT_API,
        'Version': DEFAULT_API_VERSION,
        'X-Expires': str(expires),
        'DBUser': db_user,
        'InstanceId': instance_id,
    }

    # Create Request with presign mode
    request = Request(configuration,
                      resource_path='/{}/{}/{}/get/text_plain/'.format(DEFAULT_API, DEFAULT_API_VERSION,
                                                                       DEFAULT_SERVICE),
                      method='GET',
                      query_params=query)
    request.endpoint_provider = StandardEndpointResolver()
    request.service = DEFAULT_SERVICE
    request.is_presign = True

    context = InterceptorContext(request=request)

    # Step 1: Resolve endpoint to get host
    resolve_chain = InterceptorChain()
    resolve_chain.append_request_interceptor(ResolveEndpointInterceptor())
    context = resolve_chain.execute_request(context)

    # Step 2: Save resolved host to X-Host query param, then clear host so it won't be signed
    resolved_host = context.request.host
    context.request.query_params['X-HOST'] = '{scheme}://{host}'.format(
        scheme=context.request.scheme, host=resolved_host)
    context.request.host = None

    # Step 3: Sign request (host is None, won't be included in signature)
    sign_chain = InterceptorChain()
    sign_chain.append_request_interceptor(SignRequestInterceptor())
    context = sign_chain.execute_request(context)

    return context.request.signed_query
