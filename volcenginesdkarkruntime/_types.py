from __future__ import annotations

from typing import (
    Any,
    Dict,
    List,
    Union,
    TypeVar,
)

import pydantic
from httpx import Response
from typing_extensions import override

ModelT = TypeVar("ModelT", bound=pydantic.BaseModel)

ResponseT = TypeVar(
    "ResponseT",
    bound=Union[
        object,
        str,
        None,
        "BaseModel",
        List[Any],
        Dict[str, Any],
        Response,
        "APIResponse[Any]",
        "AsyncAPIResponse[Any]",
        "HttpxBinaryResponseContent",
    ],
)


class NotGiven:
    """
    A sentinel singleton class used to distinguish omitted keyword arguments
    from those passed in with the value None (which may have different behavior).

    For example:

    ```py
    def get(timeout: Union[int, NotGiven, None] = NotGiven()) -> Response:
        ...


    get(timeout=1)  # 1s timeout
    get(timeout=None)  # No timeout
    get()  # Default timeout behavior, which may not be statically known at the method definition.
    ```
    """

    def __bool__(self) -> Literal[False]:
        return False

    @override
    def __repr__(self) -> str:
        return "NOT_GIVEN"


NOT_GIVEN = NotGiven()
