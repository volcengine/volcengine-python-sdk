# coding=utf-8
import datetime
import json
import mimetypes
import os

import six
from six.moves.urllib.parse import quote

from volcenginesdkcore.signv4 import SignerV4
from .interceptor import Interceptor


class SignRequestInterceptor(Interceptor):
    """SDK通用请求拦截器"""

    def name(self):
        return 'volcengine-sign-request-interceptor'

    def intercept(self, context):
        self.update_params_for_auth(host=context.request.host, path=context.request.true_path,
                                    method=context.request.method,
                                    headers=context.request.header_params,
                                    querys=context.request.query_params,
                                    auth_settings=context.request.auth_settings,
                                    body=context.request.body,
                                    post_params=context.request.post_params,
                                    service=context.request.service,
                                    ak=context.request.ak,
                                    sk=context.request.sk,
                                    session_token=context.request.session_token,
                                    region=context.request.region)
        return context

    def is_common(self):
        return True

    def is_request(self):
        return True

    def is_response(self):
        return False

    def update_params_for_auth(self, host, path, method, headers, querys, auth_settings, body, post_params, service, ak,
                               sk, session_token, region):
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        """
        if not auth_settings:
            return

        for auth in auth_settings:
            headers["Host"] = host
            if method in ["POST", "PUT", "DELETE", "PATCH"]:
                body = json.dumps(body)
            else:
                body = ""
            SignerV4.sign(path, method, headers, body, post_params, querys,
                          ak, sk, session_token,
                          region, service)


PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types


def parameters_to_tuples(params, collection_formats):
    """Get parameters as list of tuples, formatting collections.

    :param params: Parameters as dict or list of two-tuples
    :param dict collection_formats: Parameter collection formats
    :return: Parameters as list of tuples, collections formatted
    """
    new_params = []
    if collection_formats is None:
        collection_formats = {}
    for k, v in six.iteritems(params) if isinstance(params, dict) else params:  # noqa: E501
        if k in collection_formats:
            collection_format = collection_formats[k]
            if collection_format == 'multi':
                new_params.extend((k, value) for value in v)
            else:
                if collection_format == 'ssv':
                    delimiter = ' '
                elif collection_format == 'tsv':
                    delimiter = '\t'
                elif collection_format == 'pipes':
                    delimiter = '|'
                else:  # csv is the default
                    delimiter = ','
                new_params.append(
                    (k, delimiter.join(str(value) for value in v)))
        else:
            new_params.append((k, v))
    return new_params


def prepare_post_parameters(post_params=None, files=None):
    """Builds form parameters.

    :param post_params: Normal form parameters.
    :param files: File parameters.
    :return: Form parameters with files.
    """
    params = []

    if post_params:
        params = post_params

    if files:
        for k, v in six.iteritems(files):
            if not v:
                continue
            file_names = v if type(v) is list else [v]
            for n in file_names:
                with open(n, 'rb') as f:
                    filename = os.path.basename(f.name)
                    filedata = f.read()
                    mimetype = (mimetypes.guess_type(filename)[0] or
                                'application/octet-stream')
                    params.append(
                        tuple([k, tuple([filename, filedata, mimetype])]))

    return params


def sanitize_for_serialization(obj):
    """Builds a JSON POST object.

    If obj is None, return None.
    If obj is str, int, long, float, bool, return directly.
    If obj is datetime.datetime, datetime.date
        convert to string in iso8601 format.
    If obj is list, sanitize each element in the list.
    If obj is dict, return the dict.
    If obj is swagger model, return the properties dict.

    :param obj: The data to serialize.
    :return: The serialized form of data.
    """
    if obj is None:
        return None
    elif isinstance(obj, PRIMITIVE_TYPES):
        return obj
    elif isinstance(obj, list):
        return [sanitize_for_serialization(sub_obj)
                for sub_obj in obj]
    elif isinstance(obj, tuple):
        return tuple(sanitize_for_serialization(sub_obj)
                     for sub_obj in obj)
    elif isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()

    if isinstance(obj, dict):
        obj_dict = obj
    else:
        # Convert model obj to dict except
        # attributes `swagger_types`, `attribute_map`
        # and attributes which value is not None.
        # Convert attribute name to json key in
        # model definition for request.
        obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
                    for attr, _ in six.iteritems(obj.swagger_types)
                    if getattr(obj, attr) is not None}

    return {key: sanitize_for_serialization(val)
            for key, val in six.iteritems(obj_dict)}


class BuildRequestInterceptor(Interceptor):
    """SDK通用请求拦截器"""

    def name(self):
        return 'volcengine-build-request-interceptor'

    def intercept(self, context):

        # 从上下文中获取请求参数
        # header parameters
        if context.request.header_params:
            context.request.header_params = sanitize_for_serialization(context.request.header_params)
            context.request.header_params = dict(parameters_to_tuples(context.request.header_params,
                                                                      context.request.collection_formats))

        # path parameters
        if context.request.path_params:
            context.request.path_params = sanitize_for_serialization(context.request.path_params)
            context.request.path_params = parameters_to_tuples(context.request.path_params,
                                                               context.request.collection_formats)
            for k, v in context.request.path_params:
                # specified safe chars, encode everything
                context.request.resource_path = context.request.resource_path.replace(
                    '{%s}' % k,
                    quote(str(v), safe='')
                )

        # request module name
        context.request.md = ""

        # body
        if context.request.body:
            if type(context.request.body) is not dict:
                context.request.md = context.request.body.__module__.split(".")[0]
            context.request.body = sanitize_for_serialization(context.request.body)

        # query parameters
        method = context.request.method
        if method == "GET" and context.request.header_params.get("Content-Type") == "text/plain":
            context.request.query_params = self.__req_to_params(context.request.body)

        context.request.query_params.append(("Action", context.request.resource_path.split("/")[1]))
        context.request.query_params.append(("Version", context.request.resource_path.split("/")[2]))

        if context.request.query_params:
            context.request.query_params = sanitize_for_serialization(context.request.query_params)
            context.request.query_params = parameters_to_tuples(context.request.query_params,
                                                                context.request.collection_formats)

        if method == 'POST' and context.request.header_params.get('Content-Type').startswith(
                'application/x-www-form-urlencoded'):
            context.request.post_params = self.__req_to_params(context.request.body)
            context.request.body = None

        # post_params
        if context.request.post_params or context.request.files:
            context.request.post_params = prepare_post_parameters(context.request.post_params,
                                                                  context.request.files)
            context.request.post_params = sanitize_for_serialization(context.request.post_params)
            context.request.post_params = parameters_to_tuples(context.request.post_params,
                                                               context.request.collection_formats)

        context.request.true_path = "/"
        context.request.service = context.request.resource_path.split("/")[3]

        return context

    def is_common(self):
        return True

    def is_request(self):
        return True

    def is_response(self):
        return False

    def __req_to_params(self, req, prefix="", params=None):
        if params is None:
            params = []

        for key, value in req.items():
            if value is None:
                continue
            if isinstance(value, list):
                for index in range(len(value)):
                    if isinstance(value[index], dict):
                        self.__req_to_params(value[index], prefix + key + "." + str((index + 1)) + ".", params)
                    else:
                        params.append((prefix + key + "." + str((index + 1)), value[index]))
            elif isinstance(value, dict):
                self.__req_to_params(value, prefix + key + ".", params)
            else:
                params.append((prefix + key, value))

        return params


class ResolveEndpointInterceptor(Interceptor):
    """SDK通用请求拦截器"""

    def name(self):
        return 'volcengine-resolve-endpoint-interceptor'

    def intercept(self, context):
        host = context.request.host
        scheme = context.request.scheme
        if not host:
            service = context.request.resource_path.split('/')[3]
            context.request.endpoint_provider.scheme = scheme
            endpoint_resolver = context.request.endpoint_provider.endpoint_for(
                service, context.request.region)
            host = endpoint_resolver.host
            context.request.host = host
            prefix = endpoint_resolver.full_url
        else:
            prefix = scheme + '://' + host
        context.request.url = prefix + context.request.true_path

        return context

    def is_common(self):
        return True

    def is_request(self):
        return True

    def is_response(self):
        return False


class RuntimeOptionsInterceptor(Interceptor):
    """SDK通用请求拦截器"""

    def name(self):
        return 'volcengine-runtime-options-interceptor'

    def intercept(self, context):
        opt = context.request.runtime_options
        if not opt:
            return context

        context.request.ak = opt.ak if opt.ak is not None else context.request.ak
        context.request.sk = opt.sk if opt.sk is not None else context.request.sk
        context.request.session_token = opt.session_token \
            if opt.session_token is not None else context.request.session_token
        context.request.region = opt.region if opt.region is not None else context.request.region
        context.request.scheme = opt.scheme if opt.scheme is not None else context.request.scheme
        context.request.endpoint_provider = opt.endpoint_provider \
            if opt.endpoint_provider is not None else context.request.endpoint_provider
        context.request.request_timeout = opt.timeout if opt.timeout is not None else context.request.request_timeout

        return context

    def is_common(self):
        return True

    def is_request(self):
        return True

    def is_response(self):
        return False
