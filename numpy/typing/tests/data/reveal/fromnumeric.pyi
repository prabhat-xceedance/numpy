"""Tests for :mod:`core.fromnumeric`."""

import numpy as np

A = np.array(True, ndmin=2, dtype=np.bool_)
B = np.array(1.0, ndmin=2, dtype=np.float32)
A.setflags(write=False)
B.setflags(write=False)

a = np.bool_(True)
b = np.float32(1.0)
c = 1.0
d = np.array(1.0, dtype=np.float32)  # writeable

reveal_type(np.take(a, 0))  # E: Any
reveal_type(np.take(b, 0))  # E: Any
reveal_type(np.take(c, 0))  # E: Any
reveal_type(np.take(A, 0))  # E: Any
reveal_type(np.take(B, 0))  # E: Any
reveal_type(np.take(A, [0]))  # E: Any
reveal_type(np.take(B, [0]))  # E: Any

reveal_type(np.reshape(a, 1))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.reshape(b, 1))  # E: ndarray[Any, dtype[{float32}]]
reveal_type(np.reshape(c, 1))  # E: ndarray[Any, dtype[Any]]
reveal_type(np.reshape(A, 1))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.reshape(B, 1))  # E: ndarray[Any, dtype[{float32}]]

reveal_type(np.choose(1, [True, True]))  # E: Any
reveal_type(np.choose([1], [True, True]))  # E: ndarray[Any, dtype[Any]]
reveal_type(np.choose([1], A))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.choose([1], A, out=B))  # E: ndarray[Any, dtype[{float32}]]

reveal_type(np.repeat(a, 1))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.repeat(b, 1))  # E: ndarray[Any, dtype[{float32}]]
reveal_type(np.repeat(c, 1))  # E: ndarray[Any, dtype[Any]]
reveal_type(np.repeat(A, 1))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.repeat(B, 1))  # E: ndarray[Any, dtype[{float32}]]

# TODO: Add tests for np.put()

reveal_type(np.swapaxes([[0, 1]], 0, 0))  # E: ndarray[Any, dtype[Any]]
reveal_type(np.swapaxes(A, 0, 0))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.swapaxes(B, 0, 0))  # E: ndarray[Any, dtype[{float32}]]

reveal_type(np.transpose(a))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.transpose(b))  # E: ndarray[Any, dtype[{float32}]]
reveal_type(np.transpose(c))  # E: ndarray[Any, dtype[Any]]
reveal_type(np.transpose(A))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.transpose(B))  # E: ndarray[Any, dtype[{float32}]]

reveal_type(np.partition(a, 0, axis=None))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.partition(b, 0, axis=None))  # E: ndarray[Any, dtype[{float32}]]
reveal_type(np.partition(c, 0, axis=None))  # E: ndarray[Any, dtype[Any]]
reveal_type(np.partition(A, 0))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.partition(B, 0))  # E: ndarray[Any, dtype[{float32}]]

reveal_type(np.argpartition(a, 0))  # E: ndarray[Any, dtype[{intp}]]
reveal_type(np.argpartition(b, 0))  # E: ndarray[Any, dtype[{intp}]]
reveal_type(np.argpartition(c, 0))  # E: ndarray[Any, dtype[{intp}]]
reveal_type(np.argpartition(A, 0))  # E: ndarray[Any, dtype[{intp}]]
reveal_type(np.argpartition(B, 0))  # E: ndarray[Any, dtype[{intp}]]

reveal_type(np.sort([2, 1], 0))  # E: ndarray[Any, dtype[Any]]
reveal_type(np.sort(A, 0))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.sort(B, 0))  # E: ndarray[Any, dtype[{float32}]]

reveal_type(np.argsort(A, 0))  # E: ndarray[Any, dtype[{intp}]]
reveal_type(np.argsort(B, 0))  # E: ndarray[Any, dtype[{intp}]]

reveal_type(np.argmax(A))  # E: {intp}
reveal_type(np.argmax(B))  # E: {intp}
reveal_type(np.argmax(A, axis=0))  # E: Any
reveal_type(np.argmax(B, axis=0))  # E: Any

reveal_type(np.argmin(A))  # E: {intp}
reveal_type(np.argmin(B))  # E: {intp}
reveal_type(np.argmin(A, axis=0))  # E: Any
reveal_type(np.argmin(B, axis=0))  # E: Any

reveal_type(np.searchsorted(A[0], 0))  # E: {intp}
reveal_type(np.searchsorted(B[0], 0))  # E: {intp}
reveal_type(np.searchsorted(A[0], [0]))  # E: ndarray[Any, dtype[{intp}]]
reveal_type(np.searchsorted(B[0], [0]))  # E: ndarray[Any, dtype[{intp}]]

