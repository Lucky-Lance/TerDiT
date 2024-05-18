# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

from .module import Module
from ... import Tensor
from ..common_types import _size_2_t, _size_4_t, _size_6_t


class _ConstantPadNd(Module):
    value: float

    def __init__(self, value: float) -> None: ...

    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore


class ConstantPad1d(_ConstantPadNd):
    padding: _size_2_t = ...

    def __init__(self, padding: _size_2_t, value: float) -> None: ...


class ConstantPad2d(_ConstantPadNd):
    padding: _size_4_t = ...

    def __init__(self, padding: _size_4_t, value: float) -> None: ...


class ConstantPad3d(_ConstantPadNd):
    padding: _size_6_t = ...

    def __init__(self, padding: _size_6_t, value: float) -> None: ...


class _ReflectionPadNd(Module):
    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore
    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore

    def extra_repr(self): ...


class ReflectionPad1d(_ReflectionPadNd):
    padding: _size_2_t = ...

    def __init__(self, padding: _size_2_t) -> None: ...


class ReflectionPad2d(_ReflectionPadNd):
    padding: _size_4_t = ...

    def __init__(self, padding: _size_4_t) -> None: ...


class _ReplicationPadNd(Module):
    def forward(self, input: Tensor) -> Tensor: ...  # type: ignore
    def __call__(self, input: Tensor) -> Tensor: ...  # type: ignore

    def extra_repr(self): ...


class ReplicationPad1d(_ReplicationPadNd):
    padding: _size_2_t = ...

    def __init__(self, padding: _size_2_t) -> None: ...


class ReplicationPad2d(_ReplicationPadNd):
    padding: _size_4_t = ...

    def __init__(self, padding: _size_4_t) -> None: ...


class ReplicationPad3d(_ReplicationPadNd):
    padding: _size_6_t = ...

    def __init__(self, padding: _size_6_t) -> None: ...


class ZeroPad2d(ConstantPad2d):
    padding: _size_4_t = ...

    def __init__(self, padding: _size_4_t) -> None: ...
