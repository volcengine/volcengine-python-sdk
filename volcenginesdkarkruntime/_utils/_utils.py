from __future__ import annotations

import datetime
import functools
import random
import string
from typing import Mapping, cast, Any
from typing_extensions import TypeGuard

from .._types import NotGiven


def _gen_request_id():
    time_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    chars = string.ascii_letters + string.digits
    rand_str = "".join(random.choice(chars) for i in range(20))
    return f"{time_str}{rand_str}"


def is_mapping(obj: object) -> TypeGuard[Mapping[str, object]]:
    return isinstance(obj, Mapping)


def is_list(obj: object) -> TypeGuard[list[object]]:
    return isinstance(obj, list)


def coerce_boolean(val: str) -> bool:
    return val == "true" or val == "1" or val == "on"


def lru_cache(*, maxsize: int | None = 128) -> Callable[[CallableT], CallableT]:
    """A version of functools.lru_cache that retains the type signature
    for the wrapped function arguments.
    """
    wrapper = functools.lru_cache(  # noqa: TID251
        maxsize=maxsize,
    )
    return cast(Any, wrapper)  # type: ignore[no-any-return]


def strip_not_given(obj: object | None) -> object:
    """Remove all top-level keys where their values are instances of `NotGiven`"""
    if obj is None:
        return None

    if not is_mapping(obj):
        return obj

    return {key: value for key, value in obj.items() if not isinstance(value, NotGiven)}