reveal_type(np.resize(a, (5, 5)))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.resize(b, (5, 5)))  # E: ndarray[Any, dtype[{float32}]]
reveal_type(np.resize(c, (5, 5)))  # E: ndarray[Any, dtype[Any]]
reveal_type(np.resize(A, (5, 5)))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.resize(B, (5, 5)))  # E: ndarray[Any, dtype[{float32}]]

reveal_type(np.squeeze(a))  # E: bool_
reveal_type(np.squeeze(b))  # E: {float32}
reveal_type(np.squeeze(c))  # E: ndarray[Any, dtype[Any]]
reveal_type(np.squeeze(A))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.squeeze(B))  # E: ndarray[Any, dtype[{float32}]]

reveal_type(np.diagonal(A))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.diagonal(B))  # E: ndarray[Any, dtype[{float32}]]

reveal_type(np.trace(A))  # E: Any
reveal_type(np.trace(B))  # E: Any

reveal_type(np.ravel(a))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.ravel(b))  # E: ndarray[Any, dtype[{float32}]]
reveal_type(np.ravel(c))  # E: ndarray[Any, dtype[Any]]
reveal_type(np.ravel(A))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.ravel(B))  # E: ndarray[Any, dtype[{float32}]]

reveal_type(np.nonzero(a))  # E: tuple[ndarray[Any, dtype[{intp}]]]
reveal_type(np.nonzero(b))  # E: tuple[ndarray[Any, dtype[{intp}]]]
reveal_type(np.nonzero(c))  # E: tuple[ndarray[Any, dtype[{intp}]]]
reveal_type(np.nonzero(A))  # E: tuple[ndarray[Any, dtype[{intp}]]]
reveal_type(np.nonzero(B))  # E: tuple[ndarray[Any, dtype[{intp}]]]

reveal_type(np.shape(a))  # E: tuple[builtins.int]
reveal_type(np.shape(b))  # E: tuple[builtins.int]
reveal_type(np.shape(c))  # E: tuple[builtins.int]
reveal_type(np.shape(A))  # E: tuple[builtins.int]
reveal_type(np.shape(B))  # E: tuple[builtins.int]

reveal_type(np.compress([True], a))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.compress([True], b))  # E: ndarray[Any, dtype[{float32}]]
reveal_type(np.compress([True], c))  # E: ndarray[Any, dtype[Any]]
reveal_type(np.compress([True], A))  # E: ndarray[Any, dtype[bool_]]
reveal_type(np.compress([True], B))  # E: ndarray[Any, dtype[{float32}]]

reveal_type(np.clip(a, 0, 1.0))  # E: Any
reveal_type(np.clip(b, -1, 1))  # E: Any
reveal_type(np.clip(c, 0, 1))  # E: Any
reveal_type(np.clip(A, 0, 1))  # E: Any
reveal_type(np.clip(B, 0, 1))  # E: Any

reveal_type(np.sum(a))  # E: Any
reveal_type(np.sum(b))  # E: Any
reveal_type(np.sum(c))  # E: Any
reveal_type(np.sum(A))  # E: Any
reveal_type(np.sum(B))  # E: Any
reveal_type(np.sum(A, axis=0))  # E: Any
reveal_type(np.sum(B, axis=0))  # E: Any

reveal_type(np.all(a))  # E: bool_
reveal_type(np.all(b))  # E: bool_
reveal_type(np.all(c))  # E: bool_
reveal_type(np.all(A))  # E: bool_
reveal_type(np.all(B))  # E: bool_
reveal_type(np.all(A, axis=0))  # E: Any
reveal_type(np.all(B, axis=0))  # E: Any
reveal_type(np.all(A, keepdims=True))  # E: Any
reveal_type(np.all(B, keepdims=True))  # E: Any

reveal_type(np.any(a))  # E: bool_
reveal_type(np.any(b))  # E: bool_
reveal_type(np.any(c))  # E: bool_
reveal_type(np.any(A))  # E: bool_
reveal_type(np.any(B))  # E: bool_
reveal_type(np.any(A, axis=0))  # E: Any
reveal_type(np.any(B, axis=0))  # E: Any
reveal_type(np.any(A, keepdims=True))  # E: Any
reveal_type(np.any(B, keepdims=True))  # E: Any

reveal_type(np.cumsum(a))  # E: ndarray[Any, Any]
reveal_type(np.cumsum(b))  # E: ndarray[Any, Any]
reveal_type(np.cumsum(c))  # E: ndarray[Any, Any]
reveal_type(np.cumsum(A))  # E: ndarray[Any, Any]
reveal_type(np.cumsum(B))  # E: ndarray[Any, Any]

reveal_type(np.ptp(a))  # E: Any
reveal_type(np.ptp(b))  # E: Any
reveal_type(np.ptp(c))  # E: Any
reveal_type(np.ptp(A))  # E: Any
reveal_type(np.ptp(B))  # E: Any
reveal_type(np.ptp(A, axis=0))  # E: Any
reveal_type(np.ptp(B, axis=0))  # E: Any
reveal_type(np.ptp(A, keepdims=True))  # E: Any
reveal_type(np.ptp(B, keepdims=True))  # E: Any

