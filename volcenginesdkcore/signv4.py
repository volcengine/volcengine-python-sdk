# coding: utf-8

import datetime
import hashlib
import hmac

from six.moves.urllib.parse import quote, urlencode
from volcenginesdkcore.observability.debugger import sdk_core_logger


class SignerV4(object):

    @staticmethod
    def sign(path, method, headers, body, post_params, query, ak, sk, region, service,
             session_token=None):
        if path == '':
            path = '/'
        if method != 'GET' and not ('Content-Type' in headers):
            headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=utf-8'
        format_date = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        headers['X-Date'] = format_date

        if (method == 'POST' and headers.get('Content-Type').startswith('application/x-www-form-urlencoded')
                and post_params):
            body = urlencode(post_params)
            sdk_core_logger.debug_sign("[sign] request body after urlencode: %s", body)

        body_hash = hashlib.sha256(body.encode('utf-8')).hexdigest()
        headers['X-Content-Sha256'] = body_hash
        sdk_core_logger.debug_sign("calculated body sha256: %s", body_hash)
        if session_token:
            headers['X-Security-Token'] = session_token

        signed_headers = dict()
        for key in headers:
            if key in ['Content-Type', 'Content-Md5', 'Host'] or key.startswith('X-'):
                signed_headers[key.lower()] = headers[key]
        sdk_core_logger.debug_sign("signed headers: %s", signed_headers)

        if 'host' in signed_headers:
            v = signed_headers['host']
            if v.find(':') != -1:
                split = v.split(':')
                port = split[1]
                if str(port) == '80' or str(port) == '443':
                    signed_headers['host'] = split[0]

        signed_str = ''
        for key in sorted(signed_headers.keys()):
            signed_str += key + ':' + signed_headers[key] + '\n'

        signed_headers_string = ';'.join(sorted(signed_headers.keys()))

        canonical_request = '\n'.join(
            [method, path, SignerV4.canonical_query(dict(query)), signed_str, signed_headers_string, body_hash])
        sdk_core_logger.debug_sign("canonical_request:\n%s", canonical_request)
        credential_scope = '/'.join([format_date[:8], region, service, 'request'])
        signing_str = '\n'.join(['HMAC-SHA256', format_date, credential_scope,
                                 hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()])
        sdk_core_logger.debug_sign("string_to_sign:\n%s", signing_str)
        signing_key = SignerV4.get_signing_secret_key_v4(sk, format_date[:8], region, service)

        signature = hmac.new(signing_key, signing_str.encode('utf-8'), hashlib.sha256).hexdigest()
        sdk_core_logger.debug_sign("calculated signature: %s", signature)

        credential = ak + '/' + credential_scope
        headers[
            'Authorization'] = 'HMAC-SHA256' + ' Credential=' + credential + ', SignedHeaders=' + \
                               signed_headers_string + ', Signature=' + signature
        sdk_core_logger.debug_sign("final Authorization header: %s", headers['Authorization'])
        return

    @staticmethod
    def canonical_query(query):
        res = []
        for key in query:
            value = str(query[key])
            res.append((quote(key, safe='-_.~'), quote(value, safe='-_.~')))
        sorted_key_vals = []
        for key, value in sorted(res):
            sorted_key_vals.append('%s=%s' % (key, value))
        return '&'.join(sorted_key_vals)

    @staticmethod
    def get_signing_secret_key_v4(sk, date, region, service):
        kdate = SignerV4.hmac_sha256(sk.encode('utf-8'), date)
        kregion = SignerV4.hmac_sha256(kdate, region)
        kservice = SignerV4.hmac_sha256(kregion, service)
        return SignerV4.hmac_sha256(kservice, 'request')

    @staticmethod
    def hmac_sha256(key, msg):
        return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

    @staticmethod
    def sign_url(path, method, query, ak, sk, region, service, session_token=None, host=None):
        """
        Generate presigned URL query string (AWS Signature V4)

        :param path: Request path
        :param method: HTTP method (GET, POST, etc.)
        :param query: Query parameters dict
        :param ak: Access Key
        :param sk: Secret Key
        :param region: Service region
        :param service: Service name
        :param session_token: Optional session token
        :param host: Optional host header to sign
        :return: Query string with signature
        """
        format_date = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        date = format_date[:8]

        # Build credential scope
        credential_scope = '/'.join([date, region, service, 'request'])

        # Determine if host header should be signed
        sign_host = host is not None and host != ''

        # Add required query parameters
        query = dict(query)  # Make a copy to avoid modifying original
        query['X-Date'] = format_date
        query['X-NotSignBody'] = ''
        query['X-Credential'] = ak + '/' + credential_scope
        query['X-Algorithm'] = 'HMAC-SHA256'
        query['X-SignedHeaders'] = 'host' if sign_host else ''
        query['X-SignedQueries'] = ''

        # Generate X-SignedQueries BEFORE adding X-Security-Token
        query['X-SignedQueries'] = ';'.join(sorted(query.keys()))
        signed_query_keys = set(query.keys())

        # X-Security-Token must be added AFTER X-SignedQueries calculation
        if session_token:
            query['X-Security-Token'] = session_token

        # Build canonical request
        body_hash = hashlib.sha256(b'').hexdigest()
        canonical_query_params = {k: v for k, v in query.items() if k in signed_query_keys}

        if sign_host:
            canonical_request = '\n'.join([
                method,
                path,
                SignerV4.canonical_query(canonical_query_params),
                'host:' + host + '\n',
                'host',
                body_hash
            ])
        else:
            canonical_request = '\n'.join([
                method,
                path,
                SignerV4.canonical_query(canonical_query_params),
                '\n',
                '',
                body_hash
            ])
        sdk_core_logger.debug_sign("[sign_url] canonical_request:\n%s", canonical_request)

        # Build string to sign
        signing_str = '\n'.join([
            'HMAC-SHA256',
            format_date,
            credential_scope,
            hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()
        ])
        sdk_core_logger.debug_sign("[sign_url] string_to_sign:\n%s", signing_str)

        # Calculate signature
        signing_key = SignerV4.get_signing_secret_key_v4(sk, date, region, service)
        signature = hmac.new(signing_key, signing_str.encode('utf-8'), hashlib.sha256).hexdigest()
        sdk_core_logger.debug_sign("[sign_url] calculated signature: %s", signature)

        # Add signature to query
        query['X-Signature'] = signature

        # Return encoded query string
        return urlencode(sorted(query.items()))
