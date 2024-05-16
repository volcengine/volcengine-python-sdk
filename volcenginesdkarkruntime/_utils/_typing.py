from __future__ import annotations

from typing import cast
from typing_extensions import Required, get_args, get_origin, Annotated


def extract_type_arg(typ: type, index: int = 0) -> type:
    args = get_args(typ)
    try:
        return cast(type, args[index])
    except IndexError as err:
        raise RuntimeError(
            f"Expected type {typ} to have a type argument at index {index} but it did not"
        ) from err


def is_annotated_type(typ: type) -> bool:
    return get_origin(typ) == Annotated


# Extracts T from Annotated[T, ...] or from Required[Annotated[T, ...]]
def strip_annotated_type(typ: type) -> type:
    if is_required_type(typ) or is_annotated_type(typ):
        return strip_annotated_type(cast(type, get_args(typ)[0]))

    return typ


def is_required_type(typ: type) -> bool:
    return get_origin(typ) == Required
