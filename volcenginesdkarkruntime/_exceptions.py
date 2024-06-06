# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast, Dict
from typing_extensions import Literal

import httpx

__all__ = [
    "ArkBadRequestError",
    "ArkAuthenticationError",
    "ArkPermissionDeniedError",
    "ArkNotFoundError",
    "ArkConflictError",
    "ArkUnprocessableEntityError",
    "ArkRateLimitError",
    "ArkInternalServerError",
]


class ArkError(Exception):
    pass


class ArkAPIError(ArkError):
    message: str
    request: Optional[httpx.Request] = None
    body: Optional[object] = None
    request_id: Optional[str] = None
    """The API response body.

    If the API responded with a valid JSON structure then this property will be the
    decoded result.

    If it isn't a valid JSON structure then this will be the raw response.

    If there was no response associated with this error then it will be `None`.
    """

    code: Optional[str] = None
    param: Optional[str] = None
    type: Optional[str]

    def __init__(
        self,
        message: str,
        request: Optional[httpx.Request] = None,
        *,
        body: Optional[object] = None,
        request_id: Optional[str] = None,
    ) -> None:
        super().__init__(message)
        self.request = request
        self.message = message
        self.body = body
        self.request_id = request_id

        if isinstance(body, dict):
            self.code = body.get("code")
            self.param = body.get("param")
            self.type = body.get("type")
        else:
            self.code = None
            self.param = None
            self.type = None

    def __str__(self):
        return f"{self.message}, request_id: {self.request_id}"


class ArkAPIResponseValidationError(ArkAPIError):
    response: httpx.Response
    status_code: int

    def __init__(
        self,
        response: httpx.Response,
        body: object | None,
        *,
        message: str | None = None,
        request_id: str,
    ) -> None:
        super().__init__(
            message or "Data returned by API invalid for expected schema.",
            response.request,
            body=body,
        )
        self.response = response
        self.status_code = response.status_code
        self.request_id = request_id


class ArkAPIStatusError(ArkAPIError):
    """Raised when an API response has a status code of 4xx or 5xx."""

    response: httpx.Response
    status_code: int

    def __init__(
        self,
        message: str,
        *,
        response: httpx.Response,
        body: object | None,
        request_id: str,
    ) -> None:
        super().__init__(message, response.request, body=body, request_id=request_id)
        self.response = response
        self.status_code = response.status_code
        self.request_id = request_id


class ArkAPIConnectionError(ArkAPIError):
    def __init__(
        self,
        *,
        message: str = "Connection error.",
        request: httpx.Request,
        request_id: str,
    ) -> None:
        super().__init__(message, request, body=None, request_id=request_id)


class ArkAPITimeoutError(ArkAPIConnectionError):
    def __init__(self, request: httpx.Request, request_id: str) -> None:
        super().__init__(
            message="Request timed out.", request=request, request_id=request_id
        )


class ArkBadRequestError(ArkAPIStatusError):
    status_code: Literal[400] = (
        400  # pyright: ignore[reportIncompatibleVariableOverride]
    )


class ArkAuthenticationError(ArkAPIStatusError):
    status_code: Literal[401] = (
        401  # pyright: ignore[reportIncompatibleVariableOverride]
    )


class ArkPermissionDeniedError(ArkAPIStatusError):
    status_code: Literal[403] = (
        403  # pyright: ignore[reportIncompatibleVariableOverride]
    )


class ArkNotFoundError(ArkAPIStatusError):
    status_code: Literal[404] = (
        404  # pyright: ignore[reportIncompatibleVariableOverride]
    )


class ArkConflictError(ArkAPIStatusError):
    status_code: Literal[409] = (
        409  # pyright: ignore[reportIncompatibleVariableOverride]
    )


class ArkUnprocessableEntityError(ArkAPIStatusError):
    status_code: Literal[422] = (
        422  # pyright: ignore[reportIncompatibleVariableOverride]
    )


class ArkRateLimitError(ArkAPIStatusError):
    status_code: Literal[429] = (
        429  # pyright: ignore[reportIncompatibleVariableOverride]
    )


class ArkInternalServerError(ArkAPIStatusError):
    pass
