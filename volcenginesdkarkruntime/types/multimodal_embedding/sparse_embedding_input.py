from typing_extensions import Literal, Required, TypedDict

__all__ = ["SparseEmbeddingInput"]


class SparseEmbeddingInput(TypedDict, total=False):
    type: Required[Literal["enabled", "disabled"]]
