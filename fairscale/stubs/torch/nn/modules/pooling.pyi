# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

from .module import Module
from typing import Optional
from ... import Tensor, _size
from ..common_types import _size_any_t, _maybe_indices_t, _size_1_t, _size_2_t, _size_3_t, _ratio_3_t, _ratio_2_t


class _MaxPoolNd(Module):
    return_indices: bool = ...
    ceil_mode: bool = ...

    def __init__(self, kernel_size: _size_any_t, stride: Optional[_size_any_t] = ..., padding: _size_any_t = ...,
                 dilation: _size_any_t = ..., return_indices: bool = ..., ceil_mode: bool = ...) -> None: ...


class MaxPool1d(_MaxPoolNd):
    kernel_size: _size_1_t = ...
    stride: _size_1_t = ...
    padding: _size_1_t = ...
    dilation: _size_1_t = ...

    def forward(self, input: Tensor) -> _maybe_indices_t: ...  # type: ignore

    def __call__(self, input: Tensor) -> _maybe_indices_t: ...  # type: ignore


class MaxPool2d(_MaxPoolNd):
    kernel_size: _size_2_t = ...
    stride: _size_2_t = ...
    padding: _size_2_t = ...
    dilation: _size_2_t = ...

    def forward(self, input: Tensor) -> _maybe_indices_t: ...  # type: ignore

    def __call__(self, input: Tensor) -> _maybe_indices_t: ...  # type: ignore


class MaxPool3d(_MaxPoolNd):
    kernel_size: _size_3_t = ...
    stride: _size_3_t = ...
    padding: _size_3_t = ...
    dilation: _size_3_t = ...

    def forward(self, input: Tensor) -> _maybe_indices_t: ...  # type: ignore

    def __call__(self, input: Tensor) -> _maybe_indices_t: ...  # type: ignore


class _MaxUnpoolNd(Module):
    ...


class MaxUnpool1d(_MaxUnpoolNd):
    kernel_size: _size_1_t = ...
    stride: _size_1_t = ...
    padding: _size_1_t = ...

    def __init__(self, kernel_size: _size_1_t, stride: Optional[_size_1_t] = ..., padding: _size_1_t = ...) -> None: ...

    def forward(self, input: Tensor, indices: Tensor, output_size: Optional[_size] = ...) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor, indices: Tensor, output_size: Optional[_size] = ...) -> Tensor: ...  # type: ignore


class MaxUnpool2d(_MaxUnpoolNd):
    kernel_size: _size_2_t = ...
    stride: _size_2_t = ...
    padding: _size_2_t = ...

    def __init__(self, kernel_size: _size_2_t, stride: Optional[_size_2_t] = ..., padding: _size_2_t = ...) -> None: ...

    def forward(self, input: Tensor, indices: Tensor, output_size: Optional[_size] = ...) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor, indices: Tensor, output_size: Optional[_size] = ...) -> Tensor: ...  # type: ignore


class MaxUnpool3d(_MaxUnpoolNd):
    kernel_size: _size_3_t = ...
    stride: _size_3_t = ...
    padding: _size_3_t = ...

    def __init__(self, kernel_size: _size_3_t, stride: Optional[_size_3_t] = ..., padding: _size_3_t = ...) -> None: ...

    def forward(self, input: Tensor, indices: Tensor, output_size: Optional[_size] = ...) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor, indices: Tensor, output_size: Optional[_size] = ...) -> Tensor: ...  # type: ignore


class _AvgPoolNd(Module):
    ...


class AvgPool1d(_AvgPoolNd):
    kernel_size: _size_1_t = ...
    stride: _size_1_t = ...
    padding: _size_1_t = ...
    ceil_mode: bool = ...
    count_include_pad: bool = ...

    def __init__(self, kernel_size: _size_1_t, stride: Optional[_size_1_t] = ..., padding: _size_1_t = ...,
                 ceil_mode: bool = ..., count_include_pad: bool = ...) -> None: ...

    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore


class AvgPool2d(_AvgPoolNd):
    kernel_size: _size_2_t = ...
    stride: _size_2_t = ...
    padding: _size_2_t = ...
    ceil_mode: bool = ...
    count_include_pad: bool = ...

    def __init__(self, kernel_size: _size_2_t, stride: Optional[_size_2_t] = ..., padding: _size_2_t = ...,
                 ceil_mode: bool = ..., count_include_pad: bool = ...) -> None: ...

    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore


class AvgPool3d(_AvgPoolNd):
    kernel_size: _size_3_t = ...
    stride: _size_3_t = ...
    padding: _size_3_t = ...
    ceil_mode: bool = ...
    count_include_pad: bool = ...

    def __init__(self, kernel_size: _size_3_t, stride: Optional[_size_3_t] = ..., padding: _size_3_t = ...,
                 ceil_mode: bool = ..., count_include_pad: bool = ...) -> None: ...

    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore


class FractionalMaxPool2d(Module):
    kernel_size: _size_2_t = ...
    return_indices: bool = ...
    output_size: _size_2_t = ...
    output_ratio: _ratio_2_t = ...

    def __init__(self, kernel_size: _size_2_t, output_size: Optional[_size_2_t] = ...,
                 output_ratio: Optional[_ratio_2_t] = ..., return_indices: bool = ...) -> None: ...

    def forward(self, input: Tensor) -> _maybe_indices_t: ...  # type: ignore

    def __call__(self, input: Tensor) -> _maybe_indices_t: ...  # type: ignore


class FractionalMaxPool3d(Module):
    kernel_size: _size_3_t = ...
    return_indices: bool = ...
    output_size: _size_3_t = ...
    output_ratio: _ratio_3_t = ...

    def __init__(self, kernel_size: _size_3_t, output_size: Optional[_size_3_t] = ...,
                 output_ratio: Optional[_ratio_3_t] = ..., return_indices: bool = ...) -> None: ...

    def forward(self, input: Tensor) -> _maybe_indices_t: ...  # type: ignore

    def __call__(self, input: Tensor) -> _maybe_indices_t: ...  # type: ignore


class _LPPoolNd(Module):
    norm_type: float = ...
    ceil_mode: bool = ...

    def __init__(self, norm_type: float, kernel_size: _size_any_t, stride: Optional[_size_any_t] = ...,
                 ceil_mode: bool = ...) -> None: ...


class LPPool1d(_LPPoolNd):
    kernel_size: _size_1_t = ...
    stride: _size_1_t = ...

    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore


class LPPool2d(_LPPoolNd):
    kernel_size: _size_2_t = ...
    stride: _size_2_t = ...

    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore


class _AdaptiveMaxPoolNd(Module):
    return_indices: bool = ...

    def __init__(self, output_size: _size_any_t, return_indices: bool = ...) -> None: ...


class AdaptiveMaxPool1d(_AdaptiveMaxPoolNd):
    output_size: _size_1_t = ...

    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore


class AdaptiveMaxPool2d(_AdaptiveMaxPoolNd):
    output_size: _size_2_t = ...

    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore


class AdaptiveMaxPool3d(_AdaptiveMaxPoolNd):
    output_size: _size_3_t = ...

    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore


class _AdaptiveAvgPoolNd(Module):
    def __init__(self, output_size: _size_any_t) -> None: ...


class AdaptiveAvgPool1d(_AdaptiveAvgPoolNd):
    output_size: _size_1_t = ...

    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore


class AdaptiveAvgPool2d(_AdaptiveAvgPoolNd):
    output_size: _size_2_t = ...

    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore


class AdaptiveAvgPool3d(_AdaptiveAvgPoolNd):
    output_size: _size_3_t = ...

    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore
