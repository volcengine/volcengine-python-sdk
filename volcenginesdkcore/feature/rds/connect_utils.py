# coding: utf-8
"""
RDS MySQL connection authentication utilities.

This module provides utilities for generating authentication tokens for RDS MySQL database connections.
"""

from volcenginesdkcore.signv4 import SignerV4
from volcenginesdkcore.endpoint.providers.default_provider import DefaultEndpointProvider


def build_auth_token(credentials, db_user, instance_id, region, expires=None):
    """
    Build an authentication token (presigned URL) for connecting to RDS MySQL database.

    :param credentials: CredentialValue object with ak, sk, and optional session_token
    :param db_user: Database username
    :param instance_id: RDS instance ID
    :param region: Service region (e.g., 'cn-beijing')
    :param expires: Token expiration time in seconds (default: 900, i.e., 15 minutes)
    :return: Presigned URL string for database authentication
    :raises ValueError: If required parameters are missing or invalid
    """
    # Validate inputs
    if credentials is None:
        raise ValueError("credentials must not be None")

    if not hasattr(credentials, 'ak') or not credentials.ak:
        raise ValueError("credentials.ak must not be empty")

    if not hasattr(credentials, 'sk') or not credentials.sk:
        raise ValueError("credentials.sk must not be empty")

    if not db_user:
        raise ValueError("db_user must not be empty")

    if not instance_id:
        raise ValueError("instance_id must not be empty")

    if not region:
        raise ValueError("region must not be empty")

    # Set default expiration time
    if expires is None or expires <= 0:
        expires = 900  # 15 minutes

    # Service configuration
    service = 'rds_mysql'

    # Get endpoint
    endpoint_provider = DefaultEndpointProvider()
    resolved_endpoint = endpoint_provider.endpoint_for(service, region)
    host = resolved_endpoint.host

    # Build query parameters
    query = {
        'Action': 'ConnectDatabase',
        'Version': '2022-01-01',
        'X-Expires': str(expires),
        'DBUser': db_user,
        'InstanceId': instance_id,
    }

    # Sign the URL
    signed_query = SignerV4.sign_url(
        path='/',
        method='GET',
        query=query,
        ak=credentials.ak,
        sk=credentials.sk,
        region=region,
        service=service,
        session_token=getattr(credentials, 'session_token', None)
    )

    return signed_query
