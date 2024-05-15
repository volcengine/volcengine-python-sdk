from __future__ import annotations

from typing import Dict, Union, Any, TYPE_CHECKING, cast

import pydantic
from httpx import Timeout
from typing_extensions import Unpack, TypedDict, ClassVar

from ._compat import PYDANTIC_V2, ConfigDict
from ._models import BaseModel

__all__ = ["ExtraRequestOptions", "RequestOptions"]

from ._types import NotGiven, NOT_GIVEN
from ._utils._utils import strip_not_given


class ExtraRequestOptions(TypedDict, total=False):
    headers: Dict[str, str]
    max_retries: int
    timeout: Union[float, Timeout]
    params: Dict[str, Any]
    extra_body: Dict[str, Any]


class RequestOptions(BaseModel):
    method: str
    url: str
    headers: Union[Dict[str, str], NotGiven] = NOT_GIVEN
    body: Union[object, None] = {}
    max_retries: Union[int, NotGiven] = NOT_GIVEN
    timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN
    params: Dict[str, object] = {}
    extra_body: Dict[str, object] = {}

    if PYDANTIC_V2:
        model_config: ClassVar[ConfigDict] = ConfigDict(arbitrary_types_allowed=True)
    else:

        class Config(pydantic.BaseConfig):  # pyright: ignore[reportDeprecated]
            arbitrary_types_allowed: bool = True

    def get_max_retries(self, max_retries: int) -> int:
        if isinstance(self.max_retries, NotGiven):
            return max_retries
        return self.max_retries

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
        return cast(
            RequestOptions, super().construct(_fields_set, **kwargs)
        )  # pyright: ignore[reportDeprecated]

    if not TYPE_CHECKING:
        # type checkers incorrectly complain about this assignment
        model_construct = construct
