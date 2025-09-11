# coding=utf-8

from urllib3 import Timeout

from .interceptor import RequestInterceptor


class RuntimeOptionsInterceptor(RequestInterceptor):

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

        if opt.connect_timeout is not None or opt.read_timeout is not None:
            context.request.request_timeout = Timeout(
                connect=opt.connect_timeout if opt.connect_timeout is not None else -1,
                read=opt.read_timeout if opt.read_timeout is not None else -1,
            )

        if opt.endpoint_provider is not None:
            context.request.endpoint_provider = opt.endpoint_provider
            context.request.host = None

        # retryer arguments set
        RuntimeOptionsInterceptor.__update_retryer(context, opt)
        return context

    @staticmethod
    def __update_retryer(context, opt):
        min_retry_delay_ms = opt.min_retry_delay_ms \
            if opt.min_retry_delay_ms is not None else context.request.retryer.backoff_strategy.min_retry_delay_ms
        max_retry_delay_ms = opt.max_retry_delay_ms \
            if opt.max_retry_delay_ms is not None else context.request.retryer.backoff_strategy.max_retry_delay_ms
        retry_error_codes = opt.retry_error_codes \
            if opt.retry_error_codes is not None else context.request.retryer.retry_condition.retry_error_codes
        context.request.auto_retry = opt.auto_retry if opt.auto_retry is not None else context.request.auto_retry
        context.request.retryer.num_max_retries = opt.num_max_retries \
            if opt.num_max_retries is not None else context.request.retryer.num_max_retries
        context.request.retryer.backoff_strategy = opt.backoff_strategy \
            if opt.backoff_strategy is not None else context.request.retryer.backoff_strategy
        context.request.retryer.backoff_strategy.min_retry_delay_ms = min_retry_delay_ms
        context.request.retryer.backoff_strategy.max_retry_delay_ms = max_retry_delay_ms
        context.request.retryer.retry_condition = opt.retry_condition \
            if opt.retry_condition is not None else context.request.retryer.retry_condition
        context.request.retryer.retry_condition.retry_error_codes = retry_error_codes
