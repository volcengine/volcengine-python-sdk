from __future__ import annotations

from typing import Union, Any, TYPE_CHECKING, cast

import pydantic
from httpx import Timeout
from typing_extensions import Unpack, TypedDict, ClassVar

from ._compat import PYDANTIC_V2, ConfigDict
from ._models import BaseModel

__all__ = ["ExtraRequestOptions", "RequestOptions"]

from ._types import NotGiven

from typing import (
    Callable,
)
from typing_extensions import (
    Required,
)


from ._types import (
    Body,
    Query,
    Headers,
    AnyMapping,
    HttpxRequestFiles,
)
from ._utils import (
    is_given,
    strip_not_given,
)
from ._constants import RAW_RESPONSE_HEADER

if TYPE_CHECKING:
    pass


class ExtraRequestOptions(TypedDict, total=False):
    method: Required[str]
    url: Required[str]
    params: Query
    headers: Headers
    max_retries: int
    timeout: float | Timeout | None
    files: HttpxRequestFiles | None
    idempotency_key: str
    json_data: Body
    extra_body: AnyMapping


class RequestOptions(BaseModel):
    method: str
    url: str
    body: Union[object, None] = {}
    params: Query = {}
    headers: Union[Headers, NotGiven] = NotGiven()
    max_retries: Union[int, NotGiven] = NotGiven()
    timeout: Union[float, Timeout, None, NotGiven] = NotGiven()
    files: Union[HttpxRequestFiles, None] = None
    idempotency_key: Union[str, None] = None
    post_parser: Union[Callable[[Any], Any], NotGiven] = NotGiven()

    # It should be noted that we cannot use `json` here as that would override
    # a BaseModel method in an incompatible fashion.
    json_data: Union[Body, None] = None
    extra_body: Union[AnyMapping, None] = None

    if PYDANTIC_V2:
        model_config: ClassVar[ConfigDict] = ConfigDict(arbitrary_types_allowed=True)
    else:

        class Config(pydantic.BaseConfig):  # pyright: ignore[reportDeprecated]
            arbitrary_types_allowed: bool = True

    def get_max_retries(self, max_retries: int) -> int:
        if isinstance(self.max_retries, NotGiven):
            return max_retries
        return self.max_retries

    def _strip_raw_response_header(self) -> None:
        if not is_given(self.headers):
            return

        if self.headers.get(RAW_RESPONSE_HEADER):
            self.headers = {**self.headers}
            self.headers.pop(RAW_RESPONSE_HEADER)

    # override the `construct` method so that we can run custom transformations.
    # this is necessary as we don't want to do any actual runtime type checking
    # (which means we can't use validators) but we do want to ensure that `NotGiven`
    # values are not present
    #
    # type ignore required because we're adding explicit types to `**values`
    @classmethod
    def construct(  # type: ignore
        cls,
        _fields_set: set[str] | None = None,
        **values: Unpack[ExtraRequestOptions],
    ) -> RequestOptions:
        kwargs: dict[str, Any] = {
            # we unconditionally call `strip_not_given` on any value
            # as it will just ignore any non-mapping types
            key: strip_not_given(value)
            for key, value in values.items()
        }
        if PYDANTIC_V2:
            return super().model_construct(_fields_set, **kwargs)
        return cast(RequestOptions, super().construct(_fields_set, **kwargs))  # pyright: ignore[reportDeprecated]

    if not TYPE_CHECKING:
        # type checkers incorrectly complain about this assignment
        model_construct = construct
