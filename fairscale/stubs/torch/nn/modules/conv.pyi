# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

from .module import Module
from typing import Any, Optional, List, Tuple, Union
from ... import Tensor
from ..common_types import _size_1_t, _size_2_t, _size_3_t


class _ConvNd(Module):
    in_channels: int = ...
    out_channels: int = ...
    kernel_size: Tuple[int, ...] = ...
    stride: Tuple[int, ...] = ...
    padding: Tuple[int, ...] = ...
    dilation: Tuple[int, ...] = ...
    transposed: bool = ...
    output_padding: Tuple[int, ...] = ...
    groups: int = ...
    padding_mode: str = ...
    weight: Tensor = ...
    bias: Tensor = ...

    # padding_mode can only one of an enumerated set of strings. Python typing will eventually support precisely typing
    # this with the `Literal` type.
    def __init__(self, in_channels: Any, out_channels: Any, kernel_size: Any, stride: Any, padding: Any, dilation: Any,
                 transposed: Any, output_padding: Any, groups: Any, bias: Any, padding_mode: Any) -> None: ...

    def reset_parameters(self) -> None: ...


class Conv1d(_ConvNd):
    def __init__(self, in_channels: int, out_channels: int, kernel_size: _size_1_t, stride: _size_1_t = ...,
                 padding: _size_1_t = ..., dilation: _size_1_t = ..., groups: int = ..., bias: bool = ...,
                 padding_mode: str = ...) -> None: ...

    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore


class Conv2d(_ConvNd):
    def __init__(self, in_channels: int, out_channels: int, kernel_size: _size_2_t, stride: _size_2_t = ...,
                 padding: _size_2_t = ..., dilation: _size_2_t = ..., groups: int = ..., bias: bool = ...,
                 padding_mode: str = ...) -> None: ...

    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore


class Conv3d(_ConvNd):
    def __init__(self, in_channels: int, out_channels: int, kernel_size: _size_3_t, stride: _size_3_t = ...,
                 padding: _size_3_t = ..., dilation: _size_3_t = ..., groups: int = ..., bias: bool = ...,
                 padding_mode: str = ...) -> None: ...

    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore


class _ConvTransposeMixin:
    def forward(self, input: Tensor, output_size: Optional[List[int]] = ...): ...  # type: ignore
    def __call__(self, input: Tensor, output_size: Optional[List[int]] = ...): ...  # type: ignore

# We need a '# type: ignore' at the end of the declaration of each class that inherits from 
# `_ConvTransposeMixin` since the `forward` method declared in `_ConvTransposeMixin` is 
# incompatible with the `forward` method declared in `Module`.
class ConvTranspose1d(_ConvTransposeMixin, _ConvNd):  # type: ignore
    def __init__(self, in_channels: int, out_channels: int, kernel_size: _size_1_t, stride: _size_1_t = ...,
                 padding: _size_1_t = ..., output_padding: _size_1_t = ..., groups: int = ..., bias: bool = ...,
                 dilation: int = ..., padding_mode: str = ...) -> None: ...

    def forward(self, input: Tensor, output_size: Optional[List[int]] = ...) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor, output_size: Optional[List[int]] = ...) -> Tensor: ...  # type: ignore


class ConvTranspose2d(_ConvTransposeMixin, _ConvNd):  # type: ignore
    def __init__(self, in_channels: int, out_channels: int, kernel_size: _size_2_t, stride: _size_2_t = ...,
                 padding: _size_2_t = ..., output_padding: _size_2_t = ..., groups: int = ..., bias: bool = ...,
                 dilation: int = ..., padding_mode: str = ...) -> None: ...

    def forward(self, input: Tensor, output_size: Optional[List[int]] = ...) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor, output_size: Optional[List[int]] = ...) -> Tensor: ...  # type: ignore


class ConvTranspose3d(_ConvTransposeMixin, _ConvNd):  # type: ignore
    def __init__(self, in_channels: int, out_channels: int, kernel_size: _size_3_t, stride: _size_3_t = ...,
                 padding: _size_3_t = ..., output_padding: _size_3_t = ..., groups: int = ..., bias: bool = ...,
                 dilation: int = ..., padding_mode: str = ...) -> None: ...

    def forward(self, input: Tensor, output_size: Optional[List[int]] = ...) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor, output_size: Optional[List[int]] = ...) -> Tensor: ...  # type: ignore
