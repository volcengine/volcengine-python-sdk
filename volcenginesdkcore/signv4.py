# coding: utf-8

# Copy from https://github.com/volcengine/volc-sdk-python

import datetime
import hmac
import hashlib
from six.moves.urllib.parse import urlencode


class SignerV4(object):

    @staticmethod
    def sign(path, method, headers, body, query, ak, sk, region, service):
        if path == '':
            path = '/'
        if method != 'GET' and not ('Content-Type' in headers):
            headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=utf-8'
        format_date = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        headers['X-Date'] = format_date

        body_hash = hashlib.sha256(body.encode('utf-8')).hexdigest()
        headers['X-Content-Sha256'] = body_hash

        signed_headers = dict()
        for key in headers:
            if key in ['Content-Type', 'Content-Md5', 'Host'] or key.startswith('X-'):
                signed_headers[key.lower()] = headers[key]

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

        # The sorted() method sorts tuples by default, using the first item in each tuple.
        canonical_request = '\n'.join([method, path, urlencode(sorted(query)), signed_str, signed_headers_string, body_hash])
        credential_scope = '/'.join([format_date[:8], region, service, 'request'])
        signing_str = '\n'.join(['HMAC-SHA256', format_date, credential_scope,
                                 hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()])
        signing_key = SignerV4.get_signing_secret_key_v4(sk, format_date[:8], region, service)

        signature = hmac.new(signing_key, signing_str.encode('utf-8'), hashlib.sha256).hexdigest()

        credential = ak + '/' + credential_scope
        headers[
            'Authorization'] = 'HMAC-SHA256' + ' Credential=' + credential + ', SignedHeaders=' + \
                               signed_headers_string + ', Signature=' + signature
        return

    @staticmethod
    def get_signing_secret_key_v4(sk, date, region, service):
        kdate = SignerV4.hmac_sha256(sk.encode('utf-8'), date)
        kregion = SignerV4.hmac_sha256(kdate, region)
        kservice = SignerV4.hmac_sha256(kregion, service)
        return SignerV4.hmac_sha256(kservice, 'request')

    @staticmethod
    def hmac_sha256(key, msg):
        return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()
