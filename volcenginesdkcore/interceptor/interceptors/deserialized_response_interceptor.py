# coding=utf-8
import datetime
import json
import os
import re
import sys
import tempfile

import six

from volcenginesdkcore import rest
from volcenginesdkcore.metadata import (
    ResponseMetadata,
    ensure_response_metadata,
    get_response_metadata,
)
from .interceptor import ResponseInterceptor


class DeserializedResponseInterceptor(ResponseInterceptor):

    def name(self):
        return 'volcengine-deserialized-response-interceptor'

    def intercept(self, context):
        if getattr(context, "_deserialized_response_interceptor", None) is self:
            return context
        if context.request.preload_content:
            # deserialize response data
            if context.request.response_type:
                dresponse = self.deserialize(context.response.http_response, context.request.response_type,
                                             context.request.md)
                context.response.result = dresponse
                if hasattr(dresponse, "_metadata"):
                    context.response.metadata = dresponse._metadata
            else:
                context.result = None

        return context

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,  # noqa: F821
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def deserialize(self, response, response_type, service):
        try:
            return self._deserialize_response(response, response_type, service)
        except rest.ApiException as api_error:
            if (api_error.status == response.status and
                    api_error.body == response.data):
                raise
            cause = api_error.cause if api_error.cause is not None else api_error
            raise rest.ApiException(
                status=response.status, reason=api_error.reason, body=response.data,
                headers=response.getheaders(), cause=cause,
                previous_exception=api_error,
                code="SerializationError",
                response_details=rest.RESTClientObject._snapshot(response, response.data, True))
        except Exception as error:
            raise rest.ApiException(
                status=response.status,
                reason="Failed to deserialize response: {0}".format(error),
                body=response.data, headers=response.getheaders(), cause=error,
                code="SerializationError",
                response_details=rest.RESTClientObject._snapshot(response, response.data, True))

    def _deserialize_response(self, response, response_type, service):
        """Deserializes response into an object.

        :param service: the target service
        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        """
        # handle file downloading
        # save response body into a tmp file and return the instance
        if response_type == "file":
            return self.__deserialize_file(response)

        headers = response.getheaders() if hasattr(response, "getheaders") else None

        # fetch data from response object
        try:
            data = json.loads(response.data)
        except (ValueError, TypeError) as e:
            raise rest.ApiException(
                status=response.status, reason=response.reason,
                body=response.data, headers=headers, cause=e, code="SerializationError",
                response_details=rest.RESTClientObject._snapshot(response, response.data, True))

        # Non-standard response: the body is not a JSON object (e.g. a 504
        # gateway returning HTML/plain text, which previously decayed to a str
        # and raised AttributeError on data.get(...), escaping the caller's
        # except). Wrap it into an ApiException carrying the real HTTP status,
        # the raw body and a request id resolved from the response headers.
        if not isinstance(data, dict):
            raise rest.ApiException(
                status=response.status,
                reason=response.reason,
                body=response.data,
                headers=headers,
                response_metadata=ensure_response_metadata(None, headers),
                response_details=rest.RESTClientObject._snapshot(response, response.data, True))

        meta = data.get("ResponseMetadata")
        if meta is not None and not isinstance(meta, dict):
            raise rest.ApiException(
                status=response.status, reason="ResponseMetadata must be a JSON object",
                body=response.data, headers=headers, code="SerializationError",
                response_details=rest.RESTClientObject._snapshot(response, response.data, True))
        from volcenginesdkcore.error_details import classify_top
        code, message = classify_top(response.data)
        if code == "SerializationError":
            error = ValueError(message)
            raise rest.ApiException(
                status=response.status, reason=message, body=response.data,
                headers=headers, cause=error, code=code,
                response_details=rest.RESTClientObject._snapshot(response, response.data, True))
        if meta is not None:
            err = meta.get("Error")
            if err is not None:
                # Business error: keep the structured ResponseMetadata (request
                # id, service, ...) on the exception so the caller can report it.
                raise rest.ApiException(
                    status=response.status,
                    reason=str(err),
                    body=response.data,
                    headers=headers,
                    response_metadata=ensure_response_metadata(
                        get_response_metadata(data), headers),
                    response_details=rest.RESTClientObject._snapshot(response, response.data, True))
            else:
                data = data.get("Result")
        else:
            # Non-standard JSON without a TOP ResponseMetadata: surface the real
            # status code, raw body and a header-resolved request id instead of
            # the previous hard-coded status=200/InternalServiceError.
            raise rest.ApiException(
                status=response.status,
                reason="InternalServiceError",
                body=response.data,
                headers=headers,
                response_metadata=ensure_response_metadata(None, headers),
                response_details=rest.RESTClientObject._snapshot(response, response.data, True))

        resp_model = self.__deserialize(data, response_type, service)
        if (resp_model is None) or (type(resp_model) is dict):
            return resp_model

        # UniversalClient 直接返回
        if response_type == object:
            return resp_model

        # patch response metadata for resp_model
        resp_model._metadata = ResponseMetadata(
            service=meta.get("Service"),
            action=meta.get("Action"),
            version=meta.get("Version"),
            region=meta.get("Region"),
            request_id=meta.get("RequestId")
        )
        resp_model.metadata = metadata.__get__(resp_model)
        return resp_model

    def __deserialize_file(self, response):
        """Deserializes body to file

        Saves response body into a file in a temporary folder,
        retaining a short, safe extension from `Content-Disposition`.

        :param response:  RESTResponse.
        :return: file path.
        """
        suffix = ""
        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            match = re.search(r'filename\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^;\s]+))',
                              content_disposition, re.IGNORECASE)
            if match:
                filename = next(value for value in match.groups() if value is not None)
                filename = os.path.basename(filename.replace("\\", "/"))
                extension = os.path.splitext(filename)[1]
                # Reserve space for tempfile's prefix/random name and avoid
                # filesystem byte-length limits and Windows special names.
                if re.match(r"^\.[A-Za-z0-9]{1,16}\Z", extension):
                    suffix = extension
        fd, path = tempfile.mkstemp(suffix=suffix)
        try:
            data = response.data
            if isinstance(data, six.text_type):
                data = data.encode("utf-8")
            with os.fdopen(fd, "wb") as f:
                fd = None
                f.write(data)
            return path
        except BaseException:
            if fd is not None:
                try:
                    os.close(fd)
                except OSError:
                    pass
            try:
                os.remove(path)
            except OSError:
                pass
            raise

    def __deserialize(self, data, klass, service):
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if type(klass) == str:
            if klass.startswith('list['):
                sub_kls = re.match(r'list\[(.*)]', klass).group(1)
                return [self.__deserialize(sub_data, sub_kls, service)
                        for sub_data in data]

            if klass.startswith('dict('):
                sub_kls = re.match(r'dict\(([^,]*), (.*)\)', klass).group(2)
                return {k: self.__deserialize(v, sub_kls, service)
                        for k, v in six.iteritems(data)}

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(sys.modules[service + ".models"], klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datatime(data)
        else:
            return self.__deserialize_model(data, klass, service)

    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            return six.text_type(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return a original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            from dateutil.parser import parse
            return parse(string).date()
        except ImportError:
            return string
        except ValueError as e:
            raise rest.ApiException(
                status=0,
                reason="Failed to parse `{0}` as date object".format(string),
                cause=e
            )

    def __deserialize_datatime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string
        except ValueError as e:
            raise rest.ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as datetime object"
                    .format(string)
                ),
                cause=e
            )

    def __hasattr(self, object, name):
        return name in object.__class__.__dict__

    def __deserialize_model(self, data, klass, service):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """

        if (not klass.swagger_types and
                not self.__hasattr(klass, 'get_real_child_model')):
            return data

        kwargs = {}
        if klass.swagger_types is not None:
            for attr, attr_type in six.iteritems(klass.swagger_types):
                if (data is not None and
                        klass.attribute_map[attr] in data and
                        isinstance(data, (list, dict))):
                    value = data[klass.attribute_map[attr]]
                    kwargs[attr] = self.__deserialize(value, attr_type, service)
        instance = klass(**kwargs)

        if (isinstance(instance, dict) and
                klass.swagger_types is not None and
                isinstance(data, dict)):
            for key, value in data.items():
                if key not in klass.swagger_types:
                    instance[key] = value
        if self.__hasattr(instance, 'get_real_child_model'):
            klass_name = instance.get_real_child_model(data)
            if klass_name:
                instance = self.__deserialize(data, klass_name, service)
        return instance


def metadata(self):
    return self._metadata
