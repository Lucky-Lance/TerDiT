# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.
#
# This source code is licensed under the BSD license found in the
# LICENSE file in the root directory of this source tree.

# Copyright 2019 Kakao Brain
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
import torch

from fairscale.nn.pipe.copy import Copy, Wait
from fairscale.nn.pipe.stream import CPUStream, current_stream, get_device, is_cuda, new_stream, use_stream

skip_if_no_cuda = pytest.mark.skipif(not torch.cuda.is_available(), reason="cuda required")


def _test_copy_wait(prev_stream, next_stream, cuda_sleep=None):
    device = get_device(prev_stream)

    with use_stream(prev_stream):
        if is_cuda(prev_stream):
            cuda_sleep(0.5)
        x = torch.ones(100, device=device, requires_grad=True)

    (y,) = Copy.apply(prev_stream, next_stream, x)
    (y,) = Wait.apply(prev_stream, next_stream, x)

    with use_stream(next_stream):
        assert torch.allclose(y.sum(), torch.tensor(100.0, device=device))
        y.norm().backward()
    with use_stream(prev_stream):
        assert torch.allclose(x.grad.sum(), torch.tensor(10.0, device=device))


def test_copy_wait_cpu_cpu():
    prev_stream = CPUStream
    next_stream = CPUStream
    _test_copy_wait(prev_stream, next_stream)


@skip_if_no_cuda
def test_copy_wait_cpu_cuda(cuda_sleep):
    prev_stream = CPUStream
    next_stream = current_stream(torch.device("cuda"))
    _test_copy_wait(prev_stream, next_stream, cuda_sleep)


@skip_if_no_cuda
def test_copy_wait_cuda_cpu(cuda_sleep):
    prev_stream = current_stream(torch.device("cuda"))
    next_stream = CPUStream
    _test_copy_wait(prev_stream, next_stream, cuda_sleep)


@skip_if_no_cuda
def test_copy_wait_cuda_cuda(cuda_sleep):
    prev_stream = current_stream(torch.device("cuda"))
    next_stream = new_stream(torch.device("cuda"))
    _test_copy_wait(prev_stream, next_stream, cuda_sleep)


def test_wait_multiple_tensors():
    a = torch.rand(1, requires_grad=True)
    b = torch.rand(1, requires_grad=True)

    a, b = Wait.apply(CPUStream, CPUStream, a, b)

    assert a.grad_fn is b.grad_fn
    assert a.grad_fn.__class__ is Wait._backward_cls