reveal_type(np.amax(a))  # E: Any
reveal_type(np.amax(b))  # E: Any
reveal_type(np.amax(c))  # E: Any
reveal_type(np.amax(A))  # E: Any
reveal_type(np.amax(B))  # E: Any
reveal_type(np.amax(A, axis=0))  # E: Any
reveal_type(np.amax(B, axis=0))  # E: Any
reveal_type(np.amax(A, keepdims=True))  # E: Any
reveal_type(np.amax(B, keepdims=True))  # E: Any

reveal_type(np.amin(a))  # E: Any
reveal_type(np.amin(b))  # E: Any
reveal_type(np.amin(c))  # E: Any
reveal_type(np.amin(A))  # E: Any
reveal_type(np.amin(B))  # E: Any
reveal_type(np.amin(A, axis=0))  # E: Any
reveal_type(np.amin(B, axis=0))  # E: Any
reveal_type(np.amin(A, keepdims=True))  # E: Any
reveal_type(np.amin(B, keepdims=True))  # E: Any

reveal_type(np.prod(a))  # E: Any
reveal_type(np.prod(b))  # E: Any
reveal_type(np.prod(c))  # E: Any
reveal_type(np.prod(A))  # E: Any
reveal_type(np.prod(B))  # E: Any
reveal_type(np.prod(A, axis=0))  # E: Any
reveal_type(np.prod(B, axis=0))  # E: Any
reveal_type(np.prod(A, keepdims=True))  # E: Any
reveal_type(np.prod(B, keepdims=True))  # E: Any
reveal_type(np.prod(b, out=d))  # E: Any
reveal_type(np.prod(B, out=d))  # E: Any

reveal_type(np.cumprod(a))  # E: ndarray[Any, Any]
reveal_type(np.cumprod(b))  # E: ndarray[Any, Any]
reveal_type(np.cumprod(c))  # E: ndarray[Any, Any]
reveal_type(np.cumprod(A))  # E: ndarray[Any, Any]
reveal_type(np.cumprod(B))  # E: ndarray[Any, Any]

reveal_type(np.ndim(a))  # E: int
reveal_type(np.ndim(b))  # E: int
reveal_type(np.ndim(c))  # E: int
reveal_type(np.ndim(A))  # E: int
reveal_type(np.ndim(B))  # E: int

reveal_type(np.size(a))  # E: int
reveal_type(np.size(b))  # E: int
reveal_type(np.size(c))  # E: int
reveal_type(np.size(A))  # E: int
reveal_type(np.size(B))  # E: int

reveal_type(np.around(a))  # E: Any
reveal_type(np.around(b))  # E: Any
reveal_type(np.around(c))  # E: Any
reveal_type(np.around(A))  # E: Any
reveal_type(np.around(B))  # E: Any

reveal_type(np.mean(a))  # E: Any
reveal_type(np.mean(b))  # E: Any
reveal_type(np.mean(c))  # E: Any
reveal_type(np.mean(A))  # E: Any
reveal_type(np.mean(B))  # E: Any
reveal_type(np.mean(A, axis=0))  # E: Any
reveal_type(np.mean(B, axis=0))  # E: Any
reveal_type(np.mean(A, keepdims=True))  # E: Any
reveal_type(np.mean(B, keepdims=True))  # E: Any
reveal_type(np.mean(b, out=d))  # E: Any
reveal_type(np.mean(B, out=d))  # E: Any

reveal_type(np.std(a))  # E: Any
reveal_type(np.std(b))  # E: Any
reveal_type(np.std(c))  # E: Any
reveal_type(np.std(A))  # E: Any
reveal_type(np.std(B))  # E: Any
reveal_type(np.std(A, axis=0))  # E: Any
reveal_type(np.std(B, axis=0))  # E: Any
reveal_type(np.std(A, keepdims=True))  # E: Any
reveal_type(np.std(B, keepdims=True))  # E: Any
reveal_type(np.std(b, out=d))  # E: Any
reveal_type(np.std(B, out=d))  # E: Any

reveal_type(np.var(a))  # E: Any
reveal_type(np.var(b))  # E: Any
reveal_type(np.var(c))  # E: Any
reveal_type(np.var(A))  # E: Any
reveal_type(np.var(B))  # E: Any
reveal_type(np.var(A, axis=0))  # E: Any
reveal_type(np.var(B, axis=0))  # E: Any
reveal_type(np.var(A, keepdims=True))  # E: Any
reveal_type(np.var(B, keepdims=True))  # E: Any
reveal_type(np.var(b, out=d))  # E: Any
reveal_type(np.var(B, out=d))  # E: Any
