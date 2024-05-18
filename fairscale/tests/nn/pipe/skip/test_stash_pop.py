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
from torch import nn

from fairscale.nn.pipe.skip import pop, skippable, stash
from fairscale.nn.pipe.skip.tracker import SkipTracker, use_skip_tracker


@pytest.fixture(autouse=True)
def skip_tracker():
    skip_tracker = SkipTracker()
    with use_skip_tracker(skip_tracker):
        yield skip_tracker


def test_stash(skip_tracker):
    @skippable(stash=["foo"])
    class Stash(nn.Module):
        def forward(self, input):
            yield stash("foo", input)
            return input * 2

    l1 = Stash()

    assert len(skip_tracker.tensors) == 0

    with use_skip_tracker(skip_tracker):
        l1(torch.tensor(42))

    assert len(skip_tracker.tensors) == 1


def test_pop():
    @skippable(stash=["foo"])
    class Stash(nn.Module):
        def forward(self, input):
            yield stash("foo", input)
            return input * 2

    @skippable(pop=["foo"])
    class Pop(nn.Module):
        def forward(self, input):
            foo = yield pop("foo")
            return foo

    l1 = Stash()
    l2 = Pop()

    output = l2(l1(torch.tensor(42)))

    assert output.item() == 42


def test_declare_but_not_use():
    @skippable(stash=["foo"])
    class Stash(nn.Module):
        def forward(self, input):
            return input * 2

    @skippable(pop=["foo"])
    class Pop(nn.Module):
        def forward(self, input):
            return input * 3

    l1 = Stash()
    l2 = Pop()

    with pytest.raises(RuntimeError):
        l1(torch.tensor(42))

    with pytest.raises(RuntimeError):
        l2(torch.tensor(42))


def test_stash_not_declared():
    @skippable()
    class Stash(nn.Module):
        def forward(self, input):
            yield stash("foo", input)
            return input * 2

    l1 = Stash()

    with pytest.raises(RuntimeError):
        l1(torch.tensor(42))


def test_pop_not_declared():
    @skippable(stash=["foo"])
    class Stash(nn.Module):
        def forward(self, input):
            yield stash("foo", input)
            return input * 2

    @skippable()
    class Pop(nn.Module):
        def forward(self, input):
            foo = yield pop("foo")
            return foo

    l1 = Stash()
    l2 = Pop()

    latent = l1(torch.tensor(42))

    with pytest.raises(RuntimeError):
        l2(latent)


def test_pop_not_stashed():
    @skippable(pop=["foo"])
    class Pop(nn.Module):
        def forward(self, input):
            yield pop("foo")

    l1 = Pop()

    with pytest.raises(RuntimeError):
        l1(torch.tensor(42))


def test_stash_none():
    @skippable(stash=["foo"])
    class Stash(nn.Module):
        def forward(self, input):
            yield stash("foo", None)
            return input * 2

    l1 = Stash()
    l1(torch.tensor(42))
